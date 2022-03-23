peliculas={}

print("Bienvenidos al cine")
print ("digite la pelicula y genero que desea guardar")
for item in range(3):
 pelicula=input("Digite la pelicula: ")
 genero=input("Digite el genero: ")
 peliculas[pelicula]=genero
 
for p,g in peliculas.items():
    print("La pelicula",p,"Es de genero",g) 

