import Owlready


class SubSection(Owlready.OwlInterface):
    def __init__(self, chapNo: str = '', sectionNo: str = '', subSecNo: str = '', text: str = None):
        super().__init__()

        self.sectionNo = sectionNo
        self.subSectionNo = subSecNo
        self.chapterNo = chapNo

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.name = "SS_" + '{:03}'.format(int(self.chapterNo)) + '.' + '{:03}'.format(int(self.sectionNo)) + '.' + \
                    '{:03}'.format(int(self.subSectionNo))

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.SubSection(self.name)

    def createDataProperties(self):
        self.individual.hasSectionNo = [self.sectionNo]
        self.individual.hasSubSectionNo = [self.subSectionNo]
        self.individual.hasChapterNo = [self.chapterNo]
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createCommentaryIndividual(self, commentary):
        self.individual.containsCommentary.append(commentary.individual)

    def createHadithIndividual(self, hadith):
        self.individual.containsCommentary.append(hadith.individual)

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createFollowsProperty(self, subSection):
        self.individual.follows = [subSection.individual]

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)
