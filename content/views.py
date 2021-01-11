from django.views.generic import ListView
from .models import DailyMailColumn

class MainView(ListView):
    paginate_by = 10
    queryset = DailyMailColumn.objects.order_by('-date_added')#the - before the date_added indicates it will sort in descending order
    template_name = 'index.html'
    context_object_name = 'columns'
