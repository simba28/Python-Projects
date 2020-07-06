import requests
from bs4 import BeautifulSoup
import pprint


def create_complete_hn(pages):
    hn = []
    for page in range(1,pages+1):
        res = requests.get(f"https://news.ycombinator.com/news{'' if page==1 else '?p='+str(page)}")
        soup = BeautifulSoup(res.text , 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        hn.extend(create_custom_hn(links, subtext))
    
    return sort_stories_by_votes(hn)

def create_custom_hn(links, subtext):
    news = []
    for index, _ in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                news.append({'title':title, 'link':href, 'votes':points})
    return news

def sort_stories_by_votes(hnlist):
    print('total news are : ',len(hnlist))
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

if __name__=='__main__':
    pages = int(input('upto page?\n'))
    pprint.pprint(create_complete_hn(pages))
