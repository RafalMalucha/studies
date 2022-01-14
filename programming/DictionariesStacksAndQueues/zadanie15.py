import json

studentData = {
    "name": "Michał",
    "surname": "Głuś",
    "age": 20,
    "isGoodStudent": False,
    "friends": None,
    "grades": {
        "tpi": 2.0,
        "maths": 2.0,
        "ask": 2.0,
        "pp1": 2.0,
        "oiz": 2.0,
        "edi": 2.0,
        "english": 4.5,
        "italian": 3.0,
        "pe": 3.5,
        },
}

file = open("student.json", "w")
json.dump(studentData, file, indent = 4)
file.close()