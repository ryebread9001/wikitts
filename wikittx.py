import requests
from bs4 import BeautifulSoup
import pyttsx3

def speak(txt):
  engine = pyttsx3.init()
  engine.say(txt)
  engine.runAndWait()

#speak('hello')
 

 
url = 'https://en.wikipedia.org/w/api.php'
params = {
            'action': 'query',
            'format': 'json',
            'generator': 'random',
            'grnnamespace': 0,
            'grnlimit': 1,
            'prop': 'info'
            # 'page': subject,
            # 'format': 'json',
            # 'prop':'text',
            # 'redirects':''
        }

response = requests.get(url, params=params)
json_random = response.json()
subject_ID = json_random['query']['pages']
first_value = next(iter(subject_ID.keys()))

# now that we have random page id we need the page name
# action=query&pageids=<your_pageid_here>&format=json
params = {
          'action': 'query',
          'pageids': first_value,
          'format': 'json'
}
print(first_value)

response = requests.get(url, params=params)
data = response.json()
print(data['query']['pages'])
subject = data['query']['pages'][str(first_value)]['title']

params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop':'text',
            'redirects':''
        }
 
response = requests.get(url, params=params)
data = response.json()
raw_html = data['parse']['text']['*']
soup = BeautifulSoup(raw_html,'html.parser')
soup.find_all('p')
text = ''
 
for p in soup.find_all('p'):
    text += p.text
 
print(text[:58])
print(text)


speak(text)