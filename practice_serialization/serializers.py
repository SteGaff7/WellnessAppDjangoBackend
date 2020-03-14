from django.contrib.auth.models import User
from rest_framework import serializers
from practice_serialization.models import Comment, SimpleObj, ObjCreatedByUser

from datetime import datetime


class ObjCreatedByUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjCreatedByUser
        # If only writing then use this
        # fields = ['text', 'created']
        # read_only_fields = ['created']

        fields = ['user', 'text', 'created']
        # Won't check at validation
        read_only_fields = ['user', 'created']

    def create(self, validated_data):
        # Can accept user object or string and search for object
        username = validated_data.pop("username")
        user = User.objects.get(username=username)
        obj = ObjCreatedByUser.objects.create(user=user, **validated_data)
        return obj


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.created = datetime.now()
        instance.save()
        return instance


class SimpleObjSerializer(serializers.ModelSerializer):
    comment = CommentSerializer()

    class Meta:
        model = SimpleObj
        fields = ['my_id', 'text', 'another_field', 'comment']

    #     fields = '__all__'
    #     read_only_fields = ['account_name']

    def create(self, validated_data):
        # Create a comment object to pass to simple_obj create function
        comment_data = validated_data.pop("comment")
        comment = Comment.objects.create(**comment_data)
        simple_obj = SimpleObj.objects.create(comment=comment, **validated_data)

        return simple_obj

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.another_field = validated_data.get('another_field', instance.another_field)
        instance.save()
        return instance

    # Customize validation per field
    # def validate_text(self, value):
    #     if "text" not in value.lower():
    #         raise serializers.ValidationError("text not found in text field")
    #     return value

    # def validate(self, data):
    # Can do validation with multiple fields

    # Can include validators in meta data or field level for reusability
