from django.shortcuts import render


# Create your views here.


def test(request):
    return render(request, 'base/base.html')



def dovetail(request):
    return render(request,'core/dovtail.html')