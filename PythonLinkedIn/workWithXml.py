import xml.dom.minidom

def manipulaXml():
    doc = xml.dom.minidom.parse('/media/champslinux/HD/Python/PythonStudies/PythonLinkedIn/exemploXML.xml')
    print('Noma da primeira tag:', str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName('firstname')
    print('O primeiro nome:', primeiroNome[0].firstChild.nodeValue)

    for skill in doc.getElementsByTagName('skill'):
        print('Skill encontrada:', skill.getAttribute('name'))
manipulaXml()