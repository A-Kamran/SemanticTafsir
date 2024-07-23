import Owlready


class Surah(Owlready.OwlInterface):
    def __init__(self, name: str = '', surahNo: int = 0):
        super().__init__()

        self.name = name

        self.surahNo = str(surahNo)

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Surah('Surah_' + '{:03}'.format(int(self.surahNo)))
        self.individual.hasSurahNo = [self.surahNo]
        self.individual.hasName = [self.name]

    def createVerseIndividual(self, verse):
        self.individual.containsVerse.append(verse.individual)
