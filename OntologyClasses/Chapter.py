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

        self.Sequence = [] #CABB

        self.quran_verses_per_surah = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]



    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Chapter(self.name)

    def createDataProperties(self):

        print("lang: ",self.language)
        print("Text: ",self.text)

        self.individual.hasLanguage = [self.language]
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]
        self.individual.hasChapterNo = [self.chapterNo]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createSectionIndividual(self, section):
        self.individual.containsSection.append(section.individual)

        
    # CABB
    def find_missing_numbers(self,sequence):
        all_numbers = set(range(min(sequence), max(sequence) + 1))
        missing_numbers = list(all_numbers - set(sequence))
        return missing_numbers

    def createVerseIndividual(self, verse,onto):
        for vI in verse:
            
            chNo = vI.hasChapterNo
            vNo = vI.hasVerseNo

            print("upper ",vNo,'---',chNo)

            self.individual.containsVerse.append(vI)

            #  Code added by bilal
            self.Sequence.append(int(vNo[0]))
            self.Sequence.sort()
            print("Seq: ",self.Sequence)

            if len(self.Sequence) == 3:
                if self.Sequence[0] == self.Sequence[1]:
                    self.Sequence = self.Sequence[1:]
                    print("Seq after same same: ",self.Sequence)


            if len(self.Sequence) == 2:
                if self.Sequence[1] - self.Sequence[0] >= 2:
                    missed_verses = self.find_missing_numbers(self.Sequence)
                        # adding those missed verses relation
                    for i in missed_verses:
                        verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(i)) + '*', type=onto.Verse)
                        self.individual.containsVerse.append(verse[0])
                        print(verse[0])
                        print(f'missed verese {i} added')
                elif self.Sequence[1] - self.Sequence[0] == 1:
                    self.Sequence = self.Sequence[1:]
            
            elif len(self.Sequence) == 3:
                self.Sequence = self.Sequence[1:]
                if self.Sequence[1] - self.Sequence[0] >= 2:
                    missed_verses = self.find_missing_numbers(self.Sequence)
                        # adding those missed verses relation
                    for i in missed_verses:
                        verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(i)) + '*', type=onto.Verse)
                        self.individual.containsVerse.append(verse[0])
                        print(f'missed verese {i} added')
                elif self.Sequence[1] - self.Sequence[0] == 1:
                    self.Sequence = self.Sequence[1:]

             # check if all the verses have been added
            if len(vNo) > 0 and len(chNo) > 0 and len(self.Sequence) >= 1:
                C = self.quran_verses_per_surah[int(chNo[0]) - 1]
                if C == (int(self.Sequence[-1:][0]) + 1) and C != int(self.Sequence[-1:][0]):
                    verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(C)) + '*', type=onto.Verse)
                    self.individual.containsVerse.append(verse[0])
                    print("Last missed verse added")


    def createVerseIndividualFromVerseFragment(self, verseFragment, onto):
        
        for vgI in verseFragment:
            chNo = vgI.hasChapterNo
            vNo = vgI.hasVerseNo



            print("Lower ",vNo,'---',chNo)


            if len(chNo) > 0 and len(vNo) > 0:
                verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(vNo[0]))
                                        + '*', type=onto.Verse)

                if verse != []:
                    self.individual.containsVerse.append(verse[0])


                #  Code added by bilal

                self.Sequence.append(int(vNo[0]))
                self.Sequence.sort()
                print("Seq: ",self.Sequence)

                if len(self.Sequence) == 3:
                    if self.Sequence[0] == self.Sequence[1]:
                        self.Sequence = self.Sequence[1:]
                        print("Seq after same same: ",self.Sequence)


                if len(self.Sequence) == 2:
                    if self.Sequence[1] - self.Sequence[0] >= 2:
                        missed_verses = self.find_missing_numbers(self.Sequence)
                         # adding those missed verses relation
                        for i in missed_verses:
                            verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(i)) + '*', type=onto.Verse)
                            if verse != []:
                                self.individual.containsVerse.append(verse[0])
                                print(f'missed verese {i} added')

                    elif self.Sequence[1] - self.Sequence[0] == 1:
                        self.Sequence = self.Sequence[1:]
                elif len(self.Sequence) == 3:
                    self.Sequence = self.Sequence[1:]

                    
                 # check if all the verses have been added
                if len(vNo) > 0 and len(chNo) > 0 and len(self.Sequence) >= 1:
                    C = self.quran_verses_per_surah[int(chNo[0]) - 1]
                    if C == (int(self.Sequence[-1:][0]) + 1) and C != int(self.Sequence[-1:][0]):
                        verse = onto.search(iri='*' + 'V' + '{:03}'.format(int(chNo[0])) + ':' + '{:03}'.format(int(C)) + '*', type=onto.Verse)
                        if verse != []:    
                            self.individual.containsVerse.append(verse[0])
                            print("Last missed verse added")
        

    def createThematicVerseIndividual(self, thematicVerse):
        self.individual.references.append(thematicVerse.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)

    def createCommentaryIndividual(self, commentary):
        self.individual.containsCommentary.append(commentary.individual)

    
    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    # def createVerseFragmentIndividual(self, verseFragment):
        # self.individual.references.append(verseFragment.individual)

    # added by me
    def createSubSectionIndividual(self, subSection):
        self.individual.containsSubSection.append(subSection.individual)
