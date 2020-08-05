import tensorflow as tf
from tensorflow.keras.models import load_model

#service class
class CnnModel():
    def __init__(self):
        self.loadFashionImageClassifierModel()

    #load train model
    def loadFashionImageClassifierModel(self):
        print("* \n Loading Keras model and Flask starting server...\n please wait until server has fully started ")
        self.imageClassifier = load_model('./model/CNN_fashion_image_classifier_v1.h5')

