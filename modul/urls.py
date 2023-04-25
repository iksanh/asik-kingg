from django.urls import path
from modul import views as view


urlpatterns = [
    path('', view.index, name = 'dashboard'),
    path('portal', view.portal, name = 'portal')

]