import Owlready


class NarratorType(Owlready.OwlInterface):
    def __init__(self, narratorType: str = '', themeType: str = ''):
        super().__init__()

        if narratorType is not None:
            narratorType = Owlready.processText(narratorType)

            self.type = narratorType.split()
        else:
            self.type = None

        if themeType is not None:
            themeType = Owlready.processText(themeType)

            if self.type is not None:
                self.type += themeType.split()
            else:
                self.type = themeType.split()

        self.individual = []

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        if self.type is not None:
            for narratorType in self.type:
                individual = onto.NarratorType(narratorType)
                individual.hasType = [narratorType]

                self.individual.append(individual)
