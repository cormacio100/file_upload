from django import forms
from uploads.models import Upload

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
        #self.description =
        if _urls is not None:
            self.image = _urls[0]
            self.document = _urls[1]
        #self.kwargs = kwargs
        self.write_to_log('Initialising the FileUploadForm')
        self.display_kwargs(**kwargs)
        #super(FileUploadForm,self).__init__(uploaded_image_url,uploaded_document_url,*args,**kwargs)
        super(FileUploadForm, self).__init__(*args, **kwargs)


    def write_to_log(self,sentence):
        log.debug(sentence)
        item = 'print to log'
        print item

    def display_kwargs(self,**kwargs):
        print 'printing kwargs'
        for item in kwargs.items():
            print item
            log.debug(item)




    #   SAVE FUNCTION IS CREATED IF ANY LOGIC HOOKS NEED TO BE ADDED
    def save(self,commit=True):
        #   save(commit=False) prevents the form from auto saving
        #   The instance of the form is what gets saved
        instance = super(FileUploadForm,self).save(commit=False)

        #   auto set the user instance to that provided by the view
        instance.image = self.image
        instance.document = self.document


        if commit:
            instance.save()
        return instance





class DocumentImageForm(forms.ModelForm):
    #   Tell Django which model to used to create the form
    class Meta:
        model = Upload
        fields = ('description', 'image', 'document',)