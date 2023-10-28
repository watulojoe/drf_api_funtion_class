from django.urls import path
from . import views

urlpatterns = [

    # function based views
    path('', views.home),
    path('blog', views.blog_view),
    path('blog/<pk>', views.blog_detail_view),

    # # class based views
    # path('', views.Home.as_view()),
    # path('blog', views.BlogView.as_view()),
    # path('blog/<pk>', views.BlogDetailView.as_view()),


]
