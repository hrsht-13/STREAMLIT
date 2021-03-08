# -*- coding: utf-8 -*-
"""model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15sZDyMCXWjtIu3iMLRQp5Hjhb5PiW1Hg
"""

from tensorflow.keras.layers import Dense, Flatten, GlobalAveragePooling2D, BatchNormalization, Dropout,AveragePooling2D
import tensorflow as tf
from keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from keras.models import Model
from keras.models import Sequential
from keras.regularizers import *
from tensorflow import keras
from tensorflow.keras import layers
from pyngrok import ngrok


resnet=InceptionResNetV2(weights="imagenet")
x=resnet.layers[-2].output
fc1=Dense(3,kernel_initializer='glorot_uniform', kernel_regularizer=l2(.0005),activation='softmax')(x)
model=Model(inputs=resnet.input,outputs=fc1)
model.save("model/food_model.h5")
