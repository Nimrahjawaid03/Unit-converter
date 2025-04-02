import streamlit as st

# Conversion functions for all categories
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'micrometers': 0.000001,
        'nanometers': 0.000000001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254,
        'nautical_miles': 1852
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'metric_tons': 1000,
        'pounds': 0.453592,
        'ounces': 0.0283495,
        'carats': 0.0002,
        'stones': 6.35029
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

def convert_area(value, from_unit, to_unit):
    area_conversions = {
        'square_meters': 1,
        'square_kilometers': 1000000,
        'square_centimeters': 0.0001,
        'square_millimeters': 0.000001,
        'square_miles': 2589988.11,
        'square_yards': 0.836127,
        'square_feet': 0.092903,
        'square_inches': 0.00064516,
        'hectares': 10000,
        'acres': 4046.86
    }
    return value * area_conversions[from_unit] / area_conversions[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_conversions = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000,
        'cubic_centimeters': 0.001,
        'cubic_inches': 0.0163871,
        'cubic_feet': 28.3168,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.24,
        'fluid_ounces': 0.0295735,
        'tablespoons': 0.0147868,
        'teaspoons': 0.00492892
    }
    return value * volume_conversions[from_unit] / volume_conversions[to_unit]

def convert_speed(value, from_unit, to_unit):
    speed_conversions = {
        'meters_per_second': 1,
        'kilometers_per_hour': 0.277778,
        'miles_per_hour': 0.44704,
        'feet_per_second': 0.3048,
        'knots': 0.514444
    }
    return value * speed_conversions[from_unit] / speed_conversions[to_unit]

def convert_time(value, from_unit, to_unit):
    time_conversions = {
        'seconds': 1,
        'milliseconds': 0.001,
        'microseconds': 0.000001,
        'nanoseconds': 0.000000001,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'months': 2628000,
        'years': 31536000
    }
    return value * time_conversions[from_unit] / time_conversions[to_unit]

def convert_data_storage(value, from_unit, to_unit):
    data_conversions = {
        'bits': 1,
        'bytes': 8,
        'kilobits': 1000,
        'kilobytes': 8000,
        'megabits': 1000000,
        'megabytes': 8000000,
        'gigabits': 1000000000,
        'gigabytes': 8000000000,
        'terabits': 1000000000000,
        'terabytes': 8000000000000
    }
    return value * data_conversions[from_unit] / data_conversions[to_unit]

def convert_energy(value, from_unit, to_unit):
    energy_conversions = {
        'joules': 1,
        'kilojoules': 1000,
        'calories': 4.184,
        'kilocalories': 4184,
        'watt_hours': 3600,
        'kilowatt_hours': 3600000,
        'electronvolts': 1.60218e-19,
        'british_thermal_units': 1055.06
    }
    return value * energy_conversions[from_unit] / energy_conversions[to_unit]

def convert_pressure(value, from_unit, to_unit):
    pressure_conversions = {
        'pascals': 1,
        'kilopascals': 1000,
        'megapascals': 1000000,
        'bars': 100000,
        'atmospheres': 101325,
        'torr': 133.322,
        'psi': 6894.76
    }
    return value * pressure_conversions[from_unit] / pressure_conversions[to_unit]

def convert_power(value, from_unit, to_unit):
    power_conversions = {
        'watts': 1,
        'kilowatts': 1000,
        'megawatts': 1000000,
        'horsepower': 745.7
    }
    return value * power_conversions[from_unit] / power_conversions[to_unit]

def convert_angle(value, from_unit, to_unit):
    angle_conversions = {
        'degrees': 1,
        'radians': 57.2958,
        'gradians': 0.9
    }
    return value * angle_conversions[from_unit] / angle_conversions[to_unit]

def convert_frequency(value, from_unit, to_unit):
    frequency_conversions = {
        'hertz': 1,
        'kilohertz': 1000,
        'megahertz': 1000000,
        'gigahertz': 1000000000
    }
    return value * frequency_conversions[from_unit] / frequency_conversions[to_unit]

