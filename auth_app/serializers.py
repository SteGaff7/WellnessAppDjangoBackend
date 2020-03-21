from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext as _


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        # username = validated_data.pop("username")
        # Set password will hash the password
        password = validated_data.pop('password', None)

        # Same as User(**validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        token = Token.objects.create(user=instance)

        return instance

    def validate_password(self, password):
        if len(password) < 8:
            # ValidationError("detail", "code")
            # raise ValidationError(_('Password is not long enough: %(value)s'), code='invalid', params={'value': '42'},)
            raise ValidationError(_('Password is not long enough'), code='invalid')

        if not any(char.isdigit() for char in password):
            raise ValidationError("Must contain at least one digit")

        if not any(char.isalpha() for char in password):
            raise ValidationError("Must contain at least one character")

        return password

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
