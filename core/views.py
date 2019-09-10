from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Dovetail,Dowell,Cutsheet
import datetime
# Create your views here.


def test(request):
    return render(request, 'base/base.html')

@login_required
def dovetail(request):
    if request.method == "POST":
        dovetail = Dovetail()
        dovetail.leftArm = request.POST["leftarm"]
        dovetail.sheetname = request.POST["sheetname"]
        dovetail.rightArm = request.POST["rightarm"]
        dovetail.depth = request.POST["depth"]
        dovetail.width =request.POST["width"]
        dovetail.thickness =request.POST["thickness"]
        dovetail.centerDepth =request.POST["cdepth"]
        dovetail.createdDate =datetime.datetime.now()
        dovetail.updatedDate =datetime.datetime.now()
        dovetail.createdBy =request.user
        dovetail.save()


    return render(request,'core/dovtail.html')


@login_required
def Dovetailview(request,id):
    if request.method == "GET":
        dovetail = Dovetail.objects.get(id=id)
        return render(request, 'core/dovtailView.html',context={"dovetail":dovetail})

    if request.method == "POST":
        dovetail = Dovetail.objects.get(id=id)
        dovetail.leftArm = request.POST["leftarm"]
        dovetail.sheetname = request.POST["sheetname"]
        dovetail.rightArm = request.POST["rightarm"]
        dovetail.depth = request.POST["depth"]
        dovetail.width =request.POST["width"]
        dovetail.thickness =request.POST["thickness"]
        dovetail.centerDepth =request.POST["cdepth"]
        dovetail.updatedDate =datetime.datetime.now()
        dovetail.save()
        return render(request, 'core/dovtailView.html',context={"dovetail":dovetail})

@login_required
def Dowellview(request,id):
    if request.method == "GET":
        dowell = Dowell.objects.get(id=id)
        return render(request, 'core/dowellView.html',context={"dowell":dowell})

    if request.method == "POST":
        dowell = Dowell.objects.get(id=id)
        dowell.leftArm = request.POST["leftarm"]
        dowell.sheetname = request.POST["sheetname"]
        dowell.rightArm = request.POST["rightarm"]
        dowell.depth = request.POST["depth"]
        dowell.width =request.POST["width"]
        dowell.thickness =request.POST["thickness"]
        dowell.centerDepth =request.POST["cdepth"]
        dowell.updatedDate =datetime.datetime.now()
        dowell.save()
        return render(request, 'core/dowellView.html',context={"dowell":dowell})





@login_required()
def dovetailList(request):
    dovetail = Dovetail.objects.all()
    context = {
        "dovetails":dovetail
    }
    return render(request, 'core/dovetailList.html',context)

@login_required
def dowell(request):
    if request.method == "POST":
        dowell = Dowell()
        dowell.leftArm = request.POST["leftarm"]
        dowell.sheetname = request.POST["sheetname"]
        dowell.rightArm = request.POST["rightarm"]
        dowell.depth = request.POST["depth"]
        dowell.width =request.POST["width"]
        dowell.thickness =request.POST["thickness"]
        dowell.centerDepth =request.POST["cdepth"]
        dowell.createdDate =datetime.datetime.now()
        dowell.updatedDate =datetime.datetime.now()
        dowell.createdBy =request.user
        dowell.save()


    return render(request,'core/dowell.html')


@login_required
def dowellList(request):
    dowell = Dowell.objects.all()
    context = {
        "dowells":dowell
    }
    return render(request, 'core/dowellList.html',context)


@login_required
def cutsheet(request):
    if request.method == "GET":
        return render(request, 'core/cutsheet.html')
    if request.method == "POST":
        cutsheet = Cutsheet()
        cutsheet.orderNo = request.POST["orderNo"]
        cutsheet.trkWeight =request.POST["trkWeight"]
        cutsheet.pallets = request.POST["pallets"]
        cutsheet.orderDate = request.POST["orderDate"]
        cutsheet.shipDate = request.POST["shipDate"]
        cutsheet.totalBoxes = request.POST["totalBoxes"]
        cutsheet.shippingInstructions = request.POST["shippingInstructions"]
        cutsheet.errNo = request.POST["errNo"]
        cutsheet.sideSQFT = request.POST["sideSQFT"]
        cutsheet.bottomSQFT = request.POST["bottomSQFT"]
        cutsheet.createdDate = datetime.datetime.now()
        cutsheet.createdBy = request.user
        cutsheet.save()
        return render(request, 'core/cutsheet.html')


@login_required
def cutsheetList(request):
    cutsheets = Cutsheet.objects.all()
    context = {
        "cutsheets":cutsheets
    }
    return render(request, 'core/cutsheetList.html',context=context)


@login_required
def cutsheetview(request,id):
    if request.method == "GET":
        cutsheet = Cutsheet.objects.get(id=id)
        context = {
            "cutsheet":cutsheet
        }
        return render(request,'core/cutsheetupdate.html',context=context)
    if request.method == "POST":
        cutsheet = Cutsheet.objects.get(id=id)
        cutsheet.orderNo = request.POST["orderNo"]
        cutsheet.trkWeight =request.POST["trkWeight"]
        cutsheet.pallets = request.POST["pallets"]
        cutsheet.orderDate = request.POST["orderDate"]
        cutsheet.shipDate = request.POST["shipDate"]
        cutsheet.totalBoxes = request.POST["totalBoxes"]
        cutsheet.shippingInstructions = request.POST["shippingInstructions"]
        cutsheet.errNo = request.POST["errNo"]
        cutsheet.sideSQFT = request.POST["sideSQFT"]
        cutsheet.bottomSQFT = request.POST["bottomSQFT"]
        cutsheet.createdDate = datetime.datetime.now()
        cutsheet.createdBy = request.user
        cutsheet.save()
        context = {
            "cutsheet": cutsheet
        }
        return render(request, 'core/cutsheetupdate.html',context=context)
