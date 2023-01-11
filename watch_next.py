# This program suggests the most suitable movie to watch for someone who just watched Planet Hulk.

# Importing spacy module with an advanced language model.

import spacy

nlp = spacy.load('en_core_web_md')

# Creating planet_hulk string variable with a movie's description.
 
planet_hulk_description = "Will he save their world or destroy it?\
    When the Hulk becomes too dangerous for the Earth,\
    the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.\
    Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

description_to_compare = nlp(planet_hulk_description)

# Creating name of the file to open string variable.

file_name = "movies.txt"

# Creating a function that compares the similarity of the movie descriptions from the external file with the movie in question.
 
def watch_next(file, base_description):

    similarity_values_and_movies = []

    with open(file, "r") as movies:
        for description in movies:
            description = description.split(" :")
            similarity = nlp(description[1]).similarity(base_description)
            similarity_values_and_movies.append(f"With similarity of {similarity}, {description[0]} is the most similar movie.")

    sorted_similarity_values_and_movies = sorted(similarity_values_and_movies)
    reversed_similarity_values_and_movies = sorted_similarity_values_and_movies[::-1]
    movie_to_watch_next = reversed_similarity_values_and_movies[0]

    print(movie_to_watch_next)

# Calling the created function.

watch_next(file_name, description_to_compare)