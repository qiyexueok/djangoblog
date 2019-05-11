from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse

from .models import Banner, Post, BlogCategory, FriendlyLink, Comment
from .forms import TestUEditorForm, BlogForm

class IndexView(View):
    def get(self, request):
        banner_lists= Banner.objects.all()
        recommend_posts = Post.objects.filter(recommend=True)
        post_lists = Post.objects.all().order_by('-pub_date')[:3]
        category_lists = BlogCategory.objects.all()
        friendlylinks = FriendlyLink.objects.all()
        ctx = {
        'banner_lists': banner_lists, 'recommend_posts': recommend_posts, 'post_lists': post_lists, 'category_lists': category_lists, 'friendlylinks': friendlylinks}
        return render(request, 'index.html', ctx)


class PostView(View):
    def get(self, request,post_id):
        post = Post.objects.get(id=int(post_id))
        post.visits += 1
        post.save()
        comments = post.comment_set.all().order_by('-pub_date')
        return render(request, 'blogs/blog-post.html', {'post': post, 'comments':comments})


class CategoryView(View):
    def get(self, request, category_id):
        category = BlogCategory.objects.get(id=int(category_id))
        return render(request, 'blogs/blog-category.html', {'category': category})


class SearchView(View):
    def post(self, request):
        kw = request.POST.get('keyword', '')
        post_lists = Post.objects.filter(Q(title__icontains=kw)|Q(content__icontains=kw))
        ctx = {
            'post_lists': post_lists,
        }
        return render(request, 'blogs/list.html', ctx)


class BlogListView(View):
    def get(self, request):
        post_list = Post.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(post_list, per_page=2, request=request)
        post_list = p.page(page)
        ctx = {
            'post_list': post_list,
        }
        print(post_list.object_list)
        return render(request, 'blogs/list.html', ctx)


class First(View):
    def get(self, request):
        form = TestUEditorForm()
        return render(request, 'blogs/first.html', {'form':form})


class CommentView(View):

    def post(self, request, post_id):
        post = Post.objects.get(id=int(post_id))
        user = request.user
        content = request.POST.get('content', '')
        comment = Comment()
        comment.user = user
        comment.post= post
        comment.content = content
        comment.save()

        return HttpResponseRedirect(reverse('blog:blogpost', kwargs={'post_id': post_id}))


class WritePostView(View):
    def get(self, request):
        form = Post()

        return render(request, 'blogs/write-post.html', {'form': form})