import urllib2
import pprint

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
            m = m + 13

response = urllib2.urlopen(SERVICE_URI)
html = response.read()

procesa_posiciones_trenes(html)

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
    'mitre_tigre': 5,
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
        cant = int(arr[0])
        if cant > 0 and estacion > 0:
            index = estaciones.index(estacion)
            print 'Estacion %s' % estacion
            print 'Sentido %s' % estaciones[-1]
            print 'Proximo: %s' % arr[index*6+1]
            print 'Siguiente: %s' % arr[index*6+2]
            print 'Siguiente: %s' % arr[index*6+3]
            print 'Sentido %s' % estaciones[0]
            print 'Proximo: %s' % arr[index*6+4]
            print 'Siguiente: %s' % arr[index*6+5]
            print 'Siguiente: %s' % arr[index*6+6]
            print '\n'


estaciones = LINEAS['sarmiento']['estaciones']

for estacion in estaciones:
    check_tiempos(html, estacion, estaciones)
