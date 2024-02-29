import streamlit as st
from PIL import Image

def main():

    st.set_page_config(
        page_title="Sentiment Analysis",
        page_icon="🕸",
        layout="wide",
        initial_sidebar_state="auto")

    st.title("Sentiment Analysis Using Machine Learning 😀")
    st.markdown("----------------------------------------")
    st.subheader("About the Project")
    st.write("Our project involves sentiment analysis, leveraging a dataset comprising 27,000 samples from Kaggle. The data undergoes preprocessing through a pipeline that utilizes TF-IDF vectorization, followed by classification using the Multinomial Naive Bayes classifier. Achieving an accuracy of 78.83%, we've successfully trained the model. Additionally, we've developed a user-friendly Streamlit web app for predicting sentiments in unknown test data, enhancing accessibility and usability.")
    image = Image.open('Screenshot 2024-02-29 at 10.59.11.png')
    st.image(image)

if __name__=='__main__':
    main()
