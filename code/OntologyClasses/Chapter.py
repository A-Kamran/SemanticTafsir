import Owlready


class Chapter(Owlready.OwlInterface):
    def __init__(self, ch: str = '', lang: str = '', text: str = None):
        super().__init__()

        self.chapterNo = ch
        self.language = lang

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.name = 'C_' + '{:03}'.format(int(self.chapterNo))

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Chapter(self.name)

    def createDataProperties(self):
        self.individual.hasLanguage = [self.language]
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]
        self.individual.hasChapterNo = [self.chapterNo]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createSectionIndividual(self, section):
        self.individual.containsSection.append(section.individual)

    def createVerseIndividual(self, verse):
        for vI in verse:
            self.individual.containsVerse.append(vI)

    def createVerseIndividualFromVerseFragment(self, verseFragment, onto):
        for vgI in verseFragment:
            chNo = vgI.hasChapterNo
            vNo = vgI.hasVerseNo

            if len(chNo) > 0 and len(vNo) > 0:
                verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(vNo[0]))
                                        + '*', type=onto.Verse)

                # since in file 43 this verse list gets empty at some point so applying a check 
                if verse != []:  # this way issue gets resolved
                    self.individual.containsVerse.append(verse[0]) 


    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createCommentaryIndividual(self, commentary):
        self.individual.containsCommentary.append(commentary.individual)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)
