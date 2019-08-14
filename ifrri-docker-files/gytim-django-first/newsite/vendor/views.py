from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor
from .forms import VendorForm
import socket

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import call_command
import subprocess

def main_page(request):
   try:
      HOSTNAME = socket.gethostname()
   except:
      HOSTNAME = 'localhost'
      
   subprocess.call('/src/newsite/create_base.sh')     
   db_conn = connections['default']
   try: 
      c = db_conn.cursor().connection.cursor().execute("SELECT * FROM public.django_session LIMIT 1;")
   except:
      return render(request, 'vendor/create_base.html', {})

   return render(request, 'vendor/main.html', {'hostname': HOSTNAME})

def create_base(request):
   try:
      HOSTNAME = socket.gethostname()
   except:
      HOSTNAME = 'localhost'
            
   call_command("migrate", interactive=False)
   return render(request, 'vendor/main.html', {'hostname': HOSTNAME})

def vendor_list(request):
   vendors = Vendor.objects.order_by('name')
   return render(request, 'vendor/vendor_list.html', {'vendors': vendors})


def vendor_detail(request, pk):
   vendor = get_object_or_404(Vendor, pk=pk)
   return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})


def vendor_new(request):
   if request.method == "POST":
      form = VendorForm(request.POST)
      if form.is_valid():
         vendor = form.save(commit=False)

         vendor.name = form.cleaned_data['name']
         vendor.country = form.cleaned_data['country']
         vendor.kind = form.cleaned_data['kind']

         vendor.save()
         return redirect('vendor_detail', pk=vendor.pk)
   else:
      form = VendorForm()
   return render(request, 'vendor/vendor_edit.html', {'form': form})


def vendor_remove(request, pk):
   vendor = get_object_or_404(Vendor, pk=pk)
   vendor.delete()
   return vendor_list(request)
