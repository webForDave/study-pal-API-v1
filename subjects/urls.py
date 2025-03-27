from django.urls import path
from .views import SubjectListAPIView, SubjectDetailAPIView

urlpatterns = [
    path("", SubjectListAPIView.as_view(), name="subject_list"),
    path("<int:pk>/", SubjectDetailAPIView.as_view(), name="subject_detail")
]