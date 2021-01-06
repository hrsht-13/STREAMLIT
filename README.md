# Model Deployment using Streamlit

## Procedure:
Follow the steps to deploy the model of food recognition
#### STEP 1
Change your directory to STREAMLIT
>`%cd STREAMLIT-main/`
#### STEP 2
> `pip install -r require.txt`
#### STEP 3
> `!python model.py`
#### STEP 4
Download the weights of the model from the following [link](https://drive.google.com/file/d/18srnxP3y6hiKjDRN6ffEc9nbwPelSZtA/view?usp=sharing)

(Save the downloaded file in same directory)
#### STEP 5
Connect to your ngrok account. Run the command that will add your authtoken to the default ngrok.yml. If you dont have an account run the below command.
> `!ngrok authtoken 1mWgwxghOSQ2x0LfNFTzYTnJ9zK_81vqRPDdijfPjq8ozBdGq`
#### STEP 6
Now connect to the port and click on the url link.
> `public_url = ngrok.connect(port=8501)`

> `print (public_url)`

> `!streamlit run app.py >/dev/null`
#### STEP 7
GO AHEAD!!!!
#### STEP 8
To disconect the server use-
> `ngrok.kill()`
