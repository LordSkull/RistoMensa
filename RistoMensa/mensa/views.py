from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
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
        
        if ruolo == 'Dipendente':
            try:
                profilo = Dipendente.objects.get(email=email)
                nome_dipendente = profilo.nome
                azienda_dipendente = profilo.id_azienda.ragione_sociale
                struttura_id = profilo.id_azienda.id_struttura.id_struttura
                
                pagina = 'area_dipendente.html'
                specifiche = {'nome': nome_dipendente, 'nome_azienda': azienda_dipendente, 'ruolo': ruolo}
            
            except Dipendente.DoesNotExist:
                messages.error(request, "Nessun dipendente con questa email.")
                return render(request, 'home.html')
       
        elif ruolo == 'Gestore':
            try:
                profilo = Responsabile.objects.get(email=email)
                azienda_gestore = profilo.id_struttura.nome
                # per il responsabile prendi id_struttura direttamente
                struttura_id = profilo.id_struttura.id_struttura
            
                pagina = 'area_gestore.html'
                specifiche = {'nome': profilo.email, 'nome_azienda': azienda_gestore, 'ruolo': ruolo}
            
            except Responsabile.DoesNotExist:
                messages.error(request, "Nessun gestore mensa con questa email.")
                
        else:
            messages.error(request, "Devi selezionare un ruolo valido.")
            return render(request, 'home.html')
       
        if profilo:
            hashed = hashlib.md5(password.encode()).hexdigest()
            if hashed == profilo.password:
                request.session['user_email']   = profilo.email
                request.session['ruolo']        = ruolo
                request.session['id_struttura'] = struttura_id  
                if ruolo == 'Gestore':
                    return redirect('gestione_menu')
                else:
                    return render(request, pagina, specifiche)
            else:
                messages.error(request, "Password errata.")


def annulla(request):
   return render(request, 'area_dipendente.html')


def effettua_prenotazione(request):
    # 1) recupera dalla sessione l’ID della struttura
    struct_id = request.session.get('id_struttura')
    if not struct_id:
        return redirect('login')

   
    # 3) prendo i tavoli DI QUELLA struttura
    tavoli = Tavolo.objects.filter(struttura_associata=struct_id,disponibilità=True).order_by('id_tavolo')

    # 4) prendo i piatti associati al responsabile di quella stessa struttura
    piatti = Piatto.objects.filter(id_responsabile__id_struttura=struct_id)

    # 5) suddivido per tipo di piatto
    primi    = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.PRIMO)
    secondi = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.SECONDO)
    dessert  = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.DESSERT)

    # 6) altrimenti mostra il form
    return render(request, 'prenotazione.html', {
        'tavoli':   tavoli,
        'primi':    primi,
        'secondi':  secondi,
        'dessert':  dessert,
        'struttura': struct_id,
    })

def conferma_prenotazione(request):
    if request.method == 'POST':
        # recupero dati dal form
        data = request.POST.get('data')
        id_tavolo = request.POST.get('tavolo')
        id_primo = request.POST.get('primo')
        id_secondo = request.POST.get('secondo')
        id_dessert = request.POST.get('dessert')
        
        # recupero tavolo e piatti
        print(f"Tavolo ID ricevuto dal form: {id_tavolo}")
        tavolo = get_object_or_404(Tavolo, id_tavolo=id_tavolo)
        primo = get_object_or_404(Piatto, id_piatto=id_primo)
        secondo = get_object_or_404(Piatto, id_piatto=id_secondo)
        dessert = get_object_or_404(Piatto, id_piatto=id_dessert)
        
        totale = primo.prezzo + secondo.prezzo + dessert.prezzo

        # Recupero il dipendente dalla sessione
        email = request.session.get('user_email')
        dipendente = get_object_or_404(Dipendente, email=email)

        # 1. Salva la prenotazione
        prenotazione = Prenotazione.objects.create(
            data_prenotazione=data,
            totale_prezzo=totale,
            stato=Prenotazione.StatoPrenotazione.IN_ATTESA,  # puoi anche mettere CONFERMATA se vuoi
            id_tavolo=tavolo,
            id_dipendente=dipendente
        )
        
        # 2. Salva le associazioni tavolo-piatto (puoi aggiungere anche prenotazione_id se vuoi espandere il modello)
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=primo)
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=secondo)
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=dessert)

        # Torna la pagina di conferma
        return render(request, 'conferma_prenotazione.html', {
            'data': data,
            'tavolo': tavolo,
            'primo_scelto': primo,
            'secondo_scelto': secondo,
            'dessert_scelto': dessert,
            'totale': totale,
            'prenotazione_id': prenotazione.id_prenotazione,
        })

'''
def conferma_prenotazione(request):
    if request.method == 'POST':
        # 1) recupero i dati dal form
        data = request.POST.get('data')
        id_tavolo = request.POST.get('tavolo')
        id_primo = request.POST.get('primo')
        id_secondo = request.POST.get('secondo')
        id_dessert = request.POST.get('dessert')

        # 2) recupero il tavolo
        tavolo = get_object_or_404(Tavolo, id_tavolo=id_tavolo)

        # 3) recupero i piatti selezionati
        primo = get_object_or_404(Piatto, id_piatto=id_primo)
        secondo = get_object_or_404(Piatto, id_piatto=id_secondo)
        dessert = get_object_or_404(Piatto, id_piatto=id_dessert)

        # 4) calcolo il totale
        totale = primo.prezzo + secondo.prezzo + dessert.prezzo

        # 5) reindirizzo alla pagina di conferma
        return render(request, 'conferma_prenotazione.html', {
            'data': data,
            'tavolo': tavolo,
            'primo_scelto': primo,
            'secondo_scelto': secondo,
            'dessert_scelto': dessert,
            'totale': totale
        })
'''

def gestione_menu(request):
    # Recupera la struttura dal responsabile loggato (puoi anche prenderla dalla sessione)
    id_struttura = request.session.get('id_struttura')
    responsabile = Responsabile.objects.get(id_struttura=id_struttura)
    
    # Aggiunta piatto
    if request.method == 'POST' and 'add_piatto' in request.POST:
        nome = request.POST['nome']
        prezzo = request.POST['prezzo']
        tipo = request.POST['tipo_piatto']
        Piatto.objects.create(
            nome=nome,
            prezzo=prezzo,
            tipo_piatto=tipo,
            id_responsabile=responsabile
        )
        return redirect('gestione_menu')
    
    # Eliminazione piatto
    
    if request.method == 'POST' and 'delete_piatto' in request.POST:
        id_piatto = request.POST['delete_piatto']
        piatto = Piatto.objects.get(id_piatto=id_piatto, id_responsabile=responsabile)
        piatto.delete()
        return redirect('gestione_menu')

    # Piatti di quella mensa
    piatti = Piatto.objects.filter(id_responsabile=responsabile)
    primi = piatti.filter(tipo_piatto='primo piatto')
    secondi = piatti.filter(tipo_piatto='secondo piatto')
    dessert = piatti.filter(tipo_piatto='dessert')

    return render(request, 'area_gestore.html', {
        'primi': primi,
        'secondi': secondi,
        'dessert': dessert,
        'nome' : responsabile.email,
        'ruolo': 'Gestore',
        'nome_azienda': responsabile.id_struttura.nome,
    })