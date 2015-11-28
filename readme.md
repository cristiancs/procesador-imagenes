# Procesador de Imagenes    

Este procesador de imagenes corresponde a la tercera actividad para el ramo de Introducción a la Ingenieria en la Universidad Técnica Federico Santa María.

Requrimientos:
* Numpy
* Pillow

Modo de Uso:
```python
EscaladeGrises('file.jpg')
Negativo('file.jpg')
RotarImagen('logo-usm.jpg',90)
RotarImagen('logo-usm.jpg',180)
RotarImagen('logo-usm.jpg',270)
RotarImagen('logo-usm.jpg','espejo-horizontal')
RotarImagen('logo-usm.jpg','espejo-vertical')
FiltroOriginal('logo-usm.jpg',(149, 6, 0),100)
Filtro2('logo-usm.jpg')
Filtro3('logo-usm.jpg',(149`, 6, 0),100)

# (149, 6, 0) es el color a destacar y 100 es la tolerancia
```
Salidas:

EscaladeGrises: 

![alt text](http://imgur.com/lP3ZfbT.jpg)
Negativo: 

![alt text](http://imgur.com/Hs5Ujap.jpg)
RotarImagen(90): 

![alt text](http://imgur.com/xpm4K5F.jpg)
RotarImagen(180): 

![alt text](http://imgur.com/BSVvFDB.jpg)
RotarImagen(270): 

![alt text](http://imgur.com/yjk12IG.jpg)
RotarImagen(espejo-horizontal): 

![alt text](http://imgur.com/LGpJ7eu.jpg)
RotarImagen(espejo-vertical): 

![alt text](http://imgur.com/M3suz2f.jpg)
FiltroOriginal: 

![alt text](http://i.imgur.com/rFv2cod.jpg.jpg)
Filtro2: 

![alt text](http://i.imgur.com/OpWFPJ6.jpg)
Filtro3: 

![alt text](http://i.imgur.com/9rXumWt.jpg)