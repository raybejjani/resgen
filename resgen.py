""" resgen.py
    Generates standard resistor symbols using the configuration found
    in resgen.conf.  Makes both a horizontal and a vertical version.
    Will not overwrite an exisiting symbol. """

# -------------------------- Begin configuration ---------------------

hfile = 'resgen_h.tpl' # Horizontal resistor template
vfile = 'resgen_v.tpl' # Vertical resistor template
confile = 'resgen.conf' # Specific resistor configuration file
outpath = '..' # Where the generated symbols will be saved
""" Fill in the naming convention for footprints """
footdict = {'1206_resistor.fp':'1206',
            '0603_resistor.fp':'0603'}


# -------------------------- End configuration -----------------------


# -------------------------- File IO & Shell -------------------------
import os
import shutil
from resgen_core import *

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

def makehorz(resdict):
    """ makehorz(Resistor dictionary)
    Make the horizontal symbol """
    outname = outpath + '/' + resdict['name'] + '_horz.sym'
    if os.access(outname,os.F_OK):
        print ('resgen.makehorz: ' + outname + ' already exists.')
        return
    else:
        print('resgen.makehorz: creating ' + outname)
        fot = open(outname,'w')
        fhead = open(hfile)
        try:
            fot.write(processhorz(resdict, fhead.read(), footdict))
        finally:
            fhead.close()
            fot.close()

def makevert(resdict):
    """ makevert(Resistor dictionary)
    Make the vertical symbol """
    outname = outpath + '/' + resdict['name'] + '_vert.sym'
    if os.access(outname,os.F_OK):
        print ('resgen.makevert: ' + outname + ' already exists.')
        return
    else:
        print('resgen.makevert: creating ' + outname)
        fot = open(outname,'w')
        fhead = open(hfile)
        try:
            fot.write(processvert(resdict, fhead.read(), footdict))
        finally:
            fhead.close()
            fot.close()

""" main() """
def main():
    resdict = processconf(getconf())
    resdict['name'] = makename(resdict, footdict)
    makehorz(resdict)
    makevert(resdict)

if __name__ == "__main__":
    main()
