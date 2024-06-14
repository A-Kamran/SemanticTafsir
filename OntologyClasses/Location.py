import Owlready


class Location(Owlready.OwlInterface):
    def __init__(self, locationCounter: int = 0, text: str = None):
        super().__init__()

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.individual = None

        self.name = 'Loc_{}'.format('{:03}'.format(locationCounter))

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Location(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(Owlready.removeDiacritics(self.text))

        self.individual.hasName = [self.text]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)
