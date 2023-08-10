
from django.urls import path
from app_cad_clientes import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #rota(endpoint/views responsável, nome de referência)
    path('',views.home, name='home'), #string vazia, pois será pagina inicial 
    
    path('clientes/', views.clientes, name='listagem_clientes')
]
