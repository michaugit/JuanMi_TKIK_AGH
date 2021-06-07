## 1. Kompilator własnego języka "JuanMI" do języka Python

##2. Autorzy projektu: 
  * Anna Gnoińska: III rok, Informatyka
  * Julia Ignacyk: III rok, Informatyka
  * Michał Pieniądz: III rok, Informatyka

##3. Założenia programu:
  * ogólne cele programu: stworzenie kompilatora dla własnego języka programowania JuanMI, który ma na celu ułatwienie nauki języka programowania za pomocą wprowadzenia słów kluczowych w języku polskim
  * rodzaj translatora: kompilator
  * planowany wynik działania proframu: kompilator języka JuanMI do języka Python (wynik w postaci pliku .py)
  * planowany język implementacji: Python
  * sposób implementacji skanera/parsera: użycie generatora ANTLR 

##4. Tokeny:
```
TKN_END_LINE            :('.');
TKN_NUMBER              :('LICZBA');
TKN_STRING              :('TEKST');
TKN_BOOL                :('PRAWDA_FALSZ');
TKN_LIST                :('LISTA');
TKN_IF                  :('JEZELI');
TKN_ELSE                :('INACZEJ');
TKN_ELIF                :('JEZELI_INACZEJ');
TKN_FOR                 :('DLA');
TKN_FROM                :('OD');
TKN_TO                  :('DO');
TKN_WHILE               :('DOPOKI');
TKN_NOT                 :('NIE');
TKN_AND                 :('ORAZ');
TKN_OR                  :('LUB');
TKN_FUNCTION            :('FUNKCJA');
TKN_RETURN              :('ZWROC');
TKN_PRINT               :('WYPISZ');
TKN_TRUE                :('PRAWDA');
TKN_FALSE               :('FALSZ');
TKN_END                 :('KONIEC');
TKN_BREAK               :('PRZERWIJ');
TKN_CONTINUE            :('KONTYNUUJ');
TKN_PLUS                :'+';
TKN_MINUS               :'-';
TKN_MUL                 :'*';
TKN_DIV                 :'/';
TKN_POW                 :'^';
TKN_CONCAT              :'++';
TKN_ASSIGN              :':=';
TKN_G                   :'>';
TKN_L                   :'<';
TKN_EQ                  :'=';
TKN_GEQ                 :'>=';
TKN_LEQ                 :'<=';
TKN_NEQ                 :'/=';
TKN_DOTS                :':';
TKN_LBRACKET            :'(';
TKN_RBRACKET            :')';
TKN_LSQUARE             :'[';
TKN_RSQUARE             :']';
TKN_COMMA               :',';
TKN_COMMENT             :([#][a-zA-Z_0-9 \t;]*[\n] | '#{'[a-zA-Z_0-9 \t\n;]*'}#');
TKN_NUMBER_VAL          :[-]?[0-9]+([.][0-9]+)?;
TKN_STRING_VAL          :'"'[a-zA-Z_0-9!? \t\n;]*'"';
TKN_VAR_ID              :[a-zA-Z_][a-zA-Z0-9_]*;
TKN_WHITESPACE          :(' ' | '\t' | '\n') -> skip;
```

