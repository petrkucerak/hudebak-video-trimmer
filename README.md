# Skriptovací stříhač videí na Hudebák

Každý rok máme z Hudebního týdne závěrečné video. Nastříhání na jednotlivé části a správné formátování názvů je ale časově náročné. Proto jsem připravil tento jednoduchý python skript, který pod vstupu zadaného v json souboru videa sestříhá a přejmenuje je tak, aby splňovala standardy, které se používají na Youtube, konkrétně na účtu DCŽM Vesmír.

Skript používá knihovnu https://zulko.github.io/moviepy/index.html.

```sh
pip install moviepy # instalace knihonvy pro stříhání videí
python .\main.py 'trims_example.json' 'video.movi' # ukázka spuštění skriptu
```