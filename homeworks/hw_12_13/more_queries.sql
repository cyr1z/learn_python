-- it's bullshit. It doesn't work yet
select d.name as director, g.title as favorit_genre, m.count as count
    FROM directors d
    inner JOIN (
        select r.g_id as g_id, r.d_id as d_id
            from (
                select gf.genre_id as g_id, count(*) as count, df.director_id as d_id
                    from genres_film gf
                    INNER JOIN directors_film df on gf.film_id = df.film_id
                    GROUP BY  gf.genre_id, df.director_id) as r
        GROUP by r.g_id, r.d_id) as m
    on d.id = m.d_id
    INNER JOIN genres g on m.g_id = g.id
    ORDER by d.name;