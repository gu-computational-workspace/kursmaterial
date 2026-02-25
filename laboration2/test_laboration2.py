import random
import string
import io
from contextlib import redirect_stdout
import traceback
import sys
import os
from pathlib import Path

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
    
def error(msg):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")
    
def info(msg):
    print(f"{bcolors.OKBLUE}{msg}{bcolors.ENDC}")
    
def success(msg):
    print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")

def test_import():
    info("Testar att Todo och Todos finns i laboration2_objekt.py...")
    #print(Path(__file__).parent.parent.resolve())
    sys.path.append(str(Path(__file__).parent.parent.parent.resolve()))
    #print(sys.path)
    
    try:
        from laboration2_objekt import Todo
    except Exception as e:
        traceback.print_exc()
        error("Det gick inte att importera Todo från laboration2_objekt.py")
        exit(0)
        
    try:
        from laboration2_objekt import Todos
    except Exception as e:
        traceback.print_exc()
        error("Det gick inte att importera Todos från laboration2_objekt.py")
        exit(0)
        
    return Todos, Todo

def test_todo(Todo):
    info("Testar klassen Todo...")
    abc = string.ascii_lowercase
    todo_str = "".join([ random.choice(abc) for _ in range(10) ])
    info("Testar Todo.__init__...")
    try:
        todo = Todo(todo_str, 5)
    except Exception as e:
        traceback.print_exc()
        error("Kunde inte skapa en todo med Todo(\"...\", 0)")
        exit(0)
    info("Testar Todo.set_priority ...")
    try:
        n = random.randint(0, 50)
        todo.set_priority(n)
    except:
        error("Kunde inte köra funktionen set_priority(3) på en instans av Todo")
        exit(0)
    
    info("Testar Todo.get_priority ...")
    try:
        p = todo.get_priority()
        if p is not n:
            error(f"get_priority() != {n} efter set_priority({n})")
            exit(0)
    except Exception as e:
        traceback.print_exc()
        error("Fel vid kontroll av get_priority/set_priority, se ovan")
        exit(0)
    
    info("Testar Todo.show ...")
    try:
        s = todo.show()
        if todo_str not in s:
            error(f"todo.show() efter todo = Todo(\"{todo_str}\", {n}) innehåller inte {todo_str}")
            exit(0)
        if str(n) not in s:
            error(f"todo.show() efter todo = Todo(\"{todo_str}\", {n}) innehåller inte prioriteten {n}")
            exit(0)
    except Exception as e:
        traceback.print_exc()
        error("Fel vid kontroll av todo.show, se ovan")
        exit(0)
        
    info("Testar Todo.set_status ...")
    try:
        todo.set_status(True)
        if "done" not in todo.show():
            error(f"todo.show() efter todo.set_status(True) innehåller inte \"done\"")
            exit(0)
    except Exception as e:
        traceback.print_exc()
        error("Fel vid kontroll av todo.set_status")
        exit(0)
        
def parse_print_todos(print_function, todos, test_todos_list):
    f = io.StringIO()
    with redirect_stdout(f):
        print_function()
    out = f.getvalue()
    lines = out.strip().split("\n")
    todo_map = dict()
    todo_list = []
    lines = filter(lambda s: len(s) > 0, lines)
    for line in lines:
        try:
            parts = line.split(":")
            todo_id = int(parts[0])
            todo_show = "".join(parts[1:])
        except Exception as e:
            #import pdb; pdb.set_trace()
            traceback.print_exc()
            error(f"Det gick inte att hitta id för raden \"{line}\" i print_todos")
            exit(0)
        for text, prio in test_todos_list:
            if text in todo_show:
                todo_map[text] = dict(todo_id=todo_id, todo_show=todo_show)
                todo_list.append(dict(todo_id=todo_id, todo_show=todo_show, todo_text=text))
                
    return todo_map, todo_list
        
