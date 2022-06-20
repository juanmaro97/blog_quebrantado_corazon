from flask import Flask, render_template, request, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

# YOUTUBE VIDEO: https://www.youtube.com/watch?v=-1DmVCPB6H8&list=LL&index=17

app = Flask(__name__)       # un objeto tipo flask que recibe un nombre


@app.route('/')         # ruta raíz de la app
def index():            # una vista llamada index que está en la raíz de la app, un def es una vista
    return render_template('index.html')

@app.route('/post/<post_name>')         # ruta raíz de la app
def post_views(post_name):            # una vista llamada index que está en la raíz de la app, un def es una vista
    return render_template('/posts/'+str(post_name)+'.html')

@app.route('/about_us')         # ruta raíz de la app
def about_view():            # una vista llamada index que está en la raíz de la app, un def es una vista
    return render_template('/about.html')



def query_string():  # recuperar parámetros desde la request en URLS dinamicas

    print(request)
    print(request.args)
    print(request.args.get('param1'))
    return "OK"


def pagina_no_encontrada(error):   # vista para error 404
    return render_template('404.html'), 404    # renderiza html de 404
    # return redirect(url_for('index'))        # redirecciona a la página principal de index

if __name__=='__main__':
    app.add_url_rule('/query_string',view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada) # asociar la vista de 404 al error 404
    app.run(debug=True,port=5021)