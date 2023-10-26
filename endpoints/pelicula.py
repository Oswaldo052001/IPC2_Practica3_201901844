from flask import Blueprint, jsonify, request
from Pelicula.Lista_simple import ListaSimple
from operacion import operaciones
import pymongo

listaPeliculas = ListaSimple()  #Esta lista servira como mi base de datos
pelicula_service = Blueprint(name="pelicula_service", import_name=__name__)

##-------------------------------------------------------REGISTRAR LIBRO-------------------------------------------------

@pelicula_service.route('/new-movie', methods=['POST'])
def RegistrarPelicula():
    if request.method == "POST":
        data = request.get_json()
        if "movieId" in data and "name" in data and "genre" in data:
            if data["movieId"] != "" and  data['name'] != "" and  data['genre'] != "":
                nombre = data['name']
                genero = data['genre']
                id = data['movieId']
                
                genero = genero.lower()
                try:
                    opera = operaciones(listaPeliculas)
                    mensaje = opera.InsertarPelicula(id,nombre,genero)

                    return jsonify({"id": id, "pelicula": nombre, "genero": genero, "mensaje": mensaje})
                
                except Exception as e:
                    return jsonify({
                        "estado": "-3",
                        "mensaje": e
                    }),201
            else:
                return jsonify({
                    "estado": "-1",
                    "mensaje": "Hay campos vaciós, verifica"
                }),201
        else:
            return jsonify({
                "estado": "-1",
                "mensaje": "Campos faltantes"
            }),201
    else:
        return jsonify({
                "estado": "-1",
                "mensaje": "Service Unavailable"
            }),201

##-------------------------------------------------------OBTENER LIBROS-------------------------------------------------


@pelicula_service.route('/all-movies', methods=['GET'])
def ObtenerPeliculas():
    if request.method == "GET":
        pelicula = listaPeliculas.getInicio()
        try:
            peliculas = []
            while pelicula:
                peliculas.append(
                    {
                        "movieId": pelicula.getDato().getID(),
                        "name": pelicula.getDato().getName(),
                        "genre": pelicula.getDato().getGenero()
                    }
                )
                pelicula = pelicula.getSiguiente()
            return jsonify({
                "Peliculas": peliculas
            }),200
        except Exception as e:
            return jsonify({
                "estado": "-3",
                "mensaje": e
            }),201
    else:
        return jsonify({
                "estado": "-1",
                 "mensaje": "Service Unavailable"
            }),201


##-------------------------------------------------------BUSCAR LIBRO --------------------------------------------------


@pelicula_service.route('/all-movies-by-genre/<tipogenero>', methods=['POST','GET','PUT'])
def BuscarPeliculaGenero(tipogenero):
    if request.method == "GET":
        genero = tipogenero
        genero = genero.lower()
        
        try:
            peliculasgenero = []
            pelicula = listaPeliculas.getInicio()
            while pelicula:
                if pelicula.getDato().getGenero() == genero:
                    peliculasgenero.append(
                        {
                            "movieId": pelicula.getDato().getID(),
                            "name": pelicula.getDato().getName(),
                            "genre": pelicula.getDato().getGenero()
                        }
                    )
                pelicula = pelicula.getSiguiente()
            texto = "Peliculas de",genero
            if len(peliculasgenero) > 0:
                return jsonify({
                    "Peliculas": peliculasgenero
                }),200
            else:
                return jsonify({
                        "estado": "-1",
                        "mensaje": "Genero no encontrado"
                    }),201
            
        except:
            return jsonify({
                    "estado": "-1",
                    "mensaje": "Error"
                }),201

    else:
        return jsonify({
                "estado": "-1",
                 "mensaje": "Service Unavailable"
            }),201

##-------------------------------------------------------ACTUALIZAR LIBRO -------------------------------------------------

@pelicula_service.route('/update-movie', methods=['POST','GET','PUT'])
def ActualizarPelicula():
    if request.method == "PUT":
        data = request.get_json()
        if "movieId" in data and "name" in data and "genre" in data:
            if data["movieId"] != "" and  data['name'] != "" and  data['genre'] != "":
                nombre = data['name']
                genero = data['genre']
                id = data['movieId']

                genero = genero.lower()
                try:
                    opera = operaciones(listaPeliculas)
                    mensaje = opera.ActualizarPelicula(id,nombre,genero)
                    return jsonify({"id": id, "pelicula": nombre, "genero": genero, "mensaje": mensaje})
                
                except :
                    return jsonify({
                        "estado": "-3",
                        "mensaje": "Error en los campos, vuelva a intentarlo"
                    }),201
            else:
                return jsonify({
                    "estado": "-1",
                    "mensaje": "Hay campos vaciós, verifica"
                }),201
        else:
            return jsonify({
                "estado": "-1",
                "mensaje": "Campos faltantes"
            }),201
    else:
        return jsonify({
                "estado": "-1",
                 "mensaje": "Service Unavailable"
            }),201
