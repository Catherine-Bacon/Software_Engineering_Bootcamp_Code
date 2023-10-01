# initialise list
movies = ["Alien", "Django Unchained", "Die Hard", "Frankenstein", "Aliens"]

# for each value in movie, print out movie: plus the movies name
for i in range(len(movies)):
    print(f"Movie: {movies[i]}")

# for each value in movie, print the movie (number in list): plus movies name
for count, movie in enumerate(movies, start=1):
    print(f"Movie {count}: {movie}")
