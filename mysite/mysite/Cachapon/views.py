from django.shortcuts import render_to_response

# Create your views here.

def ImageTest(request):
    return render_to_response('test.html')