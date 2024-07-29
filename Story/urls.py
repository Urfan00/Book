from django.urls import path
from Story.views import StoryList, StoryDetailView, story, story_detail


urlpatterns = [
    path('story_list/', StoryList.as_view(), name='story_list'),
    path('story_detail/<int:pk>', StoryDetailView.as_view(), name='story_detail'),
]
