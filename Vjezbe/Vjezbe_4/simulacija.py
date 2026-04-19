import numpy as np
import matplotlib.pyplot as plt
from def_polja import Cestica


masa_e = 1 
masa_p = masa_e 
q_e = -1 
q_p = -q_e  


početno_stanje_e = [0, 0, 0, 0.1, 0.1, 0.1]  
početno_stanje_p = [0, 0, 0, 0.1, 0.1, 0.1]  
E = np.array([0, 0, 0])  
B = np.array([0, 0, 1])  

elektron = Cestica(masa_e, q_e, početno_stanje_e, E, B, dt=0.01)
pozitron = Cestica(masa_p, q_p, početno_stanje_p, E, B, dt=0.01)


 

elektron.simulacija(20)   

elektron.prikaži_putanju("Putanja elektrona")

pozitron.simulacija(20)

pozitron.prikaži_putanju("Putanja pozitrona")