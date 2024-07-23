import Owlready


class DatasetLocation(Owlready.OwlInterface):
    def __init__(self, ed: str = '', ref: str = '', pg: str = '', datasetLocationCounter: int = 0):
        super().__init__()

        self.edition = ed
        self.referenceNo = ref
        self.pageNo = pg

        self.name = 'DL_' + '{:04}'.format(datasetLocationCounter)

        self.individual = None

    def createIndividual(self, onto):
        self.individual = onto.DatasetLocation(self.name)
        self.individual.hasReferenceNo = [self.referenceNo]
        self.individual.hasEdition = [self.edition]
        self.individual.hasPageNo = [self.pageNo]
