from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = "https://codeavecjonathan.com/scraping/recette/"

response = requests.get(url)
soup = bs(response.content, "html5lib")

ingredients_list = soup.find("div", class_="ingredients")
ingredients = ingredients_list.find_all("p")

for ingredient in ingredients:
    print("Ingredinet:", ingredient.text.strip())
    
    
    

