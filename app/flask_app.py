from flask import Flask, render_template, request, redirect, url_for, flash, session
# se importa la función que regresa los datos del caso brecha salarial
from functions.dataBrecha import getData, plantillaBrecha, epilogoBrechaSinTextoFijo

# se importa la función que regresa los datos del caso violencia
from functions.dataViolencia import getDataViolencia, plantillaViolencia, epilogoViolenciaSinTextoFijo
# se importa la función que regresa los datos del caso diferencia de empleos
from functions.dataDiferenciaLaboral import plantillaEmpleos, getDataEmpleos, epilogoEmpleosSinTextoFijo


# se crea una instancia de Flask
app = Flask(__name__)

# ruta donde se muestran todos los datos extraidos
@app.route('/datos')
def index():
    # se almacenan los datos y se imprimen
    dataBrecha = getData()
    dataViolencia = getDataViolencia()
    #DEBUG: print(getDataEmpleos()  )
    dataDiferenciaLaboral = getDataEmpleos()
    
    # print(f'dataViolencia: {dataViolencia}')
    # print(data)
    # se renderiza la plantilla index.html
    return render_template('index2.html', data = dataBrecha, dataViolencia = dataViolencia, dataEmpleos=dataDiferenciaLaboral)

# ruta principal del proyecto, donde se muestran las opciones para elegir el tipo de caso
@app.route('/index.html')
@app.route('/violencia.html')
@app.route('/violencia')
@app.route('/')
def violencia():
    # se almacenan los datos y se imprimen
    dataBrecha = getData()
    dataViolencia = getDataViolencia()
    #DEBUG: print(getDataEmpleos()  )
    dataDiferenciaLaboral = getDataEmpleos()
    
    # regresa la plantilla violencia.html
    return render_template('index.html', data = dataBrecha, dataViolencia = dataViolencia, dataEmpleos=dataDiferenciaLaboral)

# ruta para mostra la plantilla generada donde el caso es caso de diferencia de empleos
@app.route('/casoLaboral.html')
def diferenciaLaboral():
    plantilla = plantillaEmpleos()
    epilogo = epilogoEmpleosSinTextoFijo()
    # se regresa la plantilla diferenciaEmpleos.html
    return render_template('casoLaboral.html', plantilla = plantilla, epilogo = epilogo)

# ruta para mostra la plantilla generada donde el caso es brecha salarial
@app.route('/casoBrecha.html')
def brechaSalarial():
    plantilla = plantillaBrecha()
    epilogo = epilogoBrechaSinTextoFijo()
    # print(f'La plantilla es: {plantilla}')
    # se regresa la plantilla diferenciaEmpleos.html
    return render_template('casoBrecha.html', plantilla = plantilla, epilogo = epilogo)


# ruta para mostra la plantilla generada donde el caso es violencia
@app.route('/casoViolencia.html')
def violenciaGenero():
    plantilla = plantillaViolencia()
    epilogo = epilogoViolenciaSinTextoFijo()
    # print(f'La plantilla es: {plantilla}')
    # se regresa la plantilla casoViolencia.html
    return render_template('casoViolencia.html', plantilla = plantilla, epilogo = epilogo)

# si __name__ == '__main__' se ejecuta el servidor
if __name__ == '__main__':
    # se ejecuta el servidor en el puerto 3000
    app.run(port = 3000, debug = True)