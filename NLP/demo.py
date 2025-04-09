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








