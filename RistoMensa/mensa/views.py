from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from mensa.models import *
from datetime import date, datetime, timedelta
from django.core.paginator import Paginator
import hashlib

# Funzione che gestisce la visualizzazione della homepage
def index(request):
    return render(request, 'home.html')

# Funzione che gestisce il login degli utenti
def login(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        ruolo = request.POST.get('Ruolo')

        # Inizializzo le variabili per il profilo utente e l'ID della struttura
        profilo = None
        struttura_id = None
        
        # Se l'utente ha selezionato il ruolo 'Dipendente'
        if ruolo == 'Dipendente':
            try:
                # Cerco un profilo Dipendente con l'email fornita
                profilo = Dipendente.objects.get(email=email)
                # Ottengo l'ID della struttura associata al dipendente
                struttura_id = profilo.id_azienda.id_struttura.id_struttura
            except Dipendente.DoesNotExist:
                 # Se non esiste un Dipendente con quell'email, mostra un messaggio di errore
                messages.error(request, "Nessun dipendente con questa email.")

        # Se l'utente ha selezionato il ruolo 'Gestore'
        elif ruolo == 'Gestore':
            try:
                # Cerco un profilo Responsabile con l'email fornita
                profilo = Responsabile.objects.get(email=email)
                # Ottengo l'ID della struttura associata al responsabile
                struttura_id = profilo.id_struttura.id_struttura
            except Responsabile.DoesNotExist:
                 # Se non esiste un Gestore con quell'email, mostra un messaggio di errore
                messages.error(request, "Nessun gestore mensa con questa email.")

        else:
            messages.error(request, "Devi selezionare un ruolo valido.")
            return render(request, 'home.html')
        
        # Se è stato trovato un profilo valido
        if profilo:
            # Codifico la password fornita usando l'hash MD5
            hashed = hashlib.md5(password.encode()).hexdigest()
            
            # Confronto la password codificata con quella salvata nel database
            if hashed == profilo.password:
                # Salvo i dati nella sessione utente
                request.session['user_email']   = profilo.email
                request.session['ruolo']        = ruolo
                request.session['id_struttura'] = struttura_id  
                
                # Reindirizzo alla pagina corretta in base al ruolo
                if ruolo == 'Gestore':
                    return redirect('gestione_menu')
                else:
                    return redirect('area_dipendente')
            else:
                messages.error(request, "Password errata.")

        # torno nella pagina di login se ho errori
        return render(request, 'home.html')

    # Per richieste GET
    return render(request, 'home.html')



def annulla(request):
   return render(request, 'area_dipendente.html')

def area_dipendente(request):
   
    # Recupero il dipendente loggato dalla sessione tramite l'email
    email = request.session.get('user_email')
   
    dipendente = get_object_or_404(Dipendente, email=email)

    # Recupero i parametri di filtro dalla richiesta GET
    periodo = request.GET.get('periodo', 'mese_corrente')
    stato = request.GET.get('stato', 'Tutti')

    # Recupero tutte le prenotazioni del dipendente, ordinate dalla più recente
    prenotazioni = Prenotazione.objects.filter(id_dipendente=dipendente).order_by('-data_prenotazione')

    # Filtro periodo selezionato
    today = datetime.today().date()
   
    if periodo == "mese_corrente":
       
        # Mostra solo le prenotazioni del mese e anno attuali
        prenotazioni = prenotazioni.filter(data_prenotazione__month=today.month, data_prenotazione__year=today.year)
    
    elif periodo == "mese_precedente":
       
        # Calcolo il mese e l'anno del mese precedente
        last_month = today.month - 1 or 12
        year = today.year if today.month > 1 else today.year - 1
        prenotazioni = prenotazioni.filter(data_prenotazione__month=last_month, data_prenotazione__year=year)
    
    elif periodo == "ultimi_3_mesi":
        
        # Mostro solo le prenotazioni del mese precedente
        # timedelta rappresenta un intervallo di tempo esempio giorni, ore, ecc..
        # Qui lo uso per calcolare la data di 90 giorni fa
        three_months_ago = today - timedelta(days=90)
        prenotazioni = prenotazioni.filter(data_prenotazione__date__gte=three_months_ago)

    # Filtro stato
    if stato and stato != "Tutti":
        prenotazioni = prenotazioni.filter(stato=stato)

    # Paginazione (10 prenotazioni per pagina)
    paginator = Paginator(prenotazioni, 10)  # 10 prenotazioni per pagina
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

     # Prepara il contesto da passare al template HTML
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
    
    # Recupera l'ID della struttura associata all'utente autenticato dalla sessione
    struct_id = request.session.get('id_struttura')
    
    # Se l'utente non ha una struttura associata (non autenticato), reindirizzo al login
    if not struct_id:
        return redirect('login')


    # Recupera la data selezionata per la prenotazione (se presente) dai parametri GET
    data = request.GET.get('data')

    fasce_orarie = Prenotazione.FASCE_ORARIE

    # Salva la data odierna in formato stringa (es. '2025-06-25')
    today = date.today().strftime('%Y-%m-%d')

    # Recupera tutti i tavoli disponibili per la struttura dell’utente
    tavoli_disponibili = Tavolo.objects.filter(struttura_associata=struct_id, disponibilità=True).order_by('id_tavolo')

    # Se è stata selezionata una data, esclude i tavoli già prenotati per quel giorno
    if data:
        tavoli_prenotati = Prenotazione.objects.filter(data_prenotazione=data).values_list('id_tavolo', flat=True)
        tavoli_disponibili = tavoli_disponibili.exclude(id_tavolo__in=tavoli_prenotati)
   
    
    

    # prendo i piatti associati al responsabile di quella stessa struttura
    piatti = Piatto.objects.filter(id_responsabile__id_struttura=struct_id)

    # suddivido per tipo di piatto
    primi = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.PRIMO)
    secondi = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.SECONDO)
    frutta = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.FRUTTA)
    dessert = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.DESSERT)
    bevande = piatti.filter(tipo_piatto=Piatto.Tipologia_piatto.BEVANDA)

    
    # Mostra la pagina di prenotazione con i dati dinamici:
    return render(request, 'prenotazione.html', {
        'tavoli':   tavoli_disponibili,
        'primi':    primi,
        'secondi':  secondi,
        'dessert':  dessert,
        'frutta':   frutta,
        'bevande':  bevande,
        'tempo_cottura': Piatto.Tempo_cottura.choices,
        'contorno': Piatto.Tipologia_contorno.choices,
        'struttura': struct_id,
        'fasce_orarie': fasce_orarie,
        'today': today,
    })



