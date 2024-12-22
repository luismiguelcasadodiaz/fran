# Ayudando a un amigo.

Este repositorio nace con la última frase de este whatsApp

![image](https://github.com/user-attachments/assets/58f3e36e-51aa-4f47-9cb7-c2b8475a5d81)



## Análisis previo.

He usado firefox web-browser. Con `CTRL + SHIFT + I` abro las `web developer tool` y empiezo a mirar.

![image](https://github.com/user-attachments/assets/c32215f6-b925-4c95-83c9-12771e4572a1)


EL diseñador de la página web, ante los 2878 expositores en la feria, para mejorar la percepción del usuario de la página web hace uso de un `infinite-scroll-component`que carga solo los 100 primeros expositores, para ofrecer el resto a medida que el usuario hace scroll down con el ratón.

Esto dificulta la extracción de datos. Tendría que hacer uso del webdriver de selenium, para lo cual no tengo conocimientos.

Una vez identificado el `infinit-scroll-component`,  manualmente hago scroll hasta el final de los expositores. Cuando visualizo "Zoup! Good, Really Good", en el `web developer tool`, sobre el `infinite-scroll-component` con el botón de la derecha `Edito como HTML`. Lo selecciono todo con `CTRL + SHIFT + FIN`. Lo copio todo al portapapeles con `CTRL + C`. Abro `Vim` y lo pego con `CTRL + SHIFT + V`. Los 4 806 442 carácteres de codigo HTML que contenía el `infinit-scroll-component`, se quedan en una única línea dentro de Vim.



Esto me permite ver qué codigo HTML se usa para mostrar individualmente cada uno de los expositores.
![image](https://github.com/user-attachments/assets/82a7ce5b-e470-4a2b-bee0-9801454c341b)

Me interesa de cada ficha individual:
+ La URL que me abre la ficha de datalle de cada expositor. (```<a href="/widget/event/natural-products-expo-west-3/exhibitor/RXhoaWJpdG9yXzIwMTE2OTk=">```html)
+ El nombre del Expositor (```<span class="sc-a13c392f-0 sc-5729954b-3 ffVsRx csdXSf">Guru Nanda, LLC</span>```html)
+ EL tipo de patrocinio (```<span class="sc-a13c392f-0 sc-5729954b-6 ffVsRx jIHVOh">Platinum</span>```html)
+ El Stand (```<span class="sc-a13c392f-0 sc-5729954b-7 ffVsRx bNBdlQ">3133</span>```html)
