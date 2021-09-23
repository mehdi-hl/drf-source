from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .permissions import IsAuthorOrReadOnly,IsStaffOrReadOnly , IsSuperUserOrStaffReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser , UserSerialiser


# Create your views here.
# class ArticleList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialiser

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerialiser
#     permission_classes =(IsStaffOrReadOnly,IsAuthorOrReadOnly)
class AticleViewSet(ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser
	filterset_fields=["status","author"]
	ordering_fields = ['publish', 'status']
	ordering=["-publish"]
	search_fields = ["title","content","author__username","author__last_name","author__first_name",]
	def get_permissions(self):
		if self.action in ['list','create']:
			permission_classes = [IsStaffOrReadOnly]
		else:
			permission_classes = [IsStaffOrReadOnly,IsAuthorOrReadOnly]
		return [permission() for permission in permission_classes]
# class UserList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerialiser
#     permission_classes = (IsSuperUserOrStaffReadOnly,)

# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerialiser
#     permission_classes = (IsSuperUserOrStaffReadOnly,)
class UseViewSet(ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerialiser
	permission_classes = (IsSuperUserOrStaffReadOnly,)
