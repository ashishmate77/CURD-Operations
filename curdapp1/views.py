from django.shortcuts import render
from .models import  ProductData
from .forms import CreateForm,UpdateForm,DeleteForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'regapp/home.html')

def Create_view(request):
    if request.method == "POST":
        cform = CreateForm(request.POST)
        if cform.is_valid():
            Product_id = request.POST.get("Product_id")
            Product_name = request.POST.get("Product_name")
            Price = request.POST.get("Price")
            Cname = request.POST.get("Cname")
            Mobile = request.POST.get("Mobile")

            data = ProductData(
                Product_id = Product_id,
                Product_name = Product_name,
                Price = Price,
                Cname = Cname,
                Mobile = Mobile,
            )
            data.save()
            cform = CreateForm()
            context = {'form':cform}
            return render(request,'regapp/create.html',context)
    else:
        cform = CreateForm()
        context = {'form': cform}
        return render(request,'regapp/create.html', context)

# FETCHE_view():-

def Fetche_view(request):
    Products = ProductData.objects.all()
    context = {'Products': Products}
    return render(request,'regapp/fetche.html',context)



#UPDATE VIEW:

def Update_view(request):

    if request.method == "POST":
        uform = UpdateForm(request.POST)
        if uform.is_valid():
            Product_id = request.POST.get("Product_id")
            Price = request.POST.get("Price")
            prod = ProductData.objects.filter(Product_id=Product_id)

            if not prod:
                return  HttpResponse("Not Available")
            else:
                prod.update(Price=Price)
                uform = UpdateForm()
                context = {'form': uform}
                return render(request, 'regapp/update.html', context)


    else:
        uform = UpdateForm()
        context = {'form': uform}
        return render(request,'regapp/update.html', context)


#DELETE VIEW:

def Delete_view(request):

    if request.method == "POST":
        dform = DeleteForm(request.POST)
        if dform.is_valid():
            Product_id = request.POST.get("Product_id")
            prod = ProductData.objects.filter(Product_id=Product_id)

            if not prod:
                return HttpResponse("Not Available")
            else:
                prod.delete()
                dform = DeleteForm()
                context = {'form': dform}
                return render(request, 'regapp/delete.html', context)

    else:
        dform = DeleteForm()
        context = {'form': dform}
        return render(request,'regapp/delete.html', context)
