#def puerto():
#    try:
#        puerto=int(input('''
#
#        ╔════════════════════════════════════════════════╗
#        ║ ¿Desea proxies con algún puerto en específico? ║
#        ╠════════════════════════════════════════════════╣
#        ║ -número entre 1 y 65535                        ║
#        ║ ej:42069                                       ║
#        ╚════════════════════════════════════════════════╝

#        >'''))
#        if puerto < 1 or puerto > 65535:
#            print('[bot]introduzca un puerto valido por favor')
#    except ValueError:
#        print('[bot]escriba un numero por favor')
#        time.sleep(1)

#añadir generadores rapidos
#añadir colores

import time
import requests
import pycountry



def cantidad():
    try:
        cantidad=int(input("""

        ╔═══════════════════════════════════════════╗
        ║ ¿Cuántos proxies desea 'tomar prestados'? ║
        ╠═══════════════════════════════════════════╣
        ║ de 1 a 1000                               ║
        ║ ej:666                                    ║
        ╚═══════════════════════════════════════════╝
        default = 100

        > """))


        if cantidad < 1000 and cantidad > 0:
            print(f'''      [bot]ok,{cantidad} proxys entonces''')
        elif cantidad > 1000 or cantidad < 1:
            print('''       [bot]te dije que el limite eran 1000....ahora tendre que matarte...''')
    except ValueError:
        print('''       [bot]pues 100 proxies agarraremos ''')
        cantidad = 100

    return cantidad

def tipoProxy():
    try:
        tipoProxy =str(input('''

        ╔═════════════════════════════════════╗
        ║    ¿Qué tipo de proxy prefieres?    ║
        ╠═════════════════════════════════════╣
        ║ - http  (101.51.139.179:8080)       ║
        ║ -socks4(s4) (177.190.145.171:5678)  ║
        ║ -socks5(s5) (210.16.73.82:1080)     ║
        ║ - all                               ║
        ╚═════════════════════════════════════╝
        default = all

        >'''))

        def tipoprint():
            print(f'''      [bot]{tipoProxy} elegimos entonces''')

        if tipoProxy == 'http':
            tipoprint()

        if tipoProxy == 'socks5' or tipoProxy == 's5' :
            tipoprint()

        if tipoProxy == 'socks4' or tipoProxy == 's4':
            tipoprint()

        if tipoProxy == 'all' or tipoProxy == '':
            tipoProxy = 'all'
            print('''       [bot]ok,todos entonces,oido cocina''')



    except ValueError:
        tipoProxy='all'
        print('''       [bot]ok,todos entonces,oido cocina''')

    return tipoProxy

def ssl():
    try:
        ssl=str(input('''

        ╔═════════════════════════════════════╗
        ║ ¿Quieres que tengan protección SSL? ║
        ╠═════════════════════════════════════╣
        ║ -si                                 ║
        ║ -no                                 ║
        ║ -all                                ║
        ╚═════════════════════════════════════╝
        default = all

        >'''))

        if ssl == 'si':
            ssl = 'yes'
            print('''       [bot]pues con SSL entonces''')

        if ssl == 'no':
            print('''       [bot]pues sin SSL entonces''')

        if ssl == 'all' or ssl == '':
            ssl = 'all'
            print('''       [bot]marchando mezcla entonces''')

    except ValueError:
        ssl = 'all'
        print('''       [bot]marchando mezcla entonces''')


    return ssl

def codigoF():
    try:

        codigo=str(input('''

        ╔════════════════════════════════════════════════════════════╗
        ║            ¿de donde quieres que sea el proxy?             ║
        ╠════════════════════════════════════════════════════════════╣
        ║ -all                                                       ║
        ║ -especifique  codigo Alpha 2/3 ISO country code            ║
        ║ (lista con los codigos:https://www.iban.com/country-codes) ║
        ║  ej: ES,US,MX...                                           ║
        ║  ej: ESP,USA,MEX..                                         ║
        ╚════════════════════════════════════════════════════════════╝

        default = all
        >''')).upper()




        if len(codigo) > 2 and len(codigo)< 4:
            pais= pycountry.countries.get(alpha_3=codigo)
            codigo = pais.alpha_2
            print(f'''       [bot]pues de {pais.name} con código {pais.alpha_2}''')


        elif codigo.lower() == 'all' or codigo == '' or len(codigo)>3:
            codigo = 'all'
            print('''       [bot]pues de todos los paises será''')

        elif len(codigo) == 2:
            pais= pycountry.countries.get(alpha_2=codigo)
            codigo = pais
            print(f'''       [bot]pues de {pais.name} con código {pais.alpha_2}''')

    except AttributeError:
        codigo = 'all'
        print('''       [bot]no existe el codigo introducido, deja en blanco si no sabes cual poner''')
        codigoF()

    return codigo

