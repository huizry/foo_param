from foo_param import calculations, utilities

if __name__ == "__main__":
    sun_radius = 696340 #km
    sun_volume = calculations.sphere_volume(sun_radius)
    print(utilities.format_volume(sun_volume, 2, "km", "sun"))

    moon_radius = 1737.4 #km
    moon_volume = calculations.sphere_volume(moon_radius)
    print(utilities.format_volume(moon_volume, 2, "km", "moon"))

    nba_ball_radius = 12 #cm
    nba_ball_volume = calculations.sphere_volume(nba_ball_radius)
    print(utilities.format_volume(nba_ball_volume, 2, "cm", "nba ball"))