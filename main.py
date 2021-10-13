import requests 
from bs4 import BeautifulSoup

query = input("Enter country name: ")
url = "https://www.britannica.com/facts/"+query

page = requests.get(url)

#basic structure
raw_results = BeautifulSoup(page.content, "html.parser")
raw_info = raw_results.find("div", class_="fact-box-details md-country-facts md-striped")

#finding info
capital = raw_info.find("dt",text="Capital").findNext("dd").string
try:
    languages = raw_info.find("dt",text="Official languages").findNext("dd").string
except:
    languages = raw_info.find("dt",text="Official language").findNext("dd").string
population_raw = raw_info.find("dt",text="Urban-rural population").find_next_siblings("dd")
urban_population = population_raw[0].string
rural_population = population_raw[1].string
area = raw_info.find("dt",text="Total area (sq km)").findNext("dd").string

#displaying results
print("Country:",query)
print("Capital:",capital)
print("Official Language:",languages)
print("Urban Population:",urban_population)
print("Rural Population",rural_population)
print("Total Area:",area,"sq km")

