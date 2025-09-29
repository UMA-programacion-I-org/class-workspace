def triangle_area(base, height=1):
    return (base * height) / 2


# Positional arguments call
print(triangle_area(4, 5))

# Named arguments call
print(triangle_area(base=6, height=7))

# Default argument call
print(triangle_area(10))
