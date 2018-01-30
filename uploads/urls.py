from django.conf.urls import url
from . import views


# specific app URL pointable from template
app_name = 'uploads'

urlpatterns = [
    #   pages
    url(r'^upload_form/$', views.upload_form, name="upload_form"),
    url(r'^model_form_upload/$', views.model_form_upload, name="model_form_upload"),
    #url(r'^listing/$', views.listing, name="listing"),
]