
# Competency questions for the Semantic Tafsir ontology

The given SPARQL are _examples_ that may be reinterpreted and reused for applications.

### Competency Question 1:
**Question:** Find all Poetry in the Tafsir that mentions a Person X.

**SPARQL Query:**
```
PREFIX schema: <http://schema.org/>
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?poetry ?poetryText ?person ?name 
WHERE {
    ?commentary rdf:type :Commentary.
    ?commentary :references ?poetry.
    ?poetry rdf:type :Poetry;
    		:hasText ?poetryText.
    ?poetry :mentions ?person.
    ?person rdf:type schema:Person.
    ?person :hasName ?name.

     VALUES(?name){("ابن عفان")}
}


```

### Competency Question 2:
**Question:** List all VerseFragments discussed in Chapter X.

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?verseFragment ?chapNum
WHERE {
    ?verse :containsVerseFragment ?verseFragment.
    ?verseFragment :hasChapterNo ?chapNum.
    VALUES(?chapNum){("110")}
}

```

### Competency Question 3:
**Question:** List all Themes associated with Verse X in the Tafsir.

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?commentary ?theme ?thing ?chapNum ?verseNum
WHERE {

    ?commentary rdf:type :Commentary.
    ?commentary :hasTheme ?theme.
    ?commentary :references ?thing.
    ?thing rdf:type :Verse.
    ?thing :hasChapterNo ?chapNum.
    ?thing :hasVerseNo ?verseNum.
    
    VALUES(?chapNum ?verseNum){("2" "1")}

}



```

### Competency Question 4:
**Question:** Which Chapter hasSection mentioning Person Y?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>

SELECT DISTINCT ?chapter ?section ?name ?commentary
WHERE {

    ?chapter :containsSection ?section.
    ?section :containsCommentary ?commentary.
    ?commentary :mentions ?thing.
    ?thing a schema:Person.
    ?thing :hasName ?name.
    
}

```

### Competency Question 5:
**Question:** How many themes are mentioned in Chapter X?

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?chapter (COUNT(DISTINCT ?theme) AS ?uniqueThemeCount)
WHERE {
    ?chapter :containsSection ?section.
    ?section :containsCommentary ?commentary.
    ?commentary :hasTheme ?theme.
}
GROUP BY ?chapter


```

### Competency Question 6:
**Question:** Which themes are discussed in multiple chapters?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?theme (COUNT(DISTINCT ?chapter) AS ?chapterCount)
WHERE {
    ?chapter :containsSection ?section.
    ?section :containsCommentary ?commentary.
    ?commentary :hasTheme ?theme.
}
GROUP BY ?theme 
HAVING (COUNT(DISTINCT ?chapter) > 1) 
ORDER BY DESC(?chapterCount)

```

### Competency Question 7:
**Question:** What are the types of HadithNarrators?

**SPARQL Query:**
```

```

### Competency Question 8:
**Question:** Which verses are most frequently referenced in the Tafsir?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?verseNum (COUNT(?commentary) AS ?referenceCount)
WHERE {
    ?commentary a :Commentary.
    ?commentary :references ?thing.
    ?thing a ?type.
    FILTER (?type = :Verse || ?type = :verseFragment)
    ?thing :hasVerseNo ?verseNum.
}
GROUP BY ?verseNum
ORDER BY DESC(?referenceCount)

```

### Competency Question 9:
**Question:** Which Commentary mentions Location B?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?commentary ?thing
WHERE {
    ?commentary a :Commentary.
    ?commentary :mentions ?thing.
	?thing a :Location.
    ?thing :hasName ?name
    
    VALUES(?name){("الكوفة")}
}

```

### Competency Question 10:
**Question:** Do all sections mention multiple persons?

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?section (COUNT(DISTINCT ?person) AS ?personCount)
WHERE {
    ?chapter :containsSection ?section.
    ?section :containsCommentary ?commentary.
    ?commentary :mentions ?person.
}
GROUP BY ?section
HAVING (COUNT(DISTINCT ?person) > 1)


```

