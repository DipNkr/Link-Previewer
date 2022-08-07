from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup


result = {'title': "", 'des': "", 'imgUrl': ""}


def scrap_web(url):
    title = ''
    des = ''
    imgUrl = ''

    try:
        # Making a GET request
        r = requests.get(url)

        if(r.status_code == 200):
            # Parsing the HTML
            soup = BeautifulSoup(r.content, 'html.parser')

            # Fetch Title
            if(soup.title):
                title = soup.title.text
            else:
                title = 'No Title Found'

            # Fetch Description
            if soup.findAll("meta", attrs={"name": "description"}):
                des = soup.find(
                    "meta", attrs={"name": "description"}).get("content")
            elif soup.find('meta', attrs={"name": "Description"}):
                des = soup.find(
                    'meta', attrs={"name": "Description"}).get("content")
            elif soup.find('meta', attrs={"name": "DESCRIPTION"}):
                des = soup.find(
                    'meta', attrs={"name": "DESCRIPTION"}).get("content")
            else:
                des = "No Description Found"

            # Fetcg image url
            if soup.findAll("meta", attrs={"property": "og:image"}):
                imgUrl = soup.find(
                    "meta", attrs={"property": "og:image"}).get("content")
            if "https://" not in imgUrl:
                imgUrl = "../static/oops.jpg"

    except HTTPError as http_error:
        return("ERROR")
    except AttributeError:
        return("There is no such attribute")

    result['title'] = title
    result['des'] = des
    result['imgUrl'] = imgUrl

    return result


# print(scrap_web("https://w3schools.com"))
