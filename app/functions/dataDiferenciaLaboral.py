# se imporat requets para poder requerir el dominio
import requests
# se importa beautifulsoup para poder hacer el parseo del dom
from bs4 import BeautifulSoup
import random

# url hacia donde se va a hacer el scrapeo, es decir a la página de stackoverflow
url = "https://onuhabitat.org.mx/index.php/division-sexual-del-trabajo-mujeres-en-el-mundo-laboral"

# por medio del encabezado se manda información al servidor para que no se de cuenta que se está haciendo scrapeo
encabezado = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                    "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

# requerimiento al dominio o servidor
respuesta = requests.get(url, headers=encabezado)

# se usa beautifulsoup para hacer el parseo del dom, creando un objeto de tipo BeautifulSoup con el contenido de la respuesta
soup = BeautifulSoup(respuesta.text, 'lxml')

# se busca el elemento tabla
tabla = soup.find('table')
# DEBUG: print(f'La tabla es: {tabla}')

if tabla is None:
    print('No se encontró la tabla')
else:
    #print(f'La tabla es: {tabla}')
    # se encuentra un span dentro de un td de la tabla
    alldata = tabla.find_all('td')
    #print(f'Los datos son: {allData}')
    

# --------------------------- Después de hacer el scrapeo ---------------------------------

# lista que almacenará todos los datos
data = []
# copiaDeDatos
copiaDeDatos = []

# se recorre la lista con todos los empleos y se almacena el texto de cada uno en la lista empleos
for td in alldata:
    ps = td.find_all('p')
    for p in ps:
        copiaDeDatos.append(p.text)

# print(f'Los empleos son: {empleosCopy}')

# Función que regresa todos los datos
def getDataEmpleos():
    # se recorren los datos de la lista copiaDeDatos, se va almacenando en un diccionario cada 4 datps, donde el primero representa el trimestre, el segundo el total, el tercero los hombres, el tercero las mujeres, el cuerto dato se omite
    # DEBUG: print(f'\nLa longitud de copiaDeDatos es: {len(copiaDeDatos)}')
    # recorre cada 4 datos
    for i in range(0, len(copiaDeDatos), 5):
        # DEBUG: print(f'\nla posicion es: {i}')
        data.append({
            'trimestre': copiaDeDatos[i],
            'total': copiaDeDatos[i+1],
            'hombres': copiaDeDatos[i+2],
            'mujeres': copiaDeDatos[i+3]
        })
    # se regresa la lista con todos los datos
    return data

# --------------------------- generación de las Plantillas ---------------------------------
# 3 tipos de plantillas
def plantilla1(dato1, dato2, dato3, dato4, dato5, porcentaje):
     # se guarda la plantilla en un string, con los datos que se van a sustituir
    plantilla = f"Durante el {dato1}, se registraron aproximadamente {dato2} casos de discriminación de género en el ámbito laboral en México. De estos casos, {dato3} correspondieron a hombres y {dato4} a mujeres. Este número mostró una diferencia del {porcentaje}% en comparación con el {dato5}.La persistencia de la inequidad de género en el entorno laboral es una preocupación constante, ya que afecta negativamente a un gran número de hombres y mujeres en todo el país."
    return plantilla

def plantilla2(dato1, dato2, dato3, dato4, dato5, porcentaje):
    plantilla = f"En México, en el periodo comprendido por el {dato1}, se reportaron alrededor de {dato2} casos de discriminación de género en el ámbito laboral. El número de casos a mujeres fue de {dato4}, y {dato3} fue a hombres. Esta cifra revela una variación con el {dato5}, y su porcentaje de {porcentaje}%. Por otra parte, se sigue trabajando para erradicar la desigualdad de género en el ámbito laboral."
    
    return plantilla

def plantilla3(dato1, dato2, dato3, dato4, dato5, porcentaje):
    plantilla = f"Durante el {dato1} analizado, se registraron aproximadamente {dato2} casos de discriminación de género en el ámbito laboral en México. De este total, {dato3} correspondieron a hombres y {dato4} a mujeres. Estos datos muestran una diferencia del {porcentaje}% en comparación con el trimestre previo, que fue {dato5}. Por último, estos datos continuan incrementando durante este trimestre, lo que representa un problema para la sociedad mexicana."
    
    return plantilla
    
# función que regresa una plantilla de forma aleatoria
def plantillaEmpleos():
    datos = getDataEmpleos()
    # función para que se elija cualquier indice de la lista de datos de forma aleatoria
    indice = random.randint(0, len(datos)-1)
    # indice2dieferente al anterior
    indice2 = random.randint(0, len(datos)-1)
    # mientras indice2 sea igual a indice, se vuelve a generar un número aleatorio
    while indice2 == indice:
        indice2 = random.randint(0, len(datos)-1)
        
    # imprimir el valor de la llave 'total' del primer dato de la lista
    print(f"El total es: {datos[indice]['total']}")
    
    # se calcula el porcentaje de diferencia entre datos[indice].total y datos[indice2].total
    # solo con 2 decimales
    porcentaje = round(calculaProcentaje(datos[indice]['total'], datos[indice2]['total']), 2)
    
    #elige una de las 3 plantillas de forma aleatoria
    plantillaSeleccionada = random.randint(1, 3)
    if plantillaSeleccionada == 1:
        plantilla = plantilla1(datos[indice]['trimestre'], datos[indice]['total'], datos[indice]['hombres'], datos[indice]['mujeres'], datos[indice2]['trimestre'], porcentaje)
    elif plantillaSeleccionada == 2:
        plantilla = plantilla2(datos[indice]['trimestre'], datos[indice]['total'], datos[indice]['hombres'], datos[indice]['mujeres'], datos[indice2]['trimestre'], porcentaje)
    else:
        plantilla = plantilla3(datos[indice]['trimestre'], datos[indice]['total'], datos[indice]['hombres'], datos[indice]['mujeres'], datos[indice2]['trimestre'], porcentaje)
        
    
    # se regresa la plantilla
    return plantilla
    
    # ---------------------------- Funciones alternativas ---------------------------------
# función que calcula el porcentaje de diferencia entre dos datos
def calculaProcentaje(dato1, dato2):
    # convierte los datos a enteros y quita el signo de porcentaje y el espacio
    dato1 = float(dato1.replace('%', '').replace(' ', ''))
    dato2 = float(dato2.replace('%', '').replace(' ', ''))
    # calcula la diferencia en procentaje entre dos datos
    diferencia = dato1 - dato2
    porcentaje = (diferencia / dato2) * 100
    return porcentaje

def epilogoEmpleosSinTextoFijo():
    # lista de palabras para formar el epílogo
    palabras_pais = ["En México", "En la República Mexicana", "En el país"]
    palabras_persisten = ["persisten", "continúan", "se mantienen"]
    palabras_desafios = ["los desafíos", "los retos", "los problemas"]
    palabras_empleo = ["de empleo", "de trabajo", "laborales"]
    palabras_genero = ["por el género", "por el sexo", "por diferencia de género"]

    # se elige una palabra aleatoria de cada lista 
    palabra_empleo = random.choice(palabras_empleo)
    palabra_genero = random.choice(palabras_genero)
    palabra_pais = random.choice(palabras_pais)
    palabra_persisten = random.choice(palabras_persisten)
    palabra_desafios = random.choice(palabras_desafios)

    #se forma un epílogo solo con las variables
    epilogo = f"{palabra_pais} {palabra_persisten} {palabra_desafios} {palabra_empleo} {palabra_genero}."
    
    return epilogo