def convert_temperature(temperature, unit):
    if unit.lower() == 'C':
        # Convert Celsius to Fahrenheit
        converted = (temperature * 9/5) + 32
        return round(converted, 2)
    elif unit.lower() == 'F':
        # Convert Fahrenheit to Celsius
        converted = (temperature - 32) * 5/9
        return round(converted, 2)
    else:
        return "Invalid unit. Please use 'celsius' or 'fahrenheit'."

# Example usage:
print(convert_temperature(100, 'C'))      # Output: 212.0
print(convert_temperature(212, 'F'))   # Output: 100.0
