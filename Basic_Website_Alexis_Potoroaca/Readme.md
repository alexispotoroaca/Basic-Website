# Parfumeria Baneasa - Aplicatie Shopping Cart

Aceasta este o aplicatie web simpla pentru un magazin de parfumuri, realizata cu Flask, HTML si Bootstrap. Utilizatorii pot naviga printre produse, le pot adauga in cos si pot plasa o comanda printr-un formular de checkout.

## Functionalitati

### Lista de produse
- Afiseaza toate parfumurile disponibile in format grila responsive.
- Fiecare produs are un card cu imagine, nume, pret si buton "Cumpara".

### Cos de cumparaturi
- Produsele pot fi adaugate in cos.
- Cosul este salvat in sesiune si persista pe durata navigarii.
- Se pot sterge produse individual.
- Pe pagina `/cart` se afiseaza continutul cosului si pretul total.

### Checkout
- Formularul se acceseaza la ruta `/checkout`.
- Afiseaza lista produselor comandate si totalul de plata.
- Contine campuri pentru datele clientului:
  - full_name
  - email
  - phone
  - address
  - payment_method (card, bank_transfer, cash)
- Comenzile sunt salvate pe server in format JSON in folderul `data/orders`.

### Rulare cu Docker
- Aplicatia poate fi rulata in container Docker.
- Comenzi:
  docker build -t iap1-tema .
  docker run -p 5000:5000 -it iap1-tema
