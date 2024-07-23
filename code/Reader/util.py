from lxml import etree


def getUniqueTags(filename, uniqueAttrib):
    tree = etree.parse(filename)

    r = tree.xpath('//*')

    for i in r:
        tag = str(i.tag).replace('{http://www.tei-c.org/ns/1.0}', '')
        if tag not in uniqueAttrib:
            uniqueAttrib.append(tag)
    return uniqueAttrib


def GetUniqueTagsFromSurat(baseUrl, numberOfFiles):
    container = []

    for i in range(numberOfFiles):
        number = '{0:03}'.format(i)
        getUniqueTags(baseUrl + number + '.xml', container)


def getSectionsForSurat(baseUrl, numberOfFiles):
    for i in range(numberOfFiles):
        number = '{0:03}'.format(i)
        tree = etree.parse(baseUrl + number + '.xml')

        r = tree.xpath('/i:TEI/i:text/i:body/i:div/i:div', namespaces={'i': 'http://www.tei-c.org/ns/1.0'})

        if len(r) == 0:
            r = tree.xpath('/i:TEI/i:text/i:body/i:div', namespaces={'i': 'http://www.tei-c.org/ns/1.0'})


def slashForPlatform():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        return '/'

    elif platform == "darwin":
        return '/'

    elif platform == "win32":
        return '\\'
