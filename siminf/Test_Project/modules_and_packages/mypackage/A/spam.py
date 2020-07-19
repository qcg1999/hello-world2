
from . import grok as g   #import from same folder
from ..B import bar as b  #import from a sibling folder

def spam_1():
    print("in spam_1")
    print("in spam_1: calling grok_1")
    g.grok_1()
    
def spam_2():
    print("in spam_2: calling bar_1")
    b.bar_1()
    