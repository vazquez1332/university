from __main__ import app
from flask import render_template, request
from .models import Estudiante, Asistencia

@app.route('/consultar_inasistencias', methods=['GET', 'POST'])
def consultar_inasistencias():
    
    if request.method == 'POST':
        dni = request.form['dni']
        inasistencias = Asistencia.query.join(Estudiante, Asistencia.idestudiante == Estudiante.id).filter(
            Estudiante.dni == dni, Asistencia.asistio == 'n').all()

        if not inasistencias:
            error_mensaje = 'No se encontró al estudiante con el DNI ingresado'
            return render_template('message.html', message=error_mensaje, tipo="")

        return render_template('inasistencias.html', inasistencias=inasistencias)
    else:
        return render_template('consultar_inasistencias.html')

