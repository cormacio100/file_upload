from django import forms
from uploads.models import Upload
import os

##########################################
#   LOGGING
##########################################
import logging
log = logging.getLogger(__name__)

class FileUploadForm(forms.ModelForm):

    image = ''
    document = ''

    #   Tell Django which model items to used to create the form
    class Meta:
        model = Upload
        fields = ('description','image','document',)

    #   constructor
    #def __init__(self,uploaded_image_url='',uploaded_document_url='',*args,**kwargs):
    def __init__(self,user,*args,**kwargs):
        _urls = kwargs.pop('_urls',None)
        self.user = user
        #   retrieve the urls of the image and document
        if _urls is not None:
            self.image = _urls[0]
            self.document = _urls[1]
        super(FileUploadForm, self).__init__(*args, **kwargs)


    #   SAVE FUNCTION IS CREATED IF ANY LOGIC HOOKS NEED TO BE ADDED
    def save(self,commit=True):
        #   save(commit=False) prevents the form from auto saving
        #   The instance of the form is what gets saved
        instance = super(FileUploadForm,self).save(commit=False)

        #   auto set the user instance to that provided by the view
        instance.image = self.image
        instance.document = self.document
        #instance.image = self.add_folder_ext(self.image,'image')
        #instance.document = self.add_folder_ext(self.document,'document')

        if commit:
            instance.save()
        return instance

    """
    def add_folder_ext(self,url,type):
        if 'image' == type:
            upload_dir = os.path.join('images/', url)
        elif 'document' == type:
            upload_dir = os.path.join('images/', url)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        return os.path.join(upload_dir, url)
    """


class DocumentImageForm(forms.ModelForm):
    #   Tell Django which model to used to create the form
    class Meta:
        model = Upload
        fields = ('description', 'image', 'document',)