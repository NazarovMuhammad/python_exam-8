from django.urls import path
from .views import About, Pagess,Contact

urlpatterns = [
    path("home", Pagess.as_view(), name="Page"),
    path("about",About.as_view(),name="About"),
    path("contact",Contact.as_view(),name="Contact"),
    ]