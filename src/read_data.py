import csv


def load_data():
    with open("data/data_centers.csv", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def search_by_state(state):
    data = load_data()
    results = []

    for row in data:
        if row["state"].lower() == state.lower():
            results.append(row)

    return results


results = search_by_state("Georgia")

for result in results:
    print(result["name"])

for result in results:
    print(result["name"])
