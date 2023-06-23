from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NoteShareViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet)
router.register('noteshares', NoteShareViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
