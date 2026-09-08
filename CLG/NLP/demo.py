from textblob import TextBlob
# Creating a TextBlob object 
txt = 'Today is a beautiful day. Tomorrow looks like bad weather.'
blob = TextBlob(txt)
#print(blob)


# Tokenization
# print(blob.sentences)# Tokenize the text into sentences
# print(blob.words) # Tokenize the text into words


# Part-of-Speech Tagging
# print(blob.tags) # Get the part-of-speech tags for each word in the text
# print(blob.sentences[0].tags) # Get the part-of-speech tags for each word in the first sentence


# print(blob.noun_phrases) # Extract noun phrases

# Sentiment Analysis with TextBlob’s Default Sentiment Analyzer
# print(blob.sentiment) # Get the sentiment of the text
# print(blob.sentiment.polarity) # Get the polarity of the text
# print(blob.sentiment.subjectivity, '\n') # Get the subjectivity of the text

# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity) # Get the polarity of each sentence
#     print(sentence.sentiment.subjectivity) # Get the subjectivity of each sentence

new_blob = TextBlob('I am not good at this.')
# print(new_blob.sentiment) # Get the sentiment of the text
# print(new_blob.sentiment.polarity) # Get the polarity of the text
# print(new_blob.sentiment.subjectivity) # Get the subjectivity of the text

from textblob import Sentence
# print(Sentence('I am not good at this.').sentiment)#Sentiment(polarity=-0.35, subjectivity=0.6000000000000001)
# print(Sentence('The movie was excellent!').sentiment)#Sentiment(polarity=1.0, subjectivity=1.0)

# print(Sentence('The movie was not good.').sentiment)#Sentiment(polarity=-0.5, subjectivity=0.5)

# Sentiment Analysis with the NaiveBayesAnalyzer
from textblob.sentiments import NaiveBayesAnalyzer

blob2 = TextBlob("I am not a good boy", analyzer=NaiveBayesAnalyzer())
# print(blob2.sentiment)# Sentiment(classification='neg', p_pos=0.47662917962091056, p_neg=0.5233708203790892)


sentence = TextBlob('Hey there! How are you?. I am not good at this.')
# for s in sentence.sentences:
#     print(s.sentiment) # Get the sentiment of each sentence


# Language Detection and Translation

blob3 = TextBlob('Bonjour tout le monde')
#print(blob3.detect_language()) # Detect the language of the text
# not working but.....

# spanish = blob3.translate(to='es')
# print(spanish)

# chinese = blob.translate(to='zh')
# print(chinese)# Translate the text to Chinese

# print(spanish.translate())# Translate the text to english
# print(chinese.translate())# Translate the text to english
# Note the slight difference in the English results.

from textblob import Word
word = Word('index')
# print(word.pluralize()) # Pluralize the word

word2 = Word('indices')
# print(word2.singularize()) # Singularize the word

heroes = TextBlob('Superman Batman Spiderman').words
# print(heroes.pluralize()) # Pluralize the words ['Supermen', 'Batmen', 'ands', 'Spidermen']
# print(heroes.singularize()) # Singularize the words ['Superman', 'Batman', 'and', 'Spiderman']

#Spell Checking and Correction
from textblob import Word

word = Word('thery')

# print(word.spellcheck())# [('they', 0.5634568607812277), ('there', 0.4252396623265131), ('theory', 0.011303476892259265)]
#for suggestion, probability in word.spellcheck():
    #print(f"Suggestion: {suggestion}, Probability: {probability:.2f}")
# Suggestion: they, Probability: 0.56
# Suggestion: there, Probability: 0.43
# Suggestion: theory, Probability: 0.01

#print(word.correct())#they
# chooses word with the highest confidence value

sentence = TextBlob('Ths sentense has missplled wrds.')
#print(sentence.correct())# The sentence has misspelled words.


# Normalization: Stemming and Lemmatization

from textblob import Word
word3 = Word('varieties')
# print(word3.stem())# varieti

# print(word3.lemmatize())#variety


# Word Frequencies
from pathlib import Path
from textblob import TextBlob

