import Owlready


class NarratorChainSegment(Owlready.OwlInterface):
    def __init__(self, name: str = ''):
        super().__init__()

        self.name = name

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.NarratorChainSegment(self.name)

    def createNarratorIndividual(self, narrator):
        self.individual.refersTo = [narrator.individual]

    def createFollowProperty(self, segment):
        self.individual.follows.append(segment.individual)
