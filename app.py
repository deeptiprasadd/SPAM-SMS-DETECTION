import streamlit as st
import string
from nltk.corpus import stopwords
import joblib
import nltk
from nltk.stem.porter import PorterStemmer



@st.cache_resource
def load_model():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer

model, tfidf = load_model()

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation: # stopwords is now accessible
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if input_sms:

    # 1. preprocess
        transformed_sms = transform_text(input_sms)
    # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
    # 3. predict
        result = model.predict(vector_input)[0]
        # result = 9
    # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
    else:
        st.write("Please enter some text to classify.")
