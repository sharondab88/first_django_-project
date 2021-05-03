from django.http import HttpResponse

# Create your views here.

data = {
" Name: Sharonda Bailey \n ",
" City: Harrisburg, NC   \n",
" Track:  Python  \n",
" Message: Please give me passing grade!!! :-) \n"
}


def index(request):
    return HttpResponse(data)


# def index(request):
#     return HttpResponse("This is my 1st django app")

