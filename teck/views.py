from django.shortcuts import  render, HttpResponse





def index_call (request):
    return render (request, 'index.html', {} )



def mobile_app_call (request):
    return render (request, 'mobile_app.html', {} )


def error500_call (request):
    return render (request, 'page_500.html', {} )
