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

TOLERANCES = {
    "grey": 0.05, "violet": 0.1, 
    "blue": 0.25, "green": 0.5, 
    "brown": 1, "red": 2, 
    "gold": 5, "silver": 10
}

def resistor_label(colors):
    if len(colors) < 4:
        return "0 ohms"
    val = colors[:3] if len(colors) > 4 else colors[:2]
    resistor = sum(COLOR[digit] * 10**power for power, digit in enumerate(val[::-1]))
    resistor *= 10**(COLOR[colors[-2].lower()] % 3)
    prefix = COLOR[colors[-2].lower()] // 3
    if resistor > 1000:
        resistor = int(resistor/1000) if resistor % 1000 == 0 else resistor/1000
        return f"{resistor} {PREFIXES[prefix+1]}ohms ±{TOLERANCES[colors[-1]]}%"
    return f"{resistor} {PREFIXES[prefix]}ohms ±{TOLERANCES[colors[-1]]}%"
