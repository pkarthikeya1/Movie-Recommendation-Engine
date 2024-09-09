import pickle
import streamlit as st
import requests





def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    # recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommender System')
movies = pickle.load(open(r'C:\Users\karthikeya\RecSys\model\movie_list.pkl','rb'))
similarity = pickle.load(open(r'C:\Users\karthikeya\RecSys\model\similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    
    st.subheader(recommended_movie_names[0])

    st.subheader(recommended_movie_names[1])

    st.subheader(recommended_movie_names[2])

    st.subheader(recommended_movie_names[3])
    
    st.subheader(recommended_movie_names[4])




