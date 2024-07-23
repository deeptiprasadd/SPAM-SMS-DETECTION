For my recent project, I developed an AI model to classify SMS messages as spam or legitimate. Here’s a brief overview:

### Approach:
1. **Data Collection and Cleaning**: Used a public dataset of labeled SMS messages, removed non-alphanumeric characters, converted text to lowercase, and removed stop words.

2. **Feature Extraction**:
   - **TF-IDF**: Converted text data into numerical features by measuring word importance.
   - **Word Embeddings**: Represented words in a continuous vector space to capture semantic relationships.

3. **Data Processing**:
   - Applied the TF-IDF vectorizer to transform the cleaned text data into numerical format.
   - Prepared the data for training and testing by splitting it into training and test sets.

4. **Model Building**

### Deployment:
- **Streamlit App**: Used a pkl file and vectorize file to build a Streamlit app that showcases the prediction results in a user-friendly interface.

### DATASET: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

This project showcased the potential of AI in improving communication systems by accurately identifying spam messages.
