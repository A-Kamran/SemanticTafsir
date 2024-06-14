import pyquran
import unicodedata

from DatasetClasses.ContainerClasses import *
from OntologyClasses.Add import *
from OntologyClasses.BookLocation import *
from OntologyClasses.Chapter import *
from OntologyClasses.Commentary import *
from OntologyClasses.DataReader import *
from OntologyClasses.DatasetLocation import *
from OntologyClasses.Hadith import *
from OntologyClasses.HadithText import *
from OntologyClasses.LineBeginning import *
from OntologyClasses.Location import *
from OntologyClasses.Narrator import *
from OntologyClasses.NarratorChain import *
from OntologyClasses.NarratorType import *
from OntologyClasses.Note import *
from OntologyClasses.Organization import *
from OntologyClasses.Other import *
from OntologyClasses.Poetry import *
from OntologyClasses.RootNarrator import *
from OntologyClasses.RootNarratorChainSegment import *
from OntologyClasses.Section import *
from OntologyClasses.Segment import *
from OntologyClasses.SubSection import *
from OntologyClasses.SubTheme import *
from OntologyClasses.Surah import *
from OntologyClasses.ThematicVerseFragment import *
from OntologyClasses.Time import *
from OntologyClasses.Verse import *
from OntologyClasses.VerseFragment import *


"""
The function writeSurahVerse reads data from a CSV file containing information about Quranic verses, processes the data,
and creates an ontology structure for Surahs (chapters) and Verses. It iterates through the CSV file line
by line, recognizes new Surahs, and associates Verses with their corresponding Surahs.
The loop terminates when it reaches a particular Surah and Verse combination (Surah 114, Verse 6)

"""
def writeSurahVerse(onto):
    file = open(r'Quran/quran.csv', 'r', encoding='utf-8-sig')

    # Initialize variables to keep track of the current Surah and its number.
    prevSurahNo = -1
    surah = None

    for line in file:
        data = line.split('|') # Split the line into components.

        # if data[0] == '2':
        #     break

        # Extract the Surah number from the data.
        surahNo = int(data[0])

        if surahNo != prevSurahNo:
        # Create an ontology individual for the Surah using Owlready.
            surah = Surah(Owlready.addUnderScore(pyquran.quran.get_sura_name(surahNo)), surahNo)
            surah.createIndividual(onto)

            prevSurahNo = surahNo

        # Create an ontology individual for the Verse and process its text.
        verse = Verse(data[0], data[1], Owlready.processText(data[2]))
        verse.createIndividual(onto)
        verse.createDataProperties()

        # Associate the Verse with its corresponding Surah.
        surah.createVerseIndividual(verse)

        # Exit the loop if we reach a specific Surah and Verse combination (Surah 114, Verse 6).
        if surahNo == 114 and int(data[1]) == 6:
            break


