from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movies_to_watch = [movie.text.split(" ", 1)[1] for movie in movie_titles]
with open("100 Days of Code Python/Beautiful Soup/100 Movies to Watch/Top 100 Movies.txt", "w") as file:
    for i in range(0,len(movies_to_watch)):
        file.write(f"{i+1}) {movies_to_watch[i]}\n")
