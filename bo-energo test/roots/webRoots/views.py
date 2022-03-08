from cmath import nan, sqrt
from django.shortcuts import render
from enum import Enum
class Case(Enum):
    x_no = 0
    x1 = 2
    x2 = 3
    x_err = 4

def calc(a,b,c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        (None,None,Case.x_err)
    D = b**2 - 4 * a * c
    if D < -0.001:
        return (None,None,Case.x_no)
    elif D > 0.001:
        x1 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
        x1 = x1.real
        x2 = x2.real
        return (x1,x2,Case.x2)
    else:
        return ((-b / (2*a)).real,None,Case.x1)

# Create your views here.
def index(request):
    if request.method =='GET':
        try:
            a = request.GET.get("a", nan)
            b = request.GET.get("b", nan)
            c = request.GET.get("c", nan)
        except:
            data = {'x1':None,'x2':None,'case':Case.x_err}
            return render(request,"home.html", data)
        try:
            x1,x2,case = calc(a,b,c)
            data = {'x1':x1,'x2':x2,'case':case}
            return render(request,"home.html",data)
        except:
            data = {'x1':None,'x2':None,'case':Case.x_err}
            return render(request,"home.html", data)
    elif request.method =='POST':
        pass