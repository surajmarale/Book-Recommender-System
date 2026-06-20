import streamlit as st
import pickle
import numpy as np

pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

st.set_page_config(page_title="Book Recommender System", layout="wide")

st.title("Book Recommender System")

book = st.selectbox(
    "Enter Book Name",
    sorted(pt.index.tolist())
)

if st.button("Recommend"):

    idx = np.where(pt.index == book)[0][0]

    similar = sorted(
        enumerate(similarity_scores[idx]),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    cols = st.columns(4)

    for i, item in enumerate(similar):

        data = books[
            books['Book-Title'] == pt.index[item[0]]
        ].drop_duplicates('Book-Title')

        with cols[i]:
            st.image(data['Image-URL-M'].values[0], width=180)
            st.write(data['Book-Title'].values[0])
            st.write(data['Book-Author'].values[0])