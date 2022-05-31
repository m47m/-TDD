from django.shortcuts import redirect, render
from django.http import HttpResponse

#from superlists.lists.models import Item

from lists.models import Item

# home_page = None
# Create your views here.
def home_page(request):
	# if request.method == 'POST':
	# 	#new_item_text = request.POST['item_text']
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	return redirect('/lists/the-only-list-in-the-world/')

	#items = Item.objects.all()
	return render(request,'home.html')

def view_list(request):
 	#pass
	items = Item.objects.all()
	return render(request,'list.html',{'items':items})

def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')