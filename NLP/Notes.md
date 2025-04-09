# Natural Language Processing (NLP) - Summary Notes

## What Is NLP?
Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language. It works with multiple forms of communication, including:
- Text
- Speech
- Sign language
- Braille
- Video

## Real-Life Applications
- Reading and replying to emails and messages
- Voice commands to smart assistants
- Language translation and detection
- Screen readers and captioned content for accessibility
- Learning and teaching languages
- Web search personalization



## NLP and Text Collections

Natural Language Processing (NLP) works on text collections such as:
- Tweets
- Facebook posts
- Conversations
- Movie reviews
- Historic documents
- News articles
- Meeting logs

A collection of such text is called a **corpus** (plural: **corpora**).

---

## Key Challenges in NLP

- Natural language is **ambiguous** and often **context-dependent**
- Meaning varies with user **perspective**, **intent**, or **tone**
- Tools like search engines **personalize** results based on user behavior
  - **Pros**: Improved relevance
  - **Cons**: Raises **privacy concerns**


## TextBlob Overview

**TextBlob** is a user-friendly, object-oriented NLP library built on **NLTK** and **Pattern**. It simplifies common NLP tasks such as:

### Key Features

- **Tokenization**: Splitting text into meaningful units (words, numbers).
- **POS Tagging**: Identifying parts of speech (noun, verb, adjective, etc.).
- **Noun Phrase Extraction**: Finding phrases like _"red brick factory"_.
- **Sentiment Analysis**: Detecting sentiment (positive, neutral, negative).
- **Language Detection & Translation**: Powered by Google Translate.
- **Inflection**: Pluralizing and singularizing words.
- **Spell Check & Correction**: Identifies and corrects spelling errors.
- **Stemming**: Reducing words to base forms (_"varieties"_ → _"varieti"_).
- **Lemmatization**: Similar to stemming, but results in valid words (_"varieties"_ → _"variety"_).
- **Word Frequencies**: Counts how often each word appears in a corpus.
- **WordNet Integration**: Access definitions, synonyms, antonyms.
- **Stop Word Elimination**: Removes common words like _"a"_, _"the"_, _"you"_.
- **n-grams**: Generates sequences of _n_ adjacent words (e.g., bigrams, trigrams).

### TextBlob Basics

`TextBlob` is the core class in the `textblob` module used for NLP.

- You can create a `TextBlob` with one or more sentences.
- `TextBlob`, `Sentence`, and `Word` objects support standard string operations and comparisons.
- They also offer built-in methods for various NLP tasks.
- All inherit from `BaseBlob`, sharing many common methods and properties.

```
from textblob import TextBlob

# Creating a TextBlob object 
txt = 'Today is a beautiful day. Tomorrow looks like bad weather.'
blob = TextBlob(txt)
print(blob)
```

## Tokenizing Text into Sentences and Words
Natural language processing often requires tokenizing text before performing other NLP
tasks. TextBlob provides convenient properties for accessing the sentences and words in
TextBlobs.
```
# Tokenization
print(blob.sentences)# Tokenize the text into sentences
print(blob.words) # Tokenize the text into words
```

The words property returns a WordList object containing a list of Word objects, representing
each word in the TextBlob with the punctuation removed:

### Parts-of-Speech (POS) Tagging

POS tagging determines each word’s part of speech based on its context. English has eight main parts of speech (nouns, verbs, adjectives, etc.), each with subcategories.

- Many words (e.g., *run*, *set*) have multiple meanings depending on usage.
- POS tagging helps computers interpret meaning by identifying grammatical roles.
- In TextBlob, the `.tags` property returns a list of `(word, POS tag)` tuples.

- PRP$ indicates a possessive pronoun.

- A TextBlob’s noun_phrases property returns a WordList object containing a list of
Word objects—one for each noun phrase in the text:

- A TextBlob’s sentiment property returns a Sentiment object indicating whether the text
is positive or negative and whether it’s objective or subjective:

```
# Part-of-Speech Tagging
print(blob.tags) # Get the part-of-speech tags for each word in the text
print(blob.sentences[0].tags) # Get the part-of-speech tags for each word in the first sentence
```
### Sentiment Analysis Overview

- **Sentiment analysis** is a key NLP task used to determine if a text expresses:
  - Positive sentiment
  - Neutral sentiment
  - Negative sentiment

