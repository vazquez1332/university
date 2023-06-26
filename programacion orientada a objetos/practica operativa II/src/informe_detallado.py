from __main__ import app
from flask import render_template, request, redirect, url_for
from .models import Estudiante, Asistencia
from .login import obtener_preceptor_actual

@app.route('/informe_detallado', methods=['GET'])
def informe_detallado():

    preceptor_actual = obtener_preceptor_actual()

    if not preceptor_actual:
        return redirect(url_for('login'))

    curso_id = request.args.get('curso_id', None)

    if not curso_id:
        return render_template('home.html')
    
    estudiantes = Estudiante.query.filter_by(idcurso=curso_id).order_by(Estudiante.nombre, Estudiante.apellido).all()
    informe = []
    
    for estudiante in estudiantes:
        asistencias = Asistencia.query.filter_by(idestudiante=estudiante.id).all()

        aula_presente = aula_ausente_justificada = aula_ausente_injustificada = 0
        edu_fisica_presente = edu_fisica_ausente_justificada = edu_fisica_ausente_injustificada = 0

        for asistencia in asistencias:
            if asistencia.codigoclase == 1:
                if asistencia.asistio == 's':
                    aula_presente += 1
                elif asistencia.asistio == 'n':
                    if asistencia.justificacion:
                        aula_ausente_justificada += 1
                    else:
                        aula_ausente_injustificada += 1
                        
            elif asistencia.codigoclase == 2:
                if asistencia.asistio == 's':
                    edu_fisica_presente += 1
                elif asistencia.asistio == 'n':
                    if asistencia.justificacion:
                        edu_fisica_ausente_justificada += 1
                    else:
                        edu_fisica_ausente_injustificada += 1

        total_inasistencias = aula_ausente_injustificada + aula_ausente_justificada + (
            edu_fisica_ausente_injustificada + edu_fisica_ausente_justificada) / 2
        
        informe.append({
            'estudiante': estudiante,
            'aula_presente': aula_presente,
            'aula_ausente_justificada': aula_ausente_justificada,
            'aula_ausente_injustificada': aula_ausente_injustificada,
            'edu_fisica_presente': edu_fisica_presente,
            'edu_fisica_ausente_justificada': edu_fisica_ausente_justificada,
            'edu_fisica_ausente_injustificada': edu_fisica_ausente_injustificada,
            'total_inasistencias': total_inasistencias
        })

    return render_template('informe_detallado.html', informe=informe)
