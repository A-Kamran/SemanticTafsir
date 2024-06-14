import Owlready

from OntologyClasses.NarratorChainSegment import NarratorChainSegment


class RootNarratorChainSegment(NarratorChainSegment):
    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.RootNarratorChainSegment(self.name)