- **Real-world application**: Companies analyze customer feedback, social media, or reviews to gauge public opinion about products/services.

- **Challenge**: Simply detecting positive or negative words like *“good”* or *“bad”* isn’t enough.
  - Example:  
    > "This is not a good product."  
    Despite the word *“good”*, the sentiment is **negative** due to the presence of *“not”*.

- **Context and word combinations** matter greatly in determining actual sentiment.

### Sentiment Analysis with TextBlob

- **Polarity**: Ranges from `-1.0` (negative) to `1.0` (positive). `0.0` is neutral.
- **Subjectivity**: Ranges from `0.0` (objective) to `1.0` (subjective).

```
# Sentiment Analysis with TextBlob’s Default Sentiment Analyzer
print(blob.sentiment) # Get the sentiment of the text
print(blob.sentiment.polarity) # Get the polarity of the text
print(blob.sentiment.subjectivity, '\n') # Get the subjectivity of the text

for sentence in blob.sentences:
    print(sentence.sentiment.polarity) # Get the polarity of each sentence
    print(sentence.sentiment.subjectivity) # Get the subjectivity of each sentence

new_blob = TextBlob('I am not good at this.')
print(new_blob.sentiment) # Get the sentiment of the text
print(new_blob.sentiment.polarity) # Get the polarity of the text
print(new_blob.sentiment.subjectivity) # Get the subjectivity of the text

from textblob import Sentence
print(Sentence('I am not good at this.').sentiment)#Sentiment(polarity=-0.35, subjectivity=0.6000000000000001)
print(Sentence('The movie was excellent!').sentiment)#Sentiment(polarity=1.0, subjectivity=1.0)

print(Sentence('The movie was not good.').sentiment)#Sentiment(polarity=-0.5, subjectivity=0.5)
```


### Sentiment Analyzers in TextBlob

- **Default Sentiment Analyzer**:
  - TextBlob uses **PatternAnalyzer** by default.
  - Based on the same techniques used in the **Pattern** library.
  - Analyzes polarity and subjectivity.

- **Alternative Analyzer**:  
  - **NaiveBayesAnalyzer** (from `textblob.sentiments` module)
  - Trained on a movie reviews dataset.
  - Implements the **Naive Bayes** machine learning algorithm.
  - Often used for **text classification** tasks.

- **Usage**:
  - You can specify the analyzer using the `analyzer` keyword when creating a `TextBlob` object.


```
# Sentiment Analysis with the NaiveBayesAnalyzer
from textblob.sentiments import NaiveBayesAnalyzer

blob2 = TextBlob("I am not a good boy", analyzer=NaiveBayesAnalyzer())
print(blob2.sentiment)# Sentiment(classification='neg', p_pos=0.47662917962091056, p_neg=0.5233708203790892)


sentence = TextBlob('Hey there! How are you?. I am not good at this.')
for s in sentence.sentences:
     print(s.sentiment) # Get the sentiment of each sentence

```

## Language Detection and Translation
### Inter-language Translation in NLP

- **Translation** is a major challenge in NLP and AI.
- **Advancements** in machine learning and artificial intelligence have enabled powerful translation tools:
  - **Google Translate**: Supports over 100 languages.
  - **Microsoft Bing Translator**: Supports around 60 languages.

#### Applications:
- Helpful for **travelers**:
  - Translate menus, road signs, etc.
- **Live speech translation**:
  - Enables real-time conversation across different languages.
  - Smartphones + in-ear headphones can now provide **near-live translation**.

#### TextBlob Translation Capabilities:
- Uses **Google Translate** behind the scenes.
- Can be applied to:
  - `TextBlob` objects
  - `Sentences`
  - `Words`

#### Language Detection and Translation:
- Method: `detect_language()`  
  - Returns the ISO code (e.g., `'en'` for English).

- print(spanish.translate())# Translate the text to english
- print(chinese.translate())# Translate the text to english
- -  Note the slight difference in the English results.

```
blob3 = TextBlob('Bonjour tout le monde')
print(blob3.detect_language()) # Detect the language of the text

# not working but.....
spanish = blob3.translate(to='es')
print(spanish)

chinese = blob.translate(to='zh')
print(chinese)# Translate the text to Chinese

print(spanish.translate())# Translate the text to english
print(chinese.translate())# Translate the text to english
#Note the slight difference in the English results.
```

