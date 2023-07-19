COLOR = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

PREFIXES = ["", "kilo", "mega", "giga", "tera", "peta"]

def label(colors):
    val = COLOR[colors[0].lower()]*10 + COLOR[colors[1].lower()]
    val *= 10**(COLOR[colors[2].lower()] % 3)
    prefix = COLOR[colors[2].lower()] // 3
    if val > 1000:
        return f"{val//1000} {PREFIXES[prefix+1]}ohms"
    return f"{val} {PREFIXES[prefix]}ohms"