blob4 = TextBlob(Path(r'E:\Languages\Python\NLP\hehe.md').read_text())
# print(blob4.word_counts['blob'])# 2
# print(blob4.word_counts['print'])# 25
# print(blob4.word_counts['g'])# 0 searches exact match 

# Getting Definitions, Synonyms and Antonyms from WordNet
from textblob import TextBlob
happy = Word('happy')
# print(happy.definitions)
#['enjoying or showing or marked by joy or pleasure', 'marked by good fortune', 'eagerly disposed to act or to be of service', 'well expressed and to the point']

# print(happy.synsets)
# [Synset('happy.a.01'), Synset('felicitous.s.02'), Synset('glad.s.02'), Synset('happy.s.04')]

synonyms = set()

for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

# print(synonyms)#{'glad', 'felicitous', 'happy', 'well-chosen'}


lemmas = happy.synsets[0].lemmas()
# print(lemmas)# [Lemma('happy.a.01.happy')]

# print(lemmas[0].antonyms())# [Lemma('unhappy.a.01.unhappy')]

# for i in happy.synsets:
#     lemmas = i.lemmas()
#     for j in lemmas:
#         antonyms = lemma.antonyms()
#         if antonyms:  # Check if there are antonyms
#             print(f"Antonyms of {lemma.name()}: {[antonym.name() for antonym in antonyms]}")
        
# deleting stop words
from nltk.corpus import stopwords

stops = stopwords.words('english')
#print(stops)

from textblob import TextBlob
blob5 = TextBlob('Today is a beautiful day.')
get_words = [word for word in blob5.words if word not in stops]
# print(get_words)# ['Today', 'beautiful', 'day']

# N grams:
from textblob import TextBlob
blob6 = TextBlob('Today is a beautiful day. Tomorrow looks like bad weather.')

# print(blob6.ngrams())
# [WordList(['Today', 'is', 'a']), 
#  WordList(['is', 'a', 'beautiful']), 
#  WordList(['a', 'beautiful', 'day']), 
#  WordList(['beautiful', 'day', 'Tomorrow']), 
#  WordList(['day', 'Tomorrow', 'looks']), 
#  WordList(['Tomorrow', 'looks', 'like']), 
#  WordList(['looks', 'like', 'bad']), 
#  WordList(['like', 'bad', 'weather'])]
# print(blob6.ngrams(n = 10))# [WordList(['Today', 'is', 'a', 'beautiful', 'day', 'Tomorrow', 'looks', 'like', 'bad', 'weather'])]
# print(len(blob6.split()))# as word_count == 10 so out put for n = 10 is a list 
# print(blob6.ngrams(n = 8))
# print(len(blob6.ngrams(n = 8)))# 10 - 8 + 1
# print(len(blob6.ngrams(n = 7)))# 10 - 7 + 1
# print(len(blob6.ngrams(n = 6)))# 10 - 6 + 1

# 12.3, 12.5 12.6, 12.7
# Visualizing Word Frequencies with Bar Charts and Word Clouds

# Visualizing Word Frequencies
# Visualizing word frequencies can enhance corpus analysis. Depending on your focus, different visualizations work better:

#Bar Chart: Shows the top 20 words in Romeo and Juliet with bars representing their frequencies.

# Word Cloud: Displays frequent words larger and less frequent words smaller.


#Loading the Data
from pathlib import Path
from textblob import TextBlob

blob7 = TextBlob(Path(r'E:\Languages\Python\NLP\romeojuliet.txt').read_text())

from nltk.corpus import stopwords
stop_words = stopwords.words('english')


#Getting the Word Frequencies
# Loading and Processing Data
# First, load Romeo and Juliet into IPython from the ch12 examples folder, along with NLTK's stopwords.

# Get word-frequency pairs using blob.word_counts.items().

# Remove stop words with a list comprehension: check if item[0] is not in stop_words.

# Sort the remaining words by frequency in descending order using sorted with itemgetter(1).

# Finally, slice the sorted list to get the top 20 words.

from pathlib import Path
from textblob import TextBlob
from nltk.corpus import stopwords
from operator import itemgetter

