import tensorflow.keras as keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from django.shortcuts import render
import re
from tensorflow.keras.models import model_from_json
import numpy as np
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
# from AI_files.FYP_AI import x
from Emotion_detection.settings import *




def fit_on_data():
    total_text=preprocessing()
    token.fit_on_texts(total_text)

def tokenize(x):
    encoded_text = token.texts_to_sequences(x)
    padded_text=pad_sequences(encoded_text,maxlen=max_length,padding='post')
    return padded_text

def predict(request):
    # modelreload = load_model('AI_files/Bilstm_model.h5')
    fit_on_data()
    sentence = request.POST['sentence']
    sentenceList=[]
    sentenceList.append(sentence)  
    
    cleaned_sentence = clean(sentenceList)
    x_test = remove_stop_words(cleaned_sentence)
    x_test = get_stemmed_text(x_test)
    x_test = get_lemmatized_text(x_test)
    X_test= tokenize(x_test)
    answer= emotions[(np.argmax(modelreload.predict(X_test)))]
    print("The predicted emotion was: ",answer)
    print(X_test)
    # X_test=tokenize(sentenceList)
    # answer= emotions[(np.argmax(modelreload.predict(X_test)))]
    # print("The predicted emotion was: ",answer)
    # print(X_test)
    return render(request,'index.html',{'emotion':answer,'sentence':sentence})
       







