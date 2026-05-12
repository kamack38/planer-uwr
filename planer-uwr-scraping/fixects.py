import json
import sys


def modify_ects_from_file(file_path, updates):
    with open(file_path, "r") as f:
        data = json.load(f)

    # updates is a list of tuples: [(name, new_ects_value), ...]
    for name, new_ects_value, new_hours, exam in updates:
        # print("Searching: ", name)
        for obj in data:
            # if obj["name"].startswith("[IM]"):
            #     print("'", name, "', ", "'", obj["name"], "'")
            if "name" in obj and obj["name"] == "[IM] " + name:
                print("Found: ", name)
                obj["ects"] = str(new_ects_value)
                obj["hours"] = new_hours
                obj["exam"] = "Yes" if exam else "No"

    # print(data)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


updates = [
    # Przedmioty obowiązkowe matematyczne
    ("Analiza matematyczna I", 11, ["60 (wyk.)", "60 (ćw.)"], True),
    ("Analiza matematyczna II", 10, ["60 (wyk.)", "60 (ćw.)"], True),
    ("Algebra I", 8, ["45 (wyk.)", "45 (ćw.)"], True),
    ("Algebra II", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Równania różniczkowe 1R", 7, ["45 (wyk.)", "30 (ćw.)"], True),
    ("Rachunek prawdopodobieństwa dla informatyków", 7, ["45 (wyk.)", "30 (ćw.)"], True),
    # Przedmioty matematyczne do wyboru (Tabela 5)
    ("Algebra 2R", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Analiza funkcjonalna 1", 7, ["45 (wyk.)", "30 (ćw.)"], True),
    ("Analiza matematyczna III", 10, ["60 (wyk.)", "60 (ćw.)"], True),
    ("Funkcje analityczne R", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Miara i całka", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Rozmaitości różniczkowalne", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Równania różniczkowe 2R", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Rachunek prawdopodobieństwa 2R", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    ("Statystyka", 7, ["30 (wyk.)", "15 (ćw.)"], True),
    ("Topologia", 6, ["30 (wyk.)", "30 (ćw.)"], True),
    # Przedmioty dodatkowe
    ("Rachunek prawdopodobieństwa 1R", 7, ["45 (wyk.)", "30 (ćw.)"], True),
    ("Algebra liniowa 2", 8, ["45 (wyk.)", "30 (ćw.)"], True),
    ("Algebra liniowa 1R", 9, ["60 (wyk.)", "30 (ćw.)"], True),
    ("Równania różniczkowe 1", 7, ["45 (wyk.)", "30 (ćw.)"], True),
]

if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

print(f"The file path provided is: {file_path}")

modify_ects_from_file(file_path, updates)
