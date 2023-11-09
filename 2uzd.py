""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

"""

"""
iegūst ziņas, izmantojot RSS plūsmu no google.lv.

kas ir RSS?

RSS ir speciāls formāts datu izplatīšanai
"""
import feedparser

# URL uz RSS plūsmu

rss_url='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

#iegūst RSS plūsmas datus

kkk=feedparser.parse(rss_url)

#parāda un noformē
for entry in kkk.entries:
    print("Virsrakss:", entry.title)
    print("Saite: ", entry.link)
    print('\n')

