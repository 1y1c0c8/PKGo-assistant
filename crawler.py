import requests, bs4 



urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
urlPkgHomePage = 'https://pokemongolive.com'

def getInfoTitle(url):
    requestGet = requests.get(url)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")
    
    titles = html.find_all("div", class_="blogList__post__content__title")

    return titles
        

def getActivityUrl(url):
    requestGet = requests.get(urlPkgNewsPage)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")

    blocks = html.find_all("a", class_='blogList__post')

    return blocks

# url = f'{urlPkgHomePage}{block["href"]}'


# for block in blocks[:3]:
#     url = f'{urlPkgHomePage}{block["href"]}'
#     print(url)
