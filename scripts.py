import sys
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies_dict = pickle.load(open('./models/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('./models/similarity.pkl', 'rb'))

def recommend(movie):
    try:
        movie_index = movies[movies['original_title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [movies.iloc[i[0]]['original_title'] for i in movies_list]
        return recommended_movies
    except IndexError:
        return ["Movie not found."]


if __name__ == "__main__":
    selected_movie_name = sys.argv[1] if len(sys.argv) > 1 else ""
    # selected_movie_name = "Big Hero 6"
    recommended_movies = recommend(selected_movie_name)
    if "Movie not found." in recommended_movies:
        print("Movie not found. Please check the title and try again.")
    else:
        print("Recommended movies:")
        for movie in recommended_movies:
            print(movie)