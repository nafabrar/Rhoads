from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.urlresolvers import reverse
from .models import Album,Song,Blog
from django.http import Http404,HttpResponseRedirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from .forms import BlogForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('music:account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




def welcome(request):
    return render(request,'welcome.html')

# class DetailView(generic.DetailView):
#     model = Album
#     template_name = 'music/detail.html'

# /music/album/add/ dont need a pk as we are creating an album
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/home')
    else:
        return render(request, 'account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def all_blogs(request):
    """Show all topics."""

    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def blogs(request):
    """Show all topics."""

    blogs = Blog.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)

def blog(request, blog_id):
    """Show a single topic, and all its entries."""
    blog = Blog.objects.get(id=blog_id)
    # Make sure the topic belongs to the current user.
    # if blog.owner != request.user:
    #     raise Http404

    chapters = blog.text
    context = {'blog': blog, 'chapters': chapters,'image':''}
    return render(request, 'blog.html', context)

@login_required
def new_blog(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('music:blogs'))

    context = {'form': form}
    return render(request, 'new_blog.html', context)

#
#
#
# @login_required
# def edit_chapter(request,chapter_id):
#     """Edit an existing entry."""
#     chapter = Chapter.objects.get(id=chapter_id)
#     blog = chapter.blog
#     if blog.owner != request.user:
#         raise Http404
#
#     if request.method != 'POST':
#         # Initial request; pre-fill form with the current entry.
#         form = ChapterForm(instance=chapter)
#     else:
#         # POST data submitted; process data.
#         form = ChapterForm(instance=chapter, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('music:blog',
#                                                 args=[blog.id]))
#
#     context = {'chapter': chapter, 'blog': blog, 'form': form}
#     return render(request, 'edit_chapter.html', context)

def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    blogs = Blog.objects.filter(owner=request.user)
    return render(request, 'blogs.html', {'blogs': blogs})

def edit_blog(request,blog_id):
    """Edit an existing blog."""
    chapter = Blog.objects.get(id=blog_id)
    blog = chapter
    if blog.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogForm(None)

    else:
        # POST data submitted; process data.
        form = BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('music:blog',
                                                args=[blog.id]))

    context = {'chapter': chapter, 'blog': blog, 'form': form}
    return render(request, 'edit_blog.html', context)

@login_required
def home(request):
    usern=request.user.username
    context ={'usern' : usern}
    return render(request,'index.html',context)
