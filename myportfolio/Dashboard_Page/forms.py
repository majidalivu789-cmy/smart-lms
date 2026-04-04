from django import forms
from .models import Student
# ===========Student Form=========
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name':forms.TextInput(attrs = {
                'placeholder':'Full Name',
                'class':'name-input',
            }),
            'gender':forms.RadioSelect(),
            'date_of_birth':forms.DateInput(attrs = {'type':'date'}),

            'cnic':forms.TextInput(attrs={
                'placeholder':'00000-0000000-0',
                'maxlength':'15',
            }),
            'country':forms.Select(),
            
            'province':forms.Select(attrs = {
                'id':'id_province',
                'onchange':'loadDistricts()',
            }),
            'district':forms.Select(attrs = {
                'id':'id_districts',
            }),
            'address':forms.Textarea(attrs = {'placeholder':'Enter Your Permanent Address'}),
            'phone_code':forms.Select(),
            'phone':forms.TextInput(),
            'education':forms.Select(),
        }
        lables = {
            
        }
    
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Fields jahan placeholder chahiye
        FIX_FIELDS = ['gender','province', 'education', 'phone_code', 'country']  # exclude gender

        for field in FIX_FIELDS:
            choices = list(self.fields[field].choices)

        # Django ka empty choice hatao
            if choices and choices[0][0] == '':
             choices.pop(0)

        # Apna placeholder add karo
            self.fields[field].choices = [
            ('', f'Select {field.replace("_"," ").title()}')
        ] + choices
            
    

        if 'gender' in self.fields:
            choices = list(self.fields['gender'].choices)

        # Agar first choice empty hai to remove karo
            if choices and choices[0][0] == '':
                choices.pop(0)

                self.fields['gender'].choices = choices
