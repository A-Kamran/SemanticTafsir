import Owlready
from OntologyClasses.Narrator import Narrator
import json
import os

class RootNarrator(Narrator):
    def __init__(self, name: str = '', ID: str = None, narratorCounter: int = 0):
        super().__init__(name, ID, narratorCounter)
        filename = 'narrator_dict.json'

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                narrator_dict = json.load(file)
        else:
            narrator_dict = {}

        print("THIS IS FROM ROOT NARRATOR: ",self.text)

        try:
            narrator_dict[self.text]
        except:
            narrator_dict[self.text]=len(narrator_dict)+1

        self.name = 'RNat_' + '{:04}'.format(narrator_dict[self.text])

        with open(filename, 'w') as file:
            json.dump(narrator_dict, file)


    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.RootNarrator(self.name)
