import Owlready
from OntologyClasses.Person import Person


class Narrator(Person, Owlready.OwlInterface):
    def __init__(self, name: str = '', ID: str = None, narratorCounter: int = 0):
        super().__init__()

        self.ID = ID

        self.text = Owlready.processText(Owlready.removeDiacritics(name))

        self.name = 'Nat_' + '{:04}'.format(narratorCounter)

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Narrator(self.name)

    def createDataProperties(self):
        if self.ID is not None:
            self.individual.hasID = [self.ID]

        self.individual.hasName = [self.text]

    def createNarratorTypeIndividual(self, narratorType):
        for t in narratorType.individual:
            self.individual.hasNarratorType.append(t)

    def createHeardFromProperty(self, narrator):
        self.individual.heardFrom.append(narrator.individual)

    def createIDProperty(self):
        if self.ID is not None:
            self.individual.hasID = [self.ID]
