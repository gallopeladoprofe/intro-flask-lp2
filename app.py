from flask import Flask, render_template, request, redirect, url_for,flash
from dao.CiudadDao import CiudadDao

app = Flask(__name__)

# flash requiere esta sentencia
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"

# endpoint o ruta
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/ciudades-index')
def ciudades_index():
    # Creacion de la instancia de ciudaddao
    ciudadDao = CiudadDao()
    lista_ciudades = ciudadDao.getCiudades()
    return render_template('ciudades-index.html', lista_ciudades=lista_ciudades)

@app.route('/ciudades')
def ciudades():
    return render_template('ciudades.html')

@app.route('/guardar-ciudad', methods=['POST'])
def guardarCiudad():
    ciudad = request.form.get('txtDescripcion').strip()
    if ciudad == None or len(ciudad) < 1:
        # mostrar un mensaje al usuario
        flash('Debe escribir algo en la descripcion', 'warning')

        # redireccionar a la vista ciudades
        return redirect(url_for('ciudades'))

    ciudaddao = CiudadDao()
    ciudaddao.guardarCiudad(ciudad.upper())

    # mostrar un mensaje al usuario
    flash('Guardado exitoso', 'success')

    # redireccionar a la vista ciudades
    return redirect(url_for('ciudades'))

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)