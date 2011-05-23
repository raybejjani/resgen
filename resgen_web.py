from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.TextArea import TextArea
from pyjamas import Window

inputArea = TextArea()
outputArea = TextArea()

def convert(sender):
    outputArea.setText(inputArea.getText())

if __name__ == '__main__':
    b = Button("Convert", convert)
    ta = TextArea()

    p = HorizontalPanel()
    p.add(inputArea)
    p.add(b)
    p.add(outputArea)
   
    p.setStyleName("panel")

    RootPanel().add(p)

