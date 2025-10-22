import config


def weight_on_planet(mass, gravity):
    return mass * gravity


mass_kg = 70  # mass of the object in kilograms
weight_earth = weight_on_planet(mass_kg, config.GRAVITY_EARTH)
weight_moon = weight_on_planet(mass_kg, config.GRAVITY_MOON)
weight_mars = weight_on_planet(mass_kg, config.GRAVITY_MARS)

print(f"Weight on Earth: {weight_earth} N")
print(f"Weight on Moon: {weight_moon} N")
print(f"Weight on Mars: {weight_mars} N")
