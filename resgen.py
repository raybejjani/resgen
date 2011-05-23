""" resgen.py
    Generates standard resistor symbols using the configuration found
    in resgen.conf.  Makes both a horizontal and a vertical version.
    Will not overwrite an exisiting symbol. """

# -------------------------- Begin configuration ---------------------

hfile = 'resgen_h.tpl' # Horizontal resistor template
vfile = 'resgen_v.tpl' # Vertical resistor template
confile = 'resgen.conf' # Specific resistor configuration file
""" Fill in the naming convention for footprints """
footdict = {'1206_resistor.fp':'1206',
            '0603_resistor.fp':'0603'}


# -------------------------- End configuration -----------------------
import os
import math
import shutil

""" getconf()
    Open the resistor configuration file and return its contents in a
    dictionary """
def getconf():
    if (not os.access(confile,os.F_OK)):
        print ('getconf: could not find the configuration file ' + confile)
        return
    fin = open(confile,'r')
    try:
        rawfile = fin.read()
    finally:
        fin.close()

    return rawfile

def processconf(rawfile):
    resdict = {}
    for line in rawfile.split('\n'):
        if line.strip().startswith('value'):
            resdict['value'] = line.split('=')[1].strip()
        if line.strip().startswith('precision'):
            resdict['precision'] = line.split('=')[1].strip()
        if line.strip().startswith('part'):
            resdict['part'] = line.split('=')[1].strip()
        if line.strip().startswith('footprint'):
            resdict['footprint'] = line.split('=')[1].strip()
    return resdict

""" makename(dictionary containing part and value)
    Creates the filename from the value parameter.
    -- Every value will have three significant figures. """
def makename(resdict):
    value = float(resdict['value'])
    if (value/1e6 >= 1):
        Mval = int(math.floor(value/1e6))
        kval = int(value - Mval*1e6)
        name = str(Mval) + 'M' + str(kval)
        while (len(name) > 4):
            name = name[0:-1] # Reduce to maximum of 3 significant figures
    elif (value/1e3 >= 1):
        kval = int(math.floor(value/1e3))
        rval = int(value - kval*1e3)
        name = str(kval) + 'k' + str(rval)
        while (len(name) > 4):
            name = name[0:-1] # Reduce to maximum of 3 significant figures
    elif (value >= 1):
        rval = int(math.floor(value))
        name = str(rval) + 'r'
        while (len(name) < 4):
            name = name + '0'
    elif (value < 1):
        mval = int(math.floor(value * 1000))
        name = str(mval) + 'm'
        while (len(name) < 4):
            name = name + '0'
    footname = resdict['footprint']
    name = name + '_' + footdict[footname] # Tack on the footprint name
    return name

""" makevalue(Resistor dictionary)
    Format the resistor value from the configuration file into the
    string shown on a schematic.
    --- Three significant digits and the engineering character for the
        10x multiplier"""
def makevalue(resdict):
    value = float(resdict['value'])
    if (value/1e6 >= 1):
        Mval = int(math.floor(value/1e6))
        kval = int(value - Mval*1e6)
        valstr = str(Mval) + '.' + str(kval)
        while len(valstr) < (int(resdict['precision']) + 1):
            valstr += '0' # Pad to specified precision
        while len(valstr) > (int(resdict['precision']) + 1):
            valstr = valstr[0:-1] # Reduce to specified precision
        if valstr.endswith('.'):
            valstr = valstr[0:-1] # Get rid of the decimal point
        valstr += 'M'
    elif (value/1e3 >= 1):
        kval = int(math.floor(value/1e3))
        rval = int(value - kval*1e3)
        valstr = str(kval) + '.' + str(rval)
        while len(valstr) < (int(resdict['precision']) + 1):
            valstr += '0' # Pad to specified precision
        while len(valstr) > (int(resdict['precision']) + 1):
            valstr = valstr[0:-1] # Reduce to specified precision
        if valstr.endswith('.'):
            valstr = valstr[0:-1] # Get rid of the decimal point
        valstr += 'k'
    elif (value >= 1):
        rval = int(math.floor(value))
        valstr = str(rval)
        if len(valstr) < (int(resdict['precision']) + 1):
            valstr += '.'
        while len(valstr) < (int(resdict['precision']) + 1):
            valstr += '0' # Pad to specified precision
        while len(valstr) > (int(resdict['precision']) + 1):
            valstr = valstr[0:-1] # Reduce to specified precision
        if valstr.endswith('.'):
            valstr = valstr[0:-1] # Get rid of the decimal point
    elif (value < 1):
        mval = int(math.floor(value * 1000))
        valstr = '0.' + str(mval)
        while len(valstr) < (int(resdict['precision']) + 2):
            valstr += '0' # Pad to specified precision
        while len(valstr) > (int(resdict['precision']) + 2):
            valstr = valstr[0:-1] # Reduce to specified precision
    return valstr


""" makehorz(Resistor dictionary)
    Make the horizontal symbol """
def makehorz(resdict):
    outname = resdict['name'] + '_horz.sym'
    if os.access(outname,os.F_OK):
        print ('resgen.makehorz: ' + outname + ' already exists.')
        return
    else:
        print('resgen.makehorz: creating ' + outname)
        fot = open(outname,'w')
        fot.close() # Just touch the file -- don't leave it open
        shutil.copyfile(hfile,outname)
        fot = open(outname,'a') # Open for appending
        fot.write('T 0 1300 8 10 0 0 0 0 1' + '\n') # Footprint
        fot.write('footprint=' + resdict['footprint'] + '\n')
        fot.write('T 0 1095 8 10 0 0 0 0 1' + '\n') # Part number
        fot.write('part=' + resdict['part'] + '\n')
        fot.write('T 1300 0 8 10 1 1 0 0 1' + '\n') # Value
        fot.write('value=' + makevalue(resdict) + '\n')
        fot.close()

""" makevert(Resistor dictionary)
    Make the vertical symbol """
def makevert(resdict):
    outname = resdict['name'] + '_vert.sym'
    if os.access(outname,os.F_OK):
        print ('resgen.makevert: ' + outname + ' already exists.')
        return
    else:
        print('resgen.makevert: creating ' + outname)
        fot = open(outname,'w')
        fot.close() # Just touch the file -- don't leave it open
        shutil.copyfile(vfile,outname)
        fot = open(outname,'a') # Open for appending
        fot.write('T 0 1700 8 10 0 0 0 0 1' + '\n') # Footprint
        fot.write('footprint=' + resdict['footprint'] + '\n')
        fot.write('T 0 1495 8 10 0 0 0 0 1' + '\n') # Part number
        fot.write('part=' + resdict['part'] + '\n')
        fot.write('T 300 500 8 10 1 1 0 0 1' + '\n') # Value
        fot.write('value=' + makevalue(resdict) + '\n')
        fot.close()



""" main() """
def main():
    resdict = processconf(getconf())
    resdict['name'] = makename(resdict)
    makehorz(resdict)
    makevert(resdict)

if __name__ == "__main__":
    main()
