from tensorflow.keras.models import Model, load_model
import json, pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences


#load model
model = load_model("emodetext_model.h5")

with open('Tokenizer', "rb") as f:
    Tokenizer = pickle.load(f)
Max_padd = 66

emotions_dico = {0: 'sadness', 1: 'anger', 2: 'love', 3: 'surprise', 4: 'fear', 5: 'joy'}


def predict_emo(text_to_predict):

    #load model
    #model = load_model("emodetext_model.h5")
    #tokenization
    my_seqence = Tokenizer.texts_to_sequences(text_to_predict)
    #padding
    my_seqence = pad_sequences(my_seqence, maxlen=Max_padd, padding='post')
    #prediction
    my_pred = np.argmax( model.predict(my_seqence), axis=-1)

    #retrieve the text emotion
    emotion = emotions_dico[my_pred[0]]
    return emotion