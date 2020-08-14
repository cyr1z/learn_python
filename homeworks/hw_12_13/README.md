## Database queries from the last lesson

link to the [database dump](https://github.com/cyr1z/learn_python/blob/master/homeworks/hw_11/films.sql)

#### Directors Favorites
selects the most hired actors of the director
```sql
select a.name as actor, d.name as director, count(*) as count
    from actors a
    inner join actors_film af on a.id = af.actor_id
    inner join directors_film df on af.film_id = df.film_id
    inner join directors d on d.id = df.director_id
    GROUP by a.name, d.name
    HAVING count(*) > 1
    order by count(*) DESC;
```

#### Most productive actors 
```sql
select a.name actor,  count(*) as roles from actors a
    inner join actors_film af on a.id = af.actor_id
    GROUP by a.name
    HAVING count(*) > 3
    order by count(*) DESC; 
```

#### Most productive directors
```sql
select d.name as director,  count(*) as films from directors d
    inner join directors_film df on d.id = df.director_id
    GROUP by d.name
    HAVING count(*) > 1
    order by count(*) DESC;
```

#### Biggest cast
```sql
SELECT title, count(*) FROM films 
	inner join actors_film af on films.id = af.film_id
	GROUP BY title
	ORDER by count(*) desc;
```

#### Best employer
```sql
select d.name as director, sum(r.count_e) as employe from directors d
    inner join directors_film df on d.id = df.director_id
    inner join (SELECT id as f_id, count(*) as count_e
                    FROM films
                    inner join actors_film af on films.id = af.film_id
                    GROUP BY id ) as r
    on df.film_id = r.f_id
    GROUP by name
    order by employe desc;
```

#### Most popular genres
```sql
select title, count(*) as count
    from genres g
    INNER JOIN genres_film gf on g.id = gf.genre_id
    GROUP BY  title
    ORDER BY count desc;
```
