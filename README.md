# stanovistats_scraper - Projekat za skrejping nekretnina

## Pregled

Ovaj projekat, napisan u Python-u, predstavlja maleni web skrejper dizajniran za prikupljanje informacija o cenama stanova i drugim povezanim detaljima sa popularnog onlajn izvora. Prikupljeni podaci zatim se čuvaju u MongoDB bazi podataka radi dalje analize ili upotrebe.

## Funkcionalnosti

1. **Web Skrejping:** Koristi tehnike web skrejpinga za izdvajanje informacija o cenama stanova, lokaciji i drugim relevantnim podacima sa sajtova za nekretnine.

2. **Integracija sa MongoDB-om:** Čuva prikupljene podatke u MongoDB bazi podataka radi lakšeg dohvata i manipulacije.

3. **Prilagodljivost:** Lako se prilagođava kako bi ciljao različite sajtove za nekretnine ili se prilagodio promenama u strukturi sajta.

## Preduslovi

- Python 3.x
- MongoDB instaliran i pokrenut / Hostovan MongoDB Atlas
- Potrebni Python paketi se mogu instalirati koristeći:

    ```bash
    pip install -r requirements.txt
    ```

## Korišćenje

1. **Klonirajte repozitorijum:**

    ```bash
    git clone https://github.com/belegisanin/stanovistats_scraper.git
    ```

2. **Navigirajte do direktorijuma projekta:**

    ```bash
    cd stanovistats_scraper
    ```

3. **Konfiguracija:**

    Napraviti datoteku `.env` kako biste dodali URL-ove sajtova za nekretnine koje želite obraditi i auth za MongoDB.

4. **Pokrenite Skrejper:**

    ```bash
    python main.py
    ```

    Ovo će pokrenuti proces skrejpinga i popuniti MongoDB bazu podataka prikupljenim podacima.

## Konfiguracija

Datoteka `.env` sadrži parametre kao što su MongoDB detalji veze i URL-ovi sajtova. Prilagodite ovu datoteku prema svojim preferencama.

```python
# Konfiguracija MongoDB-a
CONNECTION_STRING = mongodb://localhost:27017/...

# URL za skrejping
URL=https://...
```

## Napomena

1. Proverite da li vaše aktivnosti web skrejpinga poštuju uslove korišćenja ciljanih sajtova.

2. Periodično proveravajte i ažurirajte skrejper u skladu sa promenama u strukturi sajtova.

3. Ovaj projekat je u svrhu edukacije i treba ga koristiti odgovorno.

## Licenca

Ovaj projekat se nalazi pod MIT Licencom / This project is licenced under the MIT Licence

Slobodno doprinesite, prijavite probleme ili predložite poboljšanja!
