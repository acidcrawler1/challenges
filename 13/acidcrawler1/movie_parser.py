import csv

movie_data = csv.DictReader("../movie_metadata.csv")

for item in movie_data:
    print(item)