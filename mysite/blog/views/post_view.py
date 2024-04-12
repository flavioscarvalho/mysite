from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog.models import Post
from mysite.mysite.blog.forms import CommentForm
from mysite.mysite.blog.models import post



class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = "post_detail.html"

def post_detail(request, slug):
    template_name = "post_detail.html"
    pst = get_object_or_404(Post, slug=slug)
    comments = pst.comments.filter(active=True).order_by("-created_on")  # Uso correto de pst
    new_comment = None

    if request.method == "POST":
        comment_form =comment_form(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": pst,  # Corrigido para usar pst
            "comments": comments,  # Corrigido para usar dois-pontos
            "new_comment": new_comment,
            "comment_form": comment_form,
        }
    )

