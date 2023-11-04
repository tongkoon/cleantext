import re

import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

import spacy

nlp = spacy.load("en_core_web_sm")


def clean_data(text):
  pattern = re.compile(r'@\S+|https?://\S+|www\.\S+|http?:\S+|[^A-Za-z\s]+')  #ลบตัวเลขออกด้วย
  pattern = pattern.sub(r' ', text)
  pattern = pattern.lower()
  return pattern

def normalized(text):
  doc = nlp(text)
  normalized_text = ' '.join([token.lemma_ for token in doc])
  normalized_text = normalized_text.lower()
  return normalized_text

def remove_stopword(text):
  stop_words = set(stopwords.words('english'))
  pattern=text.split()
  pattern=[word for word in pattern if not word in stop_words]
  pattern=' '.join(pattern)
  return pattern

def preprocess(text):
  textStr = clean_data(text)
  textStr = normalized(textStr)
  textStr = remove_stopword(textStr)
  
  return textStr


# text = "tock Success @tovk.com i like Eat."
# print (text)

# text = clean_data(text)
# print(text)

# text = normalized(text)
# print(text)

# text = remove_stopword(text)
# print(text)