### Competency Question 11:
**Question:** Where can I find sections about a specific Verse X?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?section ?thing ?type ?verseNum
WHERE {
    ?chapter :containsSection ?section.
    ?section :isAbout ?thing.
    ?thing a  ?type.
    ?thing :hasVerseNo ?verseNum.
    FILTER (?type = :Verse || ?type = :VerseFragment)
    
#    VALUES(?thing){("#VF001:001_003")}
}

```

### Competency Question 12:
**Question:** List all verse numbers where an entity of type "Other" is mentioned.

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?verse ?thing
WHERE {
    ?verse a :Verse.
    ?verse :mentions ?thing.
    ?thing a :Other
}


```

### Competency Question 13:
**Question:** Which Commentary mentions both a Person and an Organisation?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>

SELECT ?verse ?thing
WHERE {
    ?verse a :Commentary.
    ?verse :mentions ?thing.
    ?thing a ?type
    FILTER (?type = :Organization && ?type = schema:Person)
}




```

### Competency Question 14:
**Question:** Search a Hadith where NarratorChain has Narrator A and Narrator B but not Narrator C and HadithText includes Theme A and Location B

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?hadith ?segment ?theme
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.
    
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?Nsegment .
    ?Nsegment :refersTo ?narrator .
    ?narrator :hasName ?name .
    
    ?chain :hasNarratorSegment ?segmentA .
    ?segmentA :refersTo ?narratorA .
    ?narratorA :hasName ?narratorOne.
    
    ?chain :hasNarratorSegment ?segmentB .
    ?segmentB :refersTo ?narratorB .
    ?narratorB :hasName ?narratorTwo.
    
    FILTER NOT EXISTS {
        ?chain :hasNarratorSegment ?segmentC .
        ?segmentC :refersTo ?narratorC .
        ?narratorC :hasName ?narratorThree.
    }
    
    VALUES(?themeName ?narratorOne ?narratorTwo ?narratorThree)
    { ("kalam" "يونس بن عبد الأعلى" "ابن وهب" "ابن علية") }
}
```

### Competency Question 15:
**Question:** All the Hadith narrated from Narrator A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?hadith
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?segment .
    ?segment :refersTo ?narrator .
    ?narrator :hasName "ابن وهب".
}

```

### Competency Question 16:
**Question:** How many Hadith narrated by Narrator A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT (COUNT(DISTINCT ?hadith) AS ?count)
#SELECT DISTINCT ?hadith
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?segment .
    ?segment :refersTo ?narrator .
    ?narrator :hasName ?name .
    VALUES(?name){("ابن وهب")}
}
```

### Competency Question 17:
**Question:** How many Hadith narrated by Narrator A from Narrator B

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?segment .
    ?segment :refersTo ?narrator .
    ?narrator :hasName ?narratorA;
    		  :heardFrom ?narratorID.
    ?narratorID	  :hasName ?narratorB.
    VALUES(?narratorA ?narratorB){("يونس بن عبد الأعلى" "ابن وهب")}
}

```

### Competency Question 18:
**Question:** List of narrators by the number of their narrations

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?narratorName (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?segment .
    ?segment :refersTo ?narrator .
    ?narrator :hasName ?narratorName .
}
GROUP BY ?narratorName
ORDER BY DESC(?count)


```

### Competency Question 19:
**Question:** Which Narrator narrated most Hadith about Theme A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?narratorName (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type :Hadith .
    ?hadith :containsSegment ?segment .
    ?segment :hasSubTheme ?subTheme .
    ?subTheme :isSubThemeOf ?theme .
    ?theme :hasName ?themeName.
    ?hadith :containsNarratorChain ?chain .
    ?chain :hasNarratorSegment ?narratorSegment .
    ?narratorSegment :refersTo ?narrator .
    ?narrator :hasName ?narratorName .
    
    VALUES(?themeName){("kalam")}
}
GROUP BY ?narratorName
ORDER BY DESC(?count)
LIMIT 1

