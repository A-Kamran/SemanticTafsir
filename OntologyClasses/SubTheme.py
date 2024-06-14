from OntologyClasses.Theme import *


class SubTheme(Theme):
    def createIndividual(self, onto: Owlready.owlready2.namespace.Ontology):
        for theme in self.name:
            individual = onto.SubTheme(theme)
            individual.hasName = [theme]
            self.individual.append(individual)

    def createIsSubThemeOfProperty(self, commentary):
        if commentary != None:
            # print(self.name)
            # print("COmmentary: ",commentary)
            if commentary.individual.hasTheme:
                theme = commentary.individual.hasTheme
                for a in theme:
                    for b in self.individual:
                        b.isSubThemeOf.append(a)
        else:
            print("None type issue ..lets see: ",self.name)


