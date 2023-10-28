from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status

from .models import BlogPost
from .serializers import BlogPostSerializer


"""FUNTION BASED VIEWS"""
from rest_framework.decorators import api_view
@api_view()     # if get only, you dont have to specify the http method
def home(request):
    '''creating a simple home request and response'''
    context = {"greetings": "welcome to this api"}
    print(type(context))
    return Response(context)


@api_view(['GET', 'POST'])
def blog_view(request):
    '''listing all the blog posts in the db and
        creating a new blog post
    '''
    # getting all the blog posts from the db - RETRIEVE
    if request.method == 'GET':
        blogs = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data)
    
    # creating a blog post in the db - CREATE
    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail_view(request, pk):

    '''getting the individual blog where you can
        display the blog
        update the blog
        and delete the blog
    '''
    # getting an individual blog - RETRIEVE
    try:
        blog = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # displaying the blog
    if request.method == 'GET':
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)
    
    # updating a blog - PUT
    elif request.method == 'PUT':
        serializer = BlogPostSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, {'success':'the update was successful'})
        else:
            return Response({'error': 'bad data'})
    
    # deleting a blog - DELETE
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# """FUNTION BASED VIEWS"""
# from rest_framework.views import APIView
# from django.http import Http404

# class Home(APIView):
#     '''creating a simple home request and response'''
#     def get(self, request):
#         context = {'greetings':'hello class world'}
#         return Response(context)

# class BlogView(APIView):
#     '''listing all the blog posts in the db and
#         creating a new blogpost'''
#     # getting all the blog posts in the db
#     def get(self, request):
#         blogs = BlogPost.objects.all()
#         serializer = BlogPostSerializer(blogs, many=True)
#         return Response(serializer.data)
    
#     #creating a new blogpost in the db
#     def post(self, request):
#         serializer = BlogPostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# class BlogDetailView(APIView):

    '''getting the individual blog where you can 
    display the blog
    update the blog 
    delete the blog'''

    # getting the individual blog
    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    # displaying the individual blog
    def get(self, request, pk):
       serializer = BlogPostSerializer(self.get_object(pk))
       return Response(serializer.data)

    # updating a blog
    def put(self, request, pk):
        serializer = BlogPostSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # deleting a blog
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
