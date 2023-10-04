from django.urls import path
from appweb.views import *
from .views import *


urlpatterns = [
    path('busqueda/<nombre>/<codigo>', busqueda),
    path('', inicio, name='inicio'),
    path('contacto/', contacto, name='contacto'),
    path('portafolio/', portafolio, name='portafolio'),
    path('quehacemos/', quehacemos, name='quehacemos'),
    path('quienessomos/', quienessomos, name='quienessomos'),
    path('contacto_exitoso/', contacto_exitoso, name='contacto_exitoso'),
    path('quehacemos/contacto.html', contacto, name='contacto_html'),

]
