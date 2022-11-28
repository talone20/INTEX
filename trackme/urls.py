from django.urls import path
from .views import indexPageView
from .views import myDataPageView


urlpatterns = [
    path("", indexPageView, name="trackme"),
    path("mydata/", myDataPageView, name="mydata"),



]
