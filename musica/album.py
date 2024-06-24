from flask import Blueprint, render_template
from . import db
bp = Blueprint('album.html', __name__,url_prefix='/album' )

@bp.route('/')
def albums():
    base_de_datos = db.get_db()
    consulta = """
        SELECT title, AlbumId FROM albums
        ORDER by title;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("album.html",albums=lista_de_resultado,)

@bp.route('<int:id>')
def detalle(id):
    base_de_datos = db.get_db()
    consulta1 = """
        SELECT title, AlbumId FROM albums
        WHERE AlbumId = ?
    """
    consulta2 = """
        SELECT t.name, t.TrackId FROM tracks t
        WHERE t.AlbumId = ?
    """
    resultado = base_de_datos.execute(consulta1,(id))
    albums = resultado.fetchone()
    resultado = base_de_datos.execute(consulta2(id))
    canciones = resultado.fetchall()
    pagina = render_template("detalle_album.html",
    albums = albums,
    canciones = canciones)
    return pagina
