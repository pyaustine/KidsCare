from django.shortcuts import render
from . models import Result

# third party imports

from tensorflow.keras.models import load_model

# Create your views here.

# def home(request):
#     return render(request, 'autismApp/index.html')

def home(request):
    return render(request, 'autismApp/main.html')

def welcome(request):
    return render(request, 'autismApp/welcome.html')

def survey(request):
    return render(request, 'autismApp/survey.html')


model = load_model('./savedModel/model.h5')


def predictor(request):
    if request.method == 'POST':
        age = request.POST['age']
        sex = request.POST['sex']
        a1 = request.POST['a1']
        a2 = request.POST['a2']
        a3 = request.POST['a3']
        a4 = request.POST['a4']
        a5 = request.POST['a5']
        a6 = request.POST['a6']
        a7 = request.POST['a7']
        a8 = request.POST['a8']
        a9 = request.POST['a9']
        a10 = request.POST['a10']
        jaundice = request.POST['jaundice']
        asd_history = request.POST['asd_history']
        completed_by = request.POST['completed_by']
        
        outcome = model.predict([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, age, sex, jaundice, asd_history, completed_by]])

        if outcome <= 0.5:
            outcome = 'LOW RISK'

        elif outcome > 0.5 or outcome <= 0.75:
            outcome = 'MODERATE'

        else:
            outcome = 'HIGH RISK'

        userresult = Result.objects.create(age=age,
                                           sex=sex,
                                           a1=a1,
                                           a2=a2,
                                           a3=a3,
                                           a4=a4,
                                           a5=a5,
                                           a6=a6,
                                           a7=a7,
                                           a8=a8,
                                           a9=a9,
                                           a10=a10,
                                           jaundice=jaundice,
                                           asd_history=asd_history,
                                           completed_by=completed_by,
                                           outcome=outcome
                                           )
        userresult.save()

        return render(request, 'autismApp/result.html', {'result': outcome})
    return render(request, 'autismApp/survey.html')


def privacy_policy(request):
    return render(request, 'autismApp/privacy_policy.html')


def terms_of_use(request):
    return render(request, 'autismApp/terms_of_use.html')