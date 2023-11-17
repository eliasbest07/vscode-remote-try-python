#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

mapa = {
    'piedra': '֎',
    'tijera': '✂',
    'papel': '☐'
}

@app.route('/jugar/<eleccion>', methods=['GET'])
def jugar(eleccion):
    opciones = ['piedra', 'papel', 'tijera']
    resultado = random.choice(opciones)
    ganador = determinar_ganador(eleccion, resultado)
    return jsonify({'eleccion': mapa[eleccion], 'resultado': mapa[resultado], 'ganador': ganador})

def determinar_ganador(eleccion, resultado):
    if eleccion == resultado:
        return '🜲 Intenta de nuevo 🜲'
    if (eleccion == 'piedra' and resultado == 'tijera') or \
       (eleccion == 'tijera' and resultado == 'papel') or \
       (eleccion == 'papel' and resultado == 'piedra'):
        return 'Ganaste ✔'
    else:
        return 'Perdiste ✘'