blob = TextBlob(Path(r'E:\Languages\Python\NLP\romeojuliet.txt').read_text())
stop_words = stopwords.words('english')
items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
sorted_items = sorted(items, key=itemgetter(1), reverse=True)

# Getting Top 20 Words and Visualizing
# Since the most frequent "word" is an apostrophe, we skip it and slice elements 1–20 from sorted_items.

# Convert the top20 list of tuples into a pandas DataFrame for easier plotting.

# Visualize the DataFrame using the bar method, setting x='word', y='count', and disabling the legend.

# Use plt.gcf().tight_layout() to adjust the layout and prevent word truncation.

top20 = sorted_items[1:21]

import pandas as pd
df = pd.DataFrame(top20, columns=['word', 'count'])
print(df)

axes = df.plot.bar(x='word', y='count', legend=False)

import matplotlib.pyplot as plt
plt.gcf().tight_layout()


# 12.4: Readability Assessment with Textatistic
# Readability Assessment with Textatistic
# Readability depends on vocabulary, sentence structure, length, and topic. We'll use the Textatistic library, which supports formulas like Flesch Reading Ease, Flesch-Kincaid, Gunning Fog, SMOG, and Dale-Chall.

# Installation:
# pip install textatistic
# (Windows users: Run Anaconda Prompt as Administrator if needed.)
# Calculating Readability:
# Load Romeo and Juliet into a text variable.
# Create a Textatistic object and call dict() to get stats and scores.

from pathlib import Path
from textatistic import Textatistic

text = Path(r'E:\Languages\Python\NLP\romeojuliet.txt').read_text()
readability = Textatistic(text)
print(readability.dict())
print(readability.char_count)
print(readability.word_count)
print(readability.sent_count)
print(readability.sybl_count)
print(readability.notdalechall_count)
print(readability.polysyblword_count)
print(readability.word_count)
# Statistics Provided:

# char_count: Characters
# word_count: Words
# sent_count: Sentences
# sybl_count: Syllables
# notdalechall_count: Words not familiar to 5th graders
# polysyblword_count: Words with 3+ syllables

# Readability Scores:

# flesch_score: Higher = easier (90+ = 5th grade, <30 = college level)
# fleschkincaid_score, gunningfog_score, smog_score, dalechall_score: All map to grade/education levels.
# gunningfog_score: Estimates the grade level needed to understand the text.
# smog_score: Estimates years of education required; very effective for healthcare materials.
# dalechall_score: Maps to grade levels (4th grade to college graduate); highly reliable across text types.


## (Fill-In) ________ indicates how easy is it for readers to understand text. Answer: Readability.


# 12.5 Named Entity Recognition with spaCy
# NLP can determine what a text is about. A key aspect of this is named entity recognition, which attempts to locate and categorize items like dates, times, quantities, places, people, things, organizations and more
# //*  Named entity recognition attempts to locate and categorize items like dates, times, quantities, places, people, things, organizations and more.


# Install spaCy

# Loading the Language Model
# The first step in using spaCy is to load the language model representing the natural language
# of the text you’re analyzing. To do this, you’ll call the spacy module’s load function.

import spacy
nlp = spacy.load('en_core_web_sm')
# Next, you use the nlp object to create a spaCy Doc object33 representing the document to process.
doc = nlp('In 1994, Tim Berners-Lee founded the')
# The Doc object’s ents property returns a tuple of Span objects representing the named entities found in the Doc.
for elements in doc.ents:
    print(elements.text,":", elements.label_)


## 12.6  Similarity Detection with spaCy
# Similarity detection is the process of analyzing documents to determine how alike they are. One possible similarity detection technique is word frequency counting
from pathlib import Path
import spacy
nlp_2 = spacy.load('en_core_web_sm')
doc_1 = nlp_2(Path(r'E:\Languages\Python\NLP\file_1.txt').read_text())
doc_2 = nlp_2(Path(r'E:\Languages\Python\NLP\file_2.txt').read_text())

# Comparing the Books’ Similarity
# Doc class’s similarity method to get a value from 0.0 (not similar) to 1.0 (identical) indicating
similarity = doc_1.similarity(doc_2)
print(f'similarity: {similarity}')
print(f'similarity: {similarity:.2f}')








