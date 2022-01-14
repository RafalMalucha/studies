import json

movie = {
    "Title": "John Wick",
    "Cast": ["Keanu Reeves", "some other guys I don't remember"],
    "Year": 2014,
    "Director": "Chad Stahelski",
    "ifBoring": False,
    "Genere": ["Thriller", "Action"],
}

file = open("movie.json", "w")
json.dump(movie,file,indent = 4)
file.close()