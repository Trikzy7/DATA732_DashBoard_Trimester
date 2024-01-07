import requests
from IPython.display import HTML
import json


def do_search(keyWords:list):
    """
    GOAL : Obtenir le resultat de la recherche effectuée sur le browser BING avec les mots clés en paramètre
    :param keyWords: list de keywords pour faire la recherche
    :return: json contenant le résultat renvoyer par le browser BING
    """

    # -- API KEY
    subscription_key = "09ffef10f29d441eaa7c2ddeee9226f3"
    assert subscription_key

    # -- URL API
    search_url = "https://api.bing.microsoft.com/v7.0/search"

    # -- KEY WORDS string with space separator
    separator = " "
    search_term = separator.join(keyWords)

    # -- Do the search
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    response = requests.get(search_url, headers=headers, params=params)

    response.raise_for_status()
    search_results = response.json()

    return search_results['webPages']


def get_event(keyWords:list):
    """
    GOAL : Get le titre et l'url du first article
    :param keyWords: list de keywords pour faire la recherche
    :return: dict containing title and url of first article
    """

    # -- btenir les résultats de la recherche
    search_results = do_search(keyWords)

    # -- Renvoyer le titre et l'url du 1er article
    return {
        'title': search_results['value'][0]['name'],
        'url': search_results['value'][0]['url']
    }

