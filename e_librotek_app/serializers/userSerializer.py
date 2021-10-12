from rest_framework import serializers
from e_librotek_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name',
                  'lastname', 'password', 'signUp', 'lastLogin']

    def to_representation(self, obj):
        user = User.objects.get(username=obj.username)
        return{
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "lastname": user.lastname,
            "password": user.password,
            "signUp": user.signUp,
            "lastLogin": user.lastLogin
        }
