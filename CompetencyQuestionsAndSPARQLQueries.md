# Competency questions for the Semantic Hadith ontology

The given SPARQL are _examples_ that may be reinterpreted and reused for applications.

### Competency Question 1:
**Question:** What is the source URL for Hadith X?

**SPARQL Query:**
```
```

### Competency Question 2:
**Question:** Does every Hadith 'discussesTopic' a Topic?

**SPARQL Query:**
```
SELECT DISTINCT ?hadith
WHERE {
  ?hadith rdf:type :Hadith .
  FILTER NOT EXISTS {
    ?hadith :discussesTopic ?topic .
  }
}
```
### Competency Question 3:
**Question:** What Hadith is similar to Hadith X?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?similarHadith
WHERE {
  ?similarHadith :isSimilar :SB-HD0001 .
}
```
### Competency Question 4:
**Question:** How many hadith narrations are 'partOf' a Hadith Collection Y?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT (COUNT(?hadith) AS ?count)
WHERE {
  ?hadith a :Hadith.
  ?hadith :isPartOfChapter ?chap.
  ?chap :isPartOfBook ?book.
  ?book :isPartOfCollection :SB01 .
}
```
### Competency Question 5:
**Question:** What are the types of Hadith?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT DISTINCT ?type
WHERE {
  ?hadith :hasHadithType ?type .
 
}
```
### Competency Question 6:
**Question:** Which Hadith 'containMentionOf' Event X?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT ?hadith 
WHERE {
  ?hadith :containsMentionOf :EidAdha.
}
```
### Competency Question 7:
**Question:** Find Hadith 'discussesTopic' Topic X.

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT ?hadith ?hadithText
WHERE {
  ?hadith :discussesTopic :DayOfResurrection .
   ?hadith :fullHadithText  ?hadithText.
}
```
### Competency Question 8:
**Question:** How many Hadith 'containsMentionOf' Location X?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT (COUNT(?hadith) AS ?count)
WHERE {
  ?hadith :containsMentionOf :Madina .
}
```
### Competency Question 9:
**Question:** Does Hadith X 'containsMentionOf' Person Y?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
ASK
WHERE {
  :SB-HD2324 :containsMentionOf :AbuBakr .

}
```
```
PREFIX : <http://www.semantichadith.com/ontology/>
Select  ?hadith ?hadithText
WHERE {
?hadith :containsMentionOf :AbuBakr .
   ?hadith :fullHadithText  ?hadithText.
}
```
### Competency Question 10:
**Question:** Is there a hadith that 'containMentionOf' Prophet A?

**SPARQL Query:**
```
ASK
WHERE {
  ?hadith :containsMentionOf :Musa .
}
```
```
PREFIX : <http://www.semantichadith.com/ontology/>
Select  ?hadith ?hadithText
WHERE {
?hadith :containsMentionOf :Musa .
   ?hadith :fullHadithText  ?hadithText.
}
```
### Competency Question 11:
**Question:** Which individuals are 'mentionedIn' Event A described in a Hadith?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT DISTINCT ?hadith ?hadithText ?individual
WHERE {
  ?hadith :containsMentionOf :EidAdha .
  ?hadith :containsMentionOf ?individual .
       ?hadith :fullHadithText  ?hadithText.

	 ?individual a :HistoricPerson.
}
```
### Competency Question 12:
**Question:** Are there specific entities 'mentionedIn' Hadith narrated by certain individuals?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT DISTINCT ?hadith  ?entity
WHERE {
  ?hadith :containsMentionOf ?entity .
   ?hadith :hasNarratorChain/:hasRootNarratorSegment/:refersToNarrator :HN05913 .
}
```
### Competency Question 13:
**Question:** Which narrators have not narrated any sacred Hadith?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?narrator
WHERE {
  ?narrator rdf:type :HadithNarrator .
  MINUS {
        ?narrator ^(:hasNarratorChain/:hasNarratorSegment:refersToNarrator) ?hadith.
    ?hadith rdf:type/rdfs:subClassOf* :Sacred_Hadith .
  }
}
```
### Competency Question 14:
**Question:** How many entities are mentioned in Hadith X?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(DISTINCT ?companion) AS ?count)
WHERE { 
    :SB-HD4877   :containsMentionOf ?companion .
  ?companion rdf:type/rdfs:subClassOf* :Companion .
}
```
### Competency Question 15:
**Question:** What type of Hadith is Hadith X?

**SPARQL Query:**
```
PREFIX : <http://www.semantichadith.com/ontology/>
SELECT DISTINCT ?hadithType
WHERE {
  :SB-HD4877 :hasHadithType ?hadithType .
}
```
### Competency Question 16:
**Question:** Which Hadith narrations have more than x number of narrators?

**SPARQL Query:**
```
 PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?hadith ?numNarrators
