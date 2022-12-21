import requests, bs4 

# urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
# urlPkgHomePage = 'https://pokemongolive.com'
urlPkgTrainerClubHome = "https://pogotrainer.club"
urlPkgTrainerClubWorldwide = "https://pogotrainer.club/?sort=worldwide"


class appraise:
    def aps_compute(tokens):

        total = int(tokens[0])+int(tokens[1])+int(tokens[2])
        
        if(total == 45):
            return '100'
        elif(total<45 and total>=43):
            return 10+total*2
        elif(total<43 and total>=39):
            return 10+total*2-1
        elif(total<39 and total>=34):
            return 10+total*2-2
        elif(total<34 and total>=30):
            return 10+total*2-3
        elif(total<30 and total>=25):
            return 10+total*2-4
        elif(total<25 and total>=21):
            return 10+total*2-5
        elif(total<21 and total>=16):
            return 10+total*2-6
        elif(total<16 and total>=12):
            return 10+total*2-7
        elif(total<12 and total>=7):
            return 10+total*2-8
        elif(total<7 and total>=3):
            return 10+total*2-9
        elif(total<3 and total>0):
            return 10+total*2-10

    def star_check(iv):
        if(iv < 48.9):
            return '☆☆☆'
        elif(iv < 64.4):
            return '★☆☆'
        elif(iv < 80):
            return '★★☆'
        elif(iv < 97.8):
            return '★★★'
        else:
            return '  ♛  '

class crawler():
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
        userNames = crawler.getTrainerNames(urlPkgTrainerClubWorldwide)
        userIDs = crawler.getTrainerID(urlPkgTrainerClubWorldwide)

        userInfos = []

        for index in range(3):
            userInfos.append(str(userNames[index].text)+'\n'+str(userIDs[index].text))
            
        INFO = f'{userInfos[0]}\n==============\n{userInfos[1]}\n==============\n{userInfos[2]}\n=============='
        return INFO

    # url = f'{urlPkgHomePage}{block["href"]}'


    # for block in blocks[:3]:
    #     url = f'{urlPkgHomePage}{block["href"]}'
    #     print(url)
