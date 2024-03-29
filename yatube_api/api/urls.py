from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts(?P<post_id>\d+)?', PostViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments(?P<comment_id>\d+)?',
    CommentViewSet,
    basename='comment',
)
router_v1.register(r'groups(?P<group_id>\d+)?', GroupViewSet)
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]
