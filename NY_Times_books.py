#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests
import json

kapi = 'FkUJldApfYELWWrV62CKrULS6kUSCjKL'

url = requests.get(f'https://api.nytimes.com/svc/books/v3/lists/full-overview.json?api-key={kapi}')
link = url.json()
source = link["results"]["lists"] #naviguation a la suite dans les clé "results" et "list"


# In[17]:


#stockage des livres par categorie
#source est une liste ou chaque itération corespond à une catégorie. Dans chaque categorie il y un dictionnaire de plusieurs clé/valeur
#dont une clé 'books' qui est une liste enfermant un autre dictionnaire contenant les informations de chaque livre
source = [key.get('books') for key in source] 


# In[18]:


#stockage des livres dans une liste
#books est une liste ou chaque itération correspond à un livre
books = []
for i in source:
    for x in i:
        books.append(x.items())


# In[15]:


print(books)


# In[ ]:




