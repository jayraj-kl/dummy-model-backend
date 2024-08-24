from preprocessing import preprocess_data
from prediction import get_prediction
import os

def predict():
    preprocessed_img = preprocess_data("t8.png")
    prediction = get_prediction(preprocessed_img)
    if os.path.exists("./t8.png"):
        os.remove("./t8.png")
    print(prediction)

predict()