import sqlalchemy as sq


if __name__ == '__main__':
    DB = 'postgresql://postgres:9117399126@localhost:5432/singers_db'
    engine = sq.create_engine(DB)
    connection = engine.connect()

    #задача 2 - 1
    result = connection.execute("""SELECT album_title, release_year FROM albums
                                    WHERE release_year = 2018;""").fetchall()
    print(result)

    # задача 2 - 2
    result = connection.execute("""SELECT track_title, duration FROM tracks
                                    WHERE duration = (SELECT MAX(duration) FROM tracks);""").fetchall()
    print(result)

    # задача 2 - 3
    result = connection.execute("""SELECT track_title FROM tracks
                                    WHERE duration > 3.5;""").fetchall()
    print(result)

    # задача 2 - 4
    result = connection.execute("""SELECT col_title FROM collection
                                    WHERE release_year BETWEEN 2018 AND 2020;""").fetchall()
    print(result)

    # задача 2 - 5
    result = connection.execute(f"""SELECT singer_name FROM singers
                                    WHERE singer_name NOT LIKE '%% %%';""").fetchall()
    print(result)

    # задача 2 - 6
    result = connection.execute(f"""SELECT track_title FROM tracks
                                    WHERE track_title LIKE '%%my%%';""").fetchall()
    print(result)