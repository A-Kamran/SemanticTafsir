import Owlready


class Hadith(Owlready.OwlInterface):
    def __init__(self, hNo: str = '', text: str = None):
        super().__init__()

        if hNo is not None and hNo != '':
            self.hadithNo = hNo[1:]
            self.name = 'HD_' + '{:05}'.format(int(hNo[1:]))
        else:
            self.hadithNo = None
            self.name = None

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Hadith(self.name)
        if self.hadithNo is not None:
            self.individual.hasHadithNo = [self.hadithNo]

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createThemeIndividual(self, theme):
        for individual in theme.individual:
            self.individual.hasTheme.append(individual)

    def createNarratorIndividual(self, narrator):
        self.individual.narratedBy.append(narrator.individual)

    def createHadithTextIndividual(self, hadithText):
        self.individual.hasHadithText.append(hadithText.individual)

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]

    def createNoteIndividual(self, note):
        self.individual.hasNote = [note.individual]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createFollowsProperty(self, commentary):
        self.individual.follows = [commentary.individual]

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createAddIndividual(self, addElement):
        self.individual.containsAdd.append(addElement.individual)

    def createPoetryIndividual(self, poetry):
        self.individual.references.append(poetry.individual)

    def createNarratorChainIndividual(self, narratorChain):
        self.individual.containsNarratorChain.append(narratorChain.individual)

    def createDatasetLocationIndividual(self, datasetLocation):
            self.individual.hasDatasetLocation = [datasetLocation.individual]