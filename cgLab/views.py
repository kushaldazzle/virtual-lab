from django.shortcuts import render
from .models import CgLabQuizes

# Create your views here.
def listofexperiment(request):
    return render(request,'cgLab/labHome.html',)

def experiment1(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment1")
    data ={'Exams': result}
    return render(request,'cgLab/exp1.html', context=data)

def experiment2(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment2")
    data ={'Exams': result}
    return render(request,'cgLab/exp2.html' , data)

def experiment3(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment3")
    data ={'Exams': result}
    return render(request,'cgLab/exp3.html' , data)

def experiment4(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment4")
    data ={'Exams': result}
    return render(request,'cgLab/exp4.html' , data)

def experiment5(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment5")
    data ={'Exams': result}
    return render(request,'cgLab/exp5.html' , data)

def experiment6(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment6")
    data ={'Exams': result}
    return render(request,'cgLab/exp6.html' , data)

def experiment7(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment7")
    data ={'Exams': result}
    return render(request,'cgLab/exp7.html' , data)

def experiment8(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment8")
    data ={'Exams': result}
    return render(request,'cgLab/exp8.html' , data)

def experiment9(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment9")
    data ={'Exams': result}
    return render(request,'cgLab/exp9.html' , data)

def experiment10(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment10")
    data ={'Exams': result}
    return render(request,'cgLab/exp10.html' , data)

def experiment11(request):
    result = CgLabQuizes.objects.filter(experimentNO = "experiment11")
    data ={'Exams': result}
    return render(request,'cgLab/exp11.html' , data)


