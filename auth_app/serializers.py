from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        # username = validated_data.pop("username")
        # Set password will hash the password
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        token = Token.objects.create(user=instance)

        return instance



    # https://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed
    # def update(self, instance, validated_data):
    #     for attr, value in validated_data.items():
    #         if attr == 'password':
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, attr, value)
    #     instance.save()
    #     return instance

    # Validate fields
    # And add custom exceptions:
    # https://stackoverflow.com/questions/33475334/django-rest-framework-how-to-specify-error-code-when-raising-validation-error-in
