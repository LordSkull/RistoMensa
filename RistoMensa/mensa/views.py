from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from mensa.models import *
from datetime import date, datetime
from django.core.paginator import Paginator
import hashlib
# Create your views here.

def index(request):
    return render(request, 'home.html')

def authenticated(email, password):
    return Dipendente.objects.filter(email=email,password=password).exists()

def login(request):

    if request.method =='POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        ruolo = request.POST.get('Ruolo')

        profilo = None
        struttura_id = None
        
        if ruolo == 'Dipendente':
            try:
                profilo = Dipendente.objects.get(email=email)
                struttura_id = profilo.id_azienda.id_struttura.id_struttura
    
            except Dipendente.DoesNotExist:
                messages.error(request, "Nessun dipendente con questa email.")
                return render(request, 'home.html')
       
        elif ruolo == 'Gestore':
            try:
                profilo = Responsabile.objects.get(email=email)
                azienda_gestore = profilo.id_struttura.nome
                # per il responsabile prendo l'id_struttura direttamente
                struttura_id = profilo.id_struttura.id_struttura
             
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
                    return redirect('area_dipendente')
            else:
                messages.error(request, "Password errata.")


def annulla(request):
   return render(request, 'area_dipendente.html')


def area_dipendente(request):
    # Recupera il dipendente loggato dalla sessione
    email = request.session.get('user_email')
    dipendente = get_object_or_404(Dipendente, email=email)

    # Filtro dal GET
    periodo = request.GET.get('periodo', 'mese_corrente')
    stato = request.GET.get('stato', 'Tutti')

    prenotazioni = Prenotazione.objects.filter(id_dipendente=dipendente).order_by('-data_prenotazione')

    # Filtro periodo
    today = datetime.today().date()
    if periodo == "mese_corrente":
        prenotazioni = prenotazioni.filter(data_prenotazione__month=today.month, data_prenotazione__year=today.year)
    elif periodo == "mese_precedente":
        last_month = today.month - 1 or 12
        year = today.year if today.month > 1 else today.year - 1
        prenotazioni = prenotazioni.filter(data_prenotazione__month=last_month, data_prenotazione__year=year)
    elif periodo == "ultimi_3_mesi":
        from datetime import timedelta
        three_months_ago = today - timedelta(days=90)
        prenotazioni = prenotazioni.filter(data_prenotazione__date__gte=three_months_ago)

    # Filtro stato
    if stato and stato != "Tutti":
        prenotazioni = prenotazioni.filter(stato=stato)

    # Paginazione (10 prenotazioni per pagina)
    paginator = Paginator(prenotazioni, 10)  # 10 prenotazioni per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'nome': dipendente.nome,
        'cognome': dipendente.cognome,
        'nome_azienda': dipendente.id_azienda.ragione_sociale,
        'ruolo': 'Dipendente',
        'prenotazioni': page_obj,
        'periodo': periodo,
        'stato': stato,
    }
    return render(request, 'area_dipendente.html', context)


def effettua_prenotazione(request):
    #  recupero dalla sessione l’ID della struttura
    struct_id = request.session.get('id_struttura')
    if not struct_id:
        return redirect('login')

    #  prendo i tavoli DI QUELLA struttura
    tavoli = Tavolo.objects.filter(struttura_associata=struct_id,disponibilità=True).order_by('id_tavolo')

    # prendo i piatti associati al responsabile di quella stessa struttura
    piatti = Piatto.objects.filter(id_responsabile__id_struttura=struct_id)

    # suddivido per tipo di piatto
    primi    = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.PRIMO)
    secondi = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.SECONDO)
    dessert  = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.DESSERT)

    # altrimenti mostriamo un po' il form
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

        # Questa salva la prenotazione
        prenotazione = Prenotazione.objects.create(
            data_prenotazione=data,
            totale_prezzo=totale,
            stato=Prenotazione.StatoPrenotazione.IN_ATTESA, 
            id_tavolo=tavolo,
            id_dipendente=dipendente
        )
        
        #  e qua salvo l'associazione tavolo-piatto 
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=primo)
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=secondo)
        Associazione.objects.create(id_tavolo=tavolo, id_piatto=dessert)

        # Torna la pagina di conferma
        return redirect('area_dipendente')


def elimina_prenotazione(request, id):
    if request.method == 'POST':
        prenotazione = get_object_or_404(Prenotazione, id_prenotazione=id)
        # Verifica che sia il proprietario
        if prenotazione.id_dipendente.email == request.session.get('user_email'):
            prenotazione.delete()
            messages.success(request, "Prenotazione eliminata con successo.")
        else:
            messages.error(request, "Non puoi eliminare questa prenotazione.")
    return redirect('area_dipendente')


def gestione_menu(request):
    # Recupera la struttura dal responsabile loggato 
    id_struttura = request.session.get('id_struttura')
    responsabile = Responsabile.objects.get(id_struttura=id_struttura)
    

    #----AGGIORNA STATO PRENOTAZIONE----
    if request.method == 'POST' and 'update_stato' in request.POST:
        prenotazione_id = request.POST['prenotazione_id']
        nuovo_stato = request.POST['nuovo_stato']
        pren = Prenotazione.objects.get(id_prenotazione=prenotazione_id)
        pren.stato = nuovo_stato
        pren.save()
        return redirect('gestione_menu')

    #----GESTIONE PIATTI NEL MENU----

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

    #----GESTIONE PRENOTAZIONI----
    
    data_filtro = request.GET.get('data', '')  # formato 'YYYY-MM-DD'
    stato_filtro = request.GET.get('stato', '')

    prenotazioni = Prenotazione.objects.filter(id_tavolo__struttura_associata=id_struttura).select_related('id_tavolo', 'id_dipendente')

    # Filtra per data se specificata
    if data_filtro:
        try:
            data_obj = datetime.strptime(data_filtro, '%Y-%m-%d').date()
            prenotazioni = prenotazioni.filter(data_prenotazione__date=data_obj)
        except ValueError:
            pass

    # Filtra per stato se specificato
    if stato_filtro:
        prenotazioni = prenotazioni.filter(stato=stato_filtro)

    # Piatti di quella mensa
    piatti = Piatto.objects.filter(id_responsabile=responsabile)
    primi = piatti.filter(tipo_piatto='primo piatto')
    secondi = piatti.filter(tipo_piatto='secondo piatto')
    dessert = piatti.filter(tipo_piatto='dessert')

    return render(request, 'area_gestore.html', {
        'primi': primi,
        'secondi': secondi,
        'dessert': dessert,
        'prenotazioni': prenotazioni.order_by('-data_prenotazione'),
        'data_filtro': data_filtro,
        'stato_filtro': stato_filtro,
        'nome' : responsabile.email,
        'ruolo': 'Gestore',
        'nome_azienda': responsabile.id_struttura.nome,
    })