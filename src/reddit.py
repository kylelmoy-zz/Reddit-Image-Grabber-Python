'''
Created on Mar 13, 2014

@author: Kyle Moy
'''
import requests, re
CLIENT_ID = "c7dfda0b2defaf5"
AUTH = {"Authorization":"Client-ID " + CLIENT_ID};
def parseItem(item):
    result = []
    url = item.url
    if re.match('.*imgur.com/a/.*', url):
        '''
        Imgur Album
        '''
        itemid = url.split('imgur.com/a/')[1]
        api = 'https://api.imgur.com/3/album/'
        source = requests.get(api + itemid, headers=AUTH)
        json = source.json()
        for child in json['data']['images']:
            item = redditItem(item.title,item.author,child['link'],item.permalink,item.sub)
            result += parseItem(item)
    elif re.match('.*\.(?:png|jpg|gif)', url):
        '''
        Image
        '''
        result += [item]
    elif re.match('.*imgur.com/.*', url):
        '''
        Imgur Link
        '''
        itemid = url.split('imgur.com/')[1]
        api = 'https://api.imgur.com/3/image/'
        source = requests.get(api + itemid, headers=AUTH)
        json = source.json()
        link = json['data']['link']
        item = redditItem(item.title,item.author,link,item.permalink,item.sub)
        result += [item]
    return result
    
def parse(sub, limit):
    '''
    Parse Subreddit
    '''
    items = []
    source = requests.get("http://www.reddit.com/r/" + sub + "/.json?limit=" + limit)
    json = source.json()
    for child in json['data']['children']:
        child = child['data']
        item = redditItem(child['title'], child['author'], child['url'], child['permalink'], child['subreddit'])
        items += parseItem(item)
    return items
    
class redditItem(object):
    '''
    classdocs
    '''

    def __init__(self, title, author, url, permalink, sub):
        '''
        Constructor
        '''
        self.title = title
        self.author = author
        self.url = url
        self.permalink = permalink
        self.sub = sub
        
    def display(self):
        print self.title, self.url
    