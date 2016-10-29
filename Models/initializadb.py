#!/usr/bin/python

from Model import *

try:
	db.create_all()
except Exception as e:
	print "Falhou ao criar o db ",e
