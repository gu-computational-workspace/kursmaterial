from testbook import testbook

def test_nb():
    with testbook("intro.ipynb", execute=True) as tb:
        # Testar addera-funktionen
        addera = tb.ref('addera')
        try:
            for a, b in zip(range(10), [x**2 for x in range(10)]):
                assert addera(a, b) == a + b, f"addera({a}, {b}) misslyckades: {addera(a, b)} != {a + b}"
        except AssertionError as e:
            print("Fel i addera-funktionen:", e)
            return

        # Testar multiplicera-funktionen
        multiplicera = tb.ref('multiplicera')
        try:
            for a, b in zip(range(10), [x**2 for x in range(10)]):
                assert multiplicera(a, b) == a * b, f"multiplicera({a}, {b}) misslyckades: {multiplicera(a, b)} != {a * b}"
        except AssertionError as e:
            print("Fel i multiplicera-funktionen:", e)
            return

        # Testar subtrahera-funktionen
        subtrahera = tb.ref('subtrahera')
        try:
            for a, b in zip(range(10), [x**2 for x in range(10)]):
                assert subtrahera(a, b) == a - b, f"subtrahera({a}, {b}) misslyckades: {subtrahera(a, b)} != {a - b}"
        except AssertionError as e:
            print("Fel i subtrahera-funktionen:", e)
            return

    print("Alla tester klarade. Bra jobbat!")

test_nb()
