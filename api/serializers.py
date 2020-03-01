from rest_framework import serializers
from api.models import WellnessEntry

class WellnessEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WellnessEntry
        fields = ['user', 'date', 'sleep_score', 'energy_score', 'soreness_score',
        'mood_score', 'stress_score', 'total_score']
        # Can add read only fields and change number of fields to be used
