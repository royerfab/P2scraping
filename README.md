# Projet 2 Développeur d'application Python : scraping


## Informations générales

Ce projet constitue un examen dans le cadre du parcours Développeur d'application Python d'OpenClassrooms, il est codé avec le langage Python.
Concrètement, il consiste à effectuer le scraping des informations contenues sur le site Books to Scrape, en partant d'un seul produit jusqu'à l'ensemble des produits du site.

## Auteur

Fabien ROYER

## Contributions

Le projet est achevé depuis août 2021.

## Installation

Utilisez le _package installer_ [pip](https://pypi.org/project/pip/) pour installer les packages inclus dans le fichier requirements.txt, pour cela utilisez dans le terminal la commande : 
```bash
pip install -r requirements.txt
```

## Utilisation

L'utilisation de ce code requiert d'importer les packages suivants :
- Dans le fichier scraping.py : requests, os, urllib.request, le module BeautifulSoup du package bs4.
- Dans le fichier scraping_category.py : requests, os, csv, le module BeautifulSoup du package bs4, la fonction scraping_one_product du fichier scraping.py.
- Dans le fichier scraping_website.py : requests, le module BeautifulSoup du package bs4, la fonction scraping_all_category du fichier scraping_category.py.

Pour importer un élément il est nécessaire d'utiliser la commande import, par exemple:
```bash
import requests
```
Pour exécuter le code, le point d'entrée étant le fichier scraping_website.py, il faut entrer la commande suivante dans le terminal :
```bash
python scraping_website.py
```