import glob

from lxml import etree

from Reader.ContainerMapping import *
from Reader.util import slashForPlatform
from config import projectBaseUrl

# surahNo = ["22","23","25","26","27","28","29","30","32"]
# 89,90,91,92
surahNo = ["3"]

# surahNo = ['1', '18', '107', '109', '110', '111', '112', '113', '114']

# surahNo = [str(i) for i in range(10,30)]

def startParser():
    datasetFiles = []

    combined_div_list = []

    for a in surahNo:
        formattedSurah = '{:03}'.format(int(a))

        allFiles = glob.glob(projectBaseUrl + slashForPlatform() + r"Dataset" + slashForPlatform() + '*')
        for file in allFiles:
            if formattedSurah in file:
                baseUrl = file.split(slashForPlatform())
                baseUrl = (baseUrl[len(baseUrl) - 2]) + slashForPlatform() + (baseUrl[len(baseUrl) - 1])

                datasetFiles = glob.glob(projectBaseUrl + slashForPlatform() + baseUrl + slashForPlatform() + '*.xml')
                
     
        for file in datasetFiles:
            print("File Name : ", file)

            tree = etree.parse(file)

            r = tree.xpath('/i:TEI/i:text/i:body/i:div', namespaces={'i': 'http://www.tei-c.org/ns/1.0'})

            divList = getDataPopulatedDivList(r)

            combined_div_list.append(divList)

    return combined_div_list
