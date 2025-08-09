from http.client import HTTPResponse
from django.shortcuts import render, redirect
from travel.models import UserData

# Create your views here.
# data1 = {
#     "name": "John Doe",
#     "age": 30,
# }


# data2 = {
#     "name": "Jane Smith",
#     "age": 25,
# }

# data3 = {
#     "name": "Alice Johnson",
#     "age": 28,
# }

# data4 = {
#     "name": "Bob Brown",
#     "age": 35,
# }

# datas = [data1, data2, data3,data4]
def hello(request):
    datas = UserData.objects.all()
    if request.method == "GET":
        nm = request.GET.get("name")
        if nm != None:
            datas = UserData.objects.filter(name__icontains = nm)
            
        
    return render(request, "hello.html", {"datas": datas})

def AddData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name, age)
        user = UserData(name = name, age = age)
        user.save()
        return redirect("hello")
        
        # return HTTPResponse("Data added successfully")
       
    # return render(request, "add_data.html")
