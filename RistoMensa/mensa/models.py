from django.db import models
from django_mysql.models import EnumField
# Create your models here.

class Struttura(models.Model):
    id_struttura = models.IntegerField(primary_key=True)
    nome = models.TextField(max_length=100)
    indirizzo = models.TextField(max_length=100)
    numero_tavoli_disponibili = models.IntegerField()

class Azienda(models.Model):
    id_azienda = models.IntegerField(primary_key=True)
    ragione_sociale = models.TextField(max_length=100)
    partita_iva = models.TextField(max_length=11)
    indirizzo = models.TextField(max_length=100)
    id_struttura = models.ForeignKey(Struttura, on_delete=models.CASCADE, related_name='azienda')

class Amministatore(models.Model):
    id_amministratore = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.TextField(max_length=32)
    id_azienda = models.ForeignKey(Azienda, on_delete=models.CASCADE, related_name='amministratore')


class Dipendente(models.Model):
    id_dipendente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    cognome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=32)
    id_azienda = models.ForeignKey(Azienda, on_delete=models.CASCADE, related_name='dipendente')

class Responsabile(models.Model):
    id_responsabile = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=32)
    id_struttura = models.ForeignKey(Struttura, on_delete=models.CASCADE, related_name='responsabile')

class Piatto(models.Model):
    id_piatto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80)
    descrizione = models.CharField(max_length=255, null=True)
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Tipologia_piatto(models.TextChoices):
        PRIMO = 'primo piatto',
        SECONDO = 'secondo piatto',
        DESSERT = 'dessert',
    
    tipo_piatto = EnumField(choices=Tipologia_piatto.choices)
    id_responsabile = models.ForeignKey(Responsabile, on_delete=models.CASCADE, related_name='piatto')


class Tavolo(models.Model):
    id_tavolo = models.IntegerField(primary_key=True)
    numero_posti_disponibili = models.IntegerField()
    disponibilità = models.BooleanField(default=True)
    struttura_associata = models.ForeignKey(Struttura,on_delete=models.CASCADE,related_name='tavolo')

class Prenotazione(models.Model):
    id_prenotazione = models.AutoField(primary_key=True)
    data_prenotazione = models.DateTimeField()
   # descrizione_ordine = models.TextField(max_length=255, null=True, blank=True)
    class StatoPrenotazione(models.TextChoices):
        IN_ATTESA = 'in attesa',
        ANNULLATA = 'annullata',
        CONFERMATA = 'confermata',
    
    
    stato = EnumField(choices=StatoPrenotazione.choices, default=StatoPrenotazione.IN_ATTESA)
    totale_prezzo = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    id_tavolo = models.ForeignKey(Tavolo, on_delete=models.CASCADE, related_name='prenotazione')
    id_dipendente = models.ForeignKey(Dipendente, on_delete=models.CASCADE, related_name='prenotazione')


class Associazione(models.Model):
    id_tavolo = models.ForeignKey(Tavolo, on_delete=models.CASCADE, related_name='associazione')
    id_piatto = models.ForeignKey(Piatto, on_delete=models.CASCADE, related_name='associazione')