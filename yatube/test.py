if request.method == 'GET':
        return render(request, 'posts/create_post.html', {'form': PostForm()})
    elif request.method == 'Post':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/create_post.html', {'form': form})
    else:
        return HttpResponseNotAllowed()

from django.http import HttpResponseNotAllowed