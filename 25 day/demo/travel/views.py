from django.shortcuts import render
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
    return render(request, "hello.html", {"datas": datas})
