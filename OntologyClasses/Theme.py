
import Owlready


class Theme(Owlready.OwlInterface):
    def __init__(self, name: str = None):
        super().__init__()

        if name is not None:
            name = Owlready.processText(name)

            self.name = name.split()

            removalCount = self.name.count('yes')

            try:
                for a in range(0, removalCount):
                    self.name.remove('yes')
            except ValueError:
                pass
        else:
            self.name = []

        self.individual = []

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        for theme in self.name:
            individual = onto.Theme(theme)
            individual.hasName = [theme]
            self.individual.append(individual)
