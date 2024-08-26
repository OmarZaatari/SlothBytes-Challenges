def damage(dps: int, time: int, interval: str) -> int:
    output = dps * time
    match interval:
        case "second":
            return output
        case "minute":
            return output * 60
        case "hour":
            return output * 60 * 60
        case "day":
            return output * 60 * 60 * 24
        case "standard":
            return output * 60 * 60 * 24 * 30
        case "extended":
            return output * 60 * 60 * 24 * 31
        case "february":
            return output * 60 * 60 * 24 * 28
        case "leapFebruary":
            return output * 60 * 60 * 24 * 29
        case "year":
            return output * 60 * 60 * 24 * 365
        case "leapYear":
            return output * 60 * 60 * 24 * 366


print(damage(40, 5, "second"))
print(damage(100, 1, "minute"))
print(damage(100, 1, "hour"))
print(damage(40, 5, "day"))
print(damage(40, 5, "standard"))
print(damage(40, 5, "extended"))
print(damage(40, 5, "february"))
print(damage(40, 5, "leapFebruary"))
print(damage(40, 5, "year"))
print(damage(40, 5, "leapYear"))
