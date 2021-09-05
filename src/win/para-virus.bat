@echo off

attrib -s -h
del *.lnk

@echo off
title Memoria Flash 
color 1E
@echo ----------------------------------------------
@echo ---- REPARACION DE ARCHIVOS EN MEMORIAS USB ----
@echo ----------------------------------------------
@echo Cambiando Atributo de Carpetas
Attrib /d /s -r -h -s *.* 
@echo ----------------------------------------------
@echo Eliminado Accesos Directos
if exist *.lnk del *.lnk 
@echo ----------------------------------------------
@echo Eliminado Autorun
if exist autorun.inf del autorun.inf 
@echo ----------------------------------------------
@echo Operacion OK...
@echo ----------------------------------------------
@echo ----------------------------------------------
@echo Script provisto por HiperMegaRed Blog    
@echo ----------------------------------------------
@echo ----------------------------------------------
@echo http://hipermegared.net
pause
