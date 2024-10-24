from base.views import render_with_pagination
from core.models import Post, Tag

@render_with_pagination('core/posts.html', 5)
def posts(request):
    return Post.objects.prefetch_related('tags')
