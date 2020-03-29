# from rest_framework import serializers
# from api.models import WellnessEntry, TestOwner
# from django.contrib.auth.models import User
#
# # Serializing is turning a model instance into python natives then followed by json.
# # Deserializing is turning json into instance models
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         write_only_fields = ('password',)
#
#
# class WellnessEntrySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WellnessEntry
#         fields = ['user', 'date', 'sleep_score', 'energy_score', 'soreness_score',
#                   'mood_score', 'stress_score', 'total_score', 'comments']
#         # Can add read only fields and change number of fields to be used
#
#
# class TestOwnerSerializer(serializers.ModelSerializer):
#
#     # owner = UserSerializer()
#
#     class Meta:
#         model = TestOwner
#         fields = ['owner', 'text']
