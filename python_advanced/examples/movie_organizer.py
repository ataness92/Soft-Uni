def movie_organizer(*movies):

    movies_dict = {}

    for name, genre in movies:
        if genre not in movies_dict:
            movies_dict[genre] = [name]
        else:
            movies_dict[genre].append(name)

    for genre, movies in movies_dict.items():
        movies_dict[genre] = sorted(movies_dict[genre])
    result = sorted(movies_dict.items(), key = lambda x: -len(x[1]))
    message = ""
    for genre, movies in result:
        message += f'{genre} - {len(movies)}\n'
        for movie in movies:
            message += f"* {movie}\n"

    return message

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Musicals"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))