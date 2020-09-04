# =============================================================================
# Python script for extracting Screen_name related to media twitter urls
# =============================================================================
#
#
#

from ural.twitter import extract_screen_name_from_twitter_url
import csv
from tqdm import tqdm


def removing_screen_names_repetition(urls):
    """Function returning a unique screen_name from a list of urls
    Args:
        urls (list of str): list of urls to test.
    Returns:
        set: returns a unique screen_name"""

    screen_name = set()
    for url in urls:
        nom = extract_screen_name_from_twitter_url(url)
        if nom:
            screen_name.add(nom)
    return screen_name


# ==============================Processing csv file===========================

with open("polarisation.csv", "r") as f, open("media_username.csv", "w") as f2:
    file_content = csv.DictReader(f)
    # list of urls list for each entity
    writer = csv.DictWriter(f2, fieldnames=['ID', 'NAME', 'HOME PAGE', 'SCREEN_NAME'])
    writer.writeheader()
    for row in tqdm(file_content):
        if row["type (TAGS)"] != "media":
            continue
        username = removing_screen_names_repetition(row['PREFIXES AS URL'].split(" "))
        for distinct_username in username:
            writer.writerow({'ID': row["ID"], 'NAME': row["NAME"], 'HOME PAGE': row["HOME PAGE"], 'SCREEN_NAME': distinct_username})
