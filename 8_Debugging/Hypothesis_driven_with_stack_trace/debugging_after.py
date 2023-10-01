def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])  # change from k to key


simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm",
                         "homer": "d'oh", "maggie": " (Pacifier Suck)"}  # change ' to "

print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])  # place keys within square brackets and change ' to "
# also changed spacing after function and line length to satisfy PEP 8
