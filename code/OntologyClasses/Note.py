import Owlready


class Note(Owlready.OwlInterface):
    def __init__(self, text: str = None, noteCounter: int = 0):
        super().__init__()

        if text is None:
            self.text = ''
        else:
            self.text = text

        self.name = 'Note_' + '{:04}'.format(noteCounter)

        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.Note(self.name)

        self.text = Owlready.removeSpace(Owlready.processText(self.text))
        self.individual.hasText = [self.text]
