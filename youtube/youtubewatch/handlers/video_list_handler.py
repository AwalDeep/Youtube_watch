from bs4 import BeautifulSoup
import urllib.request

class VideoListHandler:
    def __init__(self):
        pass

    def search_vid(self, search):
        url = ''.join(['https://www.youtube.com/results?search_query=', search])
        response = urllib.request.urlopen(url)

        soup = BeautifulSoup(response)    
        divs = soup.find_all("div", { "class" : "yt-lockup-content"})

        return_dict = {'data': []}
        
        for i in divs:
            href= i.find('a', href=True)
            href['href']= href['href'].replace("watch?v=", "embed/")
            return_dict['data'].append((href.text, 'https://www.youtube.com' + href['href']))
        
        return return_dict