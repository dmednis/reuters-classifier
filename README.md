# reuters-classifier
The contents of this repository try to classify the Reuters-21578 dataset using a convolutional neural network.

## Running
* Requirments: NodeJS >= 8, Python 3.5, Tensorflow, Numpy, Scipy 

### Parse raw dataset
* `cd paser`
* `npm install xml2js`
* `node parser.js`

### Pytonify dataset
* `python pythonify.py`

### Run training and evaluation
* `python train.py`


## References
* [Multi class text classification](https://github.com/jiegzhan/multi-class-text-classification-cnn)
* [Convolutional Neural Network for Text Classification in Tensorflow](https://github.com/dennybritz/cnn-text-classification-tf)
