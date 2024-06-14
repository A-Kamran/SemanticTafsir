import Owlready
from OntologyClasses.Person import Person
import json
import os


class Narrator(Person, Owlready.OwlInterface):
    def __init__(self, name: str = '', ID: str = None, narratorCounter: int = 0):
        super().__init__()
        filename = 'narrator_dict.json'

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                narrator_dict = json.load(file)
        else:
            narrator_dict = {}
        
        self.ID = ID

        self.text = Owlready.processText(Owlready.removeDiacritics(name))
        try:
            narrator_dict[self.text]
        except:
            narrator_dict[self.text]=len(narrator_dict)+1
        self.name = 'Nat_' + '{:04}'.format(narrator_dict[self.text])
        print(self.ID,self.name,self.text)

        self.individual = None
        with open(filename, 'w') as file:
            json.dump(narrator_dict, file)
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
