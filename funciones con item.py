def keyw(**datos):
    print("\nTipo de datos del argumnento",
          type(datos))
    for key, value in datos.items():
        print("{} is {}".format(key, value))

keyw(Firstname="Juan",
     lastname="Dominguez",
     Age=42,
     Phone=1234567890)
keyw(Firstname="Jhon",
     lastname="Wood",
     Email="davidvelecos@gmail.com",
     Country="wakanda",
     Age=15)