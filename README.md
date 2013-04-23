Mapa en tiempo real de trenes
-----------------------------
Para instalarlo:
-----------------
	pip install -r requirements.txt

Para correrlo
--------------
	python index.py


Para acumular datos de calidad de servicio
--------------------------------------------


  python guardar_datos.py >> markers.txt

Guarda en json los marcadores de posicion y estado de servicios

Se puede correr por ejemplo con cron o con screen y watch -n 4 "python guardar_datos.py  | tee -a markers.txt"
