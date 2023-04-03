import requests
from pprint import pprint

#clé API pour accéder à l'API
api_key="upAphVEmj2sSjKOUg3EKknGQphCuVyw4"
#Mot clé requête
print("What is the type of article your looking for? enter ONE keyword")
#query = str(input())
query="election"
print("\n")
#url de l'API 
url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={api_key}"

response = requests.get(url)
#variable data de type dictionnaire contenant les informations obtenus grâce à la librairie requests
data = response.json()


# data variable de type dictionnaire avec trois clés : ['status', 'copyright', 'response']
response=data["response"]
#data["reponse"] contient les clés ['docs', 'meta']
docs=response["docs"]
#data["response"]["docs"] est une liste dont chaque élement est un article.
# Chaque élément de la liste est de type dictionnaire et contient les clés suivantes :
# ['abstract', 'web_url', 'snippet', 'lead_paragraph', 'source', 'multimedia', 'headline', 'keywords', 'pub_date', 'document_type', 'news_desk', 'section_name', 'subsection_name', 'byline', 'type_of_material', '_id', 'word_count', 'uri']

remove=['multimedia','snippet','uri']


for article in docs :
    for y in remove :
        article.pop(y)
    
    #recupération du nom et prénom des auteurs de l'article dans une clé author
    article["byline"].pop("organization")
    article["byline"].pop("original")
    article["author"]=[]

    for author in (article["byline"]["person"]):
        name=""
        for nom in [author["firstname"],author["middlename"],author["lastname"]]:
            
            if type(nom)==str:
                name= name+" "+nom
        article["author"].append(name)
    
    #suppression de la clé byline de article contenant les informations sur les auteurs après extraction vers la clé author
    article.pop("byline")

    #extraction du résumé  print_headline
    
    article["headline"].pop('content_kicker')
    article["headline"].pop('kicker')
    article["headline"].pop('main')
    article["headline"].pop('name')
    article["headline"].pop('seo')
    article["headline"].pop('sub')
    article["headline"]=article["headline"]["print_headline"]
    

    #extraction des keywords
    mot=[]
    for keywords in article["keywords"] :
                mot.append(keywords["value"])
    
    article["keywords"]=mot
    

                

pprint(docs)