WHERE {
  ?hadith :hasNarratorChain ?chain .
  {
    SELECT ?hadith (COUNT(?narrator) AS ?numNarrators)
    WHERE {
      ?hadith :hasNarratorChain/:hasNarratorSegment/:refersToNarrator ?narrator .
    }
    GROUP BY ?hadith
  }
  FILTER (?numNarrators > 3)
}
```
### Competency Question 17:
**Question:** What is the most narrated Topic by Narrator A?

**SPARQL Query:**
```
 PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?topic (COUNT(?hadith) AS ?numHadiths)
WHERE {
  ?hadith :discussesTopic ?topic .
  ?hadith :hasNarratorChain/:hasNarratorSegment/:refersToNarrator :HN04903 .
}
GROUP BY ?topic
ORDER BY DESC(?numHadiths)
LIMIT 1
```
### Competency Question 18:
**Question:** Which topics are discussed by at least three Hadith narrations?

**SPARQL Query:**
```
 PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?topic
WHERE {
  ?hadith :discussesTopic ?topic .
}
GROUP BY ?topic
HAVING (COUNT(?hadith) >= 3)
```



**Question:** Which Hadith 'containsMentionOf' Verse 1 of Surah 111?
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
select 	?hadith ?verse
where { 
	?hadith rdf:type :Hadith .
    ?hadith :containsMentionOf ?verse
} 
VALUES (?verse)
{
    (:CH111_V001)
}
```

**Question:** Hadith Contains Mention of Quranic Verse
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>
select * where { 
	?s rdf:type :Hadith.
    ?s :containsMentionOf ?v.
} limit 100 
```
 <!-- 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>
construct 
{ 
    ?s rdf:type :Hadith.
    ?s :containsMentionOf ?v.
    ?v rdf:type :Verse.
}
where { 
	?s rdf:type :Hadith.
    ?s :containsMentionOf ?v.
} limit 100 
--> 
<img width="1107" alt="image" src="https://github.com/A-Kamran/SemanticHadithKG/assets/97387765/9c63ac0b-5e74-40e8-9c8e-ff07eb2b895a">


**Question:**  How many hadith were narrated by RAWI_A? 
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select (COUNT (?name) AS ?num)
where 
{ 
	?hadith rdf:type :Hadith .
    ?hadith :hasNarratorChain ?o .
    ?o :hasNarratorSegment	 ?x .
    ?x :refersToNarrator+	 ?y .
    ?y :name ?name
    
} 
VALUES (?name)
{
    ("عبد الله بن يوسف@ar")
}
```


**Question:**  What is the 'Lineage' of a particular narrator? 
```
PREFIX : <http://www.semantichadith.com/ontology/>

select ?lineage
where
{
    :HN05913 :lineage ?lineage.
}
```

**Question:**  Show if any 2 Narrators share same deathPlace "المدينة" 
```
PREFIX : <http://www.semantichadith.com/ontology/>

select  ?narrators
where 
{ 
    ?narrators rdf:type :HadithNarrator .
    ?narrators :deathPlace "المدينة".
}
```


**Question:**  Who is the Root Narrator of a given Hadith?  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?root ?narrator ?name
where 
{ 
    :SB-HD0001 :hasNarratorChain ?Chain. 
    ?Chain :hasRootNarratorSegment ?root.
    ?root :refersToNarrator ?narrator.
    ?narrator :name ?name
    
}  
```

**Question:**  How many Hadith 'containsMentionOf' Verse X?  
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

Select (count(?hadith) as ?numberOfhadith) 
where { 
	?hadith rdf:type :Hadith .
    ?hadith :containsMentionOf ?verse
} 
VALUES (?verse)
{
    (:CH111_V001)
}
```

**Question:**  Find all Hadith related to Hadith_X?  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?hadith
where 
{ 
    :SB-HD0001 rdf:seeAlso ?hadith.  
}  
```

**Question:**  What is the Hadith Type of Hadith_X.  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?hadithType 
where 
{ 
    :SB-HD0001 :hasHadithType ?hadithType. 
}  
```



**Question:**  Mention all Narrators and the RootNarrator for a given Hadith  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?name
where 
{ 
    :SB-HD0001 :hasNarratorChain ?Chain. 
    ?Chain :hasNarratorSegment ?root.
    ?root :refersToNarrator ?narrator.
    ?narrator :name ?name
    
}  
```

**Question:**  What are the types of Hadith?  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
select ?hadithType
where 
{ 
    ?hadithType rdf:type :HadithType.
 
} 
```


