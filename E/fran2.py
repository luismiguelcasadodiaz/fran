from bs4 import BeautifulSoup
import requests
import time
import random

def extract_exhibitor_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    
    #information Details

    information_details = soup.find_all('div', class_="sc-88662468-0 fZqqpS")
    resultado = ">"
    if not information_details:
        resultado += "None"
    else:
        for n, d1 in enumerate(information_details):
            resultado += d1.text.strip() + "!!"
    resultado += "<"


    #Pavilion_details

    pavilio_details = soup.find_all('div', class_="sc-45c084b0-2 jsVWbR")
    resultado += ">"
    if not pavilio_details:
        resultado += "None"
    else:
        for n, d2 in enumerate(pavilio_details):
            resultado += d2.text.strip() + "!!"
    resultado += "<"

    #Social Media Details

    social_media_details= soup.find_all('div', class_="ssc-9c9868a2-15 kzrhIj")
    resultado += ">"
    if not social_media_details:
        resultado += "None"
    else:
        for data in social_media_details:
            refs = data.find_all('a')
            for ref in refs:
                resultado += ref.get('href') + "!!"
    resultado += "<"

    #Contact_details
    contact_divs = soup.find('div', class_="sc-901e7a18-1 euvZgy")
    resultado += ">"
    if not contact_divs:
        resultado += "None"
    else:
        for data1 in contact_divs.descendants:
            #spans = data1.find_all('span')
            print(data1)
            spans = []
            for span in spans:
                text = span.text.strip()
                resultado += text + "!!"
    resultado += "<"

    #CDocument_details
    document_divs = soup.find_all('div', class_="sc-ebb5afa6-0 jsdHsD")
    resultado += ">"
    if not document_divs:
        resultado += "None"
    else:
        for data2 in document_divs:
            href = data2.get('href')
            if not href:
                resultado += "None" + "!!"
            else:
                resultado += href + "!!"
            spans = data2.find_all('span')
            for span in spans:
                text = span.text.strip()
                resultado += text + "!!"
    resultado += "<"
    return resultado


def extract_exhibitor_data2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    information_details = soup.find('div', class_="sc-9703737b-0 fUqUcd")
    information_details = soup.find('div', class_="sc-901e7a18-1 euvZgy")
    print(type(information_details))

    for span in information_details.find_all('div'):
        text = span.text.strip()
        print(text)

    information_details = soup.find_all('a', class_="sc-efce57e-1 dUQylZ")
    print(information_details)
    for e in information_details:
        print(e.get('href'))

salida = open("lista ampliada.tsv", "w")
with open('lista.tsv', 'r') as file:
    exhibitors = 0
    for exhibitor in file:
        name, sponsor, stand, link = exhibitor.strip().split("\t")
        time.sleep(1+2*random.random())
        exhibitors +=1
        base_url = "https://attend.expowest.com" +link[1:-1]
        data = extract_exhibitor_data2(base_url)
        print(name, sponsor, stand, link, data, sep="\t")
        salida.write(f"{name}\t{sponsor}\t{stand}\t{link}\t{data}\n")
        if exhibitors == 1:
            break
salida.close()
