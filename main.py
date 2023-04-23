from some_functions import random_line_from_file
from bs4 import BeautifulSoup
import requests


def variety_movies() -> list:
    """Returns a web scraping movie list."""
    url = "https://variety.com/lists/best-movies-of-all-time/the-graduate-1967-2/"

    response = requests.request("GET", url=url).content
    soup = BeautifulSoup(response, "html.parser")

    data = soup.select("article div h2")
    film_titles = [title.get_text() for title in data]
    return film_titles


def main():
    file_name = "100_greatest_movies.txt"
    chosen_film = random_line_from_file(file=file_name)
    print(f"Today you should watch: {chosen_film}")


if __name__ == "__main__":
    main()
