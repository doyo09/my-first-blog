from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Board, Issue, Item
from .forms import PostForm, BoardForm, ItemForm, IssueForm
from django.shortcuts import redirect

# Create your views here.
# def post_list(request):
#     posts = Post.objects.all().order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts':posts})

def post_list1(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list1.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)  # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지 않는 것
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)

    # 처음 페이지 접속 시, 비어있는 폼
    else : #request.method != 'POST'
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져온다.
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def item_request(request):
    posts = Item.objects.all().order_by('published_date')
    return render(request, 'blog/item_request.html', {'posts':posts})

def item_request_detail(request, pk):
    post = get_object_or_404(Item, pk=pk)
    return render(request, 'blog/board_detail.html', {'post': post})

def item_request_new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)  # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지 않는 것
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('item_request_detail', pk = post.pk)

    # 처음 페이지 접속 시, 비어있는 폼
    else : #request.method != 'POST'
        form = ItemForm()
    return render(request, 'blog/item_request_edit.html', {'form': form})

def item_request_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져온다.
    if request.method == "POST":
        form = ItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('item_request_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
    return render(request, 'blog/item_request_edit.html', {'form': form})

def board(request):
    posts = Board.objects.all().order_by('published_date')
    return render(request, 'blog/board.html', {'posts':posts})

def board_detail(request, pk):
    post = get_object_or_404(Board, pk=pk)
    return render(request, 'blog/board_detail.html', {'post': post})

def board_new(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)  # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지 않는 것
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board_detail', pk = post.pk)

    # 처음 페이지 접속 시, 비어있는 폼
    else : #request.method != 'POST'
        form = BoardForm()
    return render(request, 'blog/board_edit.html', {'form': form})

def board_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져온다.
    if request.method == "POST":
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
    return render(request, 'blog/board_edit.html', {'form': form})

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})

# def post_list1(request):
#     posts = Post.objects.all().order_by('published_date')
#     return render(request, 'blog/post_list1.html', {'posts':posts})
def issue(request):
    posts = Issue.objects.all().order_by('published_date')
    return render(request, 'blog/issues.html', {'posts':posts})

def issue_detail(request, pk):
    post = get_object_or_404(Issue, pk=pk)
    return render(request, 'blog/issues_detail.html', {'post': post})

def issue_new(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid() :
            post = form.save(commit=False)  # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지 않는 것
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('issue_detail', pk = post.pk)

    # 처음 페이지 접속 시, 비어있는 폼
    else : #request.method != 'POST'
        form = IssueForm()
    return render(request, 'blog/issues_edit.html', {'form': form})

def issue_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져온다.
    if request.method == "POST":
        form = IssueForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('issue_detail', pk=post.pk)
    else:
        form = IssueForm(instance=post)
    return render(request, 'blog/issues_edit.html', {'form': form})
