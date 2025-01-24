import nbformat
import sys
from nbconvert import PythonExporter
from io import StringIO


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def execute_notebook(notebook_path):
    """Läser in och exekverar en Jupyter-notebook som Python-kod."""
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)

        python_exporter = PythonExporter()
        source_code, _ = python_exporter.from_notebook_node(notebook)

        # Omdirigerar stdout till en dummy stream för att undvika print-utmatning
        old_stdout = sys.stdout
        sys.stdout = StringIO()

        env = {}
        exec(source_code, env)

        # Återställ stdout till dess ursprungliga tillstånd
        sys.stdout = old_stdout
        return env

    except FileNotFoundError:
        raise RuntimeError(f"{bcolors.FAIL}Notebooken '{notebook_path}' hittades inte.{bcolors.ENDC}")
    except Exception as e:
        raise RuntimeError(f"{bcolors.FAIL}Ett fel uppstod vid körning av notebooken: {e}{bcolors.ENDC}")


def test_function(env, func_name, operation, test_data):
    """Testar en enskild funktion med specificerad operation och testdata."""
    func = env.get(func_name)
    if not func:
        return f"{bcolors.WARNING}Fel: '{func_name}' hittades inte i miljön.{bcolors.ENDC}"

    try:
        for a, b in test_data:
            expected = operation(a, b)
            result = func(a, b)
            assert result == expected, (
                f"{bcolors.FAIL}{func_name}({a}, {b}) misslyckades: {result} != {expected}{bcolors.ENDC}"
            )
        return f"{bcolors.OKGREEN}'{func_name}' klarade alla tester.{bcolors.ENDC}"
    except AssertionError as e:
        return str(e)
    except Exception as e:
        return f"{bcolors.FAIL}Ett fel uppstod i '{func_name}': {e}{bcolors.ENDC}"


def test_nb(notebook_path):
    """Testar funktioner från en Jupyter-notebook."""
    try:
        env = execute_notebook(notebook_path)

        test_data = [(a, b) for a, b in zip(range(10), [x**2 for x in range(10)])]

        results = [
            test_function(env, "addera", lambda a, b: a + b, test_data),
            test_function(env, "multiplicera", lambda a, b: a * b, test_data),
            test_function(env, "subtrahera", lambda a, b: a - b, test_data),
        ]

        print(f"{bcolors.HEADER}Resultat från testerna:{bcolors.ENDC}")
        for result in results:
            print(result)

    except RuntimeError as e:
        print(e)


# Kör testerna
test_nb("intro.ipynb")



