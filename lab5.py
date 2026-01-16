import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS

macierz=np.array([
    [30000 , 8000,  2],
    [80000 , 9000,  9],
    [90000 , 8500,  12],
    [100000 ,12500, 15]
])
opcja=["Opcja_1","Opcja_2","Opcja_3","Opcja_4"]
typy=np.array([-1, 1, -1])
wagi=np.array([0.1, 0.6, 0.3])

topsis=TOPSIS()
dane_topsis=topsis(macierz,wagi,typy)

granica_min_max=np.array([
    [30000, 100000],   
    [8000, 12500],    
    [2, 20]           
])
spotis=SPOTIS(granica_min_max)
spotis_scores=spotis(macierz,wagi,typy)

wynik=pd.DataFrame({
    "Opcja":opcja,
    "TOPSIS":dane_topsis,
    "SPOTIS":spotis_scores
})

print(wynik)
najlepsza_topsis=wynik.loc[wynik["TOPSIS"].idxmax(),"Opcja"]
najlepsza_spotis=wynik.loc[wynik["SPOTIS"].idxmin(),"Opcja"]

if najlepsza_topsis==najlepsza_spotis:
    print("Najlepsza opcja: "+najlepsza_topsis)
else:
    print("TOPSIS i SPOTIS pokazały różne opcje:")
    print("TOPSIS" +najlepsza_topsis)
    print("SPOTIS" +najlepsza_spotis)