class Writer:
    def __init__(self):

        ## Initialize vairables for the graph
        self.commentaryCounter = 0
        self.hadithCounter = 0
        self.poetryCounter = 0
        self.currentChapter = None
        self.currentCommentary = None
        self.hadithTextCounter = 0
        self.narrators = []
        self.currentHadith = None
        self.currentSection = None
        self.currentSubSection = None
        self.personCounter = 0
        self.organizationCounter = 0
        self.timeCounter = 0
        self.locationCounter = 0
        self.otherCounter = 0
        self.addCounter = 0
        self.bookLocationCounter = 0
        self.datasetLocationCounter = 0
        self.lineBeginningCounter = 0
        self.noteCounter = 0
        self.narratorCounter = 0
        self.rootNarratorCounter = 0

    def write(self, element: list, onto, reference=None):

        """
        processes a list of elements and directs them to various methods based on their "id"
        attribute. Depending on the "id," it performs actions such as writing chapters, sections,
        subsections, commentary, hadiths, poetry, quotes, segments, line beginnings, notes, narrators,
        hadith text, book locations, data set locations, names, and additional content. If an unknown "id"
        is encountered, it prints "Unexpected Element occurred." This function is essentially a dispatcher
        for writing structured data to the graph.
        """

        for a in range(len(element)):
            if element[a].id == "div":
                self.commentaryCounter = 0
                self.hadithCounter = 0
                if element[a].type == "chapter":
                    self._writeChapter(element[a], onto)
                elif element[a].type == "section":
                    self._writeSection(element[a], onto)
                elif element[a].type == "subsection":
                    self._writeSubSection(element[a], onto)
            elif element[a].id == "head":
                self._processHead(element[a], onto, reference)
            elif element[a].id == "p":
                if element[a].n == "nothadith":
                    self.commentaryCounter += 1
                    self._writeCommentary(element[a], onto, reference)
                elif element[a].n == "hadith":
                    self.hadithTextCounter = 0
                    self._writeHadith(element[a], onto, reference)
            elif element[a].id == "quote":
                if element[a].type == "poetry":
                    self.poetryCounter += 1
                    self._writePoetry(element[a], onto, reference)
                else:
                    self._writeQuote(element[a], onto, reference)
            elif element[a].id == "seg":
                self._writeSegment(element[a], onto, reference)
            elif element[a].id == "lb":
                self._writeLineBeginning(element[a], onto, reference)
            elif element[a].id == "note":
                self._writeNote(element[a], onto, reference)
            elif element[a].id == "persName":
                self.narrators.append(element[a])

                if a + 1 < len(element):
                    if element[a + 1].id != "persName":
                        self._writeNarrator(onto, reference)
                else:
                    self._writeNarrator(onto, reference)
            elif element[a].id == "said":
                self.hadithTextCounter += 1
                self._writeHadithText(element[a], onto, reference)
            elif element[a].id == "pb":
                if element[a].type == 'turki':
                    self._writeBookLocation(element[a], onto, reference)
                elif element[a].ed == "GK":
                    self._writeDatasetLocation(element[a], onto, reference)
            elif element[a].id == "l":
                self._processL(element[a], onto, reference)
            elif element[a].id == "lg":
                self._processLG(element[a], onto, reference)
            elif element[a].id == "name":
                self._writeName(element[a], onto, reference)
            elif element[a].id == "add":
                self._writeAdd(element[a], onto, reference)
            else:
                print("Unexpected Element occurred")

    def _writeChapter(self, element: div, onto):

        """

        The _writeChapter function handles chapter elements.
        It checks if the first child is also a chapter and, if
        so, processes its children recursively. If not, it creates
        a new chapter object, sets it as the current chapter, processes
        its children, and creates data properties for the chapter.
        
        """

        if element.children:
            if element.children[0].id == 'div':
                if element.children[0].type == 'chapter':
                    self.write(element.children, onto, None)

                    return

        chapter = Chapter(element.n, element.language)
        chapter.createIndividual(onto)

        self.currentChapter = chapter

        # print("Chapter name ",chapter.name)

        if element.children:
            self.write(element.children, onto, chapter)

        print("elemnt childeen ",element.id)
        chapter.createDataProperties()

    def _processHead(self, element: head, onto, reference):

        """
        The _processHead function handles 'head' elements by
        appending the 'value' attribute to a 'reference' object's text.
        If the element has children, it recursively processes them using
        the 'write' function. Additionally, if there is a 'tail' attribute,
        it appends it to the 'reference' text. The _processHead function
        handles 'head' elements by appending the 'value' attribute to a
        'reference' object's text. If the element has children, it recursively
        processes them using the 'write' function. Additionally, if there is a
        'tail' attribute, it appends it to the 'reference' text.
        
        """

        reference.text += element.value

        if element.children:
            self.write(element.children, onto, reference)

        if element.tail is not None:
            reference.text += element.tail

    def _writeName(self, element: name, onto, reference):

        """
        The _writeName function handles 'name' elements,
        which can be for persons, organizations, times,
        locations, or other entities. It determines the
        'role' of the element and searches the ontology 
        for matching individuals. If a match is found, it
        assigns the 'other' object. If not, it creates a new
        individual, processes its children, sets data properties,
        updates the 'reference' text, and creates a name individual.
        
        """

        other = None

        reader = DataReader()

        data = element.value
        data = reader.read(element.children, data)
        data = Owlready.processText(Owlready.removeDiacritics(data))

        nameFound = False

        if element.role == 'person':
            queriedOthers = onto.search(iri='*Per_' + '*', type=onto.Person)

            for otherElement in queriedOthers:
                if otherElement.hasName:
                    if Owlready.processText(Owlready.removeDiacritics(otherElement.hasName[0])) == data:
                        nameFound = True

                        other = Other(text=data)
                        other.individual = otherElement

                        break

            if other is None:
                self.personCounter += 1
                other = Person(self.personCounter, element.value)
        elif element.role == 'organization':
            queriedOthers = onto.search(iri='*Org_' + '*', type=onto.Organization)

            for otherElement in queriedOthers:
                if otherElement.hasName:
                    if Owlready.processText(Owlready.removeDiacritics(otherElement.hasName[0])) == data:
                        nameFound = True

                        other = Other(text=data)
                        other.individual = otherElement

                        break

            if other is None:
                self.organizationCounter += 1
                other = Organization(self.organizationCounter, element.value)
        elif element.role == 'time':
            queriedOthers = onto.search(iri='*Tim_' + '*', type=onto.Time)

            for otherElement in queriedOthers:
                if otherElement.hasTime:
                    if Owlready.processText(Owlready.removeDiacritics(otherElement.hasTime[0])) == data:
                        nameFound = True

                        other = Other(text=data)
                        other.individual = otherElement

                        break

            if other is None:
                self.timeCounter += 1
                other = Time(self.timeCounter, element.value)
        elif element.role == 'location':
            queriedOthers = onto.search(iri='*Loc_' + '*', type=onto.Location)

            for otherElement in queriedOthers:
                if otherElement.hasName:
                    if Owlready.processText(Owlready.removeDiacritics(otherElement.hasName[0])) == data:
                        nameFound = True

                        other = Other(text=data)
                        other.individual = otherElement

                        break

            if other is None:
                self.locationCounter += 1
                other = Location(self.locationCounter, element.value)
        else:
            queriedOthers = onto.search(iri='*Oth_' + '*', type=onto.Other)

            for otherElement in queriedOthers:
                if otherElement.hasName:
                    if Owlready.processText(Owlready.removeDiacritics(otherElement.hasName[0])) == data:
                        nameFound = True

                        other = Other(text=data)
                        other.individual = otherElement

                        break

            if other is None:
                self.otherCounter += 1
                other = Other(self.otherCounter, element.value, element.type)

        if not nameFound:
            other.createIndividual(onto)

            if element.children:
                self.write(element.children, onto, other)

            other.createDataProperties()

        reference.text += other.text

        if element.tail is not None:
            reference.text += element.tail

        reference.createNameIndividual(other)

    def _writeSection(self, element: div, onto):

        
        """

        The _writeSection function handles 'div' elements,
        likely representing sections. It extracts the section
        number, creates a 'Section' object, and connects it to
        the current section and chapter (if available). It processes
        its children, sets data properties, and establishes relationships
        with the current chapter and verse individuals within the ontology.

        """

        sectionNo = element.n.split('.')

        section = Section(sectionNo[0], sectionNo[1], )
        section.createIndividual(onto)

        if self.currentSection is not None:
            self.currentSection.createFollowsProperty(section)

        self.currentSection = section

        if element.children:
            self.write(element.children, onto, section)

        section.createDataProperties()
        section.createCommentedInProperty()

        if self.currentChapter != None:
            print("currrent chap  is none here section: ",sectionNo)
        
            self.currentChapter.createSectionIndividual(section)

            self.currentChapter.createVerseIndividual(section.verseIndividual,onto)

            self.currentChapter.createVerseIndividualFromVerseFragment(section.verseFragmentIndividual, onto)


    def _writeSubSection(self, element: div, onto):

        """

        The _writeSubSection function handles 'div' elements representing subsections.
        It parses the subsection number, creates a 'SubSection' object, processes its
        children, and sets data properties. It establishes a "follows" relationship with
        the previous subsection, connects the subsection to the current section, and
        updates the current subsection reference.
        
        """

        subSectionNo = element.n.split('.')

        subSection = SubSection(subSectionNo[0], subSectionNo[1], subSectionNo[2])
        subSection.createIndividual(onto)
        if element.children:
            self.write(element.children, onto, subSection)

        subSection.createDataProperties()


        if self.currentSubSection is not None:
            self.currentSubSection.createFollowsProperty(subSection)

        self.currentSection.createSubSectionIndividual(subSection)

        self.currentSubSection = subSection


    def _writeQuote(self, element: quote, onto, reference):
        
        """
        This function processes a given quote element, extracts
        relevant information from its structure and content,
        and then writes corresponding data into an ontology
        (onto). It specifically deals with creating individuals
        representing verses and verse fragments, linking them to
        a parent reference, and handling various cases such as
        grouped verses and qiraat properties. The function involves
        text processing, querying the ontology for existing entities,
        and creating new entities as needed. Additionally, it manages
        the hierarchical structure of the input quote element and updates
        the text content of the parent reference accordingly.
        """

        reader = DataReader()
        data = element.value
        data = reader.read(element.children, data)
        data = Owlready.processText(data)
        withoutDiacritics = Owlready.processText(Owlready.removeDiacritics(data))

        containsSegment = False
        for child in element.children:
            if child.id == "seg" and child.ana != '':
                containsSegment = True
            # else:
                # print('debugg 1: ',child.id)

        verseFragment = None
        verse = None
        verseFragmentFound = None

        groupedVerses = False
        verses = []

        if element.n is not None:
            element.n = unicodedata.normalize('NFKD', element.n).encode('ascii', 'ignore').decode('utf-8')

            # # if condition added by me (bilal)            
            # if element.n == "18:16":
            #     print("we here in writer  ",element)

            chapterNo = element.n.split(':')[0]

            print("list index whaa ",element.n)


            if element.n.split(':')[1].find('-') != -1:

                verseRange = element.n.split(':')[1].split('-')


                if len(verseRange) > 1:
                    verseRange[1] = verseRange[1].split()[0]
            else:
                verseRange = element.n.split(':')[1].split()

                if len(verseRange) > 1:
                    verseRange = [verseRange[0], verseRange[1]]



            verseNo = []

            print("n tag: ",element.n)

            if isinstance(int(verseRange[-1]), int) and int(verseRange[0] != ''): 
                for index in range(int(verseRange[0]), int(verseRange[-1]) + 1):  
                                  
                    verseNo.append(str(index))

            if len(verseNo) > 1:


                groupedVerses = True
                verseFragmentFound = []
            else:
                verseFragmentFound = False

            for index in verseNo:
                verseFragment = None
                verse = None

                if groupedVerses:
                    data = Owlready.processText(reader.readVerseInList(element.children, "", index, None))
 

                    if data == '':
                        data = Owlready.processText(reader.readVerseInList(element.children, "", str(int(index) - 1),
                                                                           'Tail'))
                    withoutDiacritics = Owlready.processText(Owlready.removeDiacritics(data))
                
                print('chapnum: ',chapterNo)
                print('index: ',index)

                print("data: ", data)


                queriedVerses = onto.search(iri='*V' + '{:03}'.format(int(chapterNo)) + ':' + '{:03}'.format(int(index))
                                                + '*', type=onto.Verse)


                if queriedVerses:
                    if Owlready.processText(Owlready.removeDiacritics(queriedVerses[0].hasText[0])) == \
                            withoutDiacritics:
                        verse = Verse(chapterNo, index)

                        verse.individual = queriedVerses[0]
                        verse.parent = reference

                        if not containsSegment:
                            reference.createVerseIndividual(verse.individual)

                        if groupedVerses:
                            verses.append(verse)


                if verse is None:
                    queriedVerseFragments = onto.search(iri='*VF' + '{:03}'.format(int(chapterNo)) + ":" +
                                                            '{:03}'.format(int(index)) + '*', type=onto.VerseFragment)

                    for a in queriedVerseFragments:
                        if a.hasText:
                            if Owlready.processText(Owlready.removeDiacritics(a.hasText[0])) == withoutDiacritics:
                                verseFragment = VerseFragment(str(chapterNo), str(index))
                                verseFragment.individual = a
                                verseFragment.parent = reference

                                if groupedVerses:
                                    verseFragmentFound.append(True)
                                    verses.append(verseFragment)
                                else:
                                    verseFragmentFound = True

                                break

                    if verseFragment is None:
                        verseFragment = VerseFragment(chapterNo, index, element.value, element.subType)
                        verseFragment.createIndividual(onto)
                        verseFragment.parent = reference

                        if groupedVerses:
                            verseFragment.text = data
                            verses.append(verseFragment)
                            verseFragmentFound.append(False)

        if groupedVerses:
            # print("here")
            for vf in verses:
                if element.children:
                    tempText = vf.text

                    for child in element.children:
                        if child.id == 'l':
                            if Owlready.processText(child.n) == vf.verseNo:
                                self.write([child], onto, vf)

                                break
                        else:
                            self.write([child], onto, vf)

                    vf.text = tempText

            reference.text += reader.read(element.children, "")
        elif verse is not None:
            # print("here2")
            if element.children:
                self.write(element.children, onto, verse)


            reference.text += data
        elif verseFragment is not None:
            # print("here3 ", verseFragment )
            if element.children:
                self.write(element.children, onto, verseFragment)

            reference.text += data
        else:
            queriedVerseFragments = onto.search(iri='*VF_*', type=onto.VerseFragment)
            for a in queriedVerseFragments:
                if a.hasText:
                    if Owlready.processText(Owlready.removeDiacritics(a.hasText[0])) == withoutDiacritics:
                        verseFragment = VerseFragment(None, None)
                        verseFragment.individual = a
                        verseFragmentFound = True
                        break

            if verseFragment is None:
                verseFragment = VerseFragment(None, None, element.value, element.subType)
                verseFragment.createIndividual(onto)

            verseFragment.parent = reference

            if element.children:
                self.write(element.children, onto, verseFragment)

            reference.text += data

        if element.tail is not None:
            reference.text += element.tail

        if groupedVerses:
            if not containsSegment:
                for vf in verses:
                    if isinstance(vf, VerseFragment):
                        reference.createVerseFragmentIndividual(vf)

            counter = 0
            for vf in verses:
                if isinstance(vf, VerseFragment):
                    if not verseFragmentFound[counter]:
                        vf.createDataProperties()
                        vf.createVerseProperty(onto)

                        counter += 1

        if verseFragment is not None:
            reference.createVerseFragmentIndividual(verseFragment)

            if not verseFragmentFound:
                verseFragment.createDataProperties()
                verseFragment.createVerseProperty(onto)

            if element.type == 'qiraat':
                if groupedVerses:
                    for vf in verses:
                        if isinstance(vf, VerseFragment):
                            vf.createQiraatProperty()
                else:
                    verseFragment.createQiraatProperty()

    def _writeCommentary(self, element: p, onto, reference):

        """
        The `_writeCommentary` function manages the integration of
        commentary data into an ontology. It first generates a unique
        name for the commentary based on a counter and the reference name,
        creating a corresponding individual in the ontology. If there is a
        current commentary, it establishes a "follows" relationship between
        the new and current commentaries. The function then handles commentary
        themes, creating a Theme individual if an analysis exists and associating
        it with the commentary. It recursively processes child elements and creates
        data properties for the commentary. Finally, it updates the parent reference
        with the newly created commentary individual. Overall, the function orchestrates
        the organization and incorporation of commentary information, ensuring its
        proper representation in the ontology.
        """


        commentaryName = 'C_' + '{:03}'.format(self.commentaryCounter) + '_' + reference.name
        commentary = Commentary(commentaryName, element.value, self.commentaryCounter)
        commentary.createIndividual(onto)

        if self.currentCommentary is not None:
            commentary.createFollowsProperty(self.currentCommentary)
        self.currentCommentary = commentary

        if element.ana is not None and element.ana != '':
            theme = Theme(element.ana)
            if len(theme.name) >= 1:
                theme.createIndividual(onto)
                commentary.createThemeIndividual(theme)

        if element.children:
            self.write(element.children, onto, commentary)

        commentary.createDataProperties()

        reference.createCommentaryIndividual(commentary)

    def _writeSegment(self, element: seg, onto, reference):

        
        """
        The _writeSegment function integrates a segment element (seg)
        into an ontology (onto). It creates a Segment instance and
        processes the text using a DataReader. If an analysis exists,
        a SubTheme instance is created. The function searches for existing
        segments in the ontology and associates the segment with an individual
        and sub-themes if a match is found; otherwise, it creates a new
        segment individual. Child elements are processed recursively,
        and data properties are set. The function updates the parent reference
        text and appends any tail. Depending on the parent reference type and theme
        presence, it creates or associates a ThematicVerse or ThematicVerseFragment
        individual. Finally, an individual for the segment is created in the parent
        reference, ensuring proper representation in the ontology.
        """
        
        segment = Segment(element.value)

        reader = DataReader()

        data = element.value
        data = reader.read(element.children, data)
        data = Owlready.processText(data)
        withoutDiacritics = Owlready.processText(Owlready.removeDiacritics(data))

        containTheme = False
        if element.ana is not None and element.ana != '':
            theme = SubTheme(element.ana)
            if len(theme.name) >= 1:
                containTheme = True
        else:
            theme = SubTheme()

        queriedSegments = onto.search(iri='*SG_*', type=onto.Segment)

        for a in queriedSegments:
            if a.hasText:
                if Owlready.processText(Owlready.removeDiacritics(a.hasText[0])) == withoutDiacritics:
                    queriedThemes = []
                    for b in a.hasSubTheme:
                        temp = str(b)
                        if temp:
                            queriedThemes.append(temp.split('.')[1])

                    if theme.name == queriedThemes:
                        segment.individual = a

                        for b in a.hasSubTheme:
                            theme.individual.append(b)
                        break

        if segment.individual is None:
            segment.createIndividual(onto)

            if element.children:
                self.write(element.children, onto, segment)

            segment.createDataProperties()

            if len(theme.name) >= 1:
                theme.createIndividual(onto)
                segment.createThemeIndividual(theme)

        theme.createIsSubThemeOfProperty(self.currentCommentary)

        reference.text += segment.text

        if element.tail is not None:
            reference.text += element.tail

        if isinstance(reference, Verse) and containTheme:
            thematicVerse = ThematicVerse(reference.name)
            queriedThematicVerses = onto.search(iri='*' + thematicVerse.name + '*', type=onto.ThematicVerse)

            for thVerse in queriedThematicVerses:
                if thVerse.containsVerse[0] == reference.individual:
                    queriedThemes = []
                    for b in thVerse.hasSubTheme:
                        temp = str(b)
                        if temp:
                            queriedThemes.append(temp.split('.')[1])

                    if theme.name == queriedThemes:
                        thematicVerse.individual = thVerse
                        break

            if thematicVerse.individual is None:
                count = len(queriedThematicVerses) + 1
                thematicVerse.name += '_' + str(count)

                thematicVerse.createIndividual(onto)
                thematicVerse.createThemeIndividual(theme)
                thematicVerse.createVerseIndividual(reference.individual)

            reference.parent.createThematicVerseIndividual(thematicVerse)
        elif isinstance(reference, VerseFragment) and containTheme:
            thematicVerseFragment = ThematicVerseFragment(reference.name.split('_')[0])

            queriedThematicVerseFragments = onto.search(iri='*' + thematicVerseFragment.name + '_*',
                                                        type=onto.ThematicVerseFragment)
            for thVerseF in queriedThematicVerseFragments:
                if thVerseF.containsVerseFragment[0] == reference.individual:
                    queriedThemes = []
                    for b in thVerseF.hasSubTheme:
                        temp = str(b)
                        if temp:
                            queriedThemes.append(temp.split('.')[1])

                    if theme.name == queriedThemes:
                        thematicVerseFragment.individual = thVerseF
                        break

            if thematicVerseFragment.individual is None:
                count = len(queriedThematicVerseFragments) + 1
                thematicVerseFragment.name += '_' + str(count)

                thematicVerseFragment.createIndividual(onto)
                thematicVerseFragment.createThemeIndividual(theme)
                thematicVerseFragment.createVerseFragmentIndividual(reference)

            reference.parent.createThematicVerseFragmentIndividual(thematicVerseFragment)

        reference.createSegmentIndividual(segment)

    def _writeHadith(self, element: p, onto, reference):
        hadith = Hadith(element.p_id, element.value)

        if element.p_id is None:
            hadithName = self.currentHadith.name
            if hadithName.find('.') == -1:
                hadith.name = hadithName + '.1'
                hadith.hadithNo = hadith.name.split('_')[1]
            else:
                hadithName = hadithName.split('.')
                hadith.name = hadithName[0] + '.' + str(int(hadithName[1]) + 1)
                hadith.hadithNo = hadith.name.split('_')[1]

        hadith.createIndividual(onto)

        if self.currentCommentary is not None:
            hadith.createFollowsProperty(self.currentCommentary)
        self.currentCommentary = hadith

        self.currentHadith = hadith

        reference.text += hadith.text

        if element.children:
            self.write(element.children, onto, hadith)

        if element.tail is not None:
            reference.text += element.tail
            hadith.text += element.tail

        if element.ana is not None and element.ana != '':
            theme = Theme(element.ana)

            if len(theme.name) >= 1:
                theme.createIndividual(onto)
                hadith.createThemeIndividual(theme)

        reference.createHadithIndividual(hadith)

        hadith.createDataProperties()

    def _writeNarrator(self, onto, reference):
        queriedNarratorChain = onto.search(iri='*NC_01_' + self.currentHadith.name + '*', type=onto.NarratorChain)
        narratorChainCount = len(queriedNarratorChain) + 1

        narratorChain = NarratorChain('{:02}'.format(narratorChainCount) + '_' + self.currentHadith.name)
        narratorChain.createIndividual(onto)

        narratorChain.createHadithIndividual(self.currentHadith)

        self.currentHadith.createNarratorChainIndividual(narratorChain)

        prevChainSegment = None
        prevNarrator = None

        reader = DataReader()

        for a in range(0, len(self.narrators) - 1):
            narratorChainSegment = NarratorChainSegment('NC_' + '{:02}'.format(narratorChainCount) + '_CS_' +
                                                        '{:03}'.format(a + 1) + '_' + self.currentHadith.name)

            narratorChainSegment.createIndividual(onto)

            if prevChainSegment:
                prevChainSegment.createFollowProperty(narratorChainSegment)

            narratorChain.createNarratorChainSegmentIndividual(narratorChainSegment)

            prevChainSegment = narratorChainSegment

            data = self.narrators[a].value
            data = Owlready.processText(Owlready.removeDiacritics(reader.read(self.narrators[a].children, data)))

            queriedNarrators = onto.search(iri='*Nat_*', type=onto.Narrator)

            narrator = None

            for nat in queriedNarrators:
                if nat.hasName[0] == data:
                    if nat.hasID:
                        if nat.hasID[0] == self.narrators[a].n:
                            narrator = Narrator(data, self.narrators[a].n)
                            narrator.individual = nat
                    else:
                        narrator = Narrator(data, self.narrators[a].n)
                        narrator.individual = nat
                        narrator.createIDProperty()

                    break

            if narrator is None:
                self.narratorCounter += 1

                narrator = Narrator(self.narrators[a].value, self.narrators[a].n, self.narratorCounter)
                narrator.createIndividual(onto)
                narrator.createDataProperties()

            if self.narrators[a].children:
                self.write(self.narrators[a].children, onto, narrator)

            narratorType = NarratorType(self.narrators[a].ana, self.narrators[a].type)
            narratorType.createIndividual(onto)

            narrator.createNarratorTypeIndividual(narratorType)

            if prevNarrator:
                prevNarrator.createHeardFromProperty(narrator)

            prevNarrator = narrator

            narratorChainSegment.createNarratorIndividual(narrator)

            reference.text += narrator.text
            if self.narrators[a].tail:
                reference.text += self.narrators[a].tail

        rootNarratorChainSegment = RootNarratorChainSegment('NC_' + '{:02}'.format(narratorChainCount) + '_CS_' +
                                                            '{:03}'.format(len(self.narrators)) + '_'
                                                            + self.currentHadith.name)

        rootNarratorChainSegment.createIndividual(onto)

        if prevChainSegment:
            prevChainSegment.createFollowProperty(rootNarratorChainSegment)

        narratorChain.createRootNarratorChainSegmentIndividual(rootNarratorChainSegment)

        data = self.narrators[-1].value
        data = Owlready.processText(Owlready.removeDiacritics(reader.read(self.narrators[-1].children, data)))

        queriedNarrators = onto.search(iri='*RNat_*', type=onto.RootNarrator)

        rootNarrator = None

        for nat in queriedNarrators:
            if nat.hasName[0] == data:
                if nat.hasID:
                    if nat.hasID[0] == self.narrators[-1].n:
                        rootNarrator = RootNarrator(data, self.narrators[-1].n)
                        rootNarrator.individual = nat
                else:
                    rootNarrator = RootNarrator(data, self.narrators[-1].n)
                    rootNarrator.individual = nat
                    rootNarrator.createIDProperty()

                break

        if rootNarrator is None:
            self.rootNarratorCounter += 1

            rootNarrator = RootNarrator(self.narrators[-1].value, self.narrators[-1].n, self.rootNarratorCounter)
            rootNarrator.createIndividual(onto)
            rootNarrator.createDataProperties()

        if self.narrators[-1].children:
            self.write(self.narrators[-1].children, onto, rootNarrator)

        narratorType = NarratorType(self.narrators[-1].ana, self.narrators[-1].type)
        narratorType.createIndividual(onto)

        rootNarrator.createNarratorTypeIndividual(narratorType)

        if prevNarrator:
            prevNarrator.createHeardFromProperty(rootNarrator)

        rootNarratorChainSegment.createNarratorIndividual(rootNarrator)

        reference.text += rootNarrator.text
        if self.narrators[-1].tail:
            reference.text += self.narrators[-1].tail

        self.narrators.clear()

    def _writeHadithText(self, element: said, onto, reference):
        hadithNo = self.currentHadith.hadithNo
        hadithTextName = 'HT_' + '{:02}'.format(self.hadithTextCounter) + '_' + self.currentHadith.name

        hadithText = HadithText(hadithTextName, element.value, hadithNo)
        hadithText.createIndividual(onto)

        if element.children:
            self.write(element.children, onto, hadithText)

        reference.text += hadithText.text

        if element.tail is not None:
            reference.text += element.tail
            hadithText.text += element.tail

        hadithText.createDataProperties()

        reference.createHadithTextIndividual(hadithText)

    def _writePoetry(self, element: quote, onto, reference):
        poetryName = 'P_' + '{:03}'.format(self.poetryCounter)
        poetry = Poetry(poetryName)
        poetry.createIndividual(onto)

        if element.children:
            self.write(element.children, onto, poetry)

        if element.tail is not None:
            reference.text += element.tail

        poetry.createDataProperties()

        reference.createPoetryIndividual(poetry)

    def _processLG(self, element: lg, onto, reference):
        if element.children:
            self.write(element.children, onto, reference)

        if element.tail is not None:
            reference.text += element.tail

    def _processL(self, element: l, onto, reference):
        reference.text += element.value

        if element.children:
            self.write(element.children, onto, reference)

        if element.tail is not None:
            reference.text += element.tail

    def _writeAdd(self, element: add, onto, reference):
        addElement = None

        reader = DataReader()

        data = element.value
        data = reader.read(element.children, data)
        data = Owlready.processText(Owlready.removeDiacritics(data))

        addFound = False

        queriedAdd = onto.search(iri='*Add_' + '*', type=onto.Add)

        for addObject in queriedAdd:
            if Owlready.processText(Owlready.removeDiacritics(addObject.hasText[0])) == data and \
                    addObject.hasType[0] == Owlready.processText(element.type):
                addFound = True

                addElement = Add(tagType=addObject.hasType[0], text=data)
                addElement.individual = addObject

                break

        if not addFound:
            self.addCounter += 1
            addElement = Add(self.addCounter, element.type, element.value)

            addElement.createIndividual(onto)

            if element.children:
                self.write(element.children, onto, addElement)

            addElement.createDataProperties()

        reference.text += addElement.text

        if element.tail is not None:
            reference.text += element.tail

        reference.createAddIndividual(addElement)

    def _writeBookLocation(self, element: pb, onto, reference):
        self.bookLocationCounter += 1

        temp = element.n.split(':')
        bookLocation = BookLocation(element.type, temp[0], temp[1], self.bookLocationCounter)
        bookLocation.createIndividual(onto)

        reference.createBookLocationIndividual(bookLocation)

        if element.tail is not None:
            reference.text += element.tail

    def _writeDatasetLocation(self, element: pb, onto, reference):
        self.datasetLocationCounter += 1

        datasetLocation = DatasetLocation(element.ed, element.edRef, element.n, self.datasetLocationCounter)
        datasetLocation.createIndividual(onto)

        reference.createDatasetLocationIndividual(datasetLocation)

        if element.tail is not None:
            reference.text += element.tail

    def _writeLineBeginning(self, element: lb, onto, reference):
        self.lineBeginningCounter += 1

        lineBeginning = LineBeginning(element.n, self.lineBeginningCounter)
        lineBeginning.createIndividual(onto)

        reference.createLineBeginningIndividual(lineBeginning)

        if element.tail is not None:
            reference.text += element.tail

    def _writeNote(self, element: note, onto, reference):
        self.noteCounter += 1

        n = Note(element.value, self.noteCounter)
        n.createIndividual(onto)

        reference.createNoteIndividual(n)

        if element.tail is not None:
            reference.text += element.tail
