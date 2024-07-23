def _writeQuote(self, element: quote, onto, reference):
    # Create a DataReader instance for reading data from the quote element
    reader = DataReader()

    # Extract the value from the quote element
    data = element.value
    # Read additional data from the quote element using the DataReader
    data = reader.read(element.children, data)
    # Process the text using Owlready (assuming Owlready is a library)
    data = Owlready.processText(data)
    # Remove diacritics from the text and process it
    withoutDiacritics = Owlready.processText(Owlready.removeDiacritics(data))

    # Initialize variables for verse and verse fragment processing
    containsSegment = False
    verseFragment = None
    verse = None
    verseFragmentFound = None
    groupedVerses = False
    verses = []

    # Check if the element contains a segment with non-empty analysis
    for child in element.children:
        if child.id == "seg" and child.ana != '':
            containsSegment = True

    # Initialize variables for processing chapter and verse numbers
    chapterNo = None
    verseRange = None
    verseNo = None

    # Process chapter and verse numbers
    if element.n is not None:
        element.n = unicodedata.normalize('NFKD', element.n).encode('ascii', 'ignore').decode('utf-8')

        chapterNo = element.n.split(':')[0]

        # Print the current chapter and verse numbers for debugging
        print("list index whaa ", element.n)

        # Process verse ranges
        if element.n.split(':')[1].find('-') != -1:
            verseRange = element.n.split(':')[1].split('-')

            if len(verseRange) > 1:
                verseRange[1] = verseRange[1].split()[0]
        else:
            verseRange = element.n.split(':')[1].split()

            if len(verseRange) > 1:
                verseRange = [verseRange[0], verseRange[1]]

        # Initialize verse numbers list
        verseNo = []

        # Process individual verse numbers
        if isinstance(int(verseRange[-1]), int) and int(verseRange[0] != ''):
            for index in range(int(verseRange[0]), int(verseRange[-1]) + 1):
                verseNo.append(str(index))

        # Process grouped verses
        if len(verseNo) > 1:
            groupedVerses = True
            verseFragmentFound = []

    # Iterate through individual verse numbers
    for index in verseNo:
        verseFragment = None
        verse = None

        if groupedVerses:
            # Process grouped verses using the DataReader
            data = Owlready.processText(reader.readVerseInList(element.children, "", index, None))

            if data == '':
                data = Owlready.processText(reader.readVerseInList(element.children, "", str(int(index) - 1), 'Tail'))
            withoutDiacritics = Owlready.processText(Owlready.removeDiacritics(data))

        # Search for queried verses in the ontology
        queriedVerses = onto.search(iri='*V' + '{:03}'.format(int(chapterNo)) + ':' + '{:03}'.format(int(index))
                                    + '*', type=onto.Verse)

        # Process queried verses
        if queriedVerses:
            if Owlready.processText(Owlready.removeDiacritics(queriedVerses[0].hasText[0])) == withoutDiacritics:
                verse = Verse(chapterNo, index)

                verse.individual = queriedVerses[0]
                verse.parent = reference

                # Create Verse individual in the ontology if it doesn't contain a segment
                if not containsSegment:
                    reference.createVerseIndividual(verse.individual)

                # Process grouped verses
                if groupedVerses:
                    verses.append(verse)

        # Process individual verse fragments
        if verse is None:
            queriedVerseFragments = onto.search(iri='*VF' + '{:03}'.format(int(chapterNo)) + ":" +
                                                    '{:03}'.format(int(index)) + '*', type=onto.VerseFragment)

            for a in queriedVerseFragments:
                if a.hasText:
                    if Owlready.processText(Owlready.removeDiacritics(a.hasText[0])) == withoutDiacritics:
                        verseFragment = VerseFragment(str(chapterNo), str(index))
                        verseFragment.individual = a
                        verseFragment.parent = reference

                        # Process grouped verses
                        if groupedVerses:
                            verseFragmentFound.append(True)
                            verses.append(verseFragment)
                        else:
                            verseFragmentFound = True

                        break

            # Create a new VerseFragment if it doesn't exist
            if verseFragment is None:
                verseFragment = VerseFragment(chapterNo, index, element.value, element.subType)
                verseFragment.createIndividual(onto)
                verseFragment.parent = reference

                # Process grouped verses
                if groupedVerses:
                    verseFragment.text = data
                    verses.append(verseFragment)
                    verseFragmentFound.append(False)

    # Process grouped verses
    if groupedVerses:
        for vf in verses:
            if element.children:
                tempText = vf.text

                # Iterate through children elements
                for child in element.children:
                    if child.id == 'l':
                        if Owlready.processText(child.n) == vf.verseNo:
                            self.write([child], onto, vf)
                            break
                    else:
                        self.write([child], onto, vf)

                vf.text = tempText

        # Update the reference text with the processed data
        reference.text += reader.read(element.children, "")
    # Process individual verse
    elif verse is not None:
        if element.children:
            # Recursively process child elements
            self.write(element.children, onto, verse)

        # Update the reference text with the processed data
        reference.text += data
    # Process individual verse fragment
    elif verseFragment is not None:
        if element.children:
            # Recursively process child elements
            self.write(element.children, onto, verseFragment)

        # Update the reference text with the processed data
        reference.text += data
    else:
        # Process individual verse fragment if it doesn't exist
        queriedVerseFragments = onto.search(iri='*VF_*', type=onto.VerseFragment)
        for a in queriedVerseFragments:
            if a.hasText:
                if Owlready.processText(Owlready.removeDiacritics(a.hasText[0])) == withoutDiacritics:
                    verseFragment = VerseFragment(None, None)
                    verseFragment.individual = a
                    verseFragmentFound = True
                    break

        # Create a new VerseFragment if it doesn't exist
        if verseFragment is None:
            verseFragment = VerseFragment(None, None, element.value, element.subType)
            verseFragment.createIndividual(onto)

        # Update the parent reference
        verseFragment.parent = reference

        if element.children:
            # Recursively process child elements
            self.write(element.children, onto, verseFragment)

        # Update the reference text with the processed data
        reference.text += data

    # Update the reference text with the tail of the element
    if element.tail is not None:
        reference.text += element.tail

    # Process grouped verses
    if groupedVerses:
        if not containsSegment:
            for vf in verses:
                if isinstance(vf, VerseFragment):
                    reference.createVerseFragmentIndividual(vf)

        # Counter for grouped verses
        counter = 0
        for vf in verses:
            if isinstance(vf, VerseFragment):
                if not verseFragmentFound[counter]:
                    vf.createDataProperties()
                    vf.createVerseProperty(onto)

                counter += 1

    # Process individual verse fragment
    if verseFragment is not None:
        reference.createVerseFragmentIndividual(verseFragment)

        # Process individual verse fragment if it doesn't exist
        if not verseFragmentFound:
            verseFragment.createDataProperties()
            verseFragment.createVerseProperty(onto)

        # Process qiraat property for individual verse fragments
        if element.type == 'qiraat':
            if groupedVerses:
                for vf in verses:
                    if isinstance(vf, VerseFragment):
                        vf.createQiraatProperty()
            else:
                verseFragment.createQiraatProperty()
