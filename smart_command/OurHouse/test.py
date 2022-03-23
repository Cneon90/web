from .models import addation_user as Post

posts = Post.objects.all()

print(posts)