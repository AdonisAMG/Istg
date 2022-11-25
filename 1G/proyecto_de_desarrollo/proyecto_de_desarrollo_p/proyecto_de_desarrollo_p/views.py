from django.http import HttpResponse
import datetime

def saludo(request):

    p1=Persona(" Profesor Manuel", "Díaz")

    temasdelcurso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/Familia Merchan/PycharmProjects/proyecto_de_desarrollo/proyecto_de_desarrollo_p/plantillas/miplantilla.html)

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora "temas":temasdelcurso})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    documento="<html><body><h1>hasta luego, chicos</h1></body></html>"
    return HttpResponse(documento)

#tambien puede ir
#"""<html>
#<body>
#<h1>
#el print sin print. xD
#</h1>
#</body>
#</html>"""
def damefecha(request):

    fecha_actual=datetime.datetime.now()
    documento=
    """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

