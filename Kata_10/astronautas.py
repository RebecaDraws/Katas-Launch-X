def water_left(astronauts, water_left, days_left):

    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:

            raise TypeError(f"todos los argumentos deberian ser del tipo int, pero se recibió: '{argument}'")
        except RuntimeError as err:
            print((f"No hay suficiente agua para que {astronauts} astronautas sobrevivan {days_left} dias!"))   

    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        
        raise RuntimeError(f"No hay suficiente agua para que {astronauts} astronautas sobrevivan {days_left} dias!")
    return (f"Total de agua despues de {days_left} dias es: {total_water_left} litros")

print(water_left(5,100,2))



