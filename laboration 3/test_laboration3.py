import traceback
import onnxruntime as ort
from torchvision import datasets, transforms
import torch
import numpy as np
import sys
from pathlib import Path
import os

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


def test_model(n_test_samples, model_path, data_path):
    info("Laddar fashion_model.onnx...")
    try:
        ortm = ort.InferenceSession(model_path)
    except Exception:
        traceback.print_exc()
        error("Fel vid inladdning av din fashion_model.onnx")
        exit(0)

    #Kolla så att modellen är ett CNN eller ett ANN.
    if len(ortm.get_inputs()[0].shape) == 4:
        model_case = "CNN"
    elif len(ortm.get_inputs()[0].shape) == 3:
        model_case = "ANN"
    else:
        error("Din modell är inte ett CNN eller ANN. Kontrollera så att du har använt rätt lager.")
        exit(0)

    info("Laddar in testdata...")
    fashion_mnist_test = datasets.FashionMNIST(data_path, train=False, download=True, transform=transforms.ToTensor())
    test_loader = torch.utils.data.DataLoader(fashion_mnist_test, shuffle=True, batch_size=1)

    info("Testar din modell på valideringsdata (5000 bilder)...")
    n_samples = 0
    n_correct = 0
    for bild, plagg in test_loader:

        bild_in = bild.numpy() if model_case == "CNN" else bild.numpy().reshape(1, 1, 784)
        
        out = ortm.run(None, dict(input=bild_in))
        pred = np.argmax(out)
        if pred == plagg:
            n_correct += 1
        #print(f"Pref: {pred} GT: {plagg}")
        n_samples += 1
        if n_samples > n_test_samples:
            return n_correct / n_samples
    return n_correct / n_samples

def check_model(model_path):
    info("Laddar fashion_model.onnx...")
    try:
        ortm = ort.InferenceSession(model_path)
    except Exception:
        traceback.print_exc()
        error("Fel vid inladdning av din fashion_model.onnx")
        exit(0)

    #Kolla så att modellen är ett CNN eller ett ANN.
    if len(ortm.get_inputs()[0].shape) == 4:
        model_case = "CNN"
    elif len(ortm.get_inputs()[0].shape) == 3:
        model_case = "ANN"
    else:
        error("Din modell är inte ett CNN eller ANN. Kontrollera så att du har använt rätt lager.")
        exit(0)
    
    print(f"Din modell fungerar att läsa in och är av arkitekturen: {model_case}")

if __name__ == '__main__':

    DATA_PATH = 'shared/datasets/'
    model_path = 'fashion_model.onnx'
    
    #Kolla modellen
    check_model(model_path)

    #Gör tre test av modellen och ta medelvärdet        
    ACC = []
    iters = 3
    for ik in range(iters):
        info(f"Predikterar på iteration {ik+1}/3...")
        accs = test_model(5000, model_path, DATA_PATH)
        success(f"Procent korrekt för denna iteration: {accs * 100:.01f}%")
        ACC.append(accs)
    
    accuracy = sum(ACC) / iters
    
    #print a line   
    print("-------------------------------------------------------------------")
    
    success(f"Din modell hade genomsnitt rätt på {accuracy * 100:.01f}% av bilderna.")

    if accuracy >= 0.925:
        success("Bra jobbat, du har klarat laborationen! 🎉🎈  Din modell är otroligt bra!")
    elif accuracy >= 0.905 < 0.925:
        success("Bra jobbat, du har klarat laborationen! 🎉🎈  Din modell är verkligen bra!")
    elif accuracy >= 0.885 < 0.905:
        success("Bra jobbat, du har klarat laborationen! 🎉🎈  Men kanske kan du skapa en ännu bättre modell?")
    elif accuracy >= 0.80:
        info("Nästan där! Bara några procent kvar till 88.5%...")
    elif accuracy >= 0.5:
        info("Bra början, din modell svarade rätt i mer än hälften av försöken. Målet är 88.5%.")
    elif accuracy >= 0.15:
        info("Din modell har lärt sig något! Den är bättre än slumpmässigt valda parametrar men du behöver göra den smartare, vi siktar på något bättre än 88.5%!")
    else:
        error("Din modell ser inte ut att vara tränad, den har nästan samma resultat som en modell som väljer slumpmässiga prediktioner av klass. Kontrollera så att du sparar den tränade modellen!")

    #print a line   
    print("-------------------------------------------------------------------")