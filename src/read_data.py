import csv

def load_data():
    with open("data/data_centers.csv", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def search_by_state(state):
    data = load_data()

    for row in data:
        if row["state"].lower() == state.lower():
            print(row["name"])
            print(row["location"])
            print(row["status"])
            print("---")


search_by_state("Georgia")
