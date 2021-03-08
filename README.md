# Model Deployment using Streamlit

## Procedure:
Follow the steps to deploy the model of food recognition
!git clone https://github.com/hrsht-13/STREAMLIT.git
#### STEP 1
Change your directory to STREAMLIT
>`%cd STREAMLIT/`
#### STEP 2
> `pip install -r requirements.txt`
#### STEP 3
Connect to your ngrok account. Run the command that will add your authtoken to the default ngrok.yml. If you dont have an account run the below command.
> `!ngrok authtoken 1mWgwxghOSQ2x0LfNFTzYTnJ9zK_81vqRPDdijfPjq8ozBdGq`
#### STEP 4
Now connect to the port and click on the url link.
> `from pyngrok import ngrok`

> `public_url = ngrok.connect(port=8501)`

> `print (public_url)`

> `!streamlit run app.py >/dev/null`

Keep the program connected and open the generated link in the browser.
#### STEP 7
GO AHEAD!!!!
#### STEP 8
To disconect the server use-
> `ngrok.kill()`
