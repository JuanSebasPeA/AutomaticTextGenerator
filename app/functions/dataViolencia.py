# ----------------------------------- Librerías y Scrapeo ---------------------------------------

# se imporat requets para poder requerir el dominio
import requests
# se importa beautifulsoup para poder hacer el parseo del dom
from bs4 import BeautifulSoup
import random

# url hacia donde se va a hacer el scrapeo, es decir a la página de stackoverflow
url = "https://www.unionguanajuato.mx/2023/03/08/feminicidios-en-mexico-estadisticas-2023-cuantas-mujeres-son-asesinadas/"

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
    allData = tabla.find_all('td')

# --------------------------- Después de hacer el scrapeo ---------------------------------

# lista que almacenará todos los datos
data = []

# se crea una lista vacia para almacenar las fechas
years = []
# se crea una lista vacia para almacenar los numeros
casos = []

# función para obtener las fechas, las cuales son cada 3 datos, empezando por el 0
def getYears():
    # se recorre la lista de todos los datos de la tabla y se agrega a la lista de años el primer dato, y cada 3 datos se agrega el siguiente
    for i in range(len(allData)):
        if i % 3 == 0 or i == 0:
            # se quitan las etiquetas html de los datos
            years.append(allData[i].text)
    # se quita el primer elemento de la lista, ya que es un dato que no se necesita
    years.pop(0)
    # se elimina también el último elemento
    years.pop()
    
getYears()

# función para obtener los casos, cada 3 datos empezando por el índice 1
def getCases():
    for i in range(len(allData)):
        if i % 3 == 1:
            casos.append(allData[i].text)
    # se quita el primer elemento de la lista, ya que es un dato que no se necesita
    casos.pop(0)
    
getCases()

"""DEBUG: print(f'Los años son: {years}')
print(f'Los casos son: {casos}') """
  
# Función que regresa todos los datos
def getDataViolencia():
    # se almacena el año en un diccionario dentro de la lista data, junto al caso que va correspondiendo a los numeros que vayan apareciendo en la lista de casos
    for i in range(len(years)):
        data.append({
            'year': years[i],
            'case': casos[i]
        })
    print(f'Los datos son: {data}')
    return data

# ----------------------- genereación de plantillas ------------------------------
def plantilla1(dato1, dato2, dato3, dato4, porcentaje):
    # se crea la plantilla poniedo las variables entre llaves
    plantilla = f"La incidencia de violencia de género en México ha experimentado un incremento significativo en los últimos tiempos. Durante el año {dato1}, se reportaron un total de {dato2} casos de violencia de género, en contraste con los {dato4} casos registrados en el año {dato3}, lo cual representa una variación  del {porcentaje}%"
    
    return plantilla

def plantilla2(dato1, dato2, dato3, dato4, porcentaje):
     # se guarda la plantilla en un string, con los datos que se van a sustituir
    plantilla = f"La violencia de género en México ha aumentado en los últimos años, en el año {dato1} se registraron {dato2} casos de violencia de género, mientras que en el año {dato3} se registraron {dato4} casos, lo que representa un margen de diferencia del {porcentaje}%. "
    
    return plantilla

def plantilla3(dato1, dato2, dato3, dato4, porcentaje):
    plantilla = f"En los últimos años, se ha observado un preocupante aumento en los casos de violencia de género en México. Durante el año {dato1}, se documentaron {dato2} incidentes de violencia de género, mientras que en el año {dato3} se registraron {dato4} casos, lo que representa una diferencia del {porcentaje}% en comparación. Esta tendencia refleja la urgente necesidad de abordar y combatir la violencia de género en el país"
    
    return plantilla
    
# función para crear la plantilla de violencia de género, eligiendo entre las 3 plantillas
def plantillaViolencia():
    datos = getDataViolencia()
    # función para que se elija cualquier indice de la lista de datos de forma aleatoria
    indice = random.randint(0, len(datos)-1)
    # indice2dieferente al anterior
    indice2 = random.randint(0, len(datos)-1)
    # mientras indice2 sea igual a indice, se vuelve a generar un número aleatorio
    while indice2 == indice:
        indice2 = random.randint(0, len(datos)-1)
    
    # se calcula el porcentaje de diferencia entre datos[indice].total y datos[indice2].total
    # solo con 2 decimales
    porcentaje = porcentajeDiferencia(int(datos[indice]['case']), int(datos[indice2]['case']))
    
    # se elige una variable aleatoria entre 1 y 3
    plantillaAleatoria = random.randint(1, 3)
    # si la variable aleatoria es 1, se usa la plantilla 1
    if plantillaAleatoria == 1:
        plantilla = plantilla1(datos[indice]['year'], datos[indice]['case'], datos[indice2]['year'], datos[indice2]['case'], porcentaje)
        # si es 2, se usa la plantilla 2
    elif plantillaAleatoria == 2:
        plantilla = plantilla2(datos[indice]['year'], datos[indice]['case'], datos[indice2]['year'], datos[indice2]['case'], porcentaje)
        #
    else:
        # si es 3, se usa la plantilla 3
        plantilla = plantilla3(datos[indice]['year'], datos[indice]['case'], datos[indice2]['year'], datos[indice2]['case'], porcentaje)
    
    # se regresa la plantilla
    return plantilla

# función para calcular el porcentaje de diferencia entre 2 datos
def porcentajeDiferencia(dato1, dato2):
    # se calcula la diferencia entre los 2 datos
    diferencia = dato1 - dato2
    # se calcula el porcentaje de diferencia
    porcentaje = (diferencia / dato1) * 100
    # se regresa el porcentaje de diferencia
    return round(porcentaje, 2)

# función para crear el epílogo sin texto fijo

def epilogoViolenciaSinTextoFijo():
    # listas con palabras que se van a usar en el texto
    palabras_crucial = ['Es crucial', 'Es fundamental', 'Es esencial']
    palabras_feminicidios = ['los feminicidios', 'los homicidios de mujeres', 'los asesinatos por razón de género']
    palabras_mundo = ['un mundo', 'un planeta', 'un lugar']
    palabras_combatir = ['combatir', 'luchar', 'enfrentar']
    palabras_crear = [' y crear', 'y construir', 'y fomentar']
    palabras_seguro = ['seguro', 'protegido', 'salvaguardado']
    palabras_mujeres = ['para las mujeres', 'para las damas']
    
    # se elige una palabra aleatoria de cada lista
    crucial = random.choice(palabras_crucial)
    feminicidio = random.choice(palabras_feminicidios)
    combatir = random.choice(palabras_combatir)
    crear = random.choice(palabras_crear)
    mundo = random.choice(palabras_mundo)
    seguro = random.choice(palabras_seguro)
    mujeres = random.choice(palabras_mujeres)
    
    # se crea el texto con las palabras elegidas
    epilogo = f"{crucial} {combatir} {feminicidio} {crear} {mundo} {seguro} {mujeres}."
    
    return epilogo
    

