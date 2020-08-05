# ai-fashion-image-classifier
AI Fashion Item Classifier is an AI image classifier webservice built by using Python, Keras and Tensorflow. The Deep Learning CNN(Convolutional Neural Network) model adopted in this project trained with the Fashion MNIST dataset.

### Item Class Mapping
This classifer is able to identify the following 10 item classes:
|Class ID| Class Name |
| ------ | ------ |
|0|T-shirt/top|
|1|Trouser|
|2|Pullover|
|3|Dress|
|4|Coat|
|5|Sandal|
|6|Shirt|
|7|Sneaker|
|8|Bag|
|9|Ankle boot|

### How it works:
 - By sending POST method to the service with a fashion item image  
 - The classifer will tell you which class of your item belongs to
 - Magic!


### How to test fashion image classifier?

##### Method 1. Fashion image classifier tell you which class it belongs:
**Input(form-data):**
```sh
{
    "image": <YOUR_IMAGE_FILE> #Selected image
}
```

**Return result:**
```sh
{
    "Predict Item Class": "Bag" #Fashion image classifier think it belongs to which class
}
```

##### Method 2. Compare actual class with Fashion image classifier predicition:
**Input(form-data):**
```sh
{
    "class_id": <UPLOAD_IMAGE_CLASS>, #refer to above class mapping , E.g. 8 = Bag 
    "image": <YOUR_IMAGE_FILE> #Selected image
}
```
[Refer to Class mapping](#item-class-mapping)

**Return result:**
```sh
{
    "Predict Item Class": "Bag", #Fashion image classifier think it belongs to which class
    "Actual Item Class": "Trouser",  #You specific fashion image class
    "Guess Result": "Correct! Cheers~"
}
```

### Technology Used:
 - Python
 - Jupyter notebook
 - Keras
 - Tensorflow


### Training Dataset
[![Zalando](https://s3-eu-central-1.amazonaws.com/zalando-wp-zalando-research-staging/2016/12/cropped-161129_ZalandoResearch_logo_rgb.png)](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/)

**Fashion-MNIST** is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking deep learning algorithms. It shares the same image size and structure of training and testing splits.

## Deep Learning Model
### CNN (Convolutional Neural Network) Layer
- Two CNN Layer (Feature detection & Max pooling)

### FCN (Full Connected Network) Layer
- Two FCN hidden Layer (with 512 neuron)

### Folder Structure
``` bash
├── jupyter_notebook
│   └── CNN_fashion_image_classifier.ipynb #Jupyter notebook for training Keras Tensorflow model
├── loader.py   #Dependency Injection handler
├── main.py     #Main program
├── requirements.txt     #List of dependency used by this project 
├── model
│   ├── CNN_fashion_image_classifier_v1.h5 #Tensorflow model
│   ├── CnnModel.py #Tensorflow Model
├── route
│   ├── AiRoute.py  #Routing handling
├── service
│   ├── AiService.py #Business logic
└── upload
    └── tmp #Temp upload folder for image resizing
```

## Installation
It requires Python 3.7 and related dependenices

```sh
cd ai-fashion-image-classifier/

#install related dependencies
pip install -r requirements.txt

#run the fashion image classifier
python main.py
```

### Todos

 - Improve CNN model to archive higher accuracy
 - Adopt better Dependenct injection package that suit for flask_restful
 - Adopt swagger for RESTful API

License
----

MIT
