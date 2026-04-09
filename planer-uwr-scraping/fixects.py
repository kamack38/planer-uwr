import json
import sys


def modify_ects_from_file(file_path, updates):
    with open(file_path, "r") as f:
        data = json.load(f)

    # updates is a list of tuples: [(name, new_ects_value), ...]
    for name, new_ects_value, new_hours in updates:
        # print("Searching: ", name)
        for obj in data:
            # if obj["name"].startswith("[IM]"):
            #     print("'", name, "', ", "'", obj["name"], "'")
            if "name" in obj and obj["name"] == "[IM] " + name:
                print("Found: ", name)
                obj["ects"] = str(new_ects_value)
                obj["hours"] = new_hours

    # print(data)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


updates = [
    # Przedmioty obowiązkowe matematyczne
    ("Analiza matematyczna I", 11, ["60 (wyk.)", "60 (ćw.)"]),
    ("Analiza matematyczna II", 10, ["60 (wyk.)", "60 (ćw.)"]),
    ("Algebra I", 8, ["45 (wyk.)", "45 (ćw.)"]),
    ("Algebra II", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Równania różniczkowe 1R", 7, ["45 (wyk.)", "30 (ćw.)"]),
    ("Rachunek prawdopodobieństwa dla informatyków", 7, ["45 (wyk.)", "30 (ćw.)"]),
    # Przedmioty matematyczne do wyboru (Tabela 5)
    ("Algebra 2R", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Analiza funkcjonalna 1", 7, ("45 [wyk.]", "30 (ćw.)")),
    ("Analiza matematyczna III", 10, ["60 (wyk.)", "60 (ćw.)"]),
    ("Funkcje analityczne R", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Miara i całka", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Rozmaitości różniczkowalne", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Równania różniczkowe 2R", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Rachunek prawdopodobieństwa 2R", 6, ["30 (wyk.)", "30 (ćw.)"]),
    ("Statystyka", 7, ["30 (wyk.)", "15 (ćw.)"]),
    ("Topologia", 6, ["30 (wyk.)", "30 (ćw.)"]),
    # Przedmioty dodatkowe
    ("Rachunek prawdopodobieństwa 1R", 7, ["45 (wyk.)", "30 (ćw.)"]),
    ("Algebra liniowa 2", 8, ["45 (wyk.)", "30 (ćw.)"]),
    ("Algebra liniowa 1R", 9, ["60 (wyk.)", "30 (ćw.)"]),
    ("Równania różniczkowe 1", 7, ["45 (wyk.)", "30 (ćw.)"]),
]

if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

print(f"The file path provided is: {file_path}")

modify_ects_from_file(file_path, updates)
