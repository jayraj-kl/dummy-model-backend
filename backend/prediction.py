import numpy as np
from tensorflow import keras
from keras.models import model_from_json

json_file = open('model_final.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model_final.h5")


def get_prediction(train_data):
    s=''
    for i in range(len(train_data)):
        train_data[i]=np.array(train_data[i])
        train_data[i]=train_data[i].reshape(1,28,28,1)
        result = np.argmax(loaded_model.predict(train_data[i]), axis=-1)
        if(result[0]==10):
            s=s+'+'
        if(result[0]==11):
            s=s+'-'
        if(result[0]==12):
            s=s+'/'
        if(result[0]==13):
            s=s+'*'
        if(result[0]==0):
            s=s+'0' 
        if(result[0]==1):
            s=s+'1'
        if(result[0]==2):
            s=s+'2'
        if(result[0]==3):
            s=s+'3'
        if(result[0]==4):
            s=s+'4'
        if(result[0]==5):
            s=s+'5'
        if(result[0]==6):
            s=s+'6'
        if(result[0]==7):
            s=s+'7'
        if(result[0]==8):
            s=s+'8'
        if(result[0]==9):
            s=s+'9'
    return s