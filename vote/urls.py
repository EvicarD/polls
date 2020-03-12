from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from vote.views import (HomeView,
                        PublisherListView,
                        PublisherDetailView,
                        PublisherCreateView,
                        BookListView,
                        BooksCreateView,
                        CommentCreateView,
                        )

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('publisher/', PublisherListView.as_view(), name='publisher'),
    path('publisher/<slug:slug>/', PublisherDetailView.as_view(), name='detail'),
    path('publish/add/', PublisherCreateView.as_view(), name='add'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/add/', BooksCreateView.as_view(), name='add-books'),
    path('comment/add/', CommentCreateView.as_view(), name='add-comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
