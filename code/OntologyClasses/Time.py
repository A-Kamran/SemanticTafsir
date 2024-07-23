import Owlready


class Time(Owlready.OwlInterface):
    def __init__(self, timeCounter: int = 0, text: str = None):
        super().__init__()

        if text is not None:
            self.text = text
        else:
            self.text = ''

        self.individual = None

        self.name = 'Tim_{}'.format('{:03}'.format(timeCounter))

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Time(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(Owlready.removeDiacritics(self.text))

        self.individual.hasTime = [self.text]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)
