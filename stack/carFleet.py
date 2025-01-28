def carFleet(position,speed,distance):
    cars = sorted(zip(position,speed),reverse=True)

    fleets = 0
    current_time = 0

    for idx in range(len(cars)):
        position,speed = cars[idx]

        # distance = speed * time
        time_will_take = (distance - position) / speed


        if(time_will_take > current_time):
            fleets += 1
            current_time = time_will_take

    return fleets


print(carFleet([10, 8, 5, 3, 0],[2, 4, 1, 3, 1], 100))

