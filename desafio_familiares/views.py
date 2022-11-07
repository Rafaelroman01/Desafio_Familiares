from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def vista_saludo(request):
    return HttpResponse("""
    <h1>Hola coders! :) </h1>
    <p style='color:red' >Esto es una prueba</p>
    """)

def vista_listado_familiares(request):
    listado_familiares = ["Leonel Gareis", "Agustin Russo", "Cristian Garcia", "Angelo Pettinari", "Diego Ibarra", "Santiago Ortiz", "Barbara Vivante",  "Barbara Pino"]
    datos = {"tecnologia": "Familiares", "listado_familiares": listado_familiares}
    
    plantilla= loader.get_template("listado_familiares.html")
    
    documento = plantilla.render(datos)
    return HttpResponse(documento)

