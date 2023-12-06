from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api.serializers import PredictionInputSerializer, PredictionOutputSerializer



from autismApp.models import Result
import numpy as np
from tensorflow.keras.models import load_model



# Create your views here.
def testEndpoint(request):
    data = {
        'id' : 12,
        'name' : 'Austine',
        'account_number' : 987194712 
    }

    return render(request, 'api/test.html', {'data': data})

@api_view(['GET'])
def getRoutes(request):
    routes = [
        # get all routes
        'GET/api',

        # predict
        'POST/api/predict',

    ]
    return Response(routes)



class predictAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # deserialize input data
        serializer = PredictionInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #extract data
        input_data = np.array([[serializer.validated_data['age'],
                                serializer.validated_data['sex'],
                                serializer.validated_data['a1'],
                                serializer.validated_data['a2'],
                                serializer.validated_data['a3'],
                                serializer.validated_data['a4'],
                                serializer.validated_data['a5'],
                                serializer.validated_data['a6'],
                                serializer.validated_data['a7'],
                                serializer.validated_data['a8'],
                                serializer.validated_data['a9'],
                                serializer.validated_data['a10'],
                                serializer.validated_data['jaundice'],
                                serializer.validated_data['asd_history'],
                                serializer.validated_data['test_completed_by'],
                                ]])
                
        # load model
        model = load_model('./savedModel/ann_model.h5')

        # make prediction
        outcome_prob = model.predict(input_data)[0][0]
        outcome = 'LOW RISK' if outcome_prob <= 0 else 'HIGH RISK'

        # save to db
        Result.objects.create(**serializer.validated_data, outcome=outcome)

        # serializer
        output_serializer = PredictionOutputSerializer({'result': outcome})
        return Response(output_serializer.data, status=status.HTTP_200_OK)