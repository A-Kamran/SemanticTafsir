import Owlready


class BookLocation(Owlready.OwlInterface):

    def __init__(self, ed: str = '', vol: str = '', pg: str = '', bookLocationCounter: int = 0):
        super().__init__()

        self.edition = ed
        self.volumeNo = vol
        self.pageNo = pg
        self.name = 'BL_' + '{:04}'.format(bookLocationCounter)
        self.individual = None

    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.BookLocation(self.name)
        self.individual.hasEdition = [self.edition]
        self.individual.hasVolumeNo = [self.volumeNo]
        self.individual.hasPageNo = [self.pageNo]
