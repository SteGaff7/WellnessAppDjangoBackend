from rest_framework import serializers
from wellness_api.models import WellnessEntry


# Tidy up methods:
# https://stackoverflow.com/questions/45100515/what-is-the-different-between-save-create-and-update-in-django-rest-fram

class WellnessEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WellnessEntry
        # fields = '__all__'
        exclude = ['id', 'user']
        # Won't validate user field and then we can obtain in create method
        # read_only_fields = ['user']
        # Used validators in model so all are automatically generated

    def create(self, validated_data):
        """
        Create a WellnessEntry instance using the current request user passed throught
        context attribute
        """

        request = self.context.get("request")

        if request and hasattr(request, "user"):
            user = request.user
        else:
            raise serializers.ValidationError({"detail": "User not valid"})
        # Can use create or update or create, however update or create never reached as
        # validation unique constraints prevent it reaching this point, therefore PUT
        # method implemented instead
        instance, created = WellnessEntry.objects.update_or_create(user=user, **validated_data)

        return instance

    # No need to override as default behaviour seems sufficient
    # def update(self, instance, validated_data):
    #     """
    #     Add last changed field?
    #     """
    #     return instance