def conferma_prenotazione(request):
    # Mostro il riepilogo della prenotazione prima della conferma definitiva da parte dell'utente.
    if request.method == 'POST' and 'confirm' not in request.POST:
      
        # Mi prendo i dati fondamentali dalla richiuesta POST
        
        data = request.POST.get('data')
        fascia_oraria = request.POST.get('fascia_oraria')
        id_tavolo = request.POST.get('tavolo')

        # ------------------ PRRIMI PIATTI -----------------
        # Costruisco la lista dei primi piatti selezionat
        primi_selezionati = request.POST.getlist('primi') # Lista degli id dei primi scelti
        primi_scelti = []   # Lista che conterrà: piatto, quantità, tempo_cottura
        totale_primi = 0    # Somma dei prezzi dei primi
        for id_piatto in primi_selezionati:
            primo = get_object_or_404(Piatto, id_piatto=id_piatto)
            # Recupero la quantità selezionata per questo piatto (default 1)
            qty = int(request.POST.get(f'primi_qty_{id_piatto}', 1))
            # Recupero il tempo di cottura selezionato per questo piatto 
            tempo_cottura = request.POST.get(f'primo_cottura_{id_piatto}', '')
            # Se la quantità è almeno 1, aggiungo il piatto e aggiorno il totale
            if qty > 0:
                primi_scelti.append({'piatto': primo, 'quantita': qty, 'tempo_cottura': tempo_cottura})
                totale_primi += primo.prezzo * qty
            

        # ------------------ SECONDI PIATTI -----------------
        # Costruisco la lista dei secondi piatti selezionati
        secondi_selezionati = request.POST.getlist('secondi')
        secondi_scelti = []
        totale_secondi = 0
        for id_piatto in secondi_selezionati:
            secondo = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'secondi_qty_{id_piatto}', 1))
            # Recupero il contorno selezionato per questo secondo (es: patate/insalata)
            contorno = request.POST.get(f'secondo_contorno_{id_piatto}', '')
            if qty > 0:
                secondi_scelti.append({'piatto': secondo, 'quantita': qty, 'contorno': contorno})
                totale_secondi += secondo.prezzo * qty
        
        # ------------------- FRUTTA ------------------------
        # Gestione della frutta selezionata (analogo a sopra, ma senza campo aggiuntivo)
        frutta_selezionati = request.POST.getlist('frutta')
        frutta_scelti = []
        totale_frutta = 0
        for id_piatto in frutta_selezionati:
            frutta = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'frutta_qty_{id_piatto}', 1))
            if qty > 0:
                frutta_scelti.append({'piatto': frutta, 'quantita': qty})
                totale_frutta += frutta.prezzo * qty


        # ------------------- DESSERT -----------------------
        # Gestione dei dessert selezionati 
        dessert_selezionati = request.POST.getlist('dessert')
        dessert_scelti = []
        totale_dessert = 0
        for id_piatto in dessert_selezionati:
            dessert = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'dessert_qty_{id_piatto}', 1))
            if qty > 0:
                dessert_scelti.append({'piatto': dessert, 'quantita': qty})
                totale_dessert += dessert.prezzo * qty


        # ------------------- BEVANDE -----------------------
        # Gestione delle bevande selezionate
        bevande_selezionate = request.POST.getlist('bevande')
        bevande_scelte = []
        totale_bevande = 0
        for id_piatto in bevande_selezionate:
            bevande = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'bevande_qty_{id_piatto}', 1))
            if qty > 0:
                bevande_scelte.append({'piatto': bevande, 'quantita': qty})
                totale_bevande += bevande.prezzo * qty
                
        
       
        tavolo = get_object_or_404(Tavolo, id_tavolo=id_tavolo)
       
        totale_prezzo = 0
        totale_prezzo = totale_primi + totale_secondi + totale_frutta + totale_dessert + totale_bevande

       
        # Passa nel conferma_prenotazione.html
        return render(request, 'conferma_prenotazione.html', {
            'data': data,
            'tavolo': tavolo,
            'primi_scelti': primi_scelti,
            'secondi_scelti': secondi_scelti,
            'frutta_scelta': frutta_scelti,
            'dessert_scelto': dessert_scelti,
            'bevanda_scelta': bevande_scelte,
            'totale': totale_prezzo,
            'fascia_oraria': fascia_oraria,
        })
    elif request.method == 'POST' and 'confirm' in request.POST:
        # infine se è stato premuto conferma salvo tutto
        data_str = request.POST.get('data')
        data = datetime.strptime(data_str, '%Y-%m-%d').date()
        fascia_oraria = request.POST.get('fascia_oraria')        
        

        id_tavolo = request.POST.get('tavolo')
    
        # ------------------ PRRIMI PIATTI -----------------
        #  # Stessa logica di raccolta dei piatti già vista sopra
        primi_selezionati = request.POST.getlist('primi')
        primi_lista = []
        totale_primi = 0
        for id_piatto in primi_selezionati:
            primo = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'primi_qty_{id_piatto}', 1))
            tempo_cottura = request.POST.get(f'primo_cottura_{id_piatto}', '')
            if qty > 0:
                primi_lista.append({'piatto': primo, 'quantita': qty, 'tempo_cottura': tempo_cottura })
                totale_primi += primo.prezzo * qty
              
        
         # ------------------ SECONDI PIATTI -----------------
        secondi_selezionati = request.POST.getlist('secondi')
        secondi_scelti = []
        totale_secondi = 0
        for id_piatto in secondi_selezionati:
            secondo = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'secondi_qty_{id_piatto}', 1))
            contorno = request.POST.get(f'secondo_contorno_{id_piatto}', '')
            if qty > 0:
                secondi_scelti.append({'piatto': secondo, 'quantita': qty, 'contorno': contorno})
                totale_secondi += secondo.prezzo * qty

        # ------------------- FRUTTA ------------------------  
        frutta_selezionati = request.POST.getlist('frutta')
        frutta_scelti = []
        totale_frutta = 0
        for id_piatto in frutta_selezionati:
            frutta = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'frutta_qty_{id_piatto}', 1))
            if qty > 0:
                frutta_scelti.append({'piatto': frutta, 'quantita': qty})
                totale_frutta += frutta.prezzo * qty

        # ------------------- DESSERT -----------------------
        dessert_selezionati = request.POST.getlist('dessert')
        dessert_scelti = []
        totale_dessert = 0
        for id_piatto in dessert_selezionati:
            dessert = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'dessert_qty_{id_piatto}', 1))
            if qty > 0:
                dessert_scelti.append({'piatto': dessert, 'quantita': qty})
                totale_dessert += dessert.prezzo * qty

        # ------------------- BEVANDE -----------------------
        bevande_selezionate = request.POST.getlist('bevande')
        bevande_scelte = []
        totale_bevande = 0
        for id_piatto in bevande_selezionate:
            bevande = get_object_or_404(Piatto, id_piatto=id_piatto)
            qty = int(request.POST.get(f'bevande_qty_{id_piatto}', 1))
            if qty > 0:
                bevande_scelte.append({'piatto': bevande, 'quantita': qty})
                totale_bevande += bevande.prezzo * qty
                print("totale bevande:", totale_bevande)

       
        tavolo = get_object_or_404(Tavolo, id_tavolo=id_tavolo)
       
        totale_prezzo = 0
        totale_prezzo = totale_primi + totale_secondi + totale_frutta + totale_dessert + totale_bevande

        email = request.session.get('user_email')
        dipendente = get_object_or_404(Dipendente, email=email)


        # --- CONTROLLO PER DOPPIA PRENOTAZIONE ---
        prenotazione_esistente = Prenotazione.objects.filter(id_dipendente=dipendente,data_prenotazione=data,stato__in=[Prenotazione.StatoPrenotazione.IN_ATTESA, Prenotazione.StatoPrenotazione.CONFERMATA]).exists()

        if prenotazione_esistente:
            messages.error(request, "Hai già una prenotazione confermata per questa data!")
            return redirect('prenotazione')  # O dove vuoi tornare
     
        Prenotazione.objects.create(
            data_prenotazione=data,
            fascia_oraria=fascia_oraria,
            totale_prezzo=totale_prezzo,
            stato=Prenotazione.StatoPrenotazione.IN_ATTESA,
            id_tavolo=tavolo,
            id_dipendente=dipendente
        )
       
        tavolo.disponibilità = False
        tavolo.save()
    
        return redirect('area_dipendente')
    else:
        return redirect('prenotazione')

