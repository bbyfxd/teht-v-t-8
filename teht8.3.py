import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1999',
         autocommit=True
         )
def haku():
    icao = input("Syötä lentokentän ICAO-koodi: ")
    sql = "select latitude_deg, longitude_deg from airport where gps_code =" + icao + ""
    kursori = yhteys.cursor()
    kursori.excute(sql)
    response = kursori.fetchall()
    return response


print("lasketaan kahden lentokentän etäisyys!\n")
loc1 = haku()
loc2 = haku()
print(loc1[0])
print(type(loc1[0]))

gap = distance.distance(loc1, loc2).km
print(gap)
