import requests
import csv


def fetch_and_print_posts():
    r = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(r)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        statue = response.json()
        for i in statue:
            print(i["title"])


def fetch_and_save_posts():
    r = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(r)

    if response.status_code == 200:
        statue = response.json()
        with open('posts.csv', 'w', newline="") as Nfile:
            dictionaire = csv.writer(Nfile)
            all = ["id", "title", "body"]
            dictionaire.writerow(all)
            for y in statue:
                dictionaire.writerow([y["id"], y["title"], y["body"]])
