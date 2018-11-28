# POSPair
  POSPair model is a simplifying representation for Natural Language Processing. POSPair Model represents data based on part-of-speech and relations between different part-of-speech. In POSPair model, Word pairs are the unit values generated with refrence to the context present in that sentence. Besides just closeness, word frequency or syntactic relatedness, POSPair model takes into account the actual form of relationship between words, which words are related and how they are related.
  
## How It Works
Words are the smallest elements. Based on their use and functions, words are categorized into several types of part-of-speech.
1. Noun - Used to name persons, things, animals, places, ideas, or events.    **(Noun)**
2. Pronoun - Functions as a replacement for Noun.                             **(Pronoun)**
3. Adjective - Used to describe Noun or Pronoun. 		              **(Noun - Adjective OR Pronoun - Adjective)**
4. Verb - Shows action or state of being. 				      **(Noun - Verb OR Pronoun - Verb)**
5. Adverb - Describes Adjective, Verb or another Adverb. 		      **(Verb - Adverb, Adverb - Adverb, Adjective - Adverb)**
6. Preposition - Words that specify location or location in time.	      **(Noun - Preposition OR Pronoun - Preposition)**
7. Conjunction - Joins words, phrases or clauses together.		      **(Noun - Conjunction OR Pronoun - Conjunction)**
8. Interjection - Words that express emotion.				      **(Interjection)**

As per the definition and semantics of each part-of-speech, words of only specific part-of-speech are related with each other and provide some meaningful relation.

According to part-of-speech, Words are related to each other through above given relations, but in a specific manner. Above relations are one sided relations.
Eg. Adjective desribes Noun, Noun does not describe Adjective

The representation of data is done in form of word pairs. At a time, the relations between part-of-speech can be properly represented between two words only. Word pairs are the simplest form of representation.

Word pairs are generated with the refrence to the whole text. Word pairs can be understood when the whole sentence is taken into context.

## GETTING STARTED:
### PREREQUISITES:
1. Python 3.0 or higher
2. Stanford Core NLP (3.9.2)

### INSTALLING:
```
1. pip install POSPair
```
2. Read instructions on [how to install and run Stanford CoreNLP server](http://stanfordnlp.github.io/CoreNLP/corenlp-server.html#getting-started)

[**Note**: Keep the Stanford CoreNLP Server port: 9000]

3. POSPair Functions:
```
    1. POSPair.WordPairs(string)
    2. POSPair.WordPairsWithValues(string)
    3. POSPair.separateWordPair(string) [String should be word-pair]
```
Example:
```Python
import POSPair

wordPairs = POSPair.WordPairs("POSPair model is a simplifying representation.")
```
Output:
```
'POSPair model'
'model representation'
'representation is'
'representation a'
'representation simplifying'
```

Get in touch at pospair.contact@gmail.com for any queries or help.

### BUILT WITH:
1. Python
2. Stanford Core NLP
3. Pycorenlp

### CONTRIBUTING:
Read [CONTRIBUTING.md](https://github.com/jmacwan/POSPair/blob/master/CONTRIBUTING.md)

### AUTHOR:
Jim Macwan

### LICENSE:
[GNU General Public License v3.0](https://github.com/jmacwan/POSPair/blob/master/LICENSE)

### ACKNOWLEDGMENTS:
1. **Stanford Core NLP**
2. **Pycorenlp**

_Please provide feedback or get in touch at pospair.contact@gmail.com_
