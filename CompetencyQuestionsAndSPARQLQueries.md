
# Competency questions for the Semantic Tafsir ontology

The given SPARQL are _examples_ that may be reinterpreted and reused for applications.

### Competency Question 1:
**Question:** Find all Poetry in the Tafsir that mentions a Person X.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ1%20Find%20all%20Poetry%20in%20the%20Tafsir%20that%20mentions%20a%20Person%20X.)


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
**Question:** List all references made to verse fragments from Chapter X within the Tafsir.
Which VerseFragments from a given chapter are referenced across the Tafsir commentary? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ2%20List%20all%20VerseFragments%20discussed%20in%20Chapter%20X.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?x ?verseFragment ?text  
WHERE {
    ?verseFragment a :VerseFragment.
    ?verseFragment :hasChapterNo "110";
    				:hasText ?text.
    ?x :references ?verseFragment.
 	
}
```

List all VerseFragments of Chapter X. [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=All%20Verse%20Fragments%20of%20Surah%20X)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?verseFragment ?chapNum
WHERE {
    ?verse :containsVerseFragment ?verseFragment.
    ?verseFragment :hasChapterNo "110".
}

```



### Competency Question 3:
**Question:** List all Themes associated with Verse X in the Tafsir. [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ3%20List%20all%20Themes%20associated%20with%20Verse%20X%20in%20the%20Tafsir.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT DISTINCT ?commentary ?theme
WHERE {

    ?commentary rdf:type :Commentary.
    ?commentary :references :V002_001.
  
    ?commentary :hasTheme ?theme.
}

```

### Competency Question 4:
**Question:** Which Chapter hasSection mentioning Person Y? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ4%20Which%20Chapter%20hasSection%20mentioning%20Person%20Y%3F)

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>

SELECT DISTINCT ?chapter ?section ?commentary
WHERE {

    ?chapter :containsSection ?section.
    ?section :containsCommentary ?commentary.
    ?commentary :mentions ?person.
    ?person a schema:Person;
    		:hasName "ابن عباس".
    
}

```

### Competency Question 5:
**Question:** How many themes are mentioned in Chapter X? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ5%20How%20many%20themes%20are%20mentioned%20in%20Chapter%20X%3F)

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
**Question:** Which themes are discussed in multiple chapters? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ6%20Which%20themes%20are%20discussed%20in%20multiple%20chapters%3F)

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
**Question:** What are the types of HadithNarrators? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ7%20What%20are%20the%20types%20of%20HadithNarrators%3F)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?narratorType ?label ?comment
WHERE {
  ?narratorType rdf:type :NarratorType ;
                rdfs:label ?label .
  OPTIONAL { ?narratorType rdfs:comment ?comment. }
}

```

### Competency Question 8:
**Question:** Which verses are most frequently referenced in the Tafsir? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ8%20Which%20verses%20are%20most%20frequently%20referenced%20in%20the%20Tafsir%3F)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?verse (COUNT(?commentary) AS ?referenceCount)
WHERE {
  {
    # Direct references to a Verse
    ?commentary a :Commentary ;
                :references ?verse .
    ?verse a :Verse .

  }
  UNION
  {
    # Indirect references via VerseFragment
    ?commentary a :Commentary ;
                :references ?fragment .
    ?fragment a :VerseFragment ;
              :isPartOfVerse ?verse .
  }
}
GROUP BY ?verse ?verseText
ORDER BY DESC(?referenceCount)
LIMIT 10


```

### Competency Question 9:
**Question:** Which Commentary mentions Location B? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ9%20Which%20Commentary%20mentions%20Location%20B%3F)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?commentary ?text
WHERE {
    ?commentary a :Commentary;
    		:mentions ?location;
    	:hasText ?text.
 
	?location a :Location.
    ?location :hasName ?name
    
    VALUES(?name){("الكوفة")}
}
```

### Competency Question 10:
**Question:** Do all sections mention multiple persons? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ10%20%20Do%20all%20sections%20mention%20multiple%20persons%3F)

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

ASK {
  FILTER NOT EXISTS {
    SELECT ?section (COUNT(DISTINCT ?person) AS ?personCount)
    WHERE {
      ?chapter :containsSection ?section .
      ?section :containsCommentary ?commentary .
      ?commentary :mentions ?person .
    }
    GROUP BY ?section
    HAVING (?personCount <= 1)
  }
}
```

### Competency Question 11:
**Question:** Where can I find sections about a specific Verse X? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ11%20Where%20can%20I%20find%20sections%20about%20a%20specific%20Verse%20X%3F)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?section ?verse ?text 
WHERE {
    ?chapter :containsSection ?section.
    ?section :isAbout ?verse.
    ?verse a :Verse;
    	:hasText ?text.

    VALUES(?verse){(:V113_003)}
}

