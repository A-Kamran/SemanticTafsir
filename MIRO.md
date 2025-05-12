# MIRO report for the SemanticTafsir ontology
We here report the documentation for the [Semantic Tafsir Ontology](https://github.com/A-Kamran/SemanticTafsir/blob/main/SemanticTafsirOntology.owl) according to the guidelines available in [1].

## A. Basics
1. **Ontology name (MUST)**
Semantic Tafsir Ontology , version 1.0.1

2. **Ontology owner (MUST)**
[Amna Kamran](https://github.com/A-Kamran)

3. **Ontology license (MUST)**
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

4. **Ontology URL (MUST)**
<https://github.com/A-Kamran/SemanticTafsir/blob/main/SemanticTafsirOntology.owl>

5. **Ontology repository (MUST)**
<https://github.com/A-Kamran/SemanticTafsir>

6. **Methodological framework (MUST)**
The SemanticTafsir ontology is developed to encapsulate and preserve the knowledge from Tafsir, focusing on the Quranic commentary structured within its literary context. This ontology serves as a vocabulary to model Quranic verses, Tafsir interpretations, and referenced Hadith

## B. Motivation
1. **Need (MUST)**
The application of semantic web or open data in the Islamic knowledge domain is limited. There is a critical need for a formalized, machine-readable semantic representation of classical Tafsir literature to support digital preservation, scholarly analysis, and semantic interlinking of Quranic exegesis with other Islamic knowledge sources.


2. **Competition (MUST)**
While several ontologies exist for the Quran and Hadith, there is no publicly available ontology specifically designed to model the structure and interpretive content of Tafsir works, particularly those in TEI-encoded classical manuscripts.


3. **Target audience (MUST)**
The ontology is intended for use by digital humanities researchers, Islamic studies scholars, ontology engineers, and developers working on semantic web applications and knowledge graph construction in the domain of religious texts. Hadith Researchers, Students of The Islamic Knowledge. 

## C. Scope, requirements, development community
1. **Scope and coverage (MUST)**
The ontology models the structural and semantic components of Quranic exegesis, beginning with Tafsir al-Tabari. It covers verses, commentary segments, narrators, themes, and intertextual references to Hadith and other Tafsir content, with support for multilingual annotations and TEI-based manuscript structures.
The result is a vocabulary available to develop interoperable applications within the Islamic domain.

2. **Development community (MUST)**
 (IKnex),
 National University of Computer & Emerging Sciences (NUCES-FAST), Islamabad, Pakistan

3. **Communication (MUST)** [Issues](https://github.com/A-Kamran/SemanticTafsir/issues) on Github.

## D. Knowledge acquisition
1. **Knowledge acquisition method (MUST)**
Knowledge was acquired through manual analysis and annotation of the TEI-encoded digital edition of Tafsir al-Tabari, guided by domain expertise in Islamic studies and ontology engineering best practices.

3. **Source knowledge location (SHOULD)** 
The primary source is the TEI XML version of the Tafsir al-Tabari manuscript (Turki edition), available from a private digitization initiative.

5. **Content Selection (SHOULD)** 
Content was selected based on thematic richness, structural consistency, and intertextual relevance to Quranic verses and Hadith, with preference given to segments that illustrate diverse interpretive patterns and narrations.


## E. Ontology content
1. **Knowledge representation language (MUST)**
The ontology is represented in OWL 2 using RDF/XML syntax.

2. **Development environment (OPTIONAL)**
The ontology was developed using Protégé 5.5.0, with reasoning support from HermiT and visualization via GrappDB by ontotext.
OWL API  (Java API for OWL used to build, manipulate and store the ontology in various supported formats)

3. **Ontology metrics (SHOULD)**
The ontology comprises 30+ classes, 35+ object properties, 15+ data properties, and over 25,000 triples in the generated knowledge graph.

4. **Incorporation of other ontologies (MUST)**
[DCTerms](<http://purl.org/dc/terms>), [schema](<http://schema.org>), [dbpedia](<http://dbpedia.org>), [SemanticHadith](<http://www.semantichadith.com/ontology>) , through subclassing and use of owl:equivalentClass and owl:equivalentProperty.

5. **Entity naming convention (MUST)** 
Class names follow CamelCase and are prefixed with tafsir: to ensure namespace clarity and properties are mixed case.

7. **Identifier generation policy (MUST)**
Each resource is assigned a URI based on a stable base namespace and an auto-incremented or meaningful suffix derived from the source TEI data.


8. **Identity metadata policy (MUST)**
All entities have an dcterms:description/ comment natural language explaination to ensure clear identification and contextual understanding.

9. **Upper ontology (MUST)** 
See point E.4. Schema.org and Dublin Core serve as lightweight upper ontologies to ensure alignment with common metadata practices.

10. **Ontology relationships (MUST)**
Hierarchical (rdfs:subClassOf), compositional (schema:hasPart), and referential (tafsir:refersTo) relationships are modeled to capture structural and semantic connections.


11. **Axiom pattern (MUST)**
Design patterns include domain and range constraints, class disjointness, and existential quantification for key properties.

11. **Deferencable URI (OPTIONAL)** 
URIs follow a dereferenceable structure, and hosted [here](http://www.semantichadith.iknex.com)


## F. Managing change
1. **Sustainability plan (MUST)**
Some research projects are being prepared to leverage the ontology. The ontology is maintained in a version-controlled GitHub repository, enabling collaborative development and long-term sustainability.

2. **Entity deprecation strategy (MUST)**
Deprecated terms will be retained with appropriate annotations (owl:deprecated = true) and documentation of replacement terms where applicable.


3. **Versioning policy (MUST)**
The Semantic Hadith ontology adopts sequence-based identifiers for its versions with a major number and a minor number, separated by a dot. A novel release featuring only small changes will cause a switch of the minor number, while relevant and/or structural changes affects also the major number. Semantic versioning is followed (e.g., v1.0.1), with each release documented in the changelog and annotated within the ontology using owl:versionInfo.

## G. Quality assurance
1. **Testing (MUST)**
Tests have been made by checking competency questions in the paper. The Competency Questions with their Sparql Queries and results are available [here](https://github.com/A-Kamran/SemanticTafsir/blob/main/CompetencyQuestionsAndSPARQLQueries.md).
Logical consistency is validated using reasoners such as HermiT and Pellet, with structure reviewed through ontology visualization tools.

3. **Evaluation (MUST)**
Metrics, and discussions over Semantic Tafsir ontology evaluation have been discussed in the paper. Evaluation included MIRO reporting, OOPS! pitfall detection, and alignment against competency questions to assess coverage and accuracy.


4. **Examples of use (MUST)**
Example SPARQL queries demonstrate thematic retrieval, narrator-based analysis, and verse-commentary linking from the knowledge graph.

5. **Institutional endorsement (OPTIONAL)**
The project is developed under the IKNEX Lab, National University of Computer and Emerging Sciences (FAST-NUCES), Islamabad.


6. **Evidence of use (MUST)**
The ontology and KG are publicly available on GitHub and have been used to automate TEI-to-RDF conversion for Tafsir al-Tabari chapters, supporting scholarly exploration and NLP experimentation.


## References
[1] Matentzoglu, N., Malone, J., Mungall, C., & Stevens, R. (2018). MIRO: guidelines for minimum information for the reporting of an ontology. _Journal of biomedical semantics, 9_(1), 6.
