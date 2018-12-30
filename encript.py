#coding: utf-8
print (" ______         _____  ")
print (" | ___ \       |  __ \ ")
print (" | |_/ /  ___  | |  \/ ")
print (" | ___ \ / _ \ | | __  ")
print (" | |_/ /| (_) || |_\ \ ")
print (" \____/  \___/  \____/ ")
print ("  ____  ____  ____  ____ ")
print (" ||T ||||D ||||L ||||G || ")
print (" ||__||||__||||__||||__|| ")
print (" |/__\||/__\||/__\||/__\| ") 
print ("")

print "BOG SECURITY"
print("")
texto =  "hola "
opcion= 0
opcion = int(raw_input("ecriptar= 1 , desencriptar= 2: ") )
abc= ['!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','#','o','p','q','r','s','t','u','v','w','x','y','z','-','&','@','.',';','0','1','2','3','4','5','6','7','8','9','|'] #45
rpas =len(abc) #contamos la cantidad de letras de abc
 
#funcion para inverti cadena
def invertir(var):
        return var[::-1]
 
#funcion de resta
def restar(x,y):
		if x>y:
			return x-y
		else:
			return y-x
 
#funcion para eliminar los espacios
def sin(txt):
		nuevo=""
		for x in txt:
	    		if x=='|':
 	      			nuevo = nuevo+' '
 	    		else:
        			nuevo = nuevo+x
   		return nuevo
 
def espacio(texto):
		espacios= ""
		for x in texto:
	    		if x==' ':
 	      			espacios = espacios+'|'
 	    		else:
        			espacios = espacios+x.lower() #convertimos a minusculas 
   		return espacios
 
 #opcion de encriptacion
if opcion == 1:
	print"opcion de encriptacion"
	mensaje=""
	clave =""
 
	mensaje = raw_input("introduzca mensaje a ecriptar: ")
	clave = raw_input("introduzca palabra clave: ")
	n =   len(mensaje)  #cuento la cantidad de caracteres 
	posicion= 0
	ab=clave[0]
	index = abc.index(ab)
	encoding= ""
	suma = 0
	espacios=""
	espacios=espacio(mensaje)
 
	for x in espacios:
   		for y in range(rpas):
   			li = 0
     			if x==abc[y]:
     				li=y+index
     			  	if li <= rpas:
     					encoding =encoding+abc[li]
 
     		     		else       :
     		     	 		suma= restar(rpas,li)
     		     	 		encoding =encoding+abc[suma]+'$'
     		     	 		suma = 0
	#print encoding
	print "mensaje cifrado: ",invertir(encoding)
	print "su clave es:", clave
if opcion == 2:
 
	print"opcion de desencriptacion"
	mensaje=""
	mensaje= ''
	mensaje = raw_input("Introduzca mensaje Encriptado: ")
	clave = raw_input("Introduzca clave: ")
 	ab=clave[0] #seleccionamos la letra de la posicion 0 
	index = abc.index(ab)  #usamos nuestra letra la ver en donde cae en la lista de abc
 
	contador = 0
	decoding= ''
	letra= ''
	tx= ''
	suma = 0
	rango =   len(mensaje) #cuento la cantidad de caracteres
 
	w=0
	while w < rango:
			letra=mensaje[w]
	 		if letra =='$':    #cuando esta opcion se cumple restamos 44
	 				incr = w+1
	 				li = 0
					tx=mensaje[incr]
					posicion= w
					for y in range(rpas):
						if tx == abc[y]:
							li=restar(index,y)
							#print index, " - ", y,"=",li
							suma=restar(rpas,li)
							decoding =decoding+abc[suma]
							w+=1
			else:
	 				li = 0
					tx=mensaje[w]
					posicion= w
					for s in range(rpas):
						if tx == abc[s]:
							li= restar(s,index)
							decoding =decoding+abc[li]
							#print posicion
 			w+=1
	#print decoding
	mensaje =invertir(decoding)
	#print mensaje
 	print "mensaje abierto: ",sin(mensaje)
 #DEV BY:
#/********************************************\
#/                                            \
#/                                            \
#/              Emilio Barroso                \
#/                                            \
#/                                            \
#/********************************************\
