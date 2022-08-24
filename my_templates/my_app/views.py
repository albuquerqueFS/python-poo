from django.shortcuts import render

# Create your views here.
def simple_view(request):
    data = {
        'number': 1,
        'letter': 'A',
        'name': 'Henrique',
        'some_list': [1, 2, 3, 4, 5, 6],
        'some_dictionary': [
            { 'name': 'Henrique', 'position': 'Software Engineer'},
            { 'name': 'Bruno', 'position': 'Line Manager'},
            { 'name': 'Rakesh', 'position': 'BCG Buddy'}
        ]
    }
    return render(request, 'my_app/example.html', context=data)

def index_view(request):
    return render(request, 'my_app/index.html')