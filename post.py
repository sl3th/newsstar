import requests
from datetime import date,timedelta

# Time
today = date.today()
yesterday = str(today - timedelta(days=1))
last_week = str(today - timedelta(days=7))

def data(q):
    APP_KEY = '1bd6e18d6d63405189cac00cffb40864'

    URL = "https://newsapi.org/v2/everything"
    parameters = {
        "q": q,
        "apiKey": APP_KEY,
        "from": last_week,
        "to": yesterday,
        "sortBy" : 'publishedAt',
        "language" : 'en',

    }

    response = requests.get(URL, params=parameters)
    data_news = response.json()["articles"]

    data_list = []

    for i in range(len(data_news)):

        title = data_news[i]["title"]
        description = data_news[i]["description"]
        author = data_news[i]["author"]
        url = data_news[i]["url"]
        image = data_news[i]["urlToImage"]
        source = data_news[i]["source"]["name"]
        time_t = data_news[i]["publishedAt"].split('T')[1].replace('Z','').split(':')
        time = f"{time_t[0]}:{time_t[1]}"
        date_t = data_news[i]["publishedAt"].split('T')[0]

        new_data = {
            "id" : i,
            "title" : title,
            "description" : description,
            "author" : author,
            "url" : url,
            "image" : image,
            "source" : source,
            "time" : time,
            "date" : date_t,
        }

        data_list.append(new_data)
    
    return data_list

