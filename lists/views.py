from django.shortcuts import redirect, render
from django.http import HttpResponse

#from superlists.lists.models import Item

from lists.models import Item

# home_page = None
# Create your views here.
def home_page(request):
	# return HttpResponse('<html><title>To-Do lists</title></html>')
	# if request.method == 'POST':
	# 	return HttpResponse(request.POST['item_text'])

	# item = Item()
	# item.text = request.POST.get('item_text','')
	# item.save()

	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text)
		return redirect('/')

	items = Item.objects.all()
	return render(request,'home.html',{'items':items})
	# else:
	# 	new_item_text = ''

	# return render(request,'home.html',{
	# 	'new_item_text': new_item_text,
	# })