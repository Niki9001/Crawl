import requests
from bs4 import BeautifulSoup
import docx
class ITjobs:
    def __init__(self):
       self.URL = 'https://www.itjobs.ca/en/search-jobs/?location=Halifax%2C+NS&location-id=25258&location-type=1&search=1&page='
       #for i in range(10):
        #   self.URL = f"https://www.itjobs.ca/en/search-jobs/?location=Halifax%2C+NS&location-id=25258&location-type=1&search=1&page={i}"
       self.starnum = []
       for start_num in range(0,1):
           self.starnum.append(start_num)
       self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def get_detail(self):
        for page in self.starnum:
            page = str(page) # name of variable in url
            html = requests.get(self.URL, params={'page':page},headers = self.header)
            soup = BeautifulSoup(html.text,"html.parser")
            name = soup.select('#search-results > div > div > div.content-wrapper > div > div > div.result-info-wrapper > div.details-wrapper')
            file = docx.Document()


            for name in name:
                print(name.get_text())
                file.add_paragraph(f"{name}")
            file.save("test_new.docx")

if __name__== "__main__":
    cls = ITjobs()
    cls.get_detail()

