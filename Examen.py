contador=0
R="si"
saldo=0
op=0
saldon=0
while contador<=3:
 print("Bienvenido a la plataforma virtual del banco")
 print("Digite su nombre de usuario")
 usuario=input()
 print("Digite su contraseña")
 contraseña=input()
 if usuario.upper() == "RDM18" and contraseña.upper() == "RDM2002":
        print("Los datos ingreasados son corectos")
        contador=3
        R="SI"
        while (R=="SI"):
         print("Seleccione la opcion que se desea realizar")
         A= "DEPOSITO"
         print(A)
         B= "RETIRO"
         print(B) 
         C="SALDO"
         print(C)
         D="SALIR"
         print(D)
         lista=[A,B,C,D]
         corrA=False;
         corrB=False;
         while (not corrA):
             print("Su seleccion es")
             seleccion=input()
             if seleccion.upper() in lista and seleccion.upper()==A:
                 while(not corrB):
                     print("Digite el monto a ingresar")
                     op=int(input())
                     if op & 1000!=0:
                      saldon=op+saldo
                      saldo=saldon
                      print("Su deposito es", op) 
                     corrA=True 
                     corrB=True    
             elif seleccion.upper() in lista and seleccion.upper()==B:
              print("Digite el monto requerido")
              op=int(input())
              if op<=saldon:
               saldon=saldon-op
               saldo=saldon
               print("Su transaccion a sido efectuada",saldon)
              else:
               print("Saldo insuficiente para realizar la transaccion")
               corrA=True
             elif seleccion.upper() in lista and seleccion.upper()==C:
                corrA=True
                print("su saldo es un total de",saldon)
             elif seleccion.upper() in lista and seleccion.upper()==D:
                 print("Gracias por preferirnos")
                 corrA=True
                 exit()
             else:
                 print("Seleccion no valida") 
         print("Desea reaizar otra transaccion")
         R=input() 
         if R.upper()=="NO":
             print("Gracias por preferirnos")
             exit()  
 else:
  print("Los datos ingresados no son correctos :(")
  if contador==3:
   print("Limite de intentos alcanzado bloqueo de seguridad")
  contador=contador+1