def convert_fuel_consumption(value, from_unit, to_unit):
    fuel_conversions = {
        'miles_per_gallon': 1,
        'kilometers_per_liter': 2.35215,
        'liters_per_100_kilometers': 235.215
    }
    return value * fuel_conversions[from_unit] / fuel_conversions[to_unit]

# Main app
def main():
    st.title("Unit Converter")
    
    conversion_type = st.selectbox("Select Conversion Type", [
        "Length", "Weight", "Temperature", "Area", "Volume", "Speed", "Time", 
        "Data Storage", "Energy", "Pressure", "Power", "Angle", "Frequency", 
        "Fuel Consumption"
    ])
    
    units = {
        "Length": ['meters', 'kilometers', 'centimeters', 'millimeters', 'micrometers', 'nanometers', 'miles', 'yards', 'feet', 'inches', 'nautical_miles'],
        "Weight": ['kilograms', 'grams', 'milligrams', 'metric_tons', 'pounds', 'ounces', 'carats', 'stones'],
        "Temperature": ['celsius', 'fahrenheit', 'kelvin'],
        "Area": ['square_meters', 'square_kilometers', 'square_centimeters', 'square_millimeters', 'square_miles', 'square_yards', 'square_feet', 'square_inches', 'hectares', 'acres'],
        "Volume": ['liters', 'milliliters', 'cubic_meters', 'cubic_centimeters', 'cubic_inches', 'cubic_feet', 'gallons', 'quarts', 'pints', 'cups', 'fluid_ounces', 'tablespoons', 'teaspoons'],
        "Speed": ['meters_per_second', 'kilometers_per_hour', 'miles_per_hour', 'feet_per_second', 'knots'],
        "Time": ['seconds', 'milliseconds', 'microseconds', 'nanoseconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years'],
        "Data Storage": ['bits', 'bytes', 'kilobits', 'kilobytes', 'megabits', 'megabytes', 'gigabits', 'gigabytes', 'terabits', 'terabytes'],
        "Energy": ['joules', 'kilojoules', 'calories', 'kilocalories', 'watt_hours', 'kilowatt_hours', 'electronvolts', 'british_thermal_units'],
        "Pressure": ['pascals', 'kilopascals', 'megapascals', 'bars', 'atmospheres', 'torr', 'psi'],
        "Power": ['watts', 'kilowatts', 'megawatts', 'horsepower'],
        "Angle": ['degrees', 'radians', 'gradians'],
        "Frequency": ['hertz', 'kilohertz', 'megahertz', 'gigahertz'],
        "Fuel Consumption": ['miles_per_gallon', 'kilometers_per_liter', 'liters_per_100_kilometers']
    }
    
    col1, col2 = st.columns(2)
    with col1:
        from_unit = st.selectbox("From", units[conversion_type])
    with col2:
        to_unit = st.selectbox("To", units[conversion_type])
    
    value = st.number_input("Enter value", value=1.0)
    
    if st.button("Convert"):
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif conversion_type == "Area":
            result = convert_area(value, from_unit, to_unit)
        elif conversion_type == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        elif conversion_type == "Speed":
            result = convert_speed(value, from_unit, to_unit)
        elif conversion_type == "Time":
            result = convert_time(value, from_unit, to_unit)
        elif conversion_type == "Data Storage":
            result = convert_data_storage(value, from_unit, to_unit)
        elif conversion_type == "Energy":
            result = convert_energy(value, from_unit, to_unit)
        elif conversion_type == "Pressure":
            result = convert_pressure(value, from_unit, to_unit)
        elif conversion_type == "Power":
            result = convert_power(value, from_unit, to_unit)
        elif conversion_type == "Angle":
            result = convert_angle(value, from_unit, to_unit)
        elif conversion_type == "Frequency":
            result = convert_frequency(value, from_unit, to_unit)
        elif conversion_type == "Fuel Consumption":
            result = convert_fuel_consumption(value, from_unit, to_unit)
        
        st.success(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")

if __name__ == "__main__":
    main()