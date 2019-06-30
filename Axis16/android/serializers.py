from rest_framework import serializers
from .models import AmishRegistrations, FeedBackFromAndroid, NotifsAndroid


class AmishSerializers(serializers.ModelSerializer):

    class Meta:
        model = AmishRegistrations
        fields = '__all__'


class FeedSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeedBackFromAndroid
        fields = '__all__'


class NotifsSerializers(serializers.ModelSerializer):

    class Meta:
        model = NotifsAndroid
        fields = '__all__'
