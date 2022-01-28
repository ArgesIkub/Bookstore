from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from app.models import Orders
from django.urls import reverse

# Create your views here.

def all_orders(request):
    
    all_orders = Orders.objects.all()
    # all_orders = Orders.objects.filter(state='approved')

    if request.GET.get('state', False):
        all_orders = Orders.objects.filter(state=request.GET['state'])

    name = ''
    for i in all_orders:
        name += f'{i.description} - {i.state}'
        name += '</br>'
    
    return HttpResponse(name)


def update_order_state(request, pk):
    
    if request.method == 'GET':
        print(request.method)
        order = Orders.objects.get(id=pk)
        return render(request, 'app/update_state_order.html', {'order': order})
    
    else:
        order = Orders.objects.get(id=pk)

        order.state = request.POST['state']
        order.save()
        return redirect(reverse('update-order-state', args=(pk,)))