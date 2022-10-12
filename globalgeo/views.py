from django.shortcuts import render,redirect,reverse
from .models import CategoryBooks,Books,CategoryPost,Post,Comment
from .forms import ContactForm

# Create your views here.


def home_view(request):
    category = CategoryBooks.objects.all()
    category_post = CategoryPost.objects.all()
    post = Post.objects.all()


    return render(request,'index.html',{'categorys':category,'category':category_post,'post':post})



def categpost(request,cats):
    post = Post.objects.filter(category__name=cats)

    return render(request,'index.html',{'post':post})




def about_view(request):

    return render(request, 'about.html')



def detailbooks_view(request,cats):
    if request.method=='POST':
        upload1 = request.FILES['book']
        object = Books.objects.create(book=upload1)
        object.save()
    category_book = Books.objects.filter(category__category_name=cats)

    return render(request, 'work.html',{'category_books':category_book})


def detailpost_view(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()

            return redirect('detailpost_url',pk=post.id)
    else:
        form = ContactForm()


    return render(request, 'work-single.html',{'post':post,'form': form})







