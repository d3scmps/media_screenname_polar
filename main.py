# =============================================================================
# Python script for extracting Screen_name related to media twitter urls
# =============================================================================
#
# 
#

from ural.twitter import extract_screen_name_from_twitter_url
import csv 
from tqdm import tqdm

def redundance(urls):
    """Function returning a unique screen_name from a list of urls
    Args:
        urls (list of str): list of urls to test.
    Returns:
        set: returns a unique screen_name"""
    screen_name = set()
    for url in urls:
        if extract_screen_name_from_twitter_url(url):
            nom = extract_screen_name_from_twitter_url(url)
            screen_name.add(nom)
    if len(screen_name)>0:
        return screen_name 
    return None
      
# ==============================Processing csv file ===============================================
with open("polarisation.csv", "r") as f:
    file_content = csv.DictReader(f)
    #list of urls list for each entity
    urls_list = []
    with open("media_username.csv", "w") as f2:
        headers = ['ID', 'NAME','HOME PAGE','SCREEN_NAME']
        writer = csv.DictWriter(f2, fieldnames=headers)
        writer.writeheader()
    f2.close()
    for row in tqdm(file_content):
        if row["type (TAGS)"] == "media":
            media = {'ID':row['ID'], 'NAME':row['NAME'],'HOME PAGE':row['HOME PAGE'],'URLS':row['PREFIXES AS URL'].split(" ")}
            urls_list.append(media)

    with open("media_username.csv", "a") as f2:
        writer = csv.DictWriter(f2,fieldnames=headers)
        for index,entity in enumerate(urls_list) :
            username = redundance(entity["URLS"])
            if username:
                for distinct_username in username:
                    writer.writerow({'ID' : entity["ID"],'NAME' :entity["NAME"],'HOME PAGE':entity["HOME PAGE"],'SCREEN_NAME':distinct_username})
            
                    



            
            
            