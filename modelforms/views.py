from django.shortcuts import render
from .models import Post


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('email'):
                post = Post()
                post.email = request.POST.get('email')
                post.save()

                return render(request, 'modelforms/index.html')

        else:
                return render(request, 'modelforms/index.html')


def showemail(request):

    email = Post.objects.all()

    context = {'email': email}

    return render(request, 'modelforms/view.html', context)


