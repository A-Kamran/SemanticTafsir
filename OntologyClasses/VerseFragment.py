import Owlready


class VerseFragment(Owlready.OwlInterface):
    def __init__(self, chapNo: str = None, verseNo: str = None, text: str = None, subType: str = None):
        super().__init__()

        if chapNo is not None:
            self.chapterNo = chapNo
        else:
            self.chapterNo = None

        if verseNo is not None:
            self.verseNo = verseNo
        else:
            self.verseNo = None

        self.subType = subType

        if text is not None:
            self.text = text
        else:
            self.text = ''

        if self.chapterNo is not None and self.verseNo is not None:
            self.name = 'VF' + '{:03}'.format(int(self.chapterNo)) + ":" + '{:03}'.format(int(self.verseNo)) + '_'
        else:
            self.name = 'VF_'

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        count = len(onto.search(iri='*' + self.name + '*', type=onto.VerseFragment))
        count += 1
        self.name += '{:03}'.format(int(count))
        
        self.individual = onto.VerseFragment(self.name)

    def createDataProperties(self):
        if self.chapterNo is not None:
            self.individual.hasChapterNo = [self.chapterNo]

        if self.verseNo is not None:
            self.individual.hasVerseNo = [self.verseNo]

        if self.text != '':
            self.text = Owlready.processText(self.text)

            self.individual.hasText = [self.text]

         #check added by me
        if self.verseNo is not None and int(self.verseNo) == 2:        
            print(" >>>>>>>> VF name: ",self.name," Text: ",self.text)

        if self.subType is not None:
            self.individual.hasSubType = [self.subType]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createVerseProperty(self, onto):
        if self.chapterNo is not None and self.verseNo is not None:
            verses = onto.search(iri='*' + 'V' + '{:03}'.format(int(self.chapterNo)) + ':' +
                                     '{:03}'.format(int(self.verseNo)) + '*', type=onto.Verse)
            if verses:
                self.individual.isPartOfVerse = [verses[0]]

                verses[0].containsVerseFragment.append(self.individual)

    def createQiraatProperty(self):
        self.individual.hasType = ['qiraat']

    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]

    def createDatasetLocationIndividual(self, datasetLocation):
        self.individual.hasDatasetLocation = [datasetLocation.individual]

    def createAddIndividual(self, addElement):
        self.individual.containsAdd.append(addElement.individual)

    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    
    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createHadithTextIndividual(self, hadithText):
        self.individual.hasHadithText.append(hadithText.individual)

    
    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)
