
from flask import Blueprint, render_template
from . import db
bp = Blueprint('artista', __name__,url_prefix='/artista' )


@bp.route('/')
def artistas():
    base_de_datos = db.get_db()
    consulta = """
    
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("artista.html",generos=lista_de_resultado)



@bp.route('/new', methods =('GET', 'POST'))
def nuevo():
   if request.method == 'POST':
       name = request.form['name']
       con = db.get_db()
       consulta = """
               INSERT INTO artists(name)
               VALUES(?)
           """
       con.execute(consulta, (name,))
       con.commit()
       return redirect(url_for('artista.artista'))
   else:
       pagina = render_template('nuevo_artista.html',)
       return pagina
