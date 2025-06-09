from django.shortcuts import render, redirect
from django.contrib import messages
from mensa.models import *
from datetime import date
import hashlib
# Create your views here.

def index(request):
    return render(request, 'home.html')

def authenticated(email, password):
    return Dipendente.objects.filter(email=email,password=password).exists()
    #select * from User where email="dsfjnfdsjsndfj" and password="password"



def login(request):

    if request.method =='POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        ruolo = request.POST.get('Ruolo')

        profilo = None
        if ruolo == 'dipendente':
            try:
                profilo = Dipendente.objects.get(email=email)
                nome_dipendente = profilo.nome
                azienda_dipendente = profilo.id_azienda.ragione_sociale
            except Dipendente.DoesNotExist:
                messages.error(request, "Nessun dipendente con questa email.")
                return render(request, 'home.html')
        elif ruolo == 'gestore':
            try:
                profilo = Responsabile.objects.get(email=email)
            except Responsabile.DoesNotExist:
                messages.error(request, "Nessun gestore mensa con questa email.")
                
        else:
            messages.error(request, "Devi selezionare un ruolo valido.")
            return render(request, 'home.html')
       
        if profilo:
            hashed = hashlib.md5(password.encode()).hexdigest()
            if hashed == profilo.password:  
        
                return render(request, 'area_dipendente.html',{'nome': nome_dipendente, 'nome_azienda': azienda_dipendente, 'ruolo': ruolo})
            else:
                messages.error(request, "Password errata.")


def annulla(request):
   return render(request, 'area_dipendente.html')


def effettua_prenotazione(request):


    # da lavorarci 
    if request.method =='POST':
        email = request.POST.get('Email')

        dipendente = Dipendente.objects.get(email=email)
        azienda = dipendente.id_azienda
        struttura = azienda.id_struttura
        responsabili = Responsabile.objects.filter(id_struttura=struttura)
        tavoli = Tavolo.objects.all().order_by('id_tavolo')
        piatti = Piatto.objects.filter(id_responsabile__in=responsabili)
        return render(request, 'prenotazione.html',{'tavoli': tavoli, 'piatto': piatti})