# 🔤 Inflection: Pluralization and Singularization
Inflection refers to different forms of the same word:

- **Nouns**:  
  - Singular → Plural (e.g., `person` → `people`)
- **Verbs**:  
  - Tense variation (e.g., `run` → `ran`)

When analyzing **word frequencies**, it's helpful to normalize words to a single form to avoid counting the same word multiple times in different forms.

---

### 🛠 Pluralizing and Singularizing Words with `TextBlob`


``` Python
from textblob import Word
word = Word('index')
print(word.pluralize()) # Pluralize the word

word2 = Word('indices')
print(word2.singularize()) # Singularize the word

heroes = TextBlob('Superman Batman Spiderman').words
print(heroes.pluralize()) # Pluralize the words ['Supermen', 'Batmen', 'ands', 'Spidermen']
print(heroes.singularize()) # Singularize the words ['Superman', 'Batman', 'and', 'Spiderman']

```

## Spell Checking and Correction
For natural language processing tasks, it’s important that the text be free of spelling errors.  
Software packages for writing and editing text, like Microsoft Word, Google Docs and others automatically check your spelling as you type and typically display a red line under misspelled words.  
Other tools enable you to manually invoke a spelling checker.

You can check a `Word`’s spelling with its `spellcheck()` method, which returns a list of tuples containing possible correct spellings and a confidence value.  
**Note:** The word with the highest confidence value might not be the correct word for the given context.

`TextBlob`, `Sentence`, and `Word` objects all have a `.correct()` method that you can call to correct spelling.  
Calling `.correct()` on a `Word` returns the correctly spelled word that has the highest confidence value (as returned by `spellcheck()`):

You can check a Word’s spelling with its spellcheck method, which returns a list of tuples containing potential correct spellings and a confidence value.



``` Python
from textblob import Word

word = Word('thery')

print(word.spellcheck())# [('they', 0.5634568607812277), ('there', 0.4252396623265131), ('theory', 0.011303476892259265)]
for suggestion, probability in word.spellcheck():
    print(f"Suggestion: {suggestion}, Probability: {probability:.2f}")
# Suggestion: they, Probability: 0.56
# Suggestion: there, Probability: 0.43
# Suggestion: theory, Probability: 0.01

print(word.correct())#they
# chooses word with the highest confidence value

sentence = TextBlob('Ths sentense has missplled wrds.')
print(sentence.correct())# The sentence has misspelled words.

```

## Stemming and Lemmatization

Stemming removes a prefix or suffix from a word, leaving only a **stem**, which may or may not be a real word.  
Lemmatization is similar, but it factors in the word’s **part of speech** and **meaning**, and results in a **real word**.

Stemming and lemmatization are **normalization operations**, which prepare words for analysis.  
For example, before calculating statistics on words in a body of text, you might convert all words to **lowercase**, so that capitalized and lowercase words are not treated differently.

Sometimes, you might want to use a word’s **root** to represent the word’s many forms.  
For instance, the following words might all be treated as **“program”**:
- program
- programs
- programmer
- programming
- programmed
- programmes (U.K. spelling)

`Word` and `WordList` objects support stemming and lemmatization using the `.stem()` and `.lemmatize()` methods


- Lemmatization is similar to stemming, but factors in the word’s part of speech and meaning and results in a real word.


``` Python
from textblob import Word
word3 = Word('varieties')
print(word3.stem())# varieti
print(word3.lemmatize())#variety
```

## Word Frequencies and Document Similarity

Various techniques for detecting **similarity between documents** rely on **word frequencies**.

TextBlob makes it easy to count word frequencies automatically.

Let’s load Shakespeare’s *Romeo and Juliet* into a `TextBlob`.  
Assume you have the file `RomeoAndJuliet.txt` in the same folder as your script or Jupyter notebook.

You can access the word frequencies through the `word_counts` dictionary.  
For example, you can check how many times a word like "love" appears, and compare usage between different documents.

> Note: When you read a file using `Path.read_text()`, it automatically closes the file after reading.

``` Python 
from pathlib import Path
from textblob import TextBlob

blob4 = TextBlob(Path(r'E:\Languages\Python\NLP\hehe.md').read_text())
print(blob4.word_counts['blob'])# 2
print(blob4.word_counts['print'])# 25
print(blob4.word_counts['g'])# 0 searches exact match 

```
## WordNet Integration in TextBlob

