import requests
from bs4 import BeautifulSoup
import time

# Request the webpage
url = requests.get('https://www.baseball-reference.com/awards/mvp.shtml')
soup = BeautifulSoup(url.text, 'html.parser')

# Find the MVP table
table_div = soup.find('div', attrs={'id': 'div_mvp'})

# Check if the div was found
if table_div:
    table = table_div.find('table')
    # Check if the table was found
    if table:
        tbody = table.find('tbody')
        # Check if tbody was found
        if tbody:
            rows = tbody.find_all('tr')
            # Now you can process the rows
            print(f"Number of rows found: {len(rows)}")
            # Further code to process each row goes here
        else:
            print("Table body (tbody) not found.")
    else:
        print("Table not found within the div.")
else:
    print("Div with id 'div_mvp' not found.")

links = []

for row in rows:
    columns = row.find_all('td')
    if len(columns) > 0:
      links.append(columns[16])

# Ensure each entry in 'links' is already parsed by BeautifulSoup
soup_elements = [BeautifulSoup(str(elem), 'html.parser') for elem in links]

# Extract the URLs from the 'href' attributes
urls = [elem.find('a')['href'] for elem in soup_elements if elem.find('a')]

for i in range(len(urls)):
  urls[i] = "www.baseball-reference.com" + urls[i]

# print(urls)

del links
del rows
del soup_elements

# stored in war: rank, war, year, war_rank
war_list = []

for i in range(len(urls)):
    if (i % 2 == 0):
        # print(i)
        # time.sleep(1)
        year = 2023 - int(i / 2)
        print(year)
        url = requests.get('https://' + urls[i])
        soup = BeautifulSoup(url.text, 'html.parser')
        tableAL = soup.find('div', attrs = {'id' : 'div_AL_MVP_voting'}).find('table').find('tbody')
        tableNL = soup.find('div', attrs = {'id' : 'div_NL_MVP_voting'}).find('table').find('tbody')

        rowsAL = tableAL.find_all('tr')
        rowsNL = tableNL.find_all('tr')

        war_AL_year = []
        war_NL_year = []

        for i in range(15):
          rowAL = rowsAL[i]
          columns = rowAL.find_all('td')
          war = float(columns[5].text)
          rank = i + 1
          player = [rank, war, year]
          war_AL_year.append(player)

        # Sort by WAR in descending order (highest WAR first)
        war_AL_year_sorted = sorted(war_AL_year, key=lambda x: x[1], reverse=True)

        # Add WAR ranking to each player
        for i, player in enumerate(war_AL_year_sorted, start=1):
            player.append(i)  # Adding the WAR ranking to the player's data

        for player in war_AL_year_sorted:
          war_list.append(player)


        for i in range(15):
          rowNL = rowsNL[i]
          columns = rowNL.find_all('td')
          war = float(columns[5].text)
          rank = i + 1
          player = [rank, war, year]
          war_NL_year.append(player)


        # Sort by WAR in descending order (highest WAR first)
        war_NL_year_sorted = sorted(war_NL_year, key=lambda x: x[1], reverse=True)

        # Add WAR ranking to each player
        for i, player in enumerate(war_NL_year_sorted, start=1):
            player.append(i)  # Adding the WAR ranking to the player's data
        for player in war_NL_year_sorted:
          war_list.append(player)