##5. Gramatyka:
```
program:
    code EOF;

code:
    expression TKN_END_LINE |
    expression TKN_END_LINE code |
    TKN_COMMENT code;

var_type:
    TKN_NUMBER | TKN_STRING | TKN_BOOL | TKN_LIST;

varDeclaration:
    var_type TKN_VAR_ID TKN_ASSIGN value;

varAssignment:
    TKN_VAR_ID TKN_ASSIGN value;

functionDeclaration:
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_RETURN value TKN_END_LINE TKN_END |
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_END;

functionCall:
    TKN_VAR_ID TKN_LBRACKET fullValueList TKN_RBRACKET;

expression:
    varDeclaration | varAssignment | printExpression | forLoopExpression | whileLoopExpression |
    conditionalExpression TKN_END | functionCall | functionDeclaration | TKN_RETURN value;

value:
    stringExpression | booleanExpression | arithmeticExpression | listExpression |TKN_VAR_ID | functionCall;

stringExpression:
    stringExpression TKN_CONCAT stringExpression | TKN_STRING_VAL | TKN_VAR_ID | TKN_LBRACKET stringExpression TKN_RBRACKET | functionCall;

booleanExpression:
    booleanExpression (TKN_AND | TKN_OR) booleanExpression | stringExpression (TKN_EQ | TKN_NEQ) stringExpression |
    arithmeticExpression (TKN_G | TKN_L | TKN_LEQ | TKN_GEQ | TKN_EQ | TKN_NEQ) arithmeticExpression | TKN_FALSE | TKN_TRUE |
    TKN_VAR_ID | TKN_NOT booleanExpression | TKN_LBRACKET booleanExpression TKN_RBRACKET | functionCall;

arithmeticExpression:
    TKN_LBRACKET arithmeticExpression TKN_RBRACKET |
    arithmeticExpression (TKN_MUL | TKN_DIV) arithmeticExpression |
    arithmeticExpression (TKN_MINUS | TKN_PLUS) arithmeticExpression |
    TKN_NUMBER_VAL | TKN_VAR_ID | functionCall;

printExpression:
    TKN_PRINT value | TKN_PRINT TKN_LBRACKET value TKN_RBRACKET;

forLoopExpression:
    TKN_FOR TKN_VAR_ID TKN_FROM arithmeticExpression TKN_TO arithmeticExpression TKN_DOTS loopCode TKN_END;

whileLoopExpression:
    TKN_WHILE booleanExpression TKN_DOTS loopCode TKN_END;

conditionalExpression:
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) |  TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression elseExpression |
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression | TKN_IF booleanExpression TKN_DOTS (code|loopCode) elseExpression;

elifExpression:
    TKN_ELIF booleanExpression TKN_DOTS (code|loopCode) | elifExpression TKN_ELIF booleanExpression TKN_DOTS (code|loopCode);

elseExpression:
    TKN_ELSE TKN_DOTS (loopCode|code);

listExpression:
    listValue | listExpression TKN_CONCAT listValue;

listValue:
    TKN_LSQUARE valueList TKN_RSQUARE;

valueList:
    value | valueList TKN_COMMA value;

fullValueList:
    TKN_WHITESPACE | valueList;

argList:
    var_type TKN_VAR_ID | argList TKN_COMMA var_type TKN_VAR_ID;

fullArgList:
    TKN_WHITESPACE | argList;

loopCode:
    code | loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode |
    loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE |
    (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode | (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE;
```

##6. Opis i schemat struktury programu:
  * Kod źródłowy zostaje wczytany do programu z pliku.
  * Trafia on do lexera, gdzie strumień wejściowy jest odczytywany i zamieniany na tokeny, jako wynik otrzymujemy strumień tokenów.
  * Przekazujemy strumień do parsera, który ma za zadanie skojarzenie tokenów z elementami gramatyki.
  * Parser posiada funkcję utworzenia drzewa parsowania - w drzewie tym reguły złożone gramatyki są reprezentowane jako korzenie, tokeny proste jako liście drzewa. Jako wynik tej części programu otrzymujemy gotowe drzewo parsowania.
  * Posiadając już drzewo oraz wszystkie potrzebne reguły za pomocą walkera z biblioteki ANTLR oraz listenera, który został przez nas zaimplementowany możemy przejść po drzewie i wygenerować kod w języku Python.

##7. Informacje o stosowanych generatorach skanerów/parserów, pakietach zewnętrznych: 
ANTLR to generator parserów do czytania, przetwarzania, wykonywania lub tłumaczenia tekstu strukturalnego lub plików binarnych. Jest szeroko stosowany do tworzenia języków, narzędzi i frameworków. Na podstawie gramatyki, ANTLR generuje parser, który może budować i przechodzić przez drzewa parsowania.