```

### Competency Question 20:
**Question:** Most narrated Theme by Narrator A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?themeName (count(?hadith) as ?noofhadith)
#select distinct ?themeName ?hadith
where { 
    
    ?hadith rdf:type :Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.

    ?hadith :containsNarratorChain/:hasRootNarratorSegment/:refersTo/:hasName ?name. 
    
    VALUES(?name){("ابن علية")}
}	
group by ?themeName
ORDER BY DESC(?noofhadith)
Limit 1

```

### Competency Question 21:
**Question:** Number of Hadith by Theme narrated by Narrator A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select ?themeName (count(?hadith) as ?noofhadith)
#select distinct ?themeName ?hadith
where { 
    
    ?hadith rdf:type :Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.

    ?hadith :containsNarratorChain/:hasRootNarratorSegment/:refersTo/:hasName ?name. 
    
    VALUES(?name){("ابن علية")}
}	
group by ?themeName
ORDER BY DESC(?noofhadith)

```

### Competency Question 22:
**Question:** What is the frequency of a specific chain or part of a chain

**SPARQL Query:**
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 
#select ?ns1
where {
    ?h :containsNarratorChain/:hasNarratorSegment ?ns1.
    ?ns1 :refersTo ?n1.
    ?ns1 :follows/:refersTo ?n2.
    ?ns1 :follows/:follows/:refersTo ?n3.
#    ?n1 :hasID "L8613".
#    ?n2 :hasID "L5147".
#    ?n3 :hasID "L7063".
    ?n1 :hasName ?pname1.
    ?n2 :hasName ?pname2.
    ?n3 :hasName ?pname3.
} 
group by ?n1 ?n2 ?n3

```

### Competency Question 23:
**Question:** Any NarratorChain that is repeated more than 10 times

**SPARQL Query:**
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 
#select ?ns1
where {
    ?h :containsNarratorChain/:hasNarratorSegment ?ns1.
    ?ns1 :refersTo ?n1.
    ?ns1 :follows/:refersTo ?n2.
    ?ns1 :follows/:follows/:refersTo ?n3.
#    ?n1 :hasID "L8613".
#    ?n2 :hasID "L5147".
#    ?n3 :hasID "L7063".
    ?n1 :hasName ?pname1.
    ?n2 :hasName ?pname2.
    ?n3 :hasName ?pname3.
} 
group by ?n1 ?n2 ?n3
HAVING (COUNT(DISTINCT ?h) > 10)

```

### Competency Question 24:
**Question:** Frequency of partial NarratorChain repeating at least ten times

**SPARQL Query:**

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 
#select ?ns1
where {
    ?h :containsNarratorChain/:hasNarratorSegment ?ns1.
    ?ns1 :refersTo ?n1.
    ?ns1 :follows/:refersTo ?n2.
    ?ns1 :follows/:follows/:refersTo ?n3.
    ?n1 :hasName ?pname1.
    ?n2 :hasName ?pname2.
    ?n3 :hasName ?pname3.
} 
group by ?n1 ?n2 ?n3
HAVING (COUNT(DISTINCT ?h) > 10)
```

### Competency Question 25:
**Question:** Search Hadith 'mauquf' from Narrator A

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
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

### Competency Question 26:
**Question:** Search Hadith that references ayah 11:11 (or surah 11 i.e. any ayah of surah 11)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select distinct  ?hadith  ?chapNum 
where 
{ 

    ?hadith rdf:type :Hadith .
    ?hadith :follows/:references/:hasChapterNo ?chapNum.
    
    FILTER (xsd:int(?chapNum) = 11).
   }
```

### Competency Question 27:
**Question:** What Section do I need to examine to find Verse Y?

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?section ?thing
WHERE {
    ?section a :Section.
#    ?section :isAbout "VF_001". #verse name is given but not getting any result
    ?section :isAbout ?thing.
    ?thing a ?type.
    FILTER (?type = :Verse || ?type = :VerseFragment)
    
}

```

### Competency Question 28:
**Question:** What are the types of HadithNarrators?

**SPARQL Query:**
```

```

```
