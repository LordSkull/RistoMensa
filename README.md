# **Sistema Informativo – Gestione Mense Aziendali “RistoMensa”**
Il progetto RistoMensa nasce con l’obiettivo di digitalizzare e semplificare la gestione delle mense aziendali tramite un’applicazione web moderna.
L’applicativo consente a dipendenti e gestori di accedere a funzionalità differenziate per la gestione delle prenotazioni dei pasti, dei menù settimanali e delle strutture aziendali, sostituendo i vecchi processi cartacei con una soluzione più sicura, efficiente e accessibile.

---

## **Indice**
1. [Obiettivo del Sistema](#obiettivo-del-sistema)  
2. [Tecnologie Utilizzate](#tecnologie-utilizzate)  
3. [Installazione](#installazione)  
4. [Configurazione del Database](#configurazione-del-database)  
5. [Utilizzo](#utilizzo)  
6. [Licenza](#licenza)  

---

## **Obiettivo del Sistema**
La piattaforma è progettata per supportare diverse categorie di utenti (dipendenti, gestori) e offre:
- **Login Differenziato**, in base al ruolo (Gestore / Dipendente).
- **Prenotazione pasti**, per i dipendenti, con gestione settimanale.
- **Gestione dei menù**, da parte dei gestori, con visualizzazione e modifica dei piatti.
- **Gestione delle strutture aziendale**, e del personale.
- **Visualizzazione cronolgoia prenotazione** da parte degli utenti.
- **Controllo degli acccessi**  basato su sessione utente 
L’architettura assicura **modularità, scalabilità e sicurezza**, pur mantenendo un’interfaccia semplice e fruibile da qualsiasi dispositivo.

---

## **Tecnologie Usate**
### **Backend**
- **Python** – Linguaggio di programmazione principale.
- **Django** – Framework per la logica server-side.
- **mysqlclient** – Libreria per collegare Django a MySQL/MariaDB.  

### **Database**
- **MariaDB / MySQL** – Sistema di gestione relazionale dei dati.  

### **Frontend**
- **HTML / CSS** – Utilizzati per l’interfaccia utente.  
- **Bootstrap** - Framework lato frontend


## **Installazione**
1. Per eseguire l’applicazione, è necessario:  
- **Avere Python (≥3.10) installato** nel proprio ambiente.  
- **MySQL/MariaDB**, preferibilmente con phpmyadmin.  
- **pip** 

2. Clonare il progetto
```bash
git clone https://github.com/LordSkull/RistoMensa.git
cd RistoMensa
```
3. **Creare e attivare un ambiente virtuale**
```bash
python -m venv myvenv
```
Linux/macOS
```
source venv/bin/activate
```
Windows

In cmd
```
venv\Scripts\activate.bat
```
In PowerShell
```
.\venv\Scripts\Activate.ps1
```

4. **Installare le dipendenze**
```bash
pip install -r requirements.txt
```