- **WordNet** is a lexical database created by Princeton University.
- TextBlob integrates WordNet through NLTK's interface.

### Features

- Look up **definitions**, **synonyms**, and **antonyms**.
- The database does **not contain every dictionary definition**.
- You can use the `define` method with a **part of speech** argument to narrow down definitions.
- The `get_synsets` method also accepts a part of speech to return specific synsets.

``` Python 
from textblob import TextBlob
happy = Word('happy')
print(happy.definitions)
#['enjoying or showing or marked by joy or pleasure', 'marked by good fortune', 'eagerly disposed to act or to be of service', 'well expressed and to the point']
```
### Synsets

- Each **Synset** is a set of synonyms for a word.
- Example format: `happy.a.01`  
  - `happy`: lemmatized form of the word  
  - `a`: part of speech (adjective)  
  - `01`: index for the specific meaning  


### Synonyms

- Use the `lemmas()` method on a Synset to get a list of Lemma objects.
- Each Lemma represents a synonym.
- Use `lemma.name()` to get the synonym string.

``` Python 
synonyms = set()

for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print(synonyms)#{'glad', 'felicitous', 'happy', 'well-chosen'}
```
### Antonyms

- If a Lemma has antonyms in the database:
  - Use `lemma.antonyms()` to get a list of Lemma objects representing antonyms.
  - If none exist, an empty list is returned.

``` Python
lemmas = happy.synsets[0].lemmas()
print(lemmas)# [Lemma('happy.a.01.happy')]

print(lemmas[0].antonyms())# [Lemma('unhappy.a.01.unhappy')]
```
### Part of Speech Tags

- `n` – noun  
- `v` – verb  
- `a` – adjective  
- `r` – adverb  
- `s` – adjective satellite (for similar adjectives)


## Deleting Stop Words & Using N-Grams

### Stop Words

- **Stop words** are common words (like *and*, *the*, *is*) that are often removed from text because they carry little meaningful information.

- **NLTK** provides predefined lists of stop words for many languages.
- You must **download** the stop words using:


``` Python
from nltk.corpus import stopwords

stops = stopwords.words('english')
#print(stops)

from textblob import TextBlob
blob5 = TextBlob('Today is a beautiful day.')
get_words = [word for word in blob5.words if word not in stops]
print(get_words)# ['Today', 'beautiful', 'day']
```

### N-Grams

- An **n-gram** is a sequence of *n* items (letters or words) from a given text.
- Useful in tasks like:
  - Autocomplete predictions
  - Speech-to-text enhancements
  - Text pattern recognition

- **Types**:
  - **Unigram** – single word
  - **Bigram** – pair of consecutive words
  - **Trigram** – three consecutive words (default in TextBlob)

- **TextBlob Example**:

    ```python
    from textblob import TextBlob
    blob = TextBlob("Today is a beautiful day")
    print(blob.ngrams(n=3))
    ```

- Trigrams from the sentence:
  - ('Today', 'is', 'a')
  - ('is', 'a', 'beautiful')
  - ('a', 'beautiful', 'day')


``` Python

from textblob import TextBlob
blob6 = TextBlob('Today is a beautiful day. Tomorrow looks like bad weather.')

print(blob6.ngrams())
# [WordList(['Today', 'is', 'a']), 
#  WordList(['is', 'a', 'beautiful']), 
#  WordList(['a', 'beautiful', 'day']), 
#  WordList(['beautiful', 'day', 'Tomorrow']), 
#  WordList(['day', 'Tomorrow', 'looks']), 
#  WordList(['Tomorrow', 'looks', 'like']), 
#  WordList(['looks', 'like', 'bad']), 
#  WordList(['like', 'bad', 'weather'])]
# print(blob6.ngrams(n = 10))# [WordList(['Today', 'is', 'a', 'beautiful', 'day', 'Tomorrow', 'looks', 'like', 'bad', 'weather'])]
print(len(blob6.split()))# as word_count == 10 so out put for n = 10 is a list 
print(blob6.ngrams(n = 8))
print(len(blob6.ngrams(n = 8)))# 10 - 8 + 1
print(len(blob6.ngrams(n = 7)))# 10 - 7 + 1
print(len(blob6.ngrams(n = 6)))# 10 - 6 + 1
```









