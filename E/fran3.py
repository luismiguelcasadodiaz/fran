from bs4 import BeautifulSoup
import requests
import time
import random

def get_contact(soup):
    
    contact_raw = soup.find('ul', class_="list-unstyled")
    if not contact_raw:
        contact_clean = ["N/A"]
    else:
        contact_clean = []
        contact_items = contact_raw.text.split("\n")
        for contact_item in contact_items:
            contact_item = contact_item.strip()
            if len(contact_item) > 0:
                contact_clean.append(contact_item)
    return contact_clean


def get_description(soup):
    company_description_raw= soup.find('p', class_="BoothPrintProfile")
    if not company_description_raw:
        company_description = "N/A"
    else:
        company_description = company_description_raw.get_text().replace("\r\n", " ")
    return company_description

def get_brands(soup):
    company_brands = soup.find('p', class_="BoothBrands")
    if not company_brands:
        brands = "N/A"
    else:
        brands = company_brands.text
    return brands


def get_categories(soup):
    company_categories = soup.find_all('div', class_="ProductCategoryContainer")
    categorias = []
    subcategorias = []
    for categoria in company_categories:
        label = categoria.find('a')
        categorias.append(label.get_text().strip())
        subcat = get_subcategories(categoria)
        subcategorias.append(subcat)
    return categorias , subcategorias


def get_subcategories(soup):
    company_subcategories = soup.find_all('li', class_="ProductCategoryLi")
    subcategorias = []
    for subcategory in company_subcategories:
        subcategorias.append(subcategory.text)
    return subcategorias

def get_name(soup):
    title = soup.find('h2', class_="h1 content-title")
    if not title:
        resultado = "N/A"
    else:
        resultado = title.text
    return resultado

def get_booth(soup):
    booth = soup.find('p', class_="lead")
    if not booth:
        resultado = "N/A"
    else:
        resultado = booth.text
    return resultado

def main():
    url= "https://exhibitor.expowest.com/ew25/Public/Exhibitors.aspx?Index=Z"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features='html.parser')
    los_expositores = soup.find_all('a', class_="exhibitorName", href=True)
    count = 2623
    salida = open("extraccionn99.tsv", "w")
    for e in los_expositores:
        url = "https://exhibitor.expowest.com/ew25/Public/" + e.get('href')
        response = requests.get(url)
        soup = BeautifulSoup(response.content, features='html.parser')
    
        company_name = get_name(soup)
        company_booth = get_booth(soup)
        company_contact = get_contact(soup)
        company_description = get_description(soup)
        company_brands = get_brands(soup)
        categorias , subcategorias = get_categories(soup)
        #subcategorias = get_subcategories(soup)
        print(count, company_name, company_booth, company_contact, company_description, company_brands, categorias, subcategorias)
        salida.write(f"{count}\t{company_name}\t{company_booth}\t{company_contact}\t{company_description}\t{company_brands}\t{categorias}\t{subcategorias}\n")
        count +=1
        time.sleep(1+2*random.random())
        #if count == 6:
            #break
    salida.close()
if __name__ == '__main__':
    main()

