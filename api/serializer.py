from autismApp import models
from rest_framework import serializers

# input serializer
class PredictionInputSerializer(serializers.Serializer):
    age =  serializers.FloatField()
    sex = serializers.IntegerField()
    a1 = serializers.IntegerField()
    a2 = serializers.IntegerField()
    a3 = serializers.IntegerField()
    a4 = serializers.IntegerField()
    a5 = serializers.IntegerField()
    a6 = serializers.IntegerField()
    a7 = serializers.IntegerField()
    a8 = serializers.IntegerField()
    a9 = serializers.IntegerField()
    a10 = serializers.IntegerField()
    jaundice = serializers.IntegerField()
    asd_history = serializers.IntegerField()
    test_completed_by = serializers.IntegerField()


# output serializer
