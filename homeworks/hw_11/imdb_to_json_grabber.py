import imdb
import json

ia = imdb.IMDb()

if __name__ == '__main__':
    movies = {}
    top = ia.get_top250_movies()
    for i in top:
        id = i.getID()
        movie = dict(i)

        title = movie.get('title')
        year = movie.get('year')
        movie = ia.get_movie(id)
        cast = list(x['name'] for x in movie.get('cast'))
        genres = list(movie.get('genres'))
        country = movie.get('country')
        directors = list(x['name'] for x in movie.get('directors'))
        img = movie.get('full-size cover url')
        movies[id] = {'title': title, 'year': year, 'image': img, 'country': ', '.join(country),
                      'directors': directors, 'cast': cast, 'genres': genres}

    print(movies)
    with open("films.json", "w") as write_file:
        json.dump(movies, write_file)
