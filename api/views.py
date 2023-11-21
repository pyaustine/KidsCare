from django.shortcuts import render

# Create your views here.
def test(request):
    data = {
        'id' : 12,
        'name' : 'Austine',
        'account_number' : 987194712 
    }

    return render(request, 'api/test.html', {'data': data})