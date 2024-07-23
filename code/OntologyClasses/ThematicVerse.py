import Owlready


class ThematicVerse(Owlready.OwlInterface):
    def __init__(self, name: str = ''):
        super().__init__()

        self.name = 'T' + name

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.ThematicVerse(self.name)

    def createThemeIndividual(self, theme):
        for th in theme.individual:
            self.individual.hasSubTheme.append(th)

    def createVerseIndividual(self, verse):
        self.individual.containsVerse = [verse]
