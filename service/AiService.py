import os
import numpy as np
import werkzeug
import tensorflow as tf
from PIL import Image as pilImage
from model.CnnModel import CnnModel

#service class
class AiService():

    def __init__(self, cnnModel):
        self.cnnModel = cnnModel
        self.uploadPath = './upload/tmp/'

    def classify(self, imgFile):
        print(f'<Start processing>:')
        print('----------------------\n')

        #prepare filename for resize
        filename = imgFile.filename
        resizeFilename = 'resize_'+filename


        #save and read image file
        print(f'<Save, convert color and resize Image>:')
        imgFile.save(self.uploadPath + filename)

        #convert image to single gray color layer
        img = pilImage.open(self.uploadPath + filename).convert('L')
        print(f'Before: type: {type(img)}, im.size: {img.size}, im.mode: {img.mode}')

        #resize image
        resizeImg = img.resize((28, 28))
        print(f'After:  type: {type(resizeImg)}, im.size: {resizeImg.size}, im.mode: {resizeImg.mode}')

        resizeImg.save(self.uploadPath+resizeFilename)
        print('----------------------\n')

        #normalize input between 0 to 1
        print(f'<Format input - Normalize>:')
        imgArr = np.array(resizeImg)
        print(f'Before Normalize - Array: shape: {imgArr.shape} \n Orginal Value: {imgArr[0]}')
        normImgArr = np.asarray(imgArr/255,dtype=float)
        print(f'After Normalize - Array: shape: {normImgArr.shape} \n Normalized Value: {normImgArr[0]}')
        print('----------------------')

        #reshape image array
        print(f'<Format input - Reshape>:')
        print(f'Before reshape - Array: shape: {normImgArr.shape} ')
        normImgArr = normImgArr.reshape(1,28,28,1)
        print(f'After reshape - Array: shape: {normImgArr.shape} ')
        print('----------------------\n')

        #invoke CNN model to predict
        print(f'<Invoke CNN model>:')
        rawResult = self.cnnModel.imageClassifier.predict(normImgArr)
        result = np.argmax(rawResult)
        print(f'Predict result: {str(result)}')
        print('----------------------\n')
        
        print('<End processing>')
        #remove image file
        os.remove(self.uploadPath + filename)
        os.remove(self.uploadPath + resizeFilename)

        return result
