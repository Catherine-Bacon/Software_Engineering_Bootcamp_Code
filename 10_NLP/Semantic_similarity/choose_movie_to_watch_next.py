# import NLP modules
import spacy
nlp = spacy.load('en_core_web_md')

# read the movies file in as a list, removing newline characters
with open("movies.txt", "r") as f:
    movie_data = f.readlines()
for i in range(len(movie_data)):
    movie_data[i] = movie_data[i].strip("\n")

# create movie variable to compare to
comparison_movie = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the" \
                   "Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the " \
                   "Hulk can live in peace. Unfortunately, Hulk land on the plane Sakaar where he is sold into " \
                   "slavery and trained as a gladiator."

similarities = []
for movie in movie_data:
    similarity = nlp(movie).similarity(nlp(comparison_movie))
    similarities.append(similarity)
    print(f"{similarity} - {movie}")
max_index = max(range(len(similarities)), key=similarities.__getitem__)
print(f"\nThe most similar movie ({max(similarities)}) is: {movie_data[max_index]}")
