from OntologyClasses.ThematicVerse import *


class ThematicVerseFragment(ThematicVerse):
    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        self.individual = onto.ThematicVerseFragment(self.name)

    def createVerseFragmentIndividual(self, verseFragment):
        self.individual.containsVerseFragment = [verseFragment.individual]
