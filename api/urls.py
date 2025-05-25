from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from book.views import BookViewSet,CategoryViewSet,AuthorViewSet
from borrow_record.views import BorrowBookViewSet

router = routers.DefaultRouter()
router.register('books',BookViewSet),
router.register('categories',CategoryViewSet),
router.register('authors',AuthorViewSet),
router.register('borrow-records',BorrowBookViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
