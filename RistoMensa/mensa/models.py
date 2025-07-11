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

class Amministratore(models.Model):
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
    
    class Tempo_cottura(models.TextChoices):
        BREVE = 'breve',
        MEDIO = 'medio',
        LUNGO = 'lungo',


    class Tipologia_piatto(models.TextChoices):
        PRIMO = 'primo piatto',
        SECONDO = 'secondo piatto',
        FRUTTA = 'frutta',
        DESSERT = 'dessert',
        BEVANDA = 'bevande',
    
    class Tipologia_contorno(models.TextChoices):
        PATATE = 'patate al forno',
        VERDURE = 'verdure grigliate',
        INSALATA = 'insalata mista',

    class Tipologia_origine_frutta(models.TextChoices):
        LOCALE = 'locale',
        ESTERA = 'esterna',
        BIOLOGICA = 'biologica',
        CONVENZIONALE = 'convenzionale',
    
    class Tipologia_dessert(models.TextChoices):
        GELATO = 'gelato',
        TORTA = 'torta',
        BUDINO = 'budino',
        SEMIFREDDO = 'semifreddo',
    tipo_cottura = EnumField(choices=Tempo_cottura.choices, null=True) 
    tipo_piatto = EnumField(choices=Tipologia_piatto.choices)
    contorno = EnumField(choices=Tipologia_contorno.choices, null=True)
    origine_frutta = EnumField(choices=Tipologia_origine_frutta.choices, null=True)
    tipo_dessert = EnumField(choices=Tipologia_dessert.choices, null=True)
    alcolica = models.BooleanField(default=False)
    id_responsabile = models.ForeignKey(Responsabile, on_delete=models.CASCADE, related_name='piatto')


class Tavolo(models.Model):
    id_tavolo = models.IntegerField(primary_key=True)
    numero_posti_disponibili = models.IntegerField()
    disponibilità = models.BooleanField(default=True)
    struttura_associata = models.ForeignKey(Struttura,on_delete=models.CASCADE,related_name='tavolo')

class Prenotazione(models.Model):
    id_prenotazione = models.AutoField(primary_key=True)
    data_prenotazione = models.DateField()

    FASCE_ORARIE = [
        ('12:00-12:30', '12:00-12:30'),
        ('12:30-13:00', '12:30-13:00'),
        ('13:00-13:30', '13:00-13:30'),
        ('13:30-14:00', '13:30-14:00'),
        ('14:00-14:30', '14:00-14:30'),
        ('14:30-15:00', '14:30-15:00'),
    ]
    fascia_oraria = models.CharField(max_length=20, choices=FASCE_ORARIE)

    class StatoPrenotazione(models.TextChoices):
        IN_ATTESA = 'in attesa',
        ANNULLATA = 'annullata',
        CONFERMATA = 'confermata',
    
    
    stato = EnumField(choices=StatoPrenotazione.choices, default=StatoPrenotazione.IN_ATTESA)
    totale_prezzo = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    id_tavolo = models.ForeignKey(Tavolo, on_delete=models.CASCADE, related_name='prenotazione')
    id_dipendente = models.ForeignKey(Dipendente, on_delete=models.CASCADE, related_name='prenotazione')

    # mi serve per la quantità della roba
    piatti = models.ManyToManyField('Piatto', through='Associazione')

class Associazione(models.Model):
    prenotazione = models.ForeignKey('Prenotazione', on_delete=models.CASCADE)
    piatto = models.ForeignKey('Piatto', on_delete=models.CASCADE)
    quantita = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantita} x {self.piatto.nome} (Prenotazione {self.prenotazione.id_prenotazione})"
