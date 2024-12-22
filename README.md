# Ayudando a un amigo.

Este repositorio nace con la última frase de este whatsApp

![image](https://github.com/user-attachments/assets/58f3e36e-51aa-4f47-9cb7-c2b8475a5d81)



## Análisis previo.

He usado firefox web-browser. Con `CTRL + SHIFT + I` abro las `web developer tool` y empiezo a mirar.

![image](https://github.com/user-attachments/assets/c32215f6-b925-4c95-83c9-12771e4572a1)


EL diseñador de la página web, ante los 2878 expositores en la feria, para mejorar la percepción del usuario de la página web hace uso de un `infinite-scroll-component`que carga solo los 100 primeros expositores, para ofrecer el resto a medida que el usuario hace scroll down con el ratón.

Esto dificulta la extracción de datos. Tendría que hacer uso del webdriver de selenium, para lo cual no tengo conocimientos.

Una vez identificado el `infinit-scroll-component`,  manualmente hago scroll hasta el final de los expositores. Cuando visualizo "Zoup! Good, Really Good", en el `web developer tool`, sobre el `infinite-scroll-component` con el botón de la derecha `Edito como HTML`. Lo selecciono todo con `CTRL + SHIFT + FIN`. Lo copio todo al portapapeles con `CTRL + C`. Abro `Vim` y lo pego con `CTRL + SHIFT + V`. Los 4 806 442 carácteres de codigo HTML que contenía el `infinit-scroll-component`, se quedan en una única línea dentro de Vim, en un fichero al que he llamado todo.html.

![image](https://github.com/user-attachments/assets/4a853d7c-826e-4e16-9e25-dfcf10758a51)

Necesito insertar saltos de linea entre las etiquetas HTML.  el comando Vim `% s/></>\r</g` lo soluciona.

![image](https://github.com/user-attachments/assets/83c6cd05-5fb6-4a31-b129-5927f0125083)


Esto me permite ver qué codigo HTML se usa para mostrar individualmente cada uno de los expositores.
![image](https://github.com/user-attachments/assets/82a7ce5b-e470-4a2b-bee0-9801454c341b)

Me interesa de cada ficha individual:
+ La URL que me abre la ficha de datalle de cada expositor. (```<a href="/widget/event/natural-products-expo-west-3/exhibitor/RXhoaWJpdG9yXzIwMTE2OTk=">```)
+ El nombre del Expositor (```<span class="sc-a13c392f-0 sc-5729954b-3 ffVsRx csdXSf">Guru Nanda, LLC</span>```)
+ EL tipo de patrocinio (```<span class="sc-a13c392f-0 sc-5729954b-6 ffVsRx jIHVOh">Platinum</span>```)
+ El Stand (```<span class="sc-a13c392f-0 sc-5729954b-7 ffVsRx bNBdlQ">3133</span>```)


 ## Transformando formatos
 
 Creo un script Python para que me extraiga la informacion relevante ( 333 761 carácters de los 4 806 442). Voy a leer ('r') el fichero "todo.html" y crear ('w') el fichero  "lista.tsv"
 
```python
def main():
    base_url = 'todo.html'
    with open('todo.html', 'r') as file:
        data = extract_exhibitor_data(file)
    with open("lista.tsv", "w") as file:
        file.write(f"Expositor\t Patrocinio\t Stand\t url\n")
        for exhibitor in data:
            file.write(f'"{exhibitor['name']}"\t"{exhibitor['sponsor']}"\t"{exhibitor['booth_number']}"\t"{exhibitor['url']}"\n')

if __name__ == '__main__':
    main()
```
El fichero "lista.csv" tiene este aspecto:

![image](https://github.com/user-attachments/assets/51a2a0e3-569a-4807-9a46-7f8abebd0001)

## La sopa bonita. Sopa de letras ....
En el script anterior, la funcion `extract_exhibitor_data()` es la que analiza el html estático que tengo en el fichero `todo.html`
La libreria BeautifulSoup tiene las herramientas adecuadas.

El primer find_all crea un lista con 2878 registros que contiene el HTML existente entre cada pareja de etiquetas HTML <a></a>

El for pasa por cada uno de esos 2878 registros y para cada uno de ellos recupera la URL con el get() y busca todos los Spans. 

Para cada expositor podemos tener 2 spans (Expositor que o exponsoriza) o tres spans (Expositor que no exposoriza)
Los datos extraidos se van añadiendo a la lista data.
Al acabar la funcion devuelve los datos extraidos.

```python
from bs4 import BeautifulSoup

def extract_exhibitor_data(file):
    soup = BeautifulSoup(file, features='html.parser')

    # Búscame todos los contenedores con detalles del expositor.
    exhibitor_details = soup.find_all('a', href=True)  # Adjust class name if needed
    data = []
    for exhibitor in exhibitor_details:
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

        data.append({'name': name, 'sponsor':sponsor, 'booth_number': booth_number, 'url':url})  # Add extracted data to dictionary
    return data

## Segunda vuelta

Leeremos el fichero "lista.tsv". probamos con expositores

``python
with open('lista.tsv', 'r') as file:
    exhibitors = 0
    for exhibitor in file:
        name, sponsor, stand, link = exhibitor.strip().split("\t")
        exhibitors +=1
        base_url = "https://attend.expowest.com" +link[1:-1]
        data = extract_exhibitor_data(base_url)
        #print(name, sponsor, stand, link)
        if exhibitors == 7:
            break
```

