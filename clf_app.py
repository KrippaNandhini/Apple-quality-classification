import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('ext_model.pkl')

# Function to predict the quality
def predict_quality(size, weight, sweetness, crunchiness, juiciness, ripeness, acidity):
    input_data = [[size, weight, sweetness, crunchiness, juiciness, ripeness, acidity]]
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        return 'Good Quality'
    else:
        return 'Bad Quality'

# Main function to run the Streamlit app
def main():
    st.title('Apple Quality Classifier')
    st.write('This app predicts the quality of apples based on various features.')

    # Input features
    size = st.slider('Size', min_value=0.0, max_value=10.0, step=0.1)
    weight = st.slider('Weight', min_value=0.0, max_value=5.0, step=1.0)
    sweetness = st.slider('Sweetness', min_value=0.0, max_value=10.0, step=0.1)
    crunchiness = st.slider('Crunchiness', min_value=0.0, max_value=10.0, step=0.1)
    juiciness = st.slider('Juiciness', min_value=0.0, max_value=10.0, step=0.1)
    ripeness = st.slider('Ripeness', min_value=0.0, max_value=10.0, step=0.1)
    acidity = st.slider('Acidity', min_value=0.0, max_value=10.0, step=0.1)

    if st.button('Predict'):
        result = predict_quality(size, weight, sweetness, crunchiness, juiciness, ripeness, acidity)
        st.write('The predicted quality is:', result)

if __name__ == '__main__':
    main()
