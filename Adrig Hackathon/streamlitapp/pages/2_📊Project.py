import streamlit as st
from predict_result import predict_text
from predict_result import data
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt



st.title('Sentiment Analysis 😃')
st.markdown('----')

def sidbar():
    with st.sidebar:
        st.title('Sentiment Analysis with your Data')
        st.info('Welcome to the Sentiment Analysis App. Choose your options below')
        st.markdown('---')
        
        option = st.sidebar.selectbox('Make a choice', ['Predict','Data Frame'])
    if option == 'Predict':
        predict()
    elif option == 'Data Frame':
        yourdata()


def predict():
    io=st.text_input('Enter your sample line for the analysis',placeholder='Input text Here')
    result=predict_text(io)
    if io:
        if result>1:
            image = Image.open('positive.PNG')
            status='Positive'
        elif result==1:
            status='Neutral'
            image = Image.open('neutral.PNG')
        else:
            image=Image.open('negative.PNG')
            status="Negative"
        st.image(image,status)


def yourdata():
    with st.sidebar:
        doc=st.file_uploader("Upload your Review file and Click Process",type=("csv"))
        flag=0
        if st.button("Process"):
            with st.spinner("Processing"):
                if doc is not None:
                    result=data(doc)
                    flag=1
                    st.success(f'File {doc.name} is successfully Processed!')
                    
    if flag:               
        st.write(result)
        visual(result)
        

def visual(result):
    st.title('Plotting the distribution of Predicted Results')
    fig = px.histogram(x=result['sentiment'], title='Count Plot')
    fig.update_layout(
    xaxis_title="Sentiment",
    yaxis_title="Count",
    )
    st.write(fig)

    
    colors = ("yellowgreen", "gold", "red")
    tags = result['sentiment'].value_counts()
    labels='Positive','Neutral','Negative'
    explode = (0.1,0.1,0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(tags, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90,colors=colors)
    ax1.axis('equal')  
    st.title("Pie Chart")
    st.pyplot(fig1)
      
    

            
    


                    
if __name__=='__main__':
    sidbar()