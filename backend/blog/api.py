from turtle import title
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from blog import models


class BlogReleatedApi(APIView):

    def get(self, request, format=None):
        all_blogs = models.Blog.objects.all().values()
        return Response({"all_blogs": all_blogs}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            models.Blog.objects.create(
                title=request.data["title"], content=request.data["content"])
        except Exception as e:
            return Response({"message": "There was some error while posting the data",
                             "status": status.HTTP_400_BAD_REQUEST, "Error Message": e})
        return Response({"message": "Blog created successfully"}, status=status.HTTP_201_CREATED)
