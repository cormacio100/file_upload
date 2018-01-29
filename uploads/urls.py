from django.conf.urls import url
from . import views


# specific app URL pointable from template
app_name = 'uploads'

urlpatterns = [
    #   pages
    url(r'^upload_form/$', views.upload_form, name="upload_form"),
]