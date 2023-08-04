from django.core.checks import messages
from django.shortcuts import redirect, render
from frontend.forms import Customerforms 
from frontend.models  import EmpModel, OfferModel
from django.contrib import messages
from frontend.forms import Customerforms
from django.shortcuts import redirect
def showemp(request):
    showall = EmpModel.objects.all()
    return render(request, 'home.html', {"data":showall})
 

def showoffer(request):
    showall = OfferModel.objects.all()
    return render(request, 'offers.html', {"data":showall})

def home(request):
    return render(request,'Index.html')

def Insertcustomer(request):
    if request.method == "POST":
        if request.POST.get('customer_id') and request.POST.get('customer_name') and request.POST.get('customer_address') and request.POST.get('email'):
            saverecord = EmpModel()
            saverecord.customer_id = request.POST.get('customer_id')
            saverecord.customer_name = request.POST.get('customer_name')
            saverecord.customer_address = request.POST.get('customer_address')
            saverecord.email = request.POST.get('email')
            saverecord.save()
            messages.success(request,'customer ' +saverecord.customer_name +' is saved successfully!!!')
            return render(request,'Insert.html')
    else:
        return render(request,'Insert.html')

def offer(request):
    return render(request,'offers.html')

def Deletecustomer(request,customer_id):
    delcustomer = EmpModel.objects.get(pk = customer_id)
    delcustomer.delete()
    showdata = EmpModel.objects.all()
    return redirect('/')

def Editcustomer(request,customer_id):
    Editcust=EmpModel.objects.get(pk=customer_id)
    return render(request,'Edit.html',{"EmpModel":Editcust})

def Updatecustomer(request,customer_id):
    Updatecust=EmpModel.objects.get(pk=customer_id)
    form=Customerforms(request.POST,instance=Updatecust)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully....!!!')
        return render(request,'Edit.html',{"EmpModel":Updatecust})