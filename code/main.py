from Reader import Parser
from Writer.Writer import *

if __name__ == '__main__':
    onto = Owlready.loadOnto()

    writeSurahVerse(onto)

    divList = Parser.startParser()
    writer = Writer()
    for a in divList:
        writer.write(a, onto)

    Owlready.saveOnto(onto, individualSurah=True)
