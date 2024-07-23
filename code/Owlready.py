import pyarabic.araby
from owlready2 import *

from Reader.Parser import surahNo
from config import ontologyBaseUrl


def loadOnto() -> owlready2.namespace.Ontology:
    onto = get_ontology(
        # Creating and importing the ontology
        r"A-Box/Tafsir Al-Tabari T-Box.owl")
    onto_path.append(ontologyBaseUrl)  # Specify your local repository
    onto.load()  # Loading the ontology
    return onto


def saveOnto(onto: owlready2.namespace.Ontology, individualSurah: bool):
    if individualSurah:
        onto.save(file=r'A-Box/Tafsir Al-Tabari A-Box S' + surahNo[0] + '.owl')  # Saving the ontology
    else:
        onto.save(file=r'A-Box/Tafsir Al-Tabari A-Box Combined.owl')  # Saving the ontology


class OwlInterface:
    def __init__(self):
        self.parent = None
        self.name = None
        self.individual = None

    def createIndividual(self, onto: owlready2.namespace.Ontology):
        pass

    def createDataProperties(self):
        pass


def processText(text: str) -> str:
    text = text.replace('\t', '')
    text = text.replace('\n', ' ')

    while text.find('  ') != -1:
        text = text.replace('  ', ' ')

    text = text.strip()

    return text


def removeSpace(text: str) -> str:
    while text.find(' ') != -1:
        text = text.replace(' ', '')

    return text


def addUnderScore(text: str) -> str:
    text = text.replace(' ', '_')
    if text.find('_') == -1:
        text.replace('\n', '_')
    else:
        text.replace('\n', '')

    return text


def removeDiacritics(text: str) -> str:
    for a in pyarabic.araby.DIACRITICS:
        text = text.replace(a, '')

    return text