##8. Informacje o zastosowaniu specyficznych metod rozwiązania problemu: 
Język, który stworzyliśmy na potrzeby tego projektu jest językiem ułatwiającym naukę programowania. Poprzez zdefiniowanie słów kluczowych w języku polskim młodsze osoby nie mają problemu ze zrozumieniem koncepcji ich działania. To rozwiązanie pozwoli dzieciom oswajać się z programowaniem już od najmłodszych lat.

##9. Krótka instrukcja obsługi:
Na początku musimy pobrać kompletny plik JAR ANTLR. Po stworzeniu pliku .g4 składającego się z opisanych tokenów i gramatyki należy go skompilować w użyciem pobranego wcześniej JAR'a ANTLR. Używamy polecenia:

```java -Xmx500M -cp antlr-4.7.2-complete.jar org.antlr.v4.Tool -Dlanguage=Python3 JuanMI.g4```
Aby użyć wygenerowanego pliku Pythona, potrzebujemy naszej własnej klasy Listenera, która dziedziczy z wygenerowanego wcześniej Listenera (jest on nowym elementem projektu ANTLR 4 i został zaprojektowany, aby ułatwić pisanie kodu, który obsługuje zdarzenia z parsera, bez wpływu na zmianę gramatyki i ponownej kompilacji). Po stworzeniu takowej klasy możemy użyć naszego programu. Aby tego dokonać tworzymy prosty skrypt zamieszczony poniżej.
```
def translate(input_file, output_file):

    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = JuanMILexer.JuanMILexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JuanMIParser.JuanMIParser(stream)

    tree = parser.program()

    parse_tree_walker = ParseTreeWalker()
    //wykorzystujemy własną klasę zaimplentowaną na podstawie wygenerowanego wcześniej pliku JuanMIListener
    listener = JuanMIListenerImpl()

    parse_tree_walker.walk(listener, tree)

    file = open(output_file, "w+", encoding='utf-8')
    file.write(listener.code)
    file.close()


path = str(sys.argv[1])
target = str(sys.argv[2])
translate(path, target)
```
Kompilator uruchamiamy z konsoli z użyciem polecenia:
```python translate.py <plik w języku JuanMI (.txt)> <plik wyjściowy (.py)>```
Otrzymujemy plik wyjściowy w języku Python, który możemy w dowolny sposób uruchomić.

##10. Testy, przykłady:
###Przykład pierwszy:
```
# funkcja hello w jezyku JuanMI
FUNKCJA witaj(TEKST tresc):
    TEKST wiadomosc := "witaj " ++ tresc ++ "!".
    ZWROC wiadomosc.
KONIEC.

# fibonacci iteracyjnie w jezyku JuanMI
FUNKCJA fib(LICZBA zmienna):
    JEZELI zmienna = 1:
        ZWROC 0.
    JEZELI_INACZEJ zmienna = 2:
        ZWROC 1.
    INACZEJ:
        tymczasowa_1 := 0.
        tymczasowa_2 := 1.
        DLA indeks OD 2 DO zmienna:
        wynik := tymczasowa_1 + tymczasowa_2.
        tymczasowa_1 := tymczasowa_2.
        tymczasowa_2 := wynik.
        KONIEC.
        ZWROC wynik.
    KONIEC.
KONIEC.


WYPISZ(witaj("Czlowieku")).

DLA indeks OD 1 DO 10:
    JEZELI indeks < 4 LUB indeks >= 7:
        WYPISZ("fib").
        WYPISZ(fib(indeks)).
    JEZELI_INACZEJ indeks = 9:
        PRZERWIJ.
    INACZEJ:
        WYPISZ("indeks ").
        WYPISZ(indeks).
        KONTYNUUJ.
    KONIEC.
KONIEC.
```
###Wynik:
```
# funkcja hello w jezyku JuanMI

def witaj(tresc):
	wiadomosc = "witaj " + tresc + "!"
	return wiadomosc
	
# fibonacci iteracyjnie w jezyku JuanMI

def fib(zmienna):
	if zmienna == 1:
		return 0
	elif zmienna == 2:
		return 1
	else:
		tymczasowa_1 = 0
		tymczasowa_2 = 1
		for indeks in range (2, zmienna):
			wynik = tymczasowa_1 + tymczasowa_2
			tymczasowa_1 = tymczasowa_2
			tymczasowa_2 = wynik
			
		return wynik
		
	
print(witaj("Czlowieku"))
for indeks in range (1, 10):
	if indeks < 4 or indeks >= 7:
		print("fib")
		print(fib(indeks))
	elif indeks == 9:
		break
	else:
		print("indeks ")
		print(indeks)
		continue
```

