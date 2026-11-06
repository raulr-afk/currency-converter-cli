import urllib.request
import json

def converti_valuta(importo, da_valuta, a_valuta):
    # Utilizziamo un'API pubblica e gratuita che non richiede registrazione per scopi dimostrativi
    url = f"https://er-api.com{da_valuta.upper()}"
    
    try:
        # Effettua la richiesta HTTP a internet per scaricare i tassi di cambio aggiornati
        connessione = urllib.request.urlopen(url)
        dati = json.loads(connessione.read().decode())
        
        # Verifica se la valuta di destinazione esiste nei dati ricevuti
        tassi = dati.get("rates", {})
        if a_valuta.upper() in tassi:
            tasso_cambio = tassi[a_valuta.upper()]
            risultato = importo * tasso_cambio
            
            # Stampa i risultati a schermo
            print(f"--- TASSI IN TEMPO REALE (Aggiornati a: {dati.get('time_last_update_utc')}) ---")
            print(f"{importo} {da_valuta.upper()} equivalgono a: {risultato:.2f} {a_valuta.upper()}")
            print(f"Tasso di cambio attuale: 1 {da_valuta.upper()} = {tasso_cambio} {a_valuta.upper()}")
        else:
            print(f"Errore: La valuta di destinazione '{a_valuta}' non è supportata.")
            
    except Exception as e:
        print(f"Errore di connessione o di rete: {e}")

# Testiamo il programma simulando una conversione da 100 Dollari (USD) in Euro (EUR)
valore_test = 100
valuta_partenza = "USD"
valuta_arrivo = "EUR"

print(f"Avvio simulazione: Conversione di {valore_test} {valuta_partenza} in {valuta_arrivo}...\n")
converti_valuta(valore_test, valuta_partenza, valuta_arrivo)
