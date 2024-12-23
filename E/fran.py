import requests
from bs4 import BeautifulSoup

def extract_exhibitor_data(file):
    #response = requests.get(url)
    soup = BeautifulSoup(file, features='html.parser')

    # Identify the element containing exhibitor details (might need adjustment)
    #exhibitor_details = soup.find('div', class_='infinite-scroll-component__outerdiv')  # Adjust class name if needed
    exhibitor_details = soup.find_all('a', href=True)  # Adjust class name if needed
    data = []
    #print(exhibitor_details)
    for exhibitor in exhibitor_details:
        # Extract name (assuming it's in a heading)
        #url_element = exhibitor.find('a')  # Adjust tag if name is not in h3
        url = exhibitor.get('href') if exhibitor else None


        spans = exhibitor.find_all('span')  # Adjust tag if name is not in h3

        if len(spans) == 2:
            name = spans[0].text.strip() if spans[0] else None
            sponsor = None
            booth_number = spans[1].text.strip() if spans[1] else None
        if len(spans) == 3:
            name = spans[0].text.strip() if spans[0] else None
            sponsor = spans[1].text.strip() if spans[1] else None
            booth_number = spans[2].text.strip() if spans[2] else None

        # # Extract other data (adjust selectors based on HTML structure)
        # # Example: booth number
        # sponsor_element = exhibitor.find('span')  # Adjust class name if needed
        # sponsor = sponsor_element.text.strip() if sponsor_element else None

        # booth_element = exhibitor.find('span')  # Adjust class name if needed
        # booth_number = booth_element.text.strip() if booth_element else None

        # ... Extract other relevant information

        data.append({'name': name, 'sponsor':sponsor, 'booth_number': booth_number, 'url':url})  # Add extracted data to dictionary

    return data

def main():
    base_url = 'https://www.expowest.com/en/exhibitor-list/2025-Exhibitor-List.html'
    base_url = 'todo.html'
    with open('todo.html', 'r') as file:
        data = extract_exhibitor_data(file)

    # Print or store the extracted data in a CSV, JSON, or database (not implemented here)
    with open("tirame.tsv", "w") as file:
        file.write(f"Expositor\t Patrocinio\t Stand\t url\n")
        for exhibitor in data:
            # print(f"Name: {exhibitor['name']}")
            # print(f"Sponsor type: {exhibitor['sponsor']}")
            # print(f"Booth Number: {exhibitor['booth_number']}")
            # print("-"*20)  # Separator
            file.write(f'"{exhibitor['name']}"\t"{exhibitor['sponsor']}"\t"{exhibitor['booth_number']}"\t"{exhibitor['url']}"\n')

if __name__ == '__main__':
    main()