from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from e_librotek_app.serializers import BookSerializer


class BookRegisterView(views.APIView):

    def post(self, request, *args, **kwargs):
        res = {
            "status": "Success",
            "message": "The Book was successfully registered!",
            "code": 201
        }
        try:
            serializer = BookSerializer(data=request.data["book"])
            serializer.is_valid(raise_exception=True)
            serializer.save()
            '''
            tokenData = {
                "username": request.data['username'],
                "password": request.data['password']
            }
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            '''
        except Exception as e:
            res = {
                "status": "Error",
                "message": "There is an error with the request",
                "code": 500,
                "error": " ".join(str(e.args))
            }

        return Response(res, status=status.HTTP_201_CREATED)
