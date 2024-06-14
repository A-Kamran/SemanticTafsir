import Owlready


class HadithText(Owlready.OwlInterface):
    def __init__(self, name: str = '', text: str = None, hNo: str = ''):
        super().__init__()

        self.name = name

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.hadithNo = hNo

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.HadithText(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

        if self.hadithNo is not None:
            self.individual.hasHadithNo = [self.hadithNo]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createAddIndividual(self, addElement):
        self.individual.containsAdd.append(addElement.individual)

    def createPoetryIndividual(self, poetry):
        self.individual.references.append(poetry.individual)

    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createNoteIndividual(self, note):
        self.individual.hasNote = [note.individual]

    def createHadithTextIndividual(self, hadithText):
        self.individual.hasHadithText.append(hadithText.individual)
