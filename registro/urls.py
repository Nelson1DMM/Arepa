from django.urls import path, include
from registro.views import *

urlpatterns=[

    path("accounts/",include("django.contrib.auth.urls")),
    path("",Poratda,name="pagina_principal"),
    path("signup/",SignupView.as_view(),name="signup")

]
