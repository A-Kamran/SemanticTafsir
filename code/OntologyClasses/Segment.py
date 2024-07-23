import Owlready


class Segment(Owlready.OwlInterface):
    def __init__(self, text: str = None):
        super().__init__()

        self.name = 'SG_'

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        count = len(onto.search(iri='*' + self.name + '*', type=onto.Segment))
        count += 1
        self.name += '{:04}'.format(count)
        self.individual = onto.Segment(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createThemeIndividual(self, theme):
        for th in theme.individual:
            self.individual.hasSubTheme.append(th)

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createHadithTextIndividual(self, hadithText):
        self.individual.hasHadithText = [hadithText.individual]

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

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



    def createNoteIndividual(self, note):
        self.individual.hasNote = [note.individual]