from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from quotes import models


class QuotesReleatedApi(APIView):

    def get(self, request, format=None):
        all_quotes = models.Quotes.objects.all().values()
        return Response({"all quotes": all_quotes}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            models.Quotes.objects.create(
                quote=request.data["quote"], author=request.data["author"], genre=request.data["genre"])
        except Exception as e:
            return Response({"message": "There was some error while posting the data",
                             "status": status.HTTP_400_BAD_REQUEST, "Error Message": e})
        return Response({"message": "Blog created successfully"}, status=status.HTTP_201_CREATED)
