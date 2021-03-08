import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from weights import download_weights
from model import download_model

def main():

  st.set_option("deprecation.showfileUploaderEncoding",False)
  @st.cache(allow_output_mutation=True)
  def load_model():
    download_model()
    model=tf.keras.models.load_model("model/food_model.h5")
    model.compile(optimizer =tf.keras.optimizers.Adam(learning_rate=0.00001,decay=0.0001),metrics=["accuracy"],
                  loss= tf.keras.losses.CategoricalCrossentropy(label_smoothing=0.1))
    download_weights()
    model.load_weights("weights/food_weight.h5")

    return model

  model=load_model()
  st.title("FoodRecognizer")
  st.header("Deeplearning Model to predict the food")
  photo=Image.open("burger-icon-with-slice-pizza-soda-icon-illustration_138676-132.jpg")
  st.image(photo,use_column_width=True)
  file=st.file_uploader("Please Upload PHOTO", type=["jpg","png"])
  from PIL import Image,ImageOps

  def import_predict(image_data,model):
    size=(299,299)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img=img/255.0
    img_reshape=np.expand_dims(img, axis = 0)
    prediction=model.predict(img_reshape)
    return prediction

  if file is None:
    i=2
  else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    predictions=import_predict(image,model)
    class_name=["pizza","softdrink","burger"]
    string="This is a "+class_name[np.argmax(predictions)]
    st.success(string)
    
if __name__=='__main__':
    main()
    
