import json
from datetime import datetime
import pytz

if __name__ == '__main__':
    places_tz = ['Asia/Tokyo', 'Europe/Madrid', 'America/Argentina/Buenos_Aires', 'US/eastern', 'US/Pacific', 'UTC']
    cities_name = ['Tokyo', 'Madrid', 'Buenos Aires', 'New York', 'California', 'UTC']
    
    # Creamos un diccionario para guardar los datos
    resultados = {}

    for place_tz, city_name in zip(places_tz, cities_name):
        city_time = datetime.now(pytz.timezone(place_tz))
        # Guardamos la fecha/hora como texto en el diccionario
        resultados[city_name] = city_time.strftime('%Y-%m-%d %H:%M:%S')
        print(f'Fecha en {city_name} - {city_time}')

    # ESTO CREA EL ARCHIVO JSON
    with open('horas_paises.json', 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=4, ensure_ascii=False)
    
    print("\n¡Archivo horas_paises.json generado con éxito!")
