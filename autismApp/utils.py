from django.shortcuts import render
from .models import Result
import numpy as np
import time
from sklearn.externals import joblib  # For loading SVM and RF models

# third party imports
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

# Load SVM and RF models
svm_model = joblib.load('./savedModel/svm_model.pkl')  # Replace with the actual path to your SVM model file
rf_model = joblib.load('./savedModel/rf_model.pkl')    # Replace with the actual path to your RF model file

# Load ANN model
ann_model = load_model('./savedModel/ann_model.h5')

# Create your views here.
def home(request):
    return render(request, 'autismApp/main.html')

def welcome(request):
    return render(request, 'autismApp/welcome.html')

def survey(request):
    return render(request, 'autismApp/survey.html')

def predictor(request):
    if request.method == 'POST':
        age = float(request.POST['age'])
        sex = int(request.POST['sex'])
        a1 = int(request.POST['a1'])
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

        # Make predictions with all three models
        start_time = time.time()
        ann_outcome_prob = ann_model.predict(input_data)[0][0]
        ann_outcome = np.round(ann_outcome_prob).astype(int)
        ann_time = time.time() - start_time

        start_time = time.time()
        svm_outcome = svm_model.predict(input_data)[0]
        svm_time = time.time() - start_time

        start_time = time.time()
        rf_outcome = rf_model.predict(input_data)[0]
        rf_time = time.time() - start_time

        # Compare model performance based on accuracy and performance time
        outcomes = {'ANN': ann_outcome, 'SVM': svm_outcome, 'RF': rf_outcome}
        times = {'ANN': ann_time, 'SVM': svm_time, 'RF': rf_time}

        best_model = max(outcomes, key=outcomes.get)

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
                                            outcome=outcomes[best_model])
        user_outcome.save()

        return render(request, 'autismApp/result.html', {'result': outcomes[best_model], 'model': best_model})
    return render(request, 'autismApp/survey.html')

def privacy_policy(request):
    return render(request, 'autismApp/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'autismApp/terms_of_use.html')
