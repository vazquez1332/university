from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py")

import src.models
import src.login
import src.registrar_asistencia
import src.informe_detallado
import src.listado_asistencia
import src.consultar_inasistencias

if __name__ == "__main__":
    app.run(debug=True)
