from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from e_librotek_app.serializers import UserSerializer


class UserRegisterView(views.APIView):

    def post(self, request, *args, **kwargs):
        res = {
            "status": "Success",
            "message": "The User was successfully registered!",
            "code": 201
        }
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            tokenData = {
                "username": request.data['username'],
                "password": request.data['password']
            }
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(res, status=status.HTTP_201_CREATED)
        except Exception as e:
            res = {
                "status": "Error",
                "message": "There is an error with the request",
                "code": 500,
                "errors": e.args
            }
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
