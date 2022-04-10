import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:8]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


H = ['Action', 'Adventure', 'Fantasy', 'ScienceFiction', 'Crime', 'Drama', 'Thriller', 'Animation', 'Family', 'Western', 'Comedy', 'Romance', 'Horror', 
'Mystery', 'History', 'War', 'Music', 'Documentary', 'Foreign', 'TVMovie']

def suggest(gen):
    gen = gen.lower()
    url = "https://www.imdb.com/search/title/?genres={}&sort=user_rating,desc".format(gen)
    return url



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



st.markdown("""<p style="color: #3a02ab;font-size: 70px;font-family: sans-serif;"><b>FILM</b><span style="color: #f75e05;font-size: 70px;font-family: sans-serif;"><b>ISH</b></span></p>""", unsafe_allow_html=True)


movies = pickle.load(open('venv/movie_list.pkl', 'rb'))
similarity = pickle.load(open('venv/similarity.pkl', 'rb'))
movie_list = movies['title'].values

st.markdown(""" <span style="font-size: 30px; font-family: Arial, Helvetica, sans-serif; color: #040330;"> Enter or select a Movie</span>""", unsafe_allow_html=True)   
    
selected_movie = st.selectbox("", movie_list)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 , col6, col7 = st.columns(7)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])

components.html("<html> <br /> <br /><br /> </html>")
components.html(
    """
    <style type="text/css">
    #block {
                height: 100px;
                width: 100%;
                background-color: #f002a5;
                border-radius: 20px;
                position: relative;
            }
    </style>
    <body>
    <br /> 
    <div id="block">
            <span style="font-size: 42px; color: white; font-family: Arial, Helvetica, sans-serif;">    You will be redirected to IMDB best movies page </span>
    </div>
    </body>

    """
)

#components.html("<html> <br /> <br /><br /> </html>")
st.markdown(""" <span style="font-size: 30px; font-family: Arial, Helvetica, sans-serif; color: #040330;"> Enter or select a Genre</span>""", unsafe_allow_html=True)   
selected_genre = st.selectbox("", H)
if st.button("show movies"):
    link = "[List of movies]("+ suggest(selected_genre)+")"
    st.markdown(link, unsafe_allow_html=True)