**Question:**  What is the frequency of a specific chain or part of chain i.e. How many times A->B->C is repeated.  

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 
where {
    ?h :hasNarratorChain/:hasNarratorSegment ?ns1.
    ?ns1 :refersToNarrator ?n1.
    ?ns1 :precedes/:refersToNarrator ?n2.
    ?ns1 :precedes/:precedes/:refersToNarrator ?n3.
    #?n1 :narratorID "4396"^^xsd:integer.
    #?n2 :narratorID "4903"^^xsd:integer.
    #?n3 :narratorID "7272"^^xsd:integer.
    ?n1 :popularName ?pname1.
    ?n2 :popularName ?pname2.
    ?n3 :popularName ?pname3.
} group by ?n1 ?n2 ?n3

```

**Question:**  Is there ANY chain that is repeated more than x times?


```
SELECT ?chain (COUNT(?chain) AS ?chainCount)
WHERE {
  ?hadith :hasNarratorChain ?chain .
}
GROUP BY ?chain
HAVING (COUNT(?chain) > x)
```

**Question:**  Find the number of hadith where the chain has Narrator A and Narrator B but not Narrator C and matn includes TOPIC A.


```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?noofhadith {  
?b :name "The Book of Commentary@en".
{select  ?b (count(?h) as ?noofhadith) where { 
    ?h :isPartOfChapter/:isPartOfBook ?b.
	?h :hasNarratorChain/:hasNarratorSegment/:refersToNarrator ?n1.
    ?h :hasNarratorChain/:hasNarratorSegment/:refersToNarrator ?n2.
    ?n1 rdf:type :HadithNarrator.
    ?n1 :narratorID "4698"^^xsd:integer.
    ?n2 rdf:type :HadithNarrator.
    ?n2 :narratorID "3443"^^xsd:integer.
    ?n1 :name ?name1.
    ?n2 :name ?name2.
    
    FILTER NOT EXISTS {?h :hasNarratorChain/:hasNarratorSegment/:refersToNarrator ?n3.}
    ?n3 rdf:type :HadithNarrator.
    ?n3 :narratorID "989"^^xsd:integer.
    ?n3 :name ?name3.
        } Group by ?b}
    
}


```
**Question:**  What is the number of hadith by TOPIC narrated by Narrator_A?
 <!-- [Run Query]() -->

```
PREFIX : <http://www.semantichadith.com/ontology/>
select ?topic (count(?h) as ?noofhadith)
where { 
	?h :hasNarratorChain ?nc.
    ?h :isPartOfChapter/:isPartOfBook ?b.
    ?b :hadithBookIntro ?topic.
    ?nc :hasRootNarratorSegment ?ns.
    ?ns :refersToNarrator :HN04049.
   } group by ?b ?topic
```
**Question:**  Search a hadith of type 'mauquf' from Narrator_A. 
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?hadith ?narrator
where 
{ 
    ?hadith :hasHadithType :severed. 
    ?hadith :hasNarratorChain ?chain.
    ?chain :hasNarratorSegment ?narratorsegment.
    ?narratorsegment :refersToNarrator ?narrator.
	?narrator :name 'سليمان بن حرب بن بجيل@ar'.

}  
```

**Question:**  Search for a hadith narrated by someone who lived/died in Medina. 
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?hadith  ?narrator ?narratorName ?r ?d
where 
{ 
    ?hadith :hasNarratorChain ?Chain. 
    ?Chain :hasRootNarratorSegment ?root.
    ?root :refersToNarrator ?narrator.
    ?narrator :name ?narratorName.
    ?narrator :residence ?r.
    ?narrator :deathPlace ?d
    Filter (?r = 'المدينة' || ?d = 'المدينة').
}  
```
**Question:**  Find all the hadith narrated from ابن عباس about the topic 'Hajj' (Pilgrimmage)?   
 <!-- [Run Query]() -->


**Question:** PREFIX : <http://www.semantichadith.com/ontology/>
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?h 
where {
	?h :hasNarratorChain ?nc.
    ?h :isPartOfChapter/:isPartOfBook ?b.
    ?b :name ?bname.
    ?nc :hasRootNarratorSegment ?ns.
    ?ns :refersToNarrator :HN04883.
    FILTER REGEX (?bname, "The Book of Hajj@en").
   }

```
 **Question:** Find Hadith narrated by Narrator_A  

```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?hadith 
{ 
	?hadith rdf:type :Hadith .
    ?hadith :hasNarratorChain ?o .
    ?o :hasNarratorSegment	 ?x .
    ?x :refersToNarrator	 ?y .
    ?y :name ?name
    
} 
VALUES (?name)
{
    ("عبد الله بن يوسف@ar")
}
```

