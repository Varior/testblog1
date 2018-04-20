from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostSerializer
from blog.models import Post
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.save()
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   