def test_todos(Todos):
    info("Testar klassen Todos...")
    test_todos_list = [
        ("todo1", 1),
        ("todo2", 2),
        ("todo3", 4),
        ("todo4", 0)
    ]
    info("Testar Todos.__init__ ...")
    try:
        todos = Todos()
    except Exception as e:
        traceback.print_exc()
        error("Fel vid instansiering av Todos")
        exit(0)
        
    info("Testar Todos.add_todo ...")
    try:
        for text, prio in test_todos_list:
            todos.add_todo(text)
    except Exception as e:
        traceback.print_exc()
        error(f"Fel vid test av todos.add_todo({text}, {prio})")
        exit(0)
     
    info("Testar Todos.print_todos ...")
    try:
        todo_map, todo_list = parse_print_todos(todos.print_todos, todos, test_todos_list)
        texts = set([t for t, _ in test_todos_list])
        texts_in_print = set(todo_map.keys())
        if texts != texts_in_print:
            error("Hittade inte alla tasks i utskriften från print_todos")
            error(f"Skapade {texts} men hittade bara {list(texts_in_print)}")
    except Exception as e:
        traceback.print_exc()
        error("Fel vid test av print_todos()")  
        exit(0)
        
    info("Testar Todos.set_priority & Todos.print_todos ...")
    try:
        for todo_text, todo_prio in test_todos_list:
            todos.set_priority(todo_map[todo_text]["todo_id"], todo_prio)
            
        todo_map, todo_list = parse_print_todos(todos.print_todos, todos, test_todos_list)
        todo_print_order = [todo["todo_text"] for todo in todo_list]
        todo_prio_order = [text for text, prio in sorted(test_todos_list, key=lambda t: -t[1])]
        todo_prio_prios = [prio for text, prio in sorted(test_todos_list, key=lambda t: -t[1])]
        
        if todo_print_order != todo_prio_order:
            error("Ordningen av todos i print_todos motsvarar inte prioritet")
            #error(f"Prioritetsordning är {list(zip(todo_prio_order, todo_prio_prios))} medans din print_todos har ordningen {todo_print_order}")
            error(f"Prioritetsordning är {todo_prio_order} medans din print_todos har ordningen {todo_print_order}")
            exit(0)
        
    except Exception as e:
        traceback.print_exc()
        error("Fel vid test av Todos.set_priority() & Todos.print_todos()")  
        exit(0)
        
    info("Testar Todos.set_priority & Todos.print_done ...")
    try:
        todos.set_done(todo_map["todo1"]["todo_id"])
        todo_map, todo_list = parse_print_todos(todos.print_done, todos, test_todos_list)
        
        if len(todo_list) == 0:
            error("print_done visar inga todos efter todos.set_done(...)")
            exit(0)
            
        if todo_list[0]["todo_text"] != "todo1":
            error("print_done innehåller inte en todo som satts till klar med todos.set_done")
            
    except Exception as e:
        traceback.print_exc()
        error("Fel vid test av Todos.set_done & Todos.print_done")
        exit(0)
        
    info("Testar Todos.set_priority & Todos.print_not_done ...")
    try:
        todo_map, todo_list = parse_print_todos(todos.print_not_done, todos, test_todos_list)
        
        for t in ["todo2", "todo3", "todo4"]:
            if t not in todo_map:
                error("print_not_done innehåller inte en todo som inte är klar")
                exit(0)
                
        if "todo1" in todo_map:
            error("print_not_done innehåller en todo är klar")
            exit(0)
            
    except Exception as e:
        traceback.print_exc()
        error("Fel vid test av Todos.set_done & Todos.print_done")
        exit(0)
        
    info("Testar Todos.delete_todo ...")
    try:
        todo_map, todo_list = parse_print_todos(todos.print_todos, todos, test_todos_list)
        todos.delete_todo(todo_map["todo2"]["todo_id"])
        del_todo_map, del_todo_list = parse_print_todos(todos.print_todos, todos, test_todos_list)
        
        if "todo2" in del_todo_map:
                error("print_todos innehåller en todo som tagits bort med todos.delete_todo")
            
    except Exception as e:
        traceback.print_exc()
        error("Fel vid test av Todos.delete_done")
        exit(0)

Todos, Todo = test_import()
test_todo(Todo)
test_todos(Todos)
success("Allt ok! Bra jobbat!")
    