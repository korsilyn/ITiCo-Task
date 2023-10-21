from django.shortcuts import render

def index(request):
    return render(request, 'index.html', get_base_context(request))



def get_base_context(request, update=None):
    context = {
        'request': request,
        'user': request.user,
    }

    return context
