import Owlready
import json
import os

class Person(Owlready.OwlInterface):
    def __init__(self, personCounter: int = 0, text: str = None):
        super().__init__()
        filename = 'narrator_dict.json'

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                narrator_dict = json.load(file)
        else:
            narrator_dict = {}
        
        if text is not None:
            self.text = text
        else:
            self.text = ''
        try:
            narrator_dict[self.text]
        except:
            narrator_dict[self.text]=len(narrator_dict)+1

        self.individual = None

        self.name = 'Per_{}'.format('{:03}'.format(narrator_dict[self.text]))
        with open(filename, 'w') as file:
            json.dump(narrator_dict, file)

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Person(self.name)

    def createDataProperties(self):
        self.text = Owlready.processText(Owlready.removeDiacritics(self.text))

        self.individual.hasName = [self.text]

    def createSegmentIndividual(self, segment):
        self.individual.containsSegment.append(segment.individual)

    def createNameIndividual(self, other):
        self.individual.mentions.append(other.individual)
