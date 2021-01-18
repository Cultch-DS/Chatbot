import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import json
import random

with open ("chatbot.json") as file:
	data = json.load(file)

print(data)