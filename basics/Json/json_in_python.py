import json

books = {"bob": {
    "name": "first book",
    "author": "HA",
    "page": 320
}, "rob": {
    "name": "Second book",
    "author": "KNI",
    "page": 200
}, "kob": {
    "name": "Third book",
    "author": "RNT",
    "page": 350
}, "job": {
    "name": "Fourth book",
    "author": "JU",
    "page": 500
}}

if __name__ == "__main__":
    s = json.dumps(books)

    # Write file
    with open("books.txt", "w") as f:
        f.write(s)

    with open("books.txt", "r") as f:
        s = f.read()
        j = json.loads(s)
        print(s[0])
        print(j["bob"])


