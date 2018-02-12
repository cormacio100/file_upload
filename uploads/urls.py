from django.conf.urls import url
from . import views


# specific app URL pointable from template
app_name = 'uploads'

urlpatterns = [
    url(r'^model_form_upload/$', views.model_form_upload, name="model_form_upload"),
]
