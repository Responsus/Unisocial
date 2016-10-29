#!/usr/bin/python

import sys
sys.path.append("/srv/unisocial")
from Models.Model import *
from ClassesDao import FaculdadeDao


try:
	fdao = FaculdadeDao.FaculdadeDao()
	fac = fdao.select(1)
	print fac
	print fac.getNome()
except Exception as e:
	print e
