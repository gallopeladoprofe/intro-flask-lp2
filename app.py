from flask import Flask, render_template, request, redirect, url_for
from dao.CiudadDao import CiudadDao

app = Flask(__name__)

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

@app.route('/ciudades')
def ciudades():
    return render_template('ciudades.html')

@app.route('/guardar-ciudad', methods=['POST'])
def guardarCiudad():
    ciudad = request.form.get('txtDescripcion').strip()
    if ciudad == None or len(ciudad) < 1:
        return redirect(url_for('ciudades'))

    ciudaddao = CiudadDao()
    ciudaddao.guardarCiudad(ciudad)
    return f"{request.form.get('txtDescripcion')}"

@app.route('/guardar-mascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llego tu mascota <strong>{nombreMascota}</strong> al servidor"

# se pregunta por el proceso principal
if __name__=='__main__':
    app.run(debug=True)