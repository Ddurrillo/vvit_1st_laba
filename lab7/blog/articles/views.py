from articles.models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {'text': request.POST["text"], 'title': request.POST["title"]}
            if form["text"] and form["title"]:
                if form["title"] in [article.title for article in Article.objects.all()]:
                    form['errors'] = u"Название статьтьи неуникально"
                    return render(request, 'create_post.html', {'form': form})
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        return redirect("/authorize/")

def register(request):
    if not request.user.is_anonymous:
        return redirect("/archive/")
    else:
        if request.method == "POST":
            login, mail = request.POST["login"], request.POST['email']
            password, password_repeated =  request.POST["password"], request.POST["password-repeat"]
            if password != password_repeated:
                return render(request, 'registration.html', {'err': "Пароли не совпадают"})
            if login and mail and password:
                try:
                    User.objects.get(username=login)
                    return render(request, 'registration.html', {'err': "Такой пользователь уже существует"})
                except User.DoesNotExist:
                    User.objects.create_user(login, mail, password)
                    return redirect("/archive/")
            else:
                return render(request, 'registration.html', {'err': "Есть пустые поля."})
        else:
            return render(request, 'registration.html', {})

def authorize(request):
    if not request.user.is_anonymous:
        return redirect("/archive/")
    else:
        if request.method == "POST":
            username, password = request.POST["login"], request.POST["password"]
            if username and password:
                try:
                    User.objects.get(username=username)
                    try:
                        usr = authenticate(username=username, password=password)
                        login(request, usr)
                        return redirect("/archive/")
                    except:
                        return render(request, 'authorization.html', {'err': "Введён неверный пароль", 'oldlog': username})
                except:
                    return render(request, 'authorization.html', {'err': "Данного пользователя не существует"})
            else:
                 return render(request, 'authorization.html', {'err': "Есть пустые поля"})
        else:
            return render(request, 'authorization.html', {})

def deauthorize(request):
    if not request.user.is_anonymous:
        logout(request)
    return redirect("/archive/")
