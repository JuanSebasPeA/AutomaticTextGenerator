# se imporat requets para poder requerir el dominio
import requests
# se importa beautifulsoup para poder hacer el parseo del dom
from bs4 import BeautifulSoup
import random

# url hacia donde se va a hacer el scrapeo, es decir a la página de stackoverflow
url = "https://datosmacro.expansion.com/demografia/indice-brecha-genero-global/mexico"

# por medio del encabezado se manda información al servidor para que no se de cuenta que se está haciendo scrapeo
encabezado = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                    "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

# requerimiento al dominio o servidor
respuesta = requests.get(url, headers=encabezado)

# se usa beautifulsoup para hacer el parseo del dom, creando un objeto de tipo BeautifulSoup con el contenido de la respuesta
soup = BeautifulSoup(respuesta.text, 'lxml')

# se busca el elemento con el id tb0
tabla = soup.find(id = "tb0")
# varibale para almacenar las preguntas, encontrando los elementos con la clase question-summary
fechasPrueba = tabla.find_all('td', class_ = 'fecha')    
numerosPrueba = tabla.find_all('td', class_ = 'numero')

# --------------------------- Después de hacer el scrapeo ---------------------------------

# lista que almacenará todos los datos
data = []

# se crea una lista vacia para almacenar las fechas      
fechas = []
# se crea una lista vacia para almacenar los numeros
numeros = []

# función para obtener las fechas sin etiquetas
def getFechas():
    for fecha in fechasPrueba:
        fechas.append(fecha.text)

getFechas()

# función para obtener los números sin etiquetas
def getNumeros():
    for numero in numerosPrueba:
        numeros.append(numero.text)
    
getNumeros()
  
# Función que regresa todos los datos
def getData():
    # se alamcena cada fecha en diccionario, junto al dato 1 y dato 2 que va correspondiendo a los 2 primeros numeros que vayan apareciendo en la lista de numeros
    for i in range(len(fechas)):
        # print(type(fechas[0]))
        data.append({
            'fecha': fechas[i],
            'ranking': numeros[i*2],
            'index': numeros[i*2+1]
        })
    # se regresa la lista de datos
    return data

# --------------------------- generación de las Plantillas ---------------------------------
def plantilla1(dato1, dato2, dato3, dato4, dato5, dato6):
   # se guarda la plantilla en un string, con los datos que se van a sustituir
    plantilla = f"En el año {dato1}, se identificó que México ocupó el {dato2} puesto en el ranking de brecha salarial, con un índice de brecha salarial de {dato3}. Estos datos nos muestran una evidente desigualdad salarial entre hombres y mujeres en el país. La diferencia con respecto al año {dato4}, en donde México tuvo el puesto {dato5} en el ranking, fue de un índice de {dato6}."
    
    return plantilla


def plantilla2(dato1, dato2, dato3, dato4, dato5, dato6):
   # se guarda la plantilla en un string, con los datos que se van a sustituir
    plantilla = f"En cuanto a la brecha salarial, México se ubicó en el {dato2} lugar del ranking durante el año {dato1}, presentando un índice de brecha salarial de {dato3}. Estos resultados evidencian la persistente desigualdad salarial entre hombres y mujeres en el país. Cabe destacar que en el año {dato4}, México ocupó el {dato5} puesto en el ranking, mostrando un índice de brecha salarial de {dato6}. Estas cifras resaltan la necesidad de implementar medidas que promuevan la equidad salarial en México."
    
    return plantilla


def plantilla3(dato1, dato2, dato3, dato4, dato5, dato6):
   # se guarda la plantilla en un string, con los datos que se van a sustituir
    plantilla = f"Durante el año {dato1}, se pudo constatar que México se posicionó en el {dato2} lugar en el índice de brecha salarial, Con {dato3} de índice. Estos datos ponen de manifiesto la existencia de una marcada disparidad salarial entre hombres y mujeres en el país. En comparación con el año {dato4}, donde cual México fue {dato5} puesto en el ranking, se observa una variación en el índice de brecha salarial, el cual alcanzó {dato6}."
    
    return plantilla


