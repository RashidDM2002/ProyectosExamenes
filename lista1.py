diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador",

"Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose",

"Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota",

"Venezuela": "Caracas", "España": "Madrid"}
 
print("Coloque el pais") 
pais=input()
if pais in diccionario:
    print("Su capital capital es ",diccionario.get(pais))