**Question:** How many Hadith are narrated by Narrator_A who heardFrom Narrator_B?  
```
PREFIX : <http://www.semantichadith.com/ontology/>
select (COUNT (?hadith) AS ?numHadith)
where
{
    	?hadith :hasNarratorChain ?chain.
	    ?chain :hasNarratorSegment ?s.
    	?s :refersToNarrator :HN03583.
    	:HN03583 :heardFrom :HN01012.
	
}
```

**Question:** Who narrated Hadith_X?  
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?root ?narrator ?name
where 
{ 
    :SB-HD0001 :hasNarratorChain ?Chain. 
    ?Chain :hasRootNarratorSegment ?root.
    ?root :refersToNarrator ?narrator.
    ?narrator :name ?name
    
}  
```
**Question:** Are there any narrators residing in Location_X?  
```
PREFIX : <http://www.semantichadith.com/ontology/>

select  ?narrators
where 
{ 
    ?narrators rdf:type :HadithNarrator .
    ?narrators :residence "المدينة".
}

```
**Question:** Which Hadith has no 'containsMentionOf' of verse?  

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantichadith.com/ontology/>

SELECT ?s WHERE { 
    ?s rdf:type :Hadith.
    MINUS { ?s :containsMentionOf ?v. }
}

```
**Question:** What is the generation of Narrator_A?  
```
PREFIX : <http://www.semantichadith.com/ontology/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?generation
where 
{ 
    ?narrator rdf:type :HadithNarrator .
    ?narrator :popularName 'أبو بكر بن أبي سبرة القرشي'.
    ?narrator :generation ?generation.
}

```

**Question:** Which Narrators belongs to the first generation of Narrators?  
```
PREFIX : <http://www.semantichadith.com/ontology/>

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?narrator ?name
where 
{ 
    ?narrator rdf:type :HadithNarrator .
    ?narrator :name ?name.
    ?narrator :generation '1'.
}

```
**Question:** What is the most narrated TOPIC by Narrator_A?
 <!-- [Run Query]() -->
<!--
PREFIX : <http://www.semantichadith.com/ontology/
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?bname (count(?h) as ?noofhadith)
where { 
	?h :hasNarratorChain ?nc.
    ?h :isPartOfChapter/:isPartOfBook ?b.
    ?b :name ?bname.
    ?nc :hasRootNarratorSegment ?ns.
    ?ns :refersToNarrator :HN04049.
    ?n :name ?name.
    ?n :popularName ?pname.
}	group by ?bname
ORDER BY DESC(?noofhadith)
limit 1-->
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?bname (count(?h) as ?noofhadith)
where { 
    ?h :isPartOfChapter/:isPartOfBook ?b.
    ?b :name ?bname.
    FILTER REGEX (?bname, "@ar").
    ?h :hasNarratorChain/:hasRootNarratorSegment/:refersToNarrator :HN04049.    
}	group by ?bname
ORDER BY DESC(?noofhadith)
Limit 1

```
**Question:** When was Narrator_A born? (Lunar calender) 
```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?by
where 
{ 
    ?narrator rdf:type :HadithNarrator .
    ?narrator :popularName 'أبو بكر بن أبي سبرة القرشي'.
    ?narrator :birthYear ?by.
}
```
**Question:** Which narrator narrated the most Hadith?
 <!-- [Run Query]() -->

```
PREFIX : <http://www.semantichadith.com/ontology/>

select ?pname ?n (count(distinct ?h) as ?noofhadith)  
where { 
	?h :hasNarratorChain ?nc.
    ?nc :hasRootNarratorSegment ?ns.
    ?ns :refersToNarrator ?n.
    ?n :name ?name.
    ?n :popularName ?pname.
} group by ?pname ?n
ORDER BY DESC(?noofhadith)
limit 1

```

**Question:** Two separate Narrator Chains with two same narrators but in different order.  

```
PREFIX : <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
select * where { 
	?hadith :hasNarratorChain ?chain.
	?chain :hasNarratorSegment ?s.
	?s :refersToNarrator :HN08272.
    ?s :precedes | :follows ?s2.
	?s2 :refersToNarrator :HN02885.
}

```
**Question:** Visualising Two separate Narrator Chains with two same narrators but in different order. 
```
PREFIX : <http://www.semantichadith.com/ontology/>
construct {?c1 :relatedToChain ?c2} where { 
	:SB-HD5292 :hasNarratorChain ?c1.
	:SB-HD2661 :hasNarratorChain ?c2.
}
```
![image](https://github.com/A-Kamran/SemanticHadithKG/assets/97387765/77dd8d2c-d91f-4cfe-af86-9278cde01b21)

