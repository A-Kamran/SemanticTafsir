import Owlready


class Verse(Owlready.OwlInterface):
    def __init__(self, chapterNo: str = None, verseNo: str = None, text: str = None):
        super().__init__()

        self.chapterNo = chapterNo
        self.verseNo = verseNo

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.name = 'V' + '{:03}'.format(int(self.chapterNo)) + ":" + '{:03}'.format(int(self.verseNo))

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Verse(self.name)

    def createDataProperties(self):
        self.individual.hasChapterNo = [self.chapterNo]
        self.individual.hasVerseNo = [self.verseNo]
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createAddIndividual(self, addElement):
        self.individual.containsAdd.append(addElement.individual)

    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]
