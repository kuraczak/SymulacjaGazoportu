
def raportt():
    file = open("raport.txt", "w")
    amout = len(robots_list)
    file.write("Amount of robots: %i \n" % (amout))
    file.write("Amount of checkpoints: %i \n" % (len(checkpoints_list)))
    file.write("Amount of charging_stops: %i \n" % (len(charging_stops_list)))
    for i in range (0, len(robots_list)):
       file.write("Robot %i - speed: %i , battery: %i \n" %(i, robots_list[i].speed, robots_list[i].battery))
    file.write("Time of simulation %i \n" % (simulation_time*116))
    file.close()
    return
