# NASA Datu Vizualizācijas un Meklēšanas Rīks
### Ievads
 Astronomijas un kosmosa izpētes dati ir plaši pieejami, tomēr plašai sabiedrībai un skolēniem tie bieži vien nav viegli pieejami vai saprotami. NASA piedāvā vairākas publiskas API (lietojumprogrammu saskarnes), kas nodrošina piekļuvi milzīgam datu apjomam, ieskaitot Mars Rover fotoattēlus, astronomiskos attēlus (APOD - Astronomy Picture of the Day) un citus zinātniskos datus. Problēma ir tāda, ka šie dati nav viegli pieejami, analizējami un vizualizējami bez speciālām programmēšanas zināšanām. 

Mūsdienās astronomijas izglītība un kosmosa izpēte ir būtiska jauniešu intereses veicināšanai par STEM (zinātne, tehnoloģija, inženierzinātnes un matemātika) nozarēm. Šis projekts risina nepieciešamību pēc vienkāršas un izglītojošas sistēmas, kas ļauj lietotājiem piekļūt un analizēt kosmosa datus, tādējādi veicinot interesi par astronomiju un programmēšanu.
## Darba aktualitāte: 
NASA piedāvā atvērtus datu API, bet daudziem lietotājiem trūkst programmēšanas iemaņu vai ērtas piekļuves šiem datiem. 

Skolēni, pasniedzēji un astronomijas entuziasti bieži meklē attēlus vai informāciju par konkrētiem notikumiem (piem., meteoru lietus, Zemes attēli no satelītiem), bet nav vienkārša rīka, kas to nodrošinātu.
## Darba mērķis: 
Izstrādāt Python balstītu lietotni, kas pieslēdzas NASA API, sniedz lietotājam iespēju meklēt un skatīt NASA attēlus, reāllaika informāciju un saglabāt iecienītākos rezultātus datubāzē.
## Lietotāja Ceļvedis:
Šī NASA attēlu meklēšanas lietotne ir vienkārši lietojama programma, kas ļauj lietotājam meklēt NASA publiski pieejamos attēlus, izmantojot atslēgvārdus. 

Programmas palaišanai nepieciešams Visual Studio Code, Python 3 un dažas bibliotēkas, ko var uzstādīt ar:

#### pip install requests Pillow 

### Programmas palaišana:
•	Pārliecinies, ka datorā ir ieinstalēts un uzstādīts Visual Studio Code un Python 3.

•	Atver main.py failu un terminālī instalē vajadzīgās bibliotēkas ar komandu:

#### pip install requests Pillow
•	Palaid main.py failu, uzsākot kodu.
### Attēlu meklēšana: 
•	Ievadi meklējamo vārdu (piem. “Mars”) teksta laukā.

•	Spied pogu “Meklēt”.

•	Attēli tiks ielādēti no NASA datubāzes un uzklikšķinot pogu “Atvērt attēlu pārlūkā” tiks atvērts attēls jaunā interneta logā.
### Attēla lejupielāde:
•	Spied pogu “Lejupielādēt attēlu”.

•	Attēls tiks saglabāts uz datora mapē, kur atrodas tavs main.py fails.
### Favorītu saglabāšana:
•	Spied pogu “Pievieniot favorītiem” zem izvēlētā attēla.

•	Attēla dati tiks ierakstīti datubāzē, kur atrodas tavs main.py fails.

### Favorītu apskate:
•	Spied pogu “Skatīt favorītus”.\

•	Tiks atvērts jauns logs ar visiem 
saglabātajiem attēliem.

### Padomi:
•	Izmanto vienkāršus atslēgvārdus (angļu valodā), piemēram: “moon”, “earth”, “apollo”.

•	Favorītu sarakstu var tīrīt, izdzēšot attiecīgus ierakstus no datubāzes.
## Secinājumi

Projekta izstrādes gaitā tika veiksmīgi sasniegti izvirzītie mērķi un uzdevumi – izveidota funkcionāla Python programmatūra, kas izmanto NASA publisko API, lai lietotājam sniegtu iespēju meklēt un skatīt NASA attēlus pēc izvēlēta atslēgvārda. 

Programmatūras izstrāde tika veikta atbilstoši klasiskajam programmatūras dzīves cikla modelim, sākot ar problēmas izpēti un mērķauditorijas vajadzību noteikšanu, turpinot ar prasību specifikāciju, risinājuma projektēšanu, realizāciju, testēšanu un noslēdzot ar produkta demonstrēšanu.

Projekts parāda skolēna spējas praktiski pielietot programmēšanas II kursā iegūtās zināšanas – tika izmantotas vairākas Python bibliotēkas (requests, sqlite3, cryptography), objektorientētā programmēšana ar klasēm, kā arī izstrādāta datubāze ar saistītām tabulām, kurā tiek saglabāti lietotāju dati un viņu favorītattēli.

## Licence

Programmatūra tiek izplatīta saskaņā ar MIT licenci. Tas nozīmē, ka:

#### ●	Programmatūru var brīvi izmantot, modificēt un izplatīt

#### ●	Nepieciešams saglabāt oriģinālo autora paziņojumu

#### ●	Programmatūra tiek piedāvāta "kā ir", bez jebkādām garantijām

NASA API dati ir pakļauti NASA datu izmantošanas noteikumiem, kas pieejami: https://api.nasa.gov/
