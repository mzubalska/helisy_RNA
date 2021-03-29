# helisy_RNA

Baza danych RNA Bricks gromadzi informacje na temat interakcji motywów RNA
miedzy soba oraz w kontakcie z białkami. Sklasyfikowane parowania wystepujace w bazie
sa otrzymywane za pomoca klasyfikatora ClaRNA.

RNA Bricks: http://iimcb.genesilico.pl/rnabricks/

ClaRNA: http://genesilico.pl/clarna/

Pierwszym etapem korzystania z serwisu było uzyskanie listy wszystkich mozliwych parowan
o wysokiej rozdzielczosci dla „stems” i „loops” za pomoca wyszukiwarki zawartej
na stronie. W tym celu zdefiniowalismy „Query” jako:

  >segment1
 .*
 >segment2
 .*
i dokonalismy wyszukania, najpierw dla „stems” pózniej dla „loops” o wysokiej rozdzielczosci.
Wyniki dwóch wyszukiwan pobralismy w formacie .fasta z serwisu, a nastepnie
poddalismy obróbce w celu uzyskania nazw pdb z których to fragmenty pochodza, aby
pobrac pliki .CSV, które zawierałyby adnotacje pochodzace z ClaRNA na temat parowan.
W tym celu skorzystalismy z programu: 'pobranie.py'

• Metoda get pdb list hq(fasta, list pdb) przyjmuje pobrany plik z serwisu w formacie
.fasta oraz nazwe do pliku w którym beda zapisywane kolejne nazwy pdb, pochodzace
od nazw plików .pdb zawierajacych parowanie.

• Metoda download(pdb list) przyjmuje plik z lista wszystkich nazw pdb, a nastepnie
w petli pobiera kolejne pliki w formacie .CSV o zadanej nazwie.
Aby uzyskac wynik w terminalu uzywamy komendy:
python pobranie.py nazwa pliku fasta nazwa dla pliku pdb

Po uzyskaniu plików .CSV, poddalismy je równiez obróbce, w celu usuniecia niesklasyfikowanych
parowan z plików i zapisania wyników w odpowiednim formacie. 
Do usuniecia niesklasyfikowanych parowan z plików i zapisania wyników w odpowiednim
formacie posłuzylismy sie skryptem: pary_rnaview.py

• Metoda zapis(plik in, plik out) przyjmuje plik in, czyli plik w formacie .CSV, oraz
plik out, czyli nazwe do zapisu nowego pliku w formacie .bp. Metoda ta przekształca
dane z CSV do nastepujacego formatu:
zasada nr polozenia nazwa lancucha zasada nr polozenia nazwa lancucha parowanie

• Metoda zasady(plik1, plik2) przyjmuje plik1 czyli plik w formacie .bp oraz plik2
czyli nazwe do zapisu wyniku w formacie .txt. Dzieki tej metodzie eliminujemy z
pliku wszystkie kanoniczne parowania.

• Metoda wczytaj(dirpath) – słuzy do wczytywania kolejnych plików CSV zawartych
w katalogu do obróbki przez metode zapis(plik in, plik out)

• Metoda wczytaj2(path) – słuzy do wczytywania kolejnych plików bp zawartych w
katalogu do obróbki przez metode zasady(plik1, plik2)
Tym sposobem otrzymalismy 3344 plików zawierajacych niekanoniczne parowania.

UWAGA!
Serwis RNA Bricks aktualnie podlega przebudowie, nie ma juz mozliwosci bezposredniego
pobierania plików w formacie .CSV. W tej chwili jest mozliwosc pobrania paczki .zip dla
danego motywu RNA, która zawiera pliki w formacie: .fasta, .pdb oraz .txt. W plikach o
rozszerzeniu .txt zawarte sa adnotacje o rodzaju parowania z RNA Bricks, jak i równiez
z klasyfikatorów MC-Annotate oraz RNAview.
