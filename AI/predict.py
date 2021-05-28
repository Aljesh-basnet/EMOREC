# import tensorflow.keras as keras
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model

# def get_emotion(value):
#     emotions={'joy':0,'anger':1,'love':2,'sadness':3,'fear':4,'surprise':5}
#     for emo, val in emotions.items():
#         if value==val:
#             return emo

# def predict(sentence):
#     modelreload = load_model('Bilstm.h5')
#     sentenceList=[]
#     sentenceList.append(sentence)
#     token =Tokenizer()  
#     token.fit_on_texts(sentenceList)
#     encoded_text1 = token.texts_to_sequences(sentenceList)
#     X_test=pad_sequences(encoded_text1,maxlen=80,padding='post')
#     answer= get_emotion(modelreload.predict_classes(X_test))
   