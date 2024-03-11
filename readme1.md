# Implementační dokumentace k 1. úloze do IPP 2023/2024

<p>Jméno a příjmení: Samuel Hejníček<br>
Login: xhejni00</p>

## Popis chování skriptu
<p>Skript načítá ze standardního vstupu IPPcode24 a převadí jej na odpovídající reprezentaci ve formátu XML<br></p>

<p>Nejprve probíhá ve funkci main kontrola argumentů pomocí funkce process_cli_args. Následně probíhá u každého řádku kontrola, zdali se na něm nachází komentář a v případě jeho existence dochází k jeho odstranění ze zpracovávaného řádku pomocí funkce remove_comments. Po odstranění komentářu dochází u prvního řádku vstupu ke kontrole hlavičky (funkce header_check) a následně k rozdělení řádku dle mezer na několik částí.<br></p>

<p>Operační kód, nacházející se v první části, je vyhledáván v seznamech instrukcí dle počtu operandů a při shodě dochází k vytvoření instance třídy instrukce. Tato instrukce je dále předána do funkce instruction_process, kde dochází ke kontrole počtu argumentů (tj. počet zbylých částí rozděleného řádku) a přidání této instrukce do výstupního XML dokumentu. Následně je instrukce předána do jedné z funkcí handle_x_args, kde x označuje počet argumentů/operandů. Pokud operačního kód v těchto seznamech nebyl nalezen, dochází k chybě.<br></p>

<p>Funkce, které mají na starost zpracování argumentů dané instrukce určí jednotivé typy argumentů instrukce a tyto argumenty jsou pomocí regulárního výrazu (každý typ argumentu má jiný regulární výraz) ve funkci validate_regex kontrolovány zdali dodržují syntaktickou správnost.<br></p>

## Chybová hlášení
<p>Veškerá chybová hlášení jsou řešena pomocí několika výjimek, které jsou reprezentovány svou vlastní třídou, přičemž všechny tyto třídy dědí od výchozí třidy pro výjimku v jazyce Python. Při výskytu chyby dojde k výjimce a na standardní chybový výstup je vypsána chybová hláška charakterizující danou chybu. Skript je následně ukončen s odpovídajícím chybovým kódem pro danou výjimku<br></p>

## Výstupní XML reprezentace
<p>Pro vytvoření výstupního xml souboru byla použita knihovna minidom. Ve skriptu je nejprve vytvořen XML dokument, do kterého je po úspěšné kontrole vložena hlavička IPPcode24. Při vytvoření instrukce dojde rovněž k jejímu přidání do xml souboru pomocí funkce add_xml_instruction a k této instrukci jsou poté přidány jednotlivé operandy/argumenty pomocí funkce add_xml_argument. V případě, že je operandem řetězec dochází ke konverzi problematických znaků pro XML automaticky při tisku na standardní výstup, který je proveden po zpracování všech řádků ze vstupu.<br></p>
 
 