def elimina_prenotazione(request, id):
    if request.method == 'POST':
        prenotazione = get_object_or_404(Prenotazione, id_prenotazione=id)
        if prenotazione.id_dipendente.email == request.session.get('user_email'):
            prenotazione.stato = Prenotazione.StatoPrenotazione.ANNULLATA
            prenotazione.save()
            # Rendi il tavolo disponibile di nuovo
            tavolo = prenotazione.id_tavolo
            tavolo.disponibilità = True
            tavolo.save()
            messages.success(request, "Prenotazione annullata con successo.")
        else:
            messages.error(request, "Non puoi annullare questa prenotazione.")
    return redirect('area_dipendente')


def gestione_menu(request):
    # Recupera la struttura dal responsabile loggato 
    id_struttura = request.session.get('id_struttura')
    responsabile = Responsabile.objects.get(id_struttura=id_struttura)
    

    # ----AGGIORNA STATO PRENOTAZIONE----
    if request.method == 'POST' and 'update_stato' in request.POST:
        prenotazione_id = request.POST['prenotazione_id']
        nuovo_stato = request.POST['nuovo_stato']
        prenotazione = Prenotazione.objects.get(id_prenotazione=prenotazione_id)
        prenotazione.stato = nuovo_stato
        prenotazione.save()
        if nuovo_stato == Prenotazione.StatoPrenotazione.ANNULLATA:
            tavolo = prenotazione.id_tavolo
            tavolo.disponibilità = True
            tavolo.save()
        return redirect('gestione_menu')

    # ----GESTIONE PIATTI NEL MENU----

    # Aggiunta piatto
    if request.method == 'POST' and 'add_piatto' in request.POST:
        nome = request.POST['nome']
        prezzo = request.POST['prezzo']
        tipo = request.POST['tipo_piatto']
        #cottura = request.POST['tipo_cottura']
        contorno = request.POST.get('tipologia_contorno')  # Usa get per evitare KeyError
        origine_frutta = request.POST.get('origine_frutta')  # Per la frutta
        tipo_dessert = request.POST.get('tipologia_dessert')  # Per i dessert
        alcolica = request.POST.get('alcolica') == 'on'  # Checkbox per bevande alcoliche
    

        Piatto.objects.create(
            nome=nome,
            prezzo=prezzo,
            contorno=contorno,
            origine_frutta=origine_frutta,
            tipo_dessert=tipo_dessert,
            alcolica=alcolica,
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

    # ----GESTIONE PRENOTAZIONI----
    
    data_filtro = request.GET.get('data', '')  # formato 'YYYY-MM-DD'
    stato_filtro = request.GET.get('stato', '')
    prenotazioni = Prenotazione.objects.filter(id_tavolo__struttura_associata=id_struttura).select_related('id_tavolo', 'id_dipendente')

    # Filtra per data se specificata
    if data_filtro:
        try:
            data_obj = datetime.strptime(data_filtro, '%Y-%m-%d').date()
            prenotazioni = prenotazioni.filter(data_prenotazione=data_obj)
        except ValueError:
            pass

    # Filtra per stato se specificato
    if stato_filtro:
        prenotazioni = prenotazioni.filter(stato=stato_filtro)

    # Piatti di quella mensa
    piatti = Piatto.objects.filter(id_responsabile=responsabile)
    primi = piatti.filter(tipo_piatto='primo piatto')
    secondi = piatti.filter(tipo_piatto='secondo piatto')
    frutta = piatti.filter(tipo_piatto='frutta')
    dessert = piatti.filter(tipo_piatto='dessert')
    bevande = piatti.filter(tipo_piatto='bevande')

    tavoli_prenotati = Tavolo.objects.filter(struttura_associata=id_struttura,disponibilità=False)

    return render(request, 'area_gestore.html', {
        'primi': primi,
        'secondi': secondi,
        'tipologia_contorno': Piatto.Tipologia_contorno.choices,
        'origine_frutta': Piatto.Tipologia_origine_frutta.choices,
        'tipologia_dessert': Piatto.Tipologia_dessert.choices,
        'frutta': frutta,
        'dessert': dessert,
        'bevande': bevande,
        'prenotazioni': prenotazioni.order_by('-data_prenotazione'),
        'data_filtro': data_filtro,
        'stato_filtro': stato_filtro,
        'nome' : responsabile.email,
        'ruolo': 'Gestore',
        'nome_azienda': responsabile.id_struttura.nome,
        'tavoli_prenotati': tavoli_prenotati,
    })



def reset_tavoli_struttura(request):
 
    id_struttura = request.session.get('id_struttura')

    if not id_struttura:
        messages.error(request, "Struttura non trovata.")
        return redirect('gestione_menu')

    Tavolo.objects.filter(struttura_associata=id_struttura).update(disponibilità=True)
    messages.success(request, "Tutti i tavoli della tua struttura sono stati resettati a disponibili.")
    return redirect('gestione_menu')

def reset_tavolo_singolo(request, id_tavolo):
    if request.method == 'POST':
        
        tavolo = get_object_or_404(Tavolo, id_tavolo=id_tavolo)
        tavolo.disponibilità = True
        tavolo.save()
    return redirect('gestione_menu')