# función que regresa una de las plantillas de forma aleatoria    
def plantillaBrecha():
    datos = getData()
    # función para que se elija cualquier indice de la lista de datos de forma aleatoria
    indice = random.randint(0, len(datos)-1)
    # indice2dieferente al anterior
    indice2 = random.randint(0, len(datos)-1)
    # mientras indice2 sea igual a indice, se vuelve a generar un número aleatorio
    while indice2 == indice:
        indice2 = random.randint(0, len(datos)-1)
    
    """DEBUG: print(f'El indice es: {indice}')
    print(f'El indice2 es: {indice2}')"""
    
    # se elige una de las 3 plantillas de forma aleatoria
    plantillaSeleccionada = random.randint(1, 3)
    if plantillaSeleccionada == 1:
        plantilla = plantilla1(datos[indice]['fecha'], datos[indice]['ranking'], datos[indice]['index'], datos[indice2]['fecha'], datos[indice2]['ranking'], datos[indice2]['index'])
    elif plantillaSeleccionada == 2:
        plantilla = plantilla2(datos[indice]['fecha'], datos[indice]['ranking'], datos[indice]['index'], datos[indice2]['fecha'], datos[indice2]['ranking'], datos[indice2]['index'])
    else:
        plantilla = plantilla3(datos[indice]['fecha'], datos[indice]['ranking'], datos[indice]['index'], datos[indice2]['fecha'], datos[indice2]['ranking'], datos[indice2]['index'])
        
    # se regresa la plantilla
    return plantilla
    
# función que regresa el epilogo de la plantilla solo con textos alternativos
def epilogoBrechaSinTextoFijo():
    palabras_brecha = ['La brecha', 'La desigualdad', 'La disparidad']
    palabras_salarial = ['salarial', 'de sueldos', 'en los salarios']
    palabras_mexico = ['en México', 'en nuestro país', 'en esta nación']
    palabras_persiste = ['persiste', 'continúa', 'perdura']
    palabras_queremos = ['y queremos', 'y deseamos', 'y anhelamos']
    palabras_enfrentar = ['enfrentarla', 'combatirla', 'resolverla']
    palabras_medidas = ['y las medidas', 'y las acciones', 'y las políticas']
    palabras_gobierno = ['El gobierno', 'Las autoridades', 'Las entidades']
    palabras_necesitan = ['necesitan', 'requieren', 'precisan']
    palabras_justa = ['justos', 'equitativos', 'igualitarios']
    palabras_ingresos = ['ingresos', 'salarios', 'sueldos']
    palabras_asegurar = ['asegurar', 'garantizar', 'proteger']

    palabra_brecha = random.choice(palabras_brecha)
    palabra_salarial = random.choice(palabras_salarial)
    palabra_mexico = random.choice(palabras_mexico)
    palabra_persiste = random.choice(palabras_persiste)
    palabra_enfrentar = random.choice(palabras_enfrentar)
    palabra_medidas = random.choice(palabras_medidas)
    palabra_gobierno = random.choice(palabras_gobierno)
    palabra_justa = random.choice(palabras_justa)
    palabra_necesitan = random.choice(palabras_necesitan)
    palabra_asegurar = random.choice(palabras_asegurar)
    palabra_ingresos = random.choice(palabras_ingresos)
    palabra_queremos = random.choice(palabras_queremos)

    epilogo = f"{palabra_brecha} {palabra_salarial} {palabra_mexico} {palabra_persiste}, {palabra_queremos} {palabra_enfrentar}. {palabra_gobierno} {palabra_medidas} {palabra_necesitan} {palabra_asegurar} {palabra_justa} {palabra_ingresos}."

    return epilogo

