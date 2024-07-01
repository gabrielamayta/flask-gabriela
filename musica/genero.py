from flask import Blueprint, render_template
from . import db
bp = Blueprint('genero', __name__,url_prefix='/genero' )


@bp.route('/')
def genero():
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("generos.html",generos=lista_de_resultado)

@bp.route('detalle'/'<int:id>')
def detGenero(id):
    base_de_datos = db.get_db()
    consulta = """
        SELECT name FROM genres
        WHERE GenreId = ?
    """
    consulta2 = """
        SELECT t.name as nombre, g.GenreId FROM genres g
        JOIN tracks t on t.GenreId =  t.GenreId = g.GenreId
        WHERE t.GenreId = ?
    """
    resultado = base_de_datos.execute(consulta1, (id,))
    lista_de_resultado = resultado.fetchone()
    resul_detalle = base_de_datos.execute(consulta2, (id,))
    lista_generos = resul_detalle.fetchall()
    return render_template("generos/detalle.html",generos=lista_de_resultado, detalle=lista_generos)
