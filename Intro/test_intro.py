import nbformat
from nbconvert import PythonExporter

def execute_notebook(notebook_path):
    # Läser in notebook-filen
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Konverterar notebookens celler till en Python-skript
    python_exporter = PythonExporter()
    source_code, _ = python_exporter.from_notebook_node(notebook)
    
    # Skapar en miljö för att köra koden
    env = {}
    exec(source_code, env)  # Exekverar koden från notebooken i 'env'-ordboken
    return env

def test_nb():
    # Kör notebooken och hämta dess miljö
    env = execute_notebook("intro.ipynb")
    
    # Testar funktionen `addera`
    addera = env.get('addera')
    if not addera:
        print("Fel: 'addera'-funktionen hittades inte.")
        return

    try:
        for a, b in zip(range(10), [x**2 for x in range(10)]):
            # Kontrollera om addera-funktionen ger rätt resultat
            assert addera(a, b) == a + b, f"addera({a}, {b}) misslyckades: {addera(a, b)} != {a + b}"
    except AssertionError as e:
        print("Fel i addera-funktionen:", e)
        return

    # Testar funktionen `multiplicera`
    multiplicera = env.get('multiplicera')
    if not multiplicera:
        print("Fel: 'multiplicera'-funktionen hittades inte.")
        return

    try:
        for a, b in zip(range(10), [x**2 for x in range(10)]):
            # Kontrollera om multiplicera-funktionen ger rätt resultat
            assert multiplicera(a, b) == a * b, f"multiplicera({a}, {b}) misslyckades: {multiplicera(a, b)} != {a * b}"
    except AssertionError as e:
        print("Fel i multiplicera-funktionen:", e)
        return

    # Testar funktionen `subtrahera`
    subtrahera = env.get('subtrahera')
    if not subtrahera:
        print("Fel: 'subtrahera'-funktionen hittades inte.")
        return

    try:
        for a, b in zip(range(10), [x**2 for x in range(10)]):
            # Kontrollera om subtrahera-funktionen ger rätt resultat
            assert subtrahera(a, b) == a - b, f"subtrahera({a}, {b}) misslyckades: {subtrahera(a, b)} != {a - b}"
    except AssertionError as e:
        print("Fel i subtrahera-funktionen:", e)
        return

    # Om alla tester klarar sig
    print("Alla tester klarade. Bra jobbat!")

# Anropa testfunktionen
test_nb()

