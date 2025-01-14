!pip install rouge
import pandas as pd
import numpy as np
from rouge import Rouge 

def rouge_scores(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference)
    return scores

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
def solve(text):
  stopwords1 = set(stopwords.words("english"))
  words = word_tokenize(text)
  freqTable = {}
  for word in words:
    word = word.lower()
    if word in stopwords1:
      continue
    if word in freqTable:
      freqTable[word] += 1
    else:
      freqTable[word] = 1

  sentences = sent_tokenize(text)
  sentenceValue = {}
  for sentence in sentences:
    for word, freq in freqTable.items():
      if word in sentence.lower():
        if sentence in sentenceValue:
          sentenceValue[sentence] += freq
        else:
          sentenceValue[sentence] = freq
  sumValues = 0
  for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]
  average = int(sumValues / len(sentenceValue))

  summary = ''
  for sentence in sentences:
    if (sentence in sentenceValue) and(sentenceValue[sentence] > (1.2 * average)):
      summary += "" + sentence
  return summary
data = '''As per the survey, stemming in used as a pre-processing step in most of the existing research, although the generated stem may not be a valid word of the language. In the proposed approach, lemmatization is used which properly reduces words to their root form generating meaningful lemmas by takingthe context of the words into account unlike stemming. It was
also identified from the survey that in most cases, the Natural Language Toolkit (NLTK) alone was used for conducting pre-processing tasks, although it isn’t capable of performing
lemmatization and Part-of-Speech (POS) tagging accurately. In the proposed model, Stanford CoreNLP [11] is used alongside NLTK as it yields better performance at the two above mentioned tasks. Duplicate removal was hardly addressed and
is a stage that is added in the proposed approach to mitigate
overfitting.A combination of various features, that have been considered in separate experiments in existing research and have proven to be effective in identifying the significance of a sentence in a document, is used in this paper. The performance
of Support Vector Machine (SVM), K-Nearest Neighbour (KNN) and Decision Tree algorithms is compared and the generated summary is also converted to an audio clip which eliminates the need to devote specific reading time.'''
s=solve(data)
print("\n\n\n",s)
print("\n\nRouge scores:",rouge_scores(data,s))