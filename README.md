# ai-fashion-image-classifier
AI Fashion Item Classifier is an AI image classifier webservice built by using Python, Keras and Tensorflow. The CNN(Convolutional Neural Network) model adopted in this project trained with the Fashion MNIST dataset.

This classifer is able to identify the following 10 item type:
| Type  |
| ------ |
|T-shirt/top|
|Trouser|
|Pullover|
|Dress|
|Coat|
|Sandal|
|Shirt|
|Sneaker|
|Bag|
|Ankle boot|

### How it works:
 - By sending POST method to the service with a fashion item image  
 - The classifer will tell you which type of your item belongs to
 - Magic!
 

### Technology Used:
 - Python
 - Jupyter notebook
 - Keras
 - Tensorflow


## Training Dataset
[![Zalando](https://s3-eu-central-1.amazonaws.com/zalando-wp-zalando-research-staging/2016/12/cropped-161129_ZalandoResearch_logo_rgb.png)](https://research.zalando.com/welcome/mission/research-projects/fashion-mnist/)
**Fashion-MNIST** is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.


## Installation
It requires Python 3.7 and related dependenices

```sh
cd ai-fashion-image-classifier/
pip install
```

### Todos

 - Improve CNN modeal to archive higher accuracy

License
----

MIT