def anonimity():
    try:
        anonimity=str(input('''

        ╔═══════════════════════════════════════════╗
        ║ ¿Cómo de anónimo deseas que sea el proxy? ║
        ╠═══════════════════════════════════════════╣
        ║ -elite                                    ║
        ║ -anonymous(-an)                           ║
        ║ -transparent(-tr)                         ║
        ║ -all                                      ║
        ╚═══════════════════════════════════════════╝
        default = all

        >'''))

        if anonimity == 'elite':
            print('''       [bot]ooh la la, bon choix monsieur''')
        elif anonimity == 'anonymous' or anonimity=='an':
            print('''       [bot]modo espia activado, anonimato asegurado''')
        elif anonimity == 'transparent'or anonimity=='tr':
            print('''       [bot]¿eres rasho mcquin? porque menuda velocidad''')
        elif anonimity == 'all' or anonimity == '':
            anonimity='all'
            print('''       [bot]arriesgarse es de ganadores''')

    except ValueError:
        anonimity = 'all'
        print('''       [bot]arriesgarse es de ganadores''')

    return anonimity

def banner():

    bannerInput = int(input('''

    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗
    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝     ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║       ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝

    __                __                                     ___ ___                __
    |  |--.-----.----.|  |--.-----.    .-----.-----.----.    |   |   |.-----.----.--|  |.--.--.--.--.-----.
    |     |  -__|  __||     |  _  |    |  _  |  _  |   _|    |   |   ||  -__|   _|  _  ||  |  |_   _|  _  |
    |__|__|_____|____||__|__|_____|    |   __|_____|__|       \_____/ |_____|__| |_____||_____|__.__|_____|
                                    |__|
                            .----.-----.-----.    .---.-.--------.-----.----.
                            |  __|  _  |     |    |  _  |        |  _  |   _|
                            |____|_____|__|__|    |___._|__|__|__|_____|__|

                            ╔════════════════════════════════════════════════╗
                            ║                    Opciones                    ║
                            ╠════════════════════════════════════════════════╣
                            ║ [1]Generar Proxies de forma rapida             ║
                            ║ [2]Generar Proxies con parametros customizados ║
                            ╚════════════════════════════════════════════════╝



    >'''))

    if bannerInput == 2:
        print('\n\n[bot]Hola ^^, para llevar a cabo esta tarea tienes que introducir una serie de datos, yo sere tu asistente personal, espero que disfrutes de tu estancia\nvamos a ello!')
        url2 ='https://api.proxyscrape.com?request=getproxies'+'&proxytype='+str(tipoProxy())+'&timeout=5000&anonymity='+str(anonimity())+'&ssl='+str(ssl())+'&limit='+str(cantidad())+'&country='+str(codigoF())
        #url='http://pubproxy.com/api/proxy?level=anonymous&type=http&last_check=2&limit=20&https=true&cookise=true'
        r = requests.get(url2)
        f=open('proxies.txt','a',encoding='utf-8',errors='ignore')
        f.write(r.text)
        print('[bot]\nhemos terminado! comprueba el archivo proxies.txt y te llevaras una grata sorpresa ^^')

    elif bannerInput == 1:
        url1 ='https://api.proxyscrape.com?request=getproxies'+'&proxytype='+str(tipoProxy())+'&timeout=5000&anonymity=all&ssl=all&limit='+str(cantidad())+'&country=all'
        r = requests.get(url1)
        f=open('proxies.txt','a',encoding='utf-8',errors='ignore')
        f.write(r.text)
    else:
        print('no has introducido ninguna opción')
        time.sleep(1)
        banner()



banner()

