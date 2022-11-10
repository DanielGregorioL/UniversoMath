#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 18:42:18 2022

@author: UniversoMath
"""
import math
import turtle

turtle.bgcolor("black")
turtle.pencolor("green")

turtle.pensize(2)
def sier(n,d,p,q,r):
	"""
    Función que traza la n-ésima iteración
    del triángulo de sierpinsky.
    
    Parametros:
        
	   n: numero de iteraciones
	   d: longitud del triángulo
	   p: posicion inicial
	"""
	turtle.penup()
	turtle.setpos(p[0], p[1])
	turtle.pendown()
	turtle.goto(q[0],q[1])
	turtle.goto(r[0],r[1])
	turtle.goto(p[0],p[1])
	medio_pq = ((p[0]+q[0])/2, (p[1]+q[1])/2)
	medio_qr = ((q[0]+r[0])/2, (q[1]+r[1])/2)
	medio_rp = ((r[0]+p[0])/2, (r[1]+p[1])/2)
	if n>1:
		
		sier(n-1,d/2,p,medio_pq,medio_rp)
		
		turtle.penup()
		sier(n-1,d/2,medio_pq, q, medio_qr)
		turtle.penup()
		sier(n-1,d/2,medio_rp,medio_qr,r)
		

sier(2,250,(0-150,0),(250-150,0),
     (125-150,math.sqrt((250**2)-(125**2))))