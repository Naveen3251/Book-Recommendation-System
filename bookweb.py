import streamlit as st
import pickle as pk
import pandas
import numpy as np


# loading
pop = open('Populars (1).pkl', 'rb')
popular = pk.load(pop)
#books
bo=open('books2.pkl','rb')
book_data=pk.load(bo)
#similarities
sim=open('similarity_score2.pkl','rb')
similarity_score=pk.load(sim)
#matrix
ma=open('matrix.pkl','rb')
matrix=pk.load(ma)
#dis
display=pk.load(open('display.pkl','rb'))
st.title("BOOK WEB")
#recommedn function
def recommend(text):
    try:
        # fetching index
        index = np.where(matrix.index == text)[0][0]
        # getting similar items with the help of index
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]
        data = []
        for i in similar_items:
            item = []
            temp = book_data[book_data['Book-Title'] == matrix.index[i[0]]]
            item.extend(list(temp['Book-Title'].values))
            item.extend(list(temp['Book-Author'].values))
            item.extend(list(temp['Image-URL-M'].values))
            data.append(item)
        return data
    except:
        return "Enter correct name"



nav = st.sidebar.radio("BOOK WEB", ['Popularity', 'Recommend Book'])
if nav=='Popularity':
    st.header("Top 50 Books")
    # loading the data as list
    book_name = list(popular['Book-Title'].values)
    author = list(popular['Book-Author'].values)
    image = list(popular['Image-URL-L'].values)
    votes = list(popular['Popularity_ratings'].values)
    rating = list(popular['Popularity_avg_ratings'].values)

    for i in range(0, len(book_name), 5):
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(image[i])
            st.write(book_name[i])
            st.write(author[i])
            st.write('Votes : ', votes[i])
            st.write('Ratings : ', round(rating[i] * 100))
        with col2:
            st.image(image[i + 1])
            st.write(book_name[i + 1])
            st.write(author[i + 1])
            st.write('Votes : ', votes[i + 1])
            st.write('Ratings : ', round(rating[i + 1] * 100))

        with col3:
            st.image(image[i + 2])
            st.write(book_name[i + 2])
            st.write(author[i + 2])
            st.write('Votes : ', votes[i + 2])
            st.write('Ratings : ', round(rating[i + 2] * 100))

        with col4:
            st.image(image[i + 3])
            st.write(book_name[i + 3])
            st.write(author[i + 3])
            st.write('Votes : ', votes[i + 3])
            st.write('Ratings : ', round(rating[i + 3] * 100))

        with col5:
            st.image(image[i + 4])
            st.write(book_name[i + 4])
            st.write(author[i + 4])
            st.write('Votes : ', votes[i + 4])
            st.write('Ratings : ', round(rating[i + 4] * 100))


if nav=='Recommend Book':
    st.image('book.jfif')
    st.write(display.iloc[:,3])
    text=st.text_input("Enter your favourite book",key=99)
    if st.button("SUBMIT"):
       rec=recommend(text)
       if rec!="Enter correct name":
           col1, col2, col3 = st.columns(3)
           col4, col5 = st.columns(2)
           with col1:
               st.write(rec[0][0])
               st.write(rec[0][1])
               st.image(rec[0][2])
           with col2:
               st.write(rec[1][0])
               st.write(rec[1][1])
               st.image(rec[1][2])
           with col3:
               st.write(rec[2][0])
               st.write(rec[2][1])
               st.image(rec[2][2])
           with col4:
               st.write(rec[3][0])
               st.write(rec[3][1])
               st.image(rec[3][2])
           with col5:
               st.write(rec[4][0])
               st.write(rec[4][1])
               st.image(rec[4][2])
       else:
           st.error("Enter correct name")




