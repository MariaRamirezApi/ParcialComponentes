import nltk #library
from nltk.corpus import wordnet #library
synonyms = [] #list for synonyms
antonyms = [] #list for antonyms
word="good" #word
  
for syn in wordnet.synsets(word): #look up the word in the wordnet lexicon
    for l in syn.lemmas(): #synonyms
        synonyms.append(l.name()) #the synonym is added to the list
        if l.antonyms():  #find antonyms
            antonyms.append(l.antonyms()[0].name()) #the antonym is added to the list

syn = wordnet.synsets(word) #for definition and examples

print ('\nThe definition of the word',word,'is:',syn[1].definition())
print ('\nThe synonyms of the word',word,'are:\n')
print(set(synonyms))
print ('\nThe antonyms of the word',word,'are:\n')
print(set(antonyms))
print ('\nExamples of the word',word,':', str(syn[1].examples()))
