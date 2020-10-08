# ------------------------------------------------------------------------------------------------------------------
# NOTE: This only works under the assumption that the accessed web page does not change its layout and class naming
# ------------------------------------------------------------------------------------------------------------------

# Need to be installed with pip
from bs4 import BeautifulSoup
import requests

# ------------------------------------------------------------------------------------------------------------------

# Go to Billboard top 100 page
url = "https://www.billboard.com/charts/hot-100"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")


#-===========================================================
# look fot only the 'li' tags with the class of 'chart-list__element'
tags = soup.findAll("li", class_="chart-list__element")


# create an empty string to hold the movie names
listString = ""


# loop through the li tags to get a list of a tags and get the text within them
for li in tags:
    print(li.find_all('span', class_="chart-element__rank__number")[0].text)         # Song Rank

    print(li.find_all('span', class_="chart-element__information__song")[0].text)    # Song Title

    print(li.find_all('span', class_="chart-element__information__artist")[0].text)  # Song artists



#     listString = listString + "{} \n".format(a.find_all('a')[0].text)
#
#
# # create a file to add and hold all of the movie names
# with open("Anime-Movie-list.txt", 'a') as fileObject:
#     fileObject.write(listString)