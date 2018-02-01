from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Wallet
from .forms import walletForm



def index(request):

    return render(request, 'app/index.html')

def wallets(request):
    try:
        wallets = Wallet.objects.filter(user=request.user)
    except Wallet.DoesNotExist:
        raise Http404("No wallets")
    return render(request, 'app/wallets.html', {'wallets': wallets})

def createWallet(request):
    if request.method == 'POST':
          wallet = Wallet(
            user=request.user,
            name=request.POST['name'],
            bitcoin=request.POST['bitcoin'],
            etherium=request.POST['etherium'],
            litecoin=request.POST['litecoin'])
          wallet.save()
          return redirect (reverse ('app:wallets'))


    return render (request, 'app/createWallet.html')

def editWallet(request):
    if request.method == 'POST':
          wallet = Wallet(
            id=request.POST['id'],
            user=request.user,
            name=request.POST['name'],
            bitcoin=request.POST['bitcoin'],
            etherium=request.POST['etherium'],
            litecoin=request.POST['litecoin'])
          wallet.save()

    wallets = Wallet.objects.filter(user=request.user)

    return render (request, 'app/editWallet.html', {'wallets': wallets})

def deleteWallet (request):
    if request.method == 'POST':
        Wallet.objects.filter (id = request.POST['id']).delete ()

        return redirect (reverse ('app:wallets'))


    wallets = Wallet.objects.filter(user=request.user)

    return render (request, 'app/deleteWallet.html', {'wallets': wallets})





