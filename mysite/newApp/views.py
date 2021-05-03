from django.http import HttpResponse

# Create your views here.

data = {
" Name: Sharonda Bailey  ",
" City: Harrisburg, NC   ",
" Course: Python  ",
" Message: Please give me passing grade!!! :-) "
}


def index(request):
    return HttpResponse(data)


# def index(request):
#     return HttpResponse("This is my 1st django app")
