from DatasetClasses.ContainerClasses import *

quote_str = "{http://www.tei-c.org/ns/1.0}quote"
name_str = "{http://www.tei-c.org/ns/1.0}name"
seg_str = "{http://www.tei-c.org/ns/1.0}seg"
lb_str = "{http://www.tei-c.org/ns/1.0}lb"
note_str = "{http://www.tei-c.org/ns/1.0}note"
persName_str = "{http://www.tei-c.org/ns/1.0}persName"
said_str = "{http://www.tei-c.org/ns/1.0}said"
pb_str = "{http://www.tei-c.org/ns/1.0}pb"
lg_str = "{http://www.tei-c.org/ns/1.0}lg"
l_str = "{http://www.tei-c.org/ns/1.0}l"
p_str = "{http://www.tei-c.org/ns/1.0}p"
head_str = "{http://www.tei-c.org/ns/1.0}head"
div_str = "{http://www.tei-c.org/ns/1.0}div"
add_str = "{http://www.tei-c.org/ns/1.0}add"
nameSpace = "{http://www.w3.org/XML/1998/namespace}"


def getDataPopulatedParagraph(node, data):
    children = node.getchildren()
    if len(children) == 0:
        return data
    for k in children:
        if quote_str == k.tag:
            element = quote()

            element.type = k.attrib.get('type')
            element.n = k.attrib.get('n')
            element.q_id = k.attrib.get('id')
            element.value = k.attrib.get('value')
            element.subType = k.attrib.get('subtype')
            element.value = k.text
            if element.value is None:
                # print("check1: ",element.n)
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if name_str == k.tag:
            element = name()

            element.role = k.attrib.get('role')
            element.type = k.attrib.get('type')
            element.value = k.text
            element.tail = k.tail
            if element.value is None:
                element.value = ''
            element.children = []
            data.children.append(getDataPopulatedParagraph(k, element))
        if seg_str == k.tag:
            element = seg()

            element.ana = k.attrib.get("ana")
            element.value = k.attrib.get("value")
            element.value = k.text
            if element.value is None:
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if lb_str == k.tag:
            element = lb()

            element.n = k.attrib.get("n")
            element.value = k.attrib.get("value")
            element.value = k.text
            if element.value is None:
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if note_str == k.tag:
            element = note()

            element.value = k.attrib.get('value')
            element.value = k.text
            if element.value is None:
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if persName_str == k.tag:
            element = persName()

            element.ana = k.attrib.get("ana")
            element.value = k.attrib.get("value")
            element.type = k.attrib.get("type")
            element.n = k.attrib.get("n")
            element.value = k.text
            if element.value is None:
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if said_str == k.tag:
            element = said()
            element.s_id = k.attrib.get('id')
            element.value = k.attrib.get('value')
            element.value = k.text
            if element.value is None:
                element.value = ''

            element.tail = k.tail
            data.children.append(getDataPopulatedParagraph(k, element))
        if pb_str == k.tag:
            element = pb()

            element.ed = k.attrib.get('ed')

            element.edRef = k.attrib.get('edRef')

            element.n = k.attrib.get('n')

            element.ed = k.attrib.get('ed')

            element.type = k.attrib.get('type')

            element.value = k.text

            element.tail = k.tail

            data.children.append(getDataPopulatedParagraph(k, element))
        if lg_str == k.tag:
            element = lg()

            element.value = k.text

            element.tail = k.tail

            data.children.append(getDataPopulatedParagraph(k, element))
        if l_str == k.tag:
            element = l()

            element.value = k.text

            if element.value is None:
                element.value = ''

            element.n = k.attrib.get('n')

            element.tail = k.tail

            data.children.append(getDataPopulatedParagraph(k, element))
        if add_str == k.tag:
            element = add()

            element.value = k.text
            if element.value is None:
                element.value = ''

            element.type = k.attrib.get('type')

            element.tail = k.tail

            data.children.append(getDataPopulatedParagraph(k, element))

    return data


def getDataPopulatedDiv(_div):
    children = _div.getchildren()
    pList = []

    for i in children:
        if p_str == i.tag:
            pData = p()

            pData.n = i.attrib.get('n')

            pData.p_id = i.attrib.get(nameSpace + 'id')
            pData.ana = i.attrib.get('ana')
            pData.value = i.text

            
            if pData.value is None:
                pData.value = ''
            pData.tail = i.tail



            

            lst = getDataPopulatedParagraph(i, pData)
            pList.append(lst)
        elif head_str == i.tag:
            headData = head()

            headData.type = i.attrib.get('type')
            headData.n = i.attrib.get('n')
            headData.value = i.text
            if headData.value is None:
                headData.value = ''

            headData.tail = i.tail

            lst = getDataPopulatedParagraph(i, headData)
            pList.append(lst)
        elif div_str == i.tag:
            divData = div()

            divData.value = i.text
            if divData.value is None:
                divData.value = ''

            divData.tail = i.tail
            divData.n = i.attrib.get("n")
            divData.type = i.attrib.get("type")
            divData.language = i.attrib.get(nameSpace + 'lang')
            divData.children = getDataPopulatedDiv(i)
            pList.append(divData)

    return pList


def getDataPopulatedDivList(r):
    divList = []

    for i in list(r):
        divData = div()
        divData.value = i.text
        if divData.value is None:
            divData.value = ''
        divData.tail = i.tail
        divData.n = i.attrib.get("n")

        # print("DIv data in container mapping: ",divData.n)

        divData.type = i.attrib.get("type")
        divData.language = i.attrib.get(nameSpace + 'lang')
        divData.children = getDataPopulatedDiv(i)
        divList.append(divData)

    return divList
