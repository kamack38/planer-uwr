import json
import sys


def modify_ects_from_file(file_path, updates):
    with open(file_path, "r") as f:
        data = json.load(f)

    # updates is a list of tuples: [(name, new_ects_value), ...]
    for name, new_ects_value in updates:
        # print("Searching: ", name)
        for obj in data:
            # if obj["name"].startswith("[IM]"):
            #     print("'", name, "', ", "'", obj["name"], "'")
            if "name" in obj and obj["name"] == "[IM] " + name:
                print("Found: ", name)
                obj["ects"] = str(new_ects_value)

    # print(data)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


updates = [
    # Przedmioty obowiązkowe matematyczne
    ("Analiza matematyczna I", 11),
    ("Analiza matematyczna II", 10),
    ("Algebra I", 8),
    ("Algebra II", 6),
    ("Równania różniczkowe 1R", 7),
    ("Rachunek prawdopodobieństwa dla informatyków", 7),
    # Przedmioty matematyczne do wyboru (Tabela 5)
    ("Algebra 2 R", 6),
    ("Analiza funkcjonalna 1", 7),
    ("Analiza matematyczna III", 10),
    ("Funkcje analityczne R", 6),
    ("Miara i całka", 6),
    ("Rozmaitości różniczkowalne", 6),
    ("Równania różniczkowe 2R", 6),
    ("Rachunek prawdopodobieństwa 2R", 6),
    ("Statystyka", 7),
    ("Topologia", 6),
]

if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

print(f"The file path provided is: {file_path}")

modify_ects_from_file(file_path, updates)
