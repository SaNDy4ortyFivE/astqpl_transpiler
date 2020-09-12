##custom imports
from anytree import AnyNode, RenderTree

root = AnyNode(nodename='root')
parent = root

def addNodeOutput(variable):
    global parent
    n = AnyNode(parent=parent, nodename='output',variable=variable)

def addNodeEnd():
    global parent
    if len(parent.ancestors)>=1:
        #print('giving an ancestor')
        parent = parent.ancestors[-1]
    n = AnyNode(parent=parent, nodename='end')

def addNodeElse():
    global parent
    if len(parent.ancestors)>=1:
        #print('giving an ancestor')
        parent = parent.ancestors[-1]
    n = AnyNode(parent=parent, nodename='else')
    parent = n

def addIf(val1, val2, rel):
    global parent
    n = AnyNode(parent=parent, nodename='if', val1=val1, val2=val2, rel=rel)
    ##update parent to this
    parent = n
    #print('new parent',n)

def addDecl(dtype, var_name):
    global parent
    n = AnyNode(parent=parent, nodename='decl', dtype=dtype, var_name=var_name)

def addAssign(var_name, val):
    global parent
    n = AnyNode(parent=parent, nodename='assign', var_name=var_name, val=val)

def addBoth(dtype, var_name, val):
    global parent
    n = AnyNode(parent=parent,nodename='both',dtype=dtype,var_name=var_name,val=val)

def printTree():
    global root
    print(RenderTree(root))
