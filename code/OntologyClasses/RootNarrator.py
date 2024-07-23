import Owlready
from OntologyClasses.Narrator import Narrator


class RootNarrator(Narrator):
    def __init__(self, name: str = '', ID: str = None, narratorCounter: int = 0):
        super().__init__(name, ID, narratorCounter)

        self.name = 'RNat_' + '{:04}'.format(narratorCounter)

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.RootNarrator(self.name)
