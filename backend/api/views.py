# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
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
	serializer_class = ArticleSerialiser

	def get_queryset(self):
		queryset = Article.objects.all()
		
		status = self.request.query_params.get('status')
		if status is not None:
			queryset = queryset.filter(status=status)
		
		author = self.request.query_params.get('author')
		if author is not None:
			queryset = queryset.filter(author__username=author)

		return queryset
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