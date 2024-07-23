import Owlready


class Poetry(Owlready.OwlInterface):
    def __init__(self, name: str = '', text: str = None):
        super().__init__()

        self.name = name

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Poetry(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)


    def createLineBeginningIndividual(self, lineBeginning):
        self.individual.hasLineBeginning = [lineBeginning.individual]


    def createBookLocationIndividual(self, bookLocation):
        self.individual.hasBookLocation = [bookLocation.individual]
