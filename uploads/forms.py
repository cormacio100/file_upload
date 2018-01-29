from django import forms
from uploads.models import Upload

class FileUploadForm(forms.ModelForm):

    #   constructor
    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(FileUploadForm,self).__init__(*args,**kwargs)

    #   SAVE FUNCTION IS CREATED IF ANY LOGIC HOOKS NEED TO BE ADDED
    def save(self,commit=True):
        #   save(commit=False) prevents the form from auto saving
        #   The instance of the form is what gets saved
        instance = super(FileUploadForm,self).save(commit=False)

        #   auto set the user instance to that provided by the view
        #instance.title = self.title

        if commit:
            instance.save()
        return instance

    #   Tell Django which model to used to create the form
    class Meta:
        model = Upload
        fields = ('description','myfile','document')