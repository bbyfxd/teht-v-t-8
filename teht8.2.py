def hae(lentoasema):
    sql = "select type, count(type), from airport where iso_country = "\
        + lentoasema + " group by type order by count(type) asc;"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(f"i{0}: {i[1]}")

x = input("Anna maan lyhenne: ")
x = x.upper()
hae(x)