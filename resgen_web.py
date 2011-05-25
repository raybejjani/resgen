from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas import Window

import resgen_core


# -------------------------- Begin configuration ---------------------

hfile = 'resgen_h.tpl' # Horizontal resistor template
vfile = 'resgen_v.tpl' # Vertical resistor template
confile = 'resgen.conf' # Specific resistor configuration file
""" Fill in the naming convention for footprints """
footdict = {'1206_resistor.fp':'1206',
            '0603_resistor.fp':'0603'}
# --------------------------------------------------------------------

hTemplate = "v 20081231 1\nL 1100 300 1150 400 3 0 0 0 -1 -1\nL 1150 400 1250 200 3 0 0 0 -1 -1\nL 1250 200 1350 400 3 0 0 0 -1 -1\nL 1350 400 1450 200 3 0 0 0 -1 -1\nL 1450 200 1550 400 3 0 0 0 -1 -1\nL 1550 400 1650 200 3 0 0 0 -1 -1\nL 1650 200 1700 300 3 0 0 0 -1 -1\nP 2000 300 1700 300 1 0 0\n{\nT 1900 600 5 10 0 0 0 0 1\npinnumber=2\nT 1900 400 5 10 0 0 0 0 1\npinseq=2\nT 1900 800 5 10 0 0 0 0 1\npinlabel=cathode\n\nP 800 300 1100 300 1 0 0\n{\nT 0 600 5 10 0 0 0 0 1\npinnumber=1\nT 0 400 5 10 0 0 0 0 1\npinseq=1\nT 0 800 5 10 0 0 0 0 1\npinlabel=anode\n}\nT 0 1500 8 10 0 0 0 0 1\ndevice=resistor\nT 1300 500 8 10 1 1 0 0 1\nrefdes=R?"

confDefault = "# resistor value (ohms)\nvalue = 69696\n# precision (number of significant digits)\nprecision = 4\n# footprint\nfootprint = 1206_resistor.fp\n# part number\npart = 50-1"

inputArea = TextArea()
outputArea = TextArea()

def convert(sender):
    resdict = resgen_core.processconf(inputArea.getText())
    hData = resgen_core.processhorz(resdict, hTemplate, footdict)
    outputArea.setText(hData)

if __name__ == '__main__':
    b = Button("Convert", convert)

    p = HorizontalPanel()
    p.add(inputArea)
    p.add(outputArea)
   
    q = VerticalPanel()
    q.setStyleName("panel")
    q.add(b)
    q.add(p)

   
    q.setHeight("100%")
    q.setWidth("100%")
    p.setHeight("80%")
    p.setWidth("100%")
    inputArea.setHeight("100%")
    inputArea.setWidth("100%")
    outputArea.setHeight("100%")
    outputArea.setWidth("100%")

    inputArea.setText(confDefault)

    RootPanel().add(q)

