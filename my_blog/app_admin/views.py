from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, CreateView ,DeleteView
from blog.models import Article
from blog.forms import ArticleForm

# Create your views here.
def dashboard(request):
    return render(request, 'db.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')

    list_articles = Article.objects.filter(user=request.user)
    return render(request, 'my-articles.html', {'list_articles': list_articles})

class AddArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "add-article.html"
    success_url = "my-articles"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/article_form.html'
   

class DeleteArticle(DeleteView):
    model = Article
    success_url = "/my-admin/my-articles"
    


