from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone #models의 pub_date값은 자동으로 입력받을 예정이니까 timezone을 불러온다
from .models import Blog
from django.core.paginator import Paginator
from .forms import NewBlog, CommentForm
#맨처음 페이지
def welcome(request):
    return render(request,'viewcrud/index.html')

#조회 함수
def read(request):
    blogs = Blog.objects
    blogs_list = Blog.objects.all()
    paginator = Paginator(blogs_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request,'viewcrud/funccrud.html',{'blogs':blogs, 'posts':posts })
#글쓰기 함수
def create(request):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    # 글쓰기 페이지를 띄워주는 역할 == GET
    else:
        form = NewBlog()
        return render(request,'viewcrud/new.html', {'form':form})


def detail(request,blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request,'viewcrud/detail.html',{'details':details})


    





#수정 함수
def update(request, pk):

    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)

     


    #해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'viewcrud/new.html',{'form':form})

#삭제함수
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')


def add_comment(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('home')

    else:
        form = CommentForm()
    return render(request,'viewcrud/add_comment.html',{'form':form})