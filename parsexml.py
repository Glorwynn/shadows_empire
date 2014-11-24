from lxml import etree


def createDialog(dialog_structure, tag, decalage):
    nodes = dialog_structure.xpath("//" + tag + "/*")
    if tag.split('/')[-1] == 'question' and len(nodes) < 2:
        return {'sentence': nodes[0]}
    else:
        for node in nodes:
            print(decalage + node.tag)
            createDialog(dialog_structure, tag + "/" +
                         node.tag, decalage + "   ")


def printDialog(dialog_structure, tag, decalage):
    nodes = dialog_structure.xpath("//" + tag + "/*")
    for node in nodes:
        print(decalage + node.tag)
        if node.tag == 'sentence' or node.tag == 'answer':
            print(decalage + node.text)
            pass
        printDialog(dialog_structure, tag + "/" + node.tag, decalage + "   ")

s = etree.parse('dialog.xml')
printDialog(s, "dialog", "")
