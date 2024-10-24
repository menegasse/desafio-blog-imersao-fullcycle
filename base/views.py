from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

def render_with_pagination(template, per_page) -> HttpResponse:
    def decorator(func):
        def wrapper(request):
            page = request.GET.get("page") or 1

            query = func(request)
            paginator = Paginator(query, per_page)
            
            context = {
                'page': paginator.get_page(page), 
                'url': request.path_info
            }
            
            return render(request, template, context=context)
        
        return wrapper
    return decorator