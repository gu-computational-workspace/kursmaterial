from testbook import testbook
import math
import pandas
import random
import sys

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

def get_data():
    data = pandas.read_csv("./smhi.csv", sep=";")
    data["date"] = pandas.to_datetime(data["Dygn"])
    return data

def regn_datum(datum):
    dag = DATA[DATA["Dygn"] == datum]["Nederbörd(mm)"]
    if dag.size > 0:
        return dag.item()
    else:
        return 0
    
def regn_år(year):
    return DATA[(DATA["date"] >= pandas.to_datetime(f"{year}-01-01")) & (DATA["date"] < pandas.to_datetime(f"{year+1}-01-01"))]["Nederbörd(mm)"].sum()

def nederbörd_månader():
    year_month=DATA.groupby(by=lambda item: (DATA.iloc[item]["date"].year, DATA.iloc[item]["date"].month))
    summed_year_month=year_month["Nederbörd(mm)"].sum()
    monthly = summed_year_month.groupby(by=lambda item: item[1]).mean().to_dict()
    return monthly

def regn_metrics(year1, year2):
    data = DATA.copy()
    
    if year1>year2:
        x = year1
        year1=year2
        year2=x
    
    data["year"] = data["Dygn"].str[0:4].astype(int)
    filtered_data = data[(data['year'] >= year1) & (data['year'] <= year2)]
    
    mean = filtered_data["Nederbörd(mm)"].mean()
    std = filtered_data["Nederbörd(mm)"].std()
    
    return {'mean': round(mean, 2),'std': round(std, 2)}
  

def error(msg):
    print(f"{bcolors.FAIL}{msg}{bcolors.ENDC}")
    
def ok(msg):
    print(f"{bcolors.OKGREEN}{msg}{bcolors.ENDC}")

    
def get_nb_ref_safe(tb, name):
    try:
        return tb.ref(name)
    except:
        error(f"Kan inte hämta funktionen {name}, har du implementerat en funktion med namnet {name}?")
        exit(0)
    
def test_rain_date(tb):
    func = 'rain_date'
    rd = get_nb_ref_safe(tb, func)
    
    print(f"*** Testar funktionen {func} ***")
    
    # Test output type
    ret_type = type(rd(ROOT_SMHI,"1881-01-01"))
    if ret_type is not float:
        print(f"{bcolors.FAIL}Datatypen för resultatet för {func} är inte float, din funktion returnerar {ret_type}{bcolors.ENDC}")
        #return False

    years = range(1881, 1997)
    months = range(1, 13)
    days = range(1, 25)
    print("Testar rain_date...")
    n_tests = 0
    while n_tests < 50:
        test_date = f"{random.choice(years)}-{random.choice(months)}-{random.choice(days)}"    
        if regn_datum(test_date) > 0:        
            n_tests += 1
            diff = math.fabs(regn_datum(test_date) - rd(ROOT_SMHI, test_date))
            if diff > 0.1:
                err1 = f"Funktionen {func} ger inte rätt resultat för datum {test_date}"
                err2 = f"{func}({test_date}) = {rd(ROOT_SMHI, test_date)} [din implementering]"
                err3 = f"{func}({test_date}) = {regn_datum(test_date)} [facit]"
                sys.stdout.write("\n")
                for err in [err1, err2, err3]:
                    sys.stdout.write(f"{bcolors.FAIL}")
                    print(err)
                    sys.stdout.write(f"{bcolors.ENDC}")
                return False
            else:
                sys.stdout.write(f"{bcolors.OKGREEN}{test_date}, {bcolors.ENDC}")
                sys.stdout.flush()
    sys.stdout.write("\n")
    return True
            
def test_rain_year(tb):
    func = 'rain_year'
    rd = get_nb_ref_safe(tb, func)
    
    print(f"*** Testar funktionen {func} ***")
    
    ret_type = type(rd(ROOT_SMHI, 1881))
    if ret_type is not float:
        print(f"{bcolors.FAIL}Datatypen för resultatet för {func} är inte float, din funktion returnerar {ret_type}{bcolors.ENDC}")
        #return False
    
    
    years = list(range(1881, 1997))
    random.shuffle(years)
    print("Testar rain_year...")
    for i in range(50):
        
        test_year = years[i]
        diff = math.fabs(regn_år(test_year) - rd(ROOT_SMHI, test_year))

        if diff > 0.1:
            err1 = f"Funktionen {func} ger inte rätt resultat för år {test_year}"
            err2 = f"{func}({test_year}) = {rd(ROOT_SMHI, test_year)} [din implementering]"
            err3 = f"{func}({test_year}) = {regn_år(test_year)} [facit]"
            sys.stdout.write("\n")
            for err in [err1, err2, err3]:
                sys.stdout.write(f"{bcolors.FAIL}")
                print(err)
                sys.stdout.write(f"{bcolors.ENDC}")
            return False
        else:
            sys.stdout.write(f"{bcolors.OKGREEN}{test_year}, {bcolors.ENDC}")
            sys.stdout.flush()
    sys.stdout.write("\n")
    return True

