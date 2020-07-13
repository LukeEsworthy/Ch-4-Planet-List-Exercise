planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

last_two = ["Uranus", "Neptune"]
planet_list.extend(last_two)

planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[4:8]

del planet_list[8]
