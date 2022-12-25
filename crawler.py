from pkmgo_assistant import crawler

if __name__ == "__main__":
    urlPkgNewsPage = 'https://pokemongolive.com/news?hl=zh_Hant'
    imgs = crawler.getActivityImg(urlPkgNewsPage)
    print(imgs[4]["src"])