def test_rain_months(tb):
    func = 'rain_months'
    rm = get_nb_ref_safe(tb, func)

    
    print(f"*** Testar funktionen {func} ***")
    
    res = dict(rm(ROOT_SMHI))
    res = {int(k): v for k, v in res.items()}
    ret_type = type(res)
    if ret_type is not dict:
        error(f"Datatypen för returvärdet för funktionen {func} är inte dict, din funktion returnerar {ret_type}")
        return False
    
    if len(res.keys()) == 0:
        error("Din dict innehåller inga värden")
        return False

    value_type = type(list(res.values())[0])
    key_type = type(list(res.keys())[0])

    #if key_type is not int:
    #    error(f"Din dict har inte nycklar av typen int, en nyckel har typ {key_type}")
        
    if value_type is not float:
        error(f"Din dict har inte värden av typen float, en nyckel har typ {value_type}")
        return False
    
    facit = nederbörd_månader()

    for month, regn in facit.items():

        if not int(month) in res:
            error(f"Din dict innehåller inte nyckel för månad {month}")
            return False
        
        if math.fabs(regn - res[month]) > 2:
            error(f"Medelnederbörden för månad {month} är fel.")
            error(f"Din funktion: rain_months()[{month}] = {res[month]}")
            error(f"Facit: rain_months()[{month}] = {regn}")
            return False
        else:
            ok(f"Månad {month}")
            
    return True

def test_rain_metrics(tb):
    func = 'rain_metrics'
    rk = get_nb_ref_safe(tb, func)
    
    print(f"*** Testar funktionen {func} ***")
    
    ret_type = dict(rk(ROOT_SMHI, 1888, 1905))
    ret_type = type(ret_type)
    if ret_type is not dict:
        print(f"{bcolors.FAIL}Datatypen för resultatet för {func} är inte dict, din funktion returnerar {ret_type}{bcolors.ENDC}")
        #return False
        
    ret_ = rk(ROOT_SMHI, 1888, 1905)
    ret_ = dict(ret_)
    for key in ret_.keys():
        if key == 'mean' or key == 'std':
            pass
        else:
            print(f"{bcolors.FAIL}Din dictionary har fel nycklar, se till så att funktionen returnerar 'mean' och 'std' {bcolors.ENDC}")
    
    years = list(range(1881, 1997))
    random.shuffle(years)
    print("Testar rain_metrics...")
    for i in range(50):
        
        test_year1 = years[i]
        test_year2 = years[i+1]
        
        #Prediktion och GT
        gt = regn_metrics(test_year1, test_year2)
        pred = rk(ROOT_SMHI, test_year1, test_year2)

        diff = math.fabs(gt['mean'] - pred['mean']) + math.fabs(gt['std'] - pred['std']) 
        if diff > 0.1:
            err1 = f"Funktionen {func} ger inte rätt resultat för år {test_year1} och år {test_year2}"
            err2 = f"{func}({test_year1, test_year2}) = {rk(ROOT_SMHI, test_year1, test_year2)} [din implementering]"
            err3 = f"{func}({test_year1, test_year2}) = {regn_metrics(test_year1, test_year2)} [facit]"
            sys.stdout.write("\n")
            for err in [err1, err2, err3]:
                sys.stdout.write(f"{bcolors.FAIL}")
                print(err)
                sys.stdout.write(f"{bcolors.ENDC}")
            return False
        else:
            sys.stdout.write(f"{bcolors.OKGREEN}{test_year1}-{test_year2}, {bcolors.ENDC}")
            sys.stdout.flush()
    sys.stdout.write("\n")
    return True
    
def test_nb():
    all_ok = True
    try:
        with testbook("laboration1.ipynb", execute=True) as tb:
            all_ok = test_rain_date(tb) and all_ok
            all_ok = test_rain_year(tb) and all_ok
            all_ok = test_rain_months(tb) and all_ok
            all_ok = test_rain_metrics(tb) and all_ok
        sys.stdout.write("\n")
    except FileNotFoundError as e:
        error(f"{e}")
        error("Har du sparat laboration1.ipynb i din hem-mapp (/)?")
        all_ok = False
    if all_ok:
        print("Allt ok. Bra jobbat!")
    else:
        print("Minst ett test misslyckades, se meddelande i loggen ovan.")

#GLOBALA VARIABLER
ROOT_SMHI = "./smhi.csv"

#Ladda in datan i minnet.
DATA = get_data()

if __name__ == "__main__":        
    test_nb()