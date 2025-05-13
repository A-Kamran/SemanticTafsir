# TEI Conversion Notes for SemanticTafsir Knowledge Graph

This document outlines the key issues, decisions, and solutions encountered during the conversion of TEI-encoded manuscripts of *Tafsir al-Tabari* into RDF for the construction of the SemanticTafsir Knowledge Graph. It serves as both a technical reference and a record of data modelling choices.

## Overview

The TEI source data, annotated at the verse level, presented several structural inconsistencies and unique tagging patterns that required adaptation during the knowledge graph construction process. These notes document challenges encountered and the corresponding modelling solutions.

---

## 1. Structural Anomalies

### Issue: `<p>` Tags Outside Expected Context
In some surahs (e.g., 114–107), a `<p>` tag followed the `<div>` introducing a chapter, rather than appearing inside a section `<div>`.  
**Action:** Associated such paragraphs directly with the chapter using a `hasCommentary` property.

---

## 2. Unfamiliar or Irregular Tags

### Issue: `<add type="parenthesis">` Tag
Used inconsistently across Surahs 114, 111, 110, 109, 108.  
**Action:** Mapped to a new class `AdditionalText` and captured as annotations within the commentary structure.

### Issue: `<pb>` (Page Break) Nested Inside `<quote>`
Encountered in Surah 111.  
**Action:** Modelled explicitly using a `PageBreak` annotation attached to the surrounding commentary or quotation.

---

## 3. Annotation Errors and Tag Duplication

### Issue: Duplicate `<div>` Tags
Observed in Surahs 110 and 108.  
**Action:** Duplicates were overwritten or ignored during KG generation to prevent redundancy.

### Issue: Incorrect or Incomplete Grouped Verse Annotations
In Surah 2 and others, grouped verses contained unexpected formatting (e.g., extra numbers, special characters).  
**Action:** Implemented custom parsing logic to clean and standardise verse group references.

---

## 4. Tag Attribute Inconsistencies

### Issue: `<persName type="...">` Instead of Expected `ana=`
Seen in Surah 18.  
**Action:** Preserved `type` as metadata in the KG while flagging for potential future schema alignment or reprocessing.

---

## 5. Unresolved or Ambiguous Cases

Some tag structures did not follow any recognised pattern, and their semantics could not be conclusively interpreted from the context.

- These include special characters or partially annotated sections with missing tags.
- Currently logged as TODO items for further curation.

---

## Summary

The conversion of TEI to RDF required a pragmatic yet principled approach to retain semantic fidelity while accommodating structural irregularities in the source manuscripts. By combining rule-based extraction, fallback strategies, and targeted modelling enhancements, we ensured the robustness and completeness of the resulting SemanticTafsir knowledge graph.

Ongoing improvements will include:
- Expanding tag mappings as more Tafsir collections are integrated.
- Refining error handling.
- Enhancing multilingual and variant-aware tag interpretation.

For questions or contributions, please open an issue on the [Sem]()
