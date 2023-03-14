from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Post
from .serializers import (CommentSerializer, FollowSerializer,
                          PostSerializer, GroupSerializer, )
from .permissions import IsAuthorOrReadOnly, ReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related(
        'author', 'group'
    )
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [ReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        queryset = Comment.objects.filter(post__id=post_id)
        return queryset

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user,
                        post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
