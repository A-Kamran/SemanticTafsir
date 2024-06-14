import Owlready


class Add(Owlready.OwlInterface):
    def __init__(self, addCounter: int = 0, tagType: str = None, text: str = None):
        super().__init__()

        if text is not None:
            self.text = text
        else:
            self.text = ''

        if tagType is not None:
            self.type = tagType
        else:
            self.type = ''

        self.name = 'Add_{}'.format('{:03}'.format(addCounter))

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Add(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

        self.type = Owlready.processText(self.type)
        self.individual.hasType = [self.type]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment = [segment.individual]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createVerseIndividual(self, verse):
        self.individual.references.append(verse)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.references.append(verseFragment.individual)

    def createThematicVerseFragmentIndividual(self, thematicVerseFragment):
        self.individual.references.append(thematicVerseFragment.individual)
