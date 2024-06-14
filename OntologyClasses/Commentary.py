import Owlready


class Commentary(Owlready.OwlInterface):

    def __init__(self, name: str = '', text: str = None, commentaryNo: int = 0):
        super().__init__()

        self.name = name

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.commentaryNo = str(commentaryNo)

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Commentary(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)

        if self.text != "":
            self.individual.hasText = [self.text]

        self.individual.hasCommentaryNo = [self.commentaryNo]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createThemeIndividual(self, theme):
        for individual in theme.individual:
            self.individual.hasTheme.append(individual)

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createPoetryIndividual(self, poetry):
        self.individual.references.append(poetry.individual)

    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]

    def createFollowsProperty(self, commentary):
        self.individual.follows = [commentary.individual]

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createAddIndividual(self, addElement):
        self.individual.containsAdd.append(addElement.individual)

    def createNoteIndividual(self, note):
        self.individual.hasNote = [note.individual]

    def createHadithTextIndividual(self, hadithText):
        self.individual.hasHadithText.append(hadithText.individual)
