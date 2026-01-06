import csv

if __name__ == "__main__":
    items = []

    with open("nyc_weather.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append((row["date"], int(row["temperature(F)"])))

    idx = 0
    total = 0
    while idx<7:
        total += items[idx][1]
        idx += 1

    print(items)
    print("Total 7 days temp:" , total)
    print("Avg of 7 days temp",round( total/7, 2))

    idx= 0
    maximum =0

    if len(items)>=10:
        while idx<10 :
            if items[idx][1]> maximum:
                maximum =items[idx][1]
            idx += 1

    print("Total 10 days max:", maximum)
