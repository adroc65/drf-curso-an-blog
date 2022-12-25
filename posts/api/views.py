from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response

# Agregar sistema de permisos para cada modelo:
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.api.serializers import PostSerializer

# Leer permisos personalizados:
from posts.api.permissions import IsAdminOrReadOnly


# Create your views here.
"""
Usando ModelViewSet:
De esta forma solo se indica el Serializador, tal como se muestra
y se indica cuales son los datos que se muestran o se piden.
"""


class PostModelViewSet(ModelViewSet):
    # Se agrega sistema de permisos:
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


"""Usando VIEWSETS"""
""" class PostViewSet(ViewSet):
    def list(self, request):
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=posts.data)

    def retrieve(self, request, pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

    def create(self, request):
        post = PostSerializer(data=request.POST)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(status=status.HTTP_201_CREATED, data=post.data) """


"""Usando APIViews"""

"""
class PostApiView(APIView):
    def get(self, request):
        # posts = Post.objects.all()
        # posts = [post.title for post in Post.objects.all()]
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=posts.data)

    def post(self, request):
        post = PostSerializer(data=request.POST)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(status=status.HTTP_201_CREATED, data=post.data)
"""

"""
    # Sin usar Serializador
    Post.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        order=request.POST['order'],
    )
    return self.get(request)
"""
