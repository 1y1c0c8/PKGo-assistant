import requests, bs4 

# urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
# urlPkgHomePage = 'https://pokemongolive.com'
urlPkgTrainerClubHome = "https://pogotrainer.club"
urlPkgTrainerClubWorldwide = "https://pogotrainer.club/?sort=worldwide"

def getInfoTitle(url):
    requestGet = requests.get(url)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")
    
    titles = html.find_all("div", class_="blogList__post__content__title")

    return titles
        

def getActivityUrl(url):
    requestGet = requests.get(url)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")

    blocks = html.find_all("a", class_='blogList__post')

    return blocks

def getTrainerNames(url):
    requestGet = requests.get(urlPkgTrainerClubWorldwide)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")

    userNames = html.find_all("h4", class_='media-heading')

    return userNames

def getTrainerID(url):
    requestGet = requests.get(urlPkgTrainerClubWorldwide)
    html = bs4.BeautifulSoup(requestGet.text, "html.parser")

    userIDs = html.find_all("a", class_="TCLink")

    for userID in userIDs:
        userID = userID.text

    return userIDs[:3]

def mergeInfo():
    userNames = getTrainerNames(urlPkgTrainerClubWorldwide)
    userIDs = getTrainerID(urlPkgTrainerClubWorldwide)

    userInfos = []

    for index in range(3):
        userInfos.append(str(userNames[index].text)+'\n'+str(userIDs[index].text))
        
    INFO = f'{userInfos[0]}\n==============\n{userInfos[1]}\n==============\n{userInfos[2]}\n=============='
    return INFO

# url = f'{urlPkgHomePage}{block["href"]}'


# for block in blocks[:3]:
#     url = f'{urlPkgHomePage}{block["href"]}'
#     print(url)
