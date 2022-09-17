#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jess Garriga

"""
    El siguiente código corre un servidor mediante la librería Flask. 
"""

from flask import *

app = Flask(__name__) #  importamos la clase Flask y el argumento 'name' 

@app.route('/') #  usamos el decorador para indicar a Flask la url a activar con nuestra función
def home():
   template_data = {
      'titulo' : 'Curso de Python de Ada ITW',
   }
   html = """
   <h1>Esta es mi segunda página web</h1>
   <h2>Página hecha por Jess Garriga. Nos guió Jere!</h2>
"""
   return html
   
   return render_template('home.html', **template_data)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
