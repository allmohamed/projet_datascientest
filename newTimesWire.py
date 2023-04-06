# Demo code sample. Not indended for production use.

# See instructions for installing Requests module for Python
# https://requests.readthedocs.io/en/master/user/install/#install

import requests

def sectionList(key):
  requestUrl = f"https://api.nytimes.com/svc/news/v3/content/section-list.json?api-key={key}"
  requestHeaders = {
    "Accept": "application/json"
  }

  response = requests.get(requestUrl, headers=requestHeaders)
  
  data = response.json()
  results = data["results"]

  sections = [col["section"] for col in results]
  return sections





def getArticle(key, section):

  nyt = "nyt"
  requestUrl = f"https://api.nytimes.com/svc/news/v3/content/{nyt}/{section}.json?api-key={key}"
  requestHeaders = {
    "Accept": "application/json"
  }

  response = requests.get(requestUrl, headers=requestHeaders)

  data = response.json()
  results = data["results"]

  print(results)



if __name__ == "__main__":
 key = "nh8jOjOc8udr9E04wrwpJA6s3VBECjh4"
 sectionList = sectionList(key)
 
 getArticle(key, sectionList[3])


