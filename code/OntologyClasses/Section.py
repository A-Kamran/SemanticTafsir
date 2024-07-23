import Owlready


class Section(Owlready.OwlInterface):
    def __init__(self, chapNo: str = '', sectionNo: str = '', text: str = None):
        super().__init__()

        self.sectionNo = sectionNo
        self.chapterNo = chapNo

        if text is not None:
            self.text = text
        else:
            self.text = ''
        self.name = 'S_' + '{:03}'.format(int(self.chapterNo)) + '.' + '{:03}'.format(int(self.sectionNo))
        self.individual = None

        self.verseIndividual = []
        self.verseFragmentIndividual = []

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Section(self.name)

    def createDataProperties(self):
        self.individual.hasChapterNo = [self.chapterNo]
        self.individual.hasSectionNo = [self.sectionNo]

        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createVerseIndividual(self, verse):
        self.individual.isAbout.append(verse)

        self.verseIndividual.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.isAbout.append(verseFragment.individual)

        self.verseFragmentIndividual.append(verseFragment.individual)

    def createCommentaryIndividual(self, commentary):
        self.individual.containsCommentary.append(commentary.individual)

    def createHadithIndividual(self, hadith):
        self.individual.containsCommentary.append(hadith.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createCommentedInProperty(self):
        for vI in self.verseIndividual:
            vI.commentedIn.append(self.individual)

        for vgI in self.verseFragmentIndividual:
            vgI.commentedIn.append(self.individual)

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.isAbout.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.isAbout.append(thematicVerseFragment.individual)

    def createFollowsProperty(self, section):
        self.individual.follows = [section.individual]

    def createSubSectionIndividual(self, subSection):
        self.individual.containsSubSection.append(subSection.individual)

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment = [segment.individual]