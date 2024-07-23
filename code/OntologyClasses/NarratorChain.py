import Owlready


class NarratorChain(Owlready.OwlInterface):
    def __init__(self, name: str = ''):
        super().__init__()

        self.name = 'NC_' + name

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.NarratorChain(self.name)

    def createHadithIndividual(self, hadith):
        self.individual.isPartOfHadith = [hadith.individual]

    def createNarratorChainSegmentIndividual(self, narratorChainSegment):
        self.individual.hasNarratorSegment.append(narratorChainSegment.individual)

    def createRootNarratorChainSegmentIndividual(self, rootNarratorChainSegment):
        self.individual.hasRootNarratorSegment.append(rootNarratorChainSegment.individual)
