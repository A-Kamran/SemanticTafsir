import Owlready


class LineBeginning(Owlready.OwlInterface):
    def __init__(self, lb: str = '', lineBeginningCounter: int = 0):
        super().__init__()

        self.text = lb

        self.name = 'LB_' + '{:04}'.format(lineBeginningCounter)

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.LineBeginning(self.name)

        self.text = Owlready.processText(self.text)
        self.individual.hasText = [self.text]
