from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


@login_required(login_url=reverse_lazy('login'))
def shop_list(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_post = Post(title=form.cleaned_data['title'], body=form.cleaned_data['body'], author=request.user)
            new_post.save()
    posts = Post.objects.all().filter(author=request.user)
    return render(request, 'shop_list/index.html', context={'posts': posts,
                                                            'form': form})
