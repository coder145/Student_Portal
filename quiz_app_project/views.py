from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm
from .models import MatricNumber
import re
# Create your views here.

def ConFirmPass(MatricNo,entry_pass):
    MatricCheck = re.compile("[0-9]{9}") 
    if MatricCheck.search(MatricNo):
        try:
            entry = MatricNumber.objects.get(matricnumber = MatricNo)
            db_password = entry.hashedpasword_set.all()[0]
            if db_password.password == entry_pass:
                return(None,'',True)
            else:
                return("p","Invalid Password ",False)
        except:
            return("m","matric number isn't registered",False)
    else:
        return ("m","Invalid Matric Number or the Matric Number isn't registerd",False)
    pass

def index(request):
    MatricError =""
    PasswordError = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            LoginMatricNumber = form.cleaned_data["Uname"]
            LoginPass_word = form.cleaned_data["Pass_word"]
            check = ConFirmPass(LoginMatricNumber,LoginPass_word)
            if check[2]:
                return HttpResponseRedirect(f"/project/{LoginMatricNumber}/")
            else:
                match check[0]:
                    case "m":
                        MatricError = check[1]
                    case "p":
                        PasswordError = check[1]


    else:
        form = LoginForm()

    return render(request,"START_PAGE/Login_page/lOGIN PAGE_1.html",{"MatricError":MatricError,"PasswordError":PasswordError})

def main_page(request,extra):
    return render(request,"quiz_app_project/main_page.html",{"data":extra})

def sign_up(request):

    
    return render(request,"START_PAGE/Sign_up/SIGN UP PROJECT PAGE_1.html",)



