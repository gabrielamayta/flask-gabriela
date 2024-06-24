from flask import Blueprint, render_template
from . import db
bp = Blueprint('genero', __name__,url_prefix='/genero' )


@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero/generos.html",generos=lista_de_resultado)

@bp.route('<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    consulta2 = """
        SELECT g.name, t.name FROM genres g 
        JOIN tracks t on t.GenreId =  t.GenreId = g.GenreId
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchone()
    resul_detalle = base_de_datos.execute(consulta2)
    lista_generos = resul_detalle.fetchall()
    return render_template("genero.html",generos=lista_de_resultado, 
                           detalle=lista_generos)
