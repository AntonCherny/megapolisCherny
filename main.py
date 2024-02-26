
with open("space.txt", "r", encoding="utf8") as f:
    reader=list(int.reader(f,delimiter=',', quotechar='"'))[1:]


'''
with open("space_new.txt", "r", encoding="utf8") as pl:
    reader = list(reader(pl,delimiter=',', quotechar='"'))[1:]
    for ShipName, planet, coord_place, direction in reader:
        if input() in ShipName:
            print(f"Корабль {ShipName} был отправлен с планеты: {planet} и его направление движения было: {direction}")
            if input('stop'):
                break
'''
