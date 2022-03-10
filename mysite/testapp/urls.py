from django.urls import path
from .views import test, get_rubric

urlpatterns = [
    path("", test, name="test"),
    path("rublic/<int:pk>", get_rubric, name="rubric"),
]
