from django import forms

class LoginForm(forms.Form):
    Uname = forms.CharField(label = "Uname",max_length=20)
    Pass_word = forms.CharField(label="Pass_word", max_length=100)
    Remember = forms.BooleanField(label = "check", required=False)


class SignUp(forms.Form):
    FirstName = forms.CharField(label = 'Fname', max_length = 20)
    LastName = forms.CharField(label = 'Lname', max_length = 20 )
    Pass_Word = forms.CharField(label = "pass_word", max_length=64)
    CPass_Word = forms.CharField(label= "cPass_Word",max_length= 64)
    School_mail = forms.CharField(label= "SE", max_length=64)
    Matric_num = forms.IntegerField(label="MatricNum")
    level = forms.IntegerField(label= "level" )
    Department = int()
    
    pass
