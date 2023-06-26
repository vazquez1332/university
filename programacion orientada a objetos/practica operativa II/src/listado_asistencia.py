from __main__ import app
from flask import render_template, request
from .models import Estudiante, Asistencia
from datetime import datetime

def obtener_listado_asistencia(curso_id, fecha, codigoclase):
    fecha_date = datetime.strptime(fecha, "%Y-%m-%d").date()
    estudiantes = Estudiante.query.filter_by(idcurso=curso_id).all()
    lista_asistencia = []

    for estudiante in estudiantes:
        asistencia = Asistencia.query.filter_by(idestudiante=estudiante.id, fecha=fecha_date, codigoclase=codigoclase).first()
        
        lista_asistencia.append({
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'asistio': asistencia.asistio if asistencia else ''
        })

    lista_asistencia.sort(key=lambda l: (l['apellido'], l['nombre']))
    
    return lista_asistencia


@app.route('/listado_asistencia_form', methods=['GET', 'POST'])
def listado_asistencia_form():

    curso_id = request.args.get('curso_id')
    
    if request.method == 'POST':
        fecha = request.form['fecha']
        codigoclase = request.form['codigoclase']

        lista_asistencia = obtener_listado_asistencia(curso_id, fecha, codigoclase)
        
        return render_template('listado_asistencia.html', lista_asistencia=lista_asistencia, curso_id=curso_id)
    
    return render_template('listado_asistencia_form.html', curso_id=curso_id)
