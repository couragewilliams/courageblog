
from django.shortcuts import redirect, render
from .models import Posts
from .forms import PostCreationForm
from django.contrib import messages
from django.core import paginator
# Create your views here.
# posts=[
#     {
#         'title':'first post',
#         'content': 'my blog first post',
#         'date': '25 febuary 2020',
#         'author': 'miracle'
#     },
    
#     {
#         'title':'second post',
#         'content': 'my blog second post',
#         'date': '26 febuary 2020',
#         'author': 'mhikaru'
#     }
# ]
def home(request):
    posts = Posts.objects.all()
    # posts = Posts.objects.filter(author_id = 1)
    # posts = Posts.objects.get()
    print(posts)
    context = {'posts':posts}
    return render(request,'blog/index.html',context)
def about(request):
    return render(request,'blog/about.html')
def createpost(request):
    profile=request.user
    form = PostCreationForm()
    if request.method=='POST':
        form=PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.author=profile
            project.save()
            messages.success(request, 'post created successfully')
            return redirect('home')
    return render(request, 'blog/createpost.html',{'form':form})

def updatepost(request, pk):
    post = Posts.objects.get(id=pk)
    form = PostCreationForm(instance=post)
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'post updated successfully')
            return redirect('home')
    context = {'form':form}
    return render(request, 'blog/updatepost.html',context)

def deletepost(request, pk):
    post = Posts.objects.filter(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'post deleted successfully')
        return redirect('home')
    return render(request, 'blog/deletepost.html')

def single(request, pk):
    post = Posts.objects.filter(id=pk)
    context = {'post':post}
    return render(request, 'blog/singlepost.html', context)