
# -*- coding: utf8 -*-
"""
>>> anotar(0,1,0,2,1,0)
'15 - 0'


>>> anotar(0,1,0,2,2,0)
'15 - 0'

>>> anotar(40,1,40,2,2,0)
'15 - 0'

>>> anotar('device',1,'device',2,1,0)
'15 - 0'
"""
global mu 

def anotar(punto,jug1,puntos2,jug2,anotador,numeroEmpate):
	
	if punto !='device' and puntos2!='device':
		
	
		if anotador==1:
			if punto==0:
				punto= punto+15
			elif punto==15:	
				punto= punto+30
			elif punto>15:
				punto= punto+40
			elif punto==40:
				punto='device'
		
			
		
		
		elif anotador==2:	
			if 	puntos2==0:
				puntos2= puntos2+15
			elif puntos2==15:	
				puntos2= puntos2+30
			elif puntos2>15:	
				puntos2= puntos2+40
			elif puntos2==40:
				puntos2= 'device'	
	mu =' Marcador ['+mostrarScore(punto,jug1,puntos2,jug2,anotador,numeroEmpate)+']'
	
	return mu
	
	

	
def mostrarScore(punto,jug1,puntos2,jug2,anotador,numeroEmpate):
	
	if punto==puntos2 and punto =='device':
		if anotador==1:
			if punto=='device':
				if numeroEmpate==0:
					punto='adv'
				else:
					punto='-'
			
		
		
		elif anotador==2:	
			if puntos2=='device':
				if numeroEmpate==0:
					puntos2='adv'
				else:
					punto='-'
		variable= punto +' - '+ puntos2	
	
	elif punto>40:
		variable ='set - 40'
	elif puntos2>40:
		variable='40 - set'		
		
	
	return variable	
		
	