```

### Competency Question 12:
**Question:** List all verse numbers where an entity of type "Other" is mentioned. [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ12%20List%20all%20verse%20numbers%20where%20an%20entity%20of%20type%20%22Other%22%20is%20mentioned.%20)

**SPARQL Query:**
```

PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?verse ?other ?name
WHERE {
    ?verse a :Verse.
    ?verse :mentions ?other.
    ?other a :Other;
    :hasName ?name.
}


```

### Competency Question 13:
**Question:** Which Commentary mentions both a Person and an Organisation? [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ13%20Which%20Commentary%20mentions%20both%20a%20Person%20and%20an%20Organisation%3F)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX schema: <http://schema.org/>

SELECT ?commentary ?text
WHERE {
    ?commentary a :Commentary;
    	:hasText ?text.

    # Must mention at least one Person
    ?commentary :mentions ?person .
    ?person a schema:Person .

    # Must also mention at least one Organization
    ?commentary :mentions ?org .
    ?org a :Organization .
}


```

### Competency Question 14:
**Question:** Search a Hadith where NarratorChain has Narrator A and Narrator B but not Narrator C and HadithText includes Theme A and Location B.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ14%20%20Search%20a%20Hadith%20where%20NarratorChain%20has%20Narrator%20A%20and%20Narrator%20B%20but%20not%20Narrator%20C%20and%20HadithText%20includes%20Theme%20A%20and%20Location%20B.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT DISTINCT ?hadith ?theme 
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.
    
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narratorA .
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narratorB .
    ?narratorA :hasName ?narratorOne.
    ?narratorB :hasName ?narratorTwo.
    
    FILTER NOT EXISTS {
         ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narratorC .
        ?narratorC :hasName ?narratorThree.
    }
    
    VALUES(?themeName ?narratorOne ?narratorTwo ?narratorThree)
    { ("kalam" "يونس بن عبد الأعلى" "ابن وهب" "ابن علية") }
}
```

### Competency Question 15:
**Question:** All the Hadith narrated from Narrator A.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ15%20All%20the%20Hadith%20narrated%20from%20Narrator%20A)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT DISTINCT ?hadith ?hadithText
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narrator.
    ?narrator :hasName "ابن وهب".
    ?hadith :hasText ?hadithText.
}

```

### Competency Question 16:
**Question:** How many Hadith narrated by Narrator A.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ16%20How%20many%20Hadith%20narrated%20by%20Narrator%20A.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT DISTINCT (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narrator.
    ?narrator :hasName "ابن وهب".
}
```

### Competency Question 17:
**Question:** How many Hadith narrated by Narrator A from Narrator B.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ17%20How%20many%20Hadith%20narrated%20by%20Narrator%20A%20from%20Narrator%20B.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT DISTINCT (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narrator.
    ?narrator :hasName ?narratorA;
	hadith:heardFrom ?narrator2.
    ?narrator2	  :hasName ?narratorB.
    VALUES(?narratorA ?narratorB){("يونس بن عبد الأعلى" "ابن وهب")}
}
```

### Competency Question 18:
**Question:** List of narrators by the number of their narrations. [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ18%20List%20of%20narrators%20by%20the%20number%20of%20their%20narrations.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT ?narratorName (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narrator.
    ?narrator :hasName ?narratorName .
}
GROUP BY ?narratorName
ORDER BY DESC(?count)


```

### Competency Question 19:
**Question:** Which Narrator narrated most Hadith about Theme A.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ19%20Which%20Narrator%20narrated%20most%20Hadith%20about%20Theme%20A.)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT ?narratorName (COUNT(DISTINCT ?hadith) AS ?count)
WHERE {
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsSegment ?segment .
    ?segment :hasSubTheme ?subTheme .
    ?subTheme :isSubThemeOf ?theme .
    ?theme :hasName ?themeName.
    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator ?narrator.
    ?narrator :hasName ?narratorName .
    
    VALUES(?themeName){("kalam")}
}
GROUP BY ?narratorName
ORDER BY DESC(?count)
LIMIT 1

```

### Competency Question 20:
**Question:** Most narrated Theme by Narrator A.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ20%20please%20create%20a%20github%20documentation%20for%20these%20tags%20that%20are%20used%20to%20annotate%20the%20tafsir%20)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
Prefix hadith: <http://www.semantichadith.com/ontology/>