###Przykład drugi:
```
# funkcja obliczajaca pole prostokata
FUNKCJA prostokat(LICZBA zmienna1, LICZBA zmienna2):
    LICZBA wynik := zmienna1 * zmienna2.
    ZWROC wynik.
KONIEC.

# funkcja obliczajaca pole trojkata
FUNKCJA trojkat(LICZBA zmienna1, LICZBA zmienna2):
    LICZBA wynik := zmienna1 * zmienna2 * 0.5.
    ZWROC wynik.
KONIEC.

WYPISZ("Pole prostokata o bokach 2 i 3").
WYPISZ(prostokat(2,3)).

WYPISZ("Pole trojkata o bokach 4 i 5").
WYPISZ(trojkat(4,5)).
```

###Wynik:
```
# funkcja obliczajaca pole prostokata

def prostokat(zmienna1, zmienna2):
	wynik = zmienna1 * zmienna2
	return wynik
	
# funkcja obliczajaca pole trojkata

def trojkat(zmienna1, zmienna2):
	wynik = zmienna1 * zmienna2 * 0.5
	return wynik
	
# funkcja obliczajaca pole kwadratu

def kwadrat(zmienna):
	wynik = zmienna * zmienna
	return wynik
	
print("Pole prostokata o bokach 2 i 3")
print(prostokat(2, 3))
print("Pole trojkata o bokach 4 i 5")
print(trojkat(4, 5))
print("Pole kwadratu o boku 4")
print(kwadrat(4))
```
###Przykład trzeci:
```
# deklaracja listy
LISTA lista := [1, 3, 5, 6].

LICZBA indeks := 0.

DOPOKI indeks < 10:
    JEZELI indeks = 4:
        WYPISZ("Jestem numerem 4").
    JEZELI_INACZEJ indeks = 9:
        WYPISZ("To juz jest koniec").
    INACZEJ:
        WYPISZ(indeks).
    KONIEC.
    indeks := indeks + 1.
KONIEC.
```
###Wynik:
```
# deklaracja listy

lista = [1, 3, 5, 6]
indeks = 0
while indeks < 10:
	if indeks == 4:
		print("Jestem numerem 4")
	elif indeks == 9:
		print("To juz jest koniec")
	else:
		print(indeks)
		
	indeks = indeks + 1
```
###Przykłady błędów:
```
line 9:15 token recognition error at: '"Jestem numerem 4)'
line 9:33 no viable alternative at input 'DOPOKIindeks<10:JEZELIindeks=4:WYPISZ(.'
```

```
line 5:10 token recognition error at: 'ę'
line 9:15 token recognition error at: '"Jestem numerem 4)'
line 5:11 no viable alternative at input 'LICZBAindks'
```


##11. Możliwe rozszerzenia programu:
  * dodanie możliwości obsługi programów wieloplikowych
  * wprowadzenie obsługi funkcji lamda
  * rozszerzenia języka o klasy i obiekty
  * możliwość implementacji słowników 

##12. Ograniczenia programu:
  * brak możliwości definiowania klas oraz obiektów
  * brak obsługi programów wieloplikowych
  * brak obsługi funkcji lambda
  * brak obsługi słowników

##13. Inne informacje zależne od tematu:
https://www.javadoc.io/doc/org.antlr/antlr4/latest/index.html 
http://blog.anvard.org/articles/2016/03/15/antlr-python.html 
https://stackoverflow.com/questions/39572300/translator-using-antlr4 
https://fiksacie.wordpress.com/2014/11/08/antlr-generujemy-wlasny-parser/ 



 

