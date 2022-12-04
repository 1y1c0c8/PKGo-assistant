import requests, bs4



urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'


def getInfoTitle(url):
    requestGet = requests.get(url)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")
    
    titles = html.find_all("div", class_="blogList__post__content__title")

    return titles
        

getInfoTitle(urlPkgNewsPage)