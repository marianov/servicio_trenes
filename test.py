import datetime
import json
import urllib2
import pprint
import ipdb

pp = pprint.PrettyPrinter(indent=4)

# Respuesta ajax de mapa

SERVICE_KEY = 'v%23v%23QTUtWp%23MpWRy80Q0knTE10I30kj%23JNyZ'
SERVICE_RND = 'cqbzhBACphR46LlX&'
SERVICE_URI = 'http://trenes.mininterior.gov.ar/mitre/ajax_formaciones_mitre_tigre.php?%s'
SERVICE_URI = SERVICE_URI % ('rnd=%skey=%s' % (SERVICE_RND, SERVICE_KEY))


def procesa_posiciones_trenes(response):
    arr = response.split('_')
    if arr.__len__() > 0:
        cant = int(arr[0])
        m = 1
        markers = []
        for n in range(1, cant):
            marker = {
                'id': arr[m],
                'viaje': arr[m+12],
                'ramal': arr[m+3],
                'lat': arr[m+1],
                'lng': arr[m+2],
                'en_servicio': arr[m+10],
                'demorada': arr[m+5],
                'detenida': arr[m+6],
                'sin_senal': arr[m+7],
                'estado': arr[m+8],
                'velocidad': arr[m+11]
            }
            if marker['ramal'] == 5:
                marker['destino'] = 'Retiro'
            else:
                marker['destino'] = 'Tigre'
            markers.append( marker )
            m = m + 13
        return { "time": json.dumps(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')), "markers" : markers }

html = ""
# a veces este servicio devuelve 0 bytes, aunque con code 200 OK
while not html: 
  response = urllib2.urlopen(SERVICE_URI)
  html = response.read()


print json.dumps(procesa_posiciones_trenes(html)) 

# Respuesta ajax de widget

LINEAS = {
    'sarmiento': {
        'id': 1,
        'estaciones': [
            'Once', 'Caballito', 'Flores', 'Floresta', 'Villa Luro',
            'Liniers', 'Ciudadela', 'Ramos Mejia', 'Haedo', 'Moron', 'Castelar',
            'Ituzaingo', 'Padua', 'Merlo', 'Paso del Rey', 'Moreno'
        ]
    },
    'mitre_tigre': {
      'id': 5,
      'estaciones': [
         'Retiro','L. de la Torre','Belgrano c','Nu&ntilde;ez','Rivadavia','Vicente L&oacute;pez','Olivos','La Lucila','Mart&iacute;nez','Acassuso','San Isidro c','B&eacute;ccar','Victoria','Virreyes','San Fernando c','Carup&aacute','Tigre'
        ]
    },
    'mitre_mitre': 7,
    'mitre_suarez': 9,
}

SERVICE_URI = 'http://trenes.mininterior.gov.ar/ajax_arribos.php?ramal=%s&%s'
SERVICE_URI = SERVICE_URI % (
    LINEAS['sarmiento']['id'],
    'rnd=%skey=%s' % (
        SERVICE_RND,
        SERVICE_KEY
    )
)

response = urllib2.urlopen(SERVICE_URI)
html = response.read()


def check_tiempos(response, estacion, estaciones):
    arr = response.split("_")
    if arr.__len__() > 0:
      try:
        cant = int(arr[0])
        if cant > 0 and estacion > 0:
            index = estaciones.index(estacion)
            print 'Estacion %s' % estacion
            print 'Sentido %s' % estaciones[-1]
            # no tengo claro en que condiciones el array viene mas corto que lo esperado
            print 'Proximo: %s' %   ( arr[index*6+1] if (index*6+1 < len(arr) ) else "-" )
            print 'Siguiente: %s' % ( arr[index*6+2] if (index*6+2 < len(arr) ) else "-")
            print 'Siguiente: %s' % ( arr[index*6+3] if (index*6+3 < len(arr) ) else "-")

            print 'Sentido %s' % estaciones[0]

            print 'Proximo: %s' %   ( arr[index*6+4] if (index*6+4 < len(arr) ) else "-" )
            print 'Siguiente: %s' % ( arr[index*6+5] if (index*6+5 < len(arr) ) else "-")
            print 'Siguiente: %s' % ( arr[index*6+6] if (index*6+6 < len(arr) ) else "-")


            print '\n'
      except:
            ipdb.set_trace()


estaciones = LINEAS['sarmiento']['estaciones']
# 
# for estacion in estaciones:
#     check_tiempos(html, estacion, estaciones)
# 
# estaciones = LINEAS['mitre_tigre']['estaciones']
# 
# for estacion in estaciones:
#     check_tiempos(html, estacion, estaciones)
