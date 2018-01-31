from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Wallet
from .forms import walletForm



def index(request):
    latest_wallet_list = Wallet.objects.order_by('name')[:5]
    context = {'latest_wallet_list': latest_wallet_list}
    return render(request, 'app/index.html', context)

def wallets(request):
    try:
        wallets = Wallet.objects.filter(user=request.user)
    except Wallet.DoesNotExist:
        raise Http404("No wallets")
    return render(request, 'app/wallets.html', {'wallets': wallets})


def results(request, user_id):
    response = "You're looking at %s."
    return HttpResponse(response % user_id)

def profile(request, user_id):
    response = "Logged in"
    return HttpResponse(response)

def createWallet(request):
    if request.method == 'POST':
          wallet = Wallet(
            user=request.user,
            name=request.POST['name'],
            bitcoin=request.POST['bitcoin'],
            etherium=request.POST['etherium'],
            litecoin=request.POST['litecoin'])
          wallet.save()

    context = {}

    # entry_list = Wallet.objects.all ()
    # context ['entries'] = entry_list
    #
    # form = EntryForm ()
    # context ['form'] = form

    return render (request, 'app/createWallet.html', context)

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

