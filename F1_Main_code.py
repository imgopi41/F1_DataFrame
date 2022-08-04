import pandas as pd

data = {
    "Driver":["Max Verstappen","Charles Leclerc","Sergio Perez","Carlos Sainz","Geroge Russell","Lewis Hamilton","Lando Norris","Esteban Ocan","Valtteri Bottas","Fernando Alonso","Kevin Magnussen","Daniel Ricciardo"],
    "Position":[1,2,3,4,5,6,7,8,9,10,11,12],
    "Number":[33,16,11,55,63,44,4,31,63,14,20,3],
    "Country":["Netherlands","Poland","Mexcio","Spain","Great Britain","Great Britain","Great Britain","France",'Finland',"Spain","Dainsh","Australia"],
    "Car":["Red Bull","Ferrari","Red Bull","Ferrari","Mercedes","Mercedes","McLaren","Alpine F1 Team","Alfa Romeo","Alpine F1 Team","Haas F1 Team","McLaren"],
    "Points":[208,170,163,144,143,127,70,56,46,37,22,19],
    "Gap":[0,-63,-70,-89,-90,-106,-163,-177,-187,-196,-211,-214]
}

dr = pd.DataFrame(data)
dr.set_index("Position",inplace=True)
print(dr)