select ?themeName (count(?hadith) as ?noofhadith)
#select distinct ?themeName ?hadith
where { 
    
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.

    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator/:hasName ?name.
    
    VALUES(?name){("ابن علية")}
}	
group by ?themeName
ORDER BY DESC(?noofhadith)
Limit 1

```

### Competency Question 21:
**Question:** Number of Hadith by Theme narrated by Narrator A.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ21%20Number%20of%20Hadith%20by%20Theme%20narrated%20by%20Narrator%20A)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
Prefix hadith: <http://www.semantichadith.com/ontology/>

select ?themeName (count(?hadith) as ?noofhadith)
#select distinct ?themeName ?hadith
where { 
    
    ?hadith rdf:type hadith:Hadith .
    ?hadith :containsSegment ?segment.
    ?segment :hasSubTheme ?subTheme.
    ?subTheme :isSubThemeOf ?theme.
    ?theme :hasName ?themeName.

    ?hadith :containsNarratorChain/hadith:hasNarratorSegment/hadith:refersToNarrator/:hasName ?name.
    
    VALUES(?name){("ابن علية")}
}	
group by ?themeName
ORDER BY DESC(?noofhadith)
```

### Competency Question 22:
**Question:** What is the frequency of a specific chain or part of a chain.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ22%20What%20is%20the%20frequency%20of%20a%20specific%20chain%20or%20part%20of%20a%20chain.)

**SPARQL Query:**
```
PREFIX hadith: <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 

where {
    ?h :containsNarratorChain/hadith:hasNarratorSegment ?ns1.
    ?ns1 hadith:refersToNarrator ?n1.
    ?ns1 hadith:follows/hadith:refersToNarrator ?n2.
    ?ns1 hadith:follows/hadith:follows/hadith:refersToNarrator ?n3.

} 
group by ?n1 ?n2 ?n3

```

### Competency Question 23:
**Question:** Any NarratorChain that is repeated more than 10 times.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ23%20Any%20NarratorChain%20that%20is%20repeated%20more%20than%2010%20times)

**SPARQL Query:**
```
PREFIX hadith: <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 

where {
    ?h :containsNarratorChain/hadith:hasNarratorSegment ?ns1.
    ?ns1 hadith:refersToNarrator ?n1.
    ?ns1 hadith:follows/hadith:refersToNarrator ?n2.
    ?ns1 hadith:follows/hadith:follows/hadith:refersToNarrator ?n3.

} 
group by ?n1 ?n2 ?n3
HAVING (COUNT(DISTINCT ?h) > 10)

```

### Competency Question 24:
**Question:** Frequency of partial NarratorChain repeating at least ten times.  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ24%20Frequency%20of%20partial%20NarratorChain%20repeating%20at%20least%20ten%20times.)

**SPARQL Query:**

```
PREFIX hadith: <http://www.semantichadith.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select ?n1 ?n2 ?n3 (count(distinct ?h) as ?noofhadith) 

where {
    ?h :containsNarratorChain/hadith:hasNarratorSegment ?ns1.
    ?ns1 hadith:refersToNarrator ?n1.
    ?ns1 hadith:follows/hadith:refersToNarrator ?n2.
    ?ns1 hadith:follows/hadith:follows/hadith:refersToNarrator ?n3.

} 
group by ?n1 ?n2 ?n3
HAVING (COUNT(DISTINCT ?h) > 10)
```

### Competency Question 25:
<!--
**Question:** Search Hadith 'mauquf' from Narrator A.  [Run Query]()

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
-->
**Question:** Search Hadith that references ayah 11:6 (or surah 11 i.e. any ayah of surah 11).  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ25%20Search%20Hadith%20that%20references%20ayah%2011%3A6)

**SPARQL Query:**
```
PREFIX hadith: <http://www.semantichadith.com/ontology/>
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

select distinct  ?hadith  
where 
{ 

    ?hadith rdf:type hadith:Hadith .
    ?hadith :references ?verse.
    ?verse :hasChapterNo "11".
    ?verse :hasVerseNo "6".
    
}
```

### Competency Question 26:
**Question:** What Section do I need to examine to find Verse Y?  [Run Query](http://semantictafsir.iknex.com/sparql?savedQueryName=CQ26%20What%20Section%20do%20I%20need%20to%20examine%20to%20find%20Verse%20Y)

**SPARQL Query:**
```
PREFIX : <http://www.semantictafsir.com/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX hadith: <http://www.semantichadith.com/ontology/>

SELECT ?section ?verse
WHERE {
    ?section a :Section.
    ?section :isAbout ?verse.
    ?verse :hasChapterNo "2".
    ?verse :hasVerseNo "4".
}

```

