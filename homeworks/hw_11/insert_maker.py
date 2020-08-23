import json

actors = list()
films = list()
actor_film = list()
directors = list()
directors_film = list()
genres = list()
genres_film = list()

if __name__ == '__main__':
    with open("films.json", "r") as read_file:
        data = json.load(read_file)
        for idx ,film in enumerate(data, 3):
            film_string = f"('{data[film]['title']}', '{data[film]['year']}', '{data[film]['country']}', '{data[film]['image']}')"
            if '"' in film_string:
                continue
            print(f"insert into films (title, year, country, image) values {film_string};")

            films.append(film_string)
            for a in data[film]['cast']:
                if a not in actors:
                    if '"' in a or "'" in a:
                        continue
                    actors.append(a)
                    print(f"insert into actors (name) values ('{a}');")

                actor_film.append((actors.index(a) + 1, idx))
                print(f"insert into actors_film (actor_id, film_id) values ('{actors.index(a) + 1}', '{idx}');")

            for d in data[film]['directors']:
                if d not in directors:
                    if '"' in d or "'" in d:
                        continue
                    directors.append(d)
                    print(f"insert into directors (name) values ('{d}');")

                directors_film.append((directors.index(d) + 1, idx))
                print(f"insert into directors_film (director_id, film_id) values ('{directors.index(d) + 1}', "
                      f"'{idx}');")

            for g in data[film]['genres']:
                if '"' in g or "'" in g:
                    continue
                if g not in genres:
                    genres.append(g)
                    genres_film.append((genres.index(g) + 1, idx))
                    print(f"insert into genres (title) values ('{g}');")
                print(f"insert into genres_film (genre_id, film_id) values ('{genres.index(g) + 1}', '{idx}');")
