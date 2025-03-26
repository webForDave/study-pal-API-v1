from django.urls import path
from .views import GoalListAPIView, GoalDetailAPIView

urlpatterns = [
    path("<int:pk>/", GoalDetailAPIView.as_view(), name="goal_detail"),
    path("", GoalListAPIView.as_view(), name="goal_list")
]