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

import numpy as np

model = load_model('./savedModel/model.h5')

def predictor(request):
    if request.method == 'POST':
        age = float(request.POST['age'])
        sex = int(request.POST['sex'])
        a1 = int(request.POST['a1'])
        a2 = int(request.POST['a2'])
        a3 = int(request.POST['a3'])
        a4 = int(request.POST['a4'])
        a5 = int(request.POST['a5'])
        a6 = int(request.POST['a6'])
        a7 = int(request.POST['a7'])
        a8 = int(request.POST['a8'])
        a9 = int(request.POST['a9'])
        a10 = int(request.POST['a10'])
        jaundice = int(request.POST['jaundice'])
        asd_history = int(request.POST['asd_history'])
        test_completed_by = int(request.POST['test_completed_by'])

        # Prepare input data for prediction
        input_data = np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, age, sex, jaundice, asd_history, test_completed_by]])

        # Make prediction
        outcome_prob = model.predict(input_data)[0][0]
        outcome = np.round(outcome_prob).astype(int)

        print('The outcome is', outcome)

        if outcome <= 0:
            outcome = 'LOW RISK'
        else:
            outcome = 'HIGH RISK'

        # Assuming Result is your model output table
        user_outcome = Result.objects.create(age=age,
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
                                           test_completed_by=test_completed_by,
                                           outcome=outcome
                                           )
        user_outcome.save()

        return render(request, 'autismApp/result.html', {'result': outcome})
    return render(request, 'autismApp/survey.html')



def privacy_policy(request):
    return render(request, 'autismApp/privacy_policy.html')


def terms_of_use(request):
    return render(request, 'autismApp/terms_of_use.html')