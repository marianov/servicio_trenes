import urllib2
import pprint

SERVICE_KEY = 'v%23v%23QTUtWp%23MpWRy80Q0knTE10I30kj%23JNyZ'
SERVICE_RND = 'cqbzhBACphR46LlX&'
SERVICE_URI = 'http://trenes.mininterior.gov.ar/mitre/ajax_formaciones_mitre_tigre.php?%s'
SERVICE_URI = SERVICE_URI % ('rnd=%skey=%s' % (SERVICE_RND, SERVICE_KEY))

pp = pprint.PrettyPrinter(indent=4)

response = urllib2.urlopen(SERVICE_URI)


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
            pp.pprint(marker)

html = response.read()

procesa_posiciones_trenes(html)
