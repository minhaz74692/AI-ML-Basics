import csv
import re


def solution1():
    items = []

    with open("nyc_weather.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append((row["date"], int(row["temperature(F)"])))

    idx = 0
    total = 0
    while idx < 7:
        total += items[idx][1]
        idx += 1

    print(items)
    print("Total 7 days temp:", total)
    print("Avg of 7 days temp", round(total / 7, 2))

    idx = 0
    maximum = 0

    if len(items) >= 10:
        while idx < 10:
            if items[idx][1] > maximum:
                maximum = items[idx][1]
            idx += 1

    print("Total 10 days max:", maximum)


def solution2():
    item_map = {}
    with open("nyc_weather.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # items.append((row["date"], int(row["temperature(F)"])))
            item_map[row["date"]] = int(row["temperature(F)"])

    print(item_map)
    print("Temperature on Jan 9: ", item_map["Jan 9"])
    print("Temperature on Jan 9: ", item_map["Jan 4"])


def solution3():
    poem =None
    with open("poem.txt", "r") as file:
        poem = file.read()

    word_map = {}
    words = re.findall(r"\b[a-zA-Z]+\b", poem.lower())
    print(words)

    for word in words:
        # print(word)
        if word in word_map.keys():
            word_map[word] = int(word_map[word]) + 1
        else:
            word_map[word] = 1

    for key, value in word_map.items():
        print("'"+  key +  "'" +  ": ", value)


if __name__ == "__main__":
   # solution1()
   # solution2()
   solution3()
