import Owlready


class Other(Owlready.OwlInterface):
    def __init__(self, otherCounter: int = 0, text: str = None, nameType: str = None):
        super().__init__()

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.type = None

        if nameType is not None:
            if '' != nameType != 'other':
                self.type = nameType

        self.individual = None

        self.name = 'Oth_{}'.format('{:03}'.format(otherCounter))

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Other(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(Owlready.removeDiacritics(self.text))

        self.individual.hasName = [self.text]

        if self.type is not None:
            self.individual.hasType = [self.type]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)
