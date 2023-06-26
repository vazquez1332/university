from __main__ import app
from flask import render_template, request, redirect, url_for
from .models import Curso, Estudiante, Asistencia, db
from .login import obtener_preceptor_actual
from datetime import datetime

@app.route('/registrar_asistencia', methods=['GET', 'POST'])
def registrar_asistencia():

    preceptor_actual = obtener_preceptor_actual()

    if not preceptor_actual:
        return redirect(url_for('login'))

    curso_id = request.args.get('curso_id', None)

    if not curso_id:
        return redirect(url_for('home'))

    curso = Curso.query.filter_by(id=curso_id, idpreceptor=preceptor_actual.id).first()

    if not curso:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        clase = int(request.form['clase'])
        fecha = request.form['fecha']
        
        for estudiante in curso.estudiantes:
            asistencia = request.form.get(f'asistencia_{estudiante.id}') 
            justificacion = request.form.get(f'justificacion_{estudiante.id}', '')
            registro_asistencia = Asistencia(
                idestudiante=estudiante.id,
                fecha=datetime.strptime(fecha, "%Y-%m-%d").date(),
                codigoclase=clase,
                asistio=asistencia,
                justificacion=justificacion if asistencia == 'n' else ''
            )

            db.session.add(registro_asistencia)
        db.session.commit()
        return render_template("message.html", message="Asistencia registrada con exito", tipo="")

    estudiantes = Estudiante.query.filter_by(idcurso=curso_id).order_by(Estudiante.nombre, Estudiante.apellido).all()

    return render_template('registrar_asistencia.html', curso=curso, estudiantes=estudiantes)

