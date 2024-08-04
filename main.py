from PyQt5.QtWidgets import QMessageBox

#def main():


def length_converter(value, from_unit, to_unit):
    units = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "foot": 3.28084,
        "centimeter": 100,
        "inch": 39.3701,
        "decimeter": 10,
        "millimeter": 1000,
        "micrometer": 1e6,
        "nautical mile": 0.000539957,
        "yard": 1.09361
    }
    return value * (units[to_unit] / units[from_unit])


def weight_converter(value, from_unit, to_unit):
    units = {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounce": 0.03527396195,  
        "ton": 1e-6
    }
    return value * (units[to_unit] / units[from_unit])


def temp_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    
    return value


def get_unit_list(units_dropdown, from_dropdown, to_dropdown):
    unit_type = units_dropdown.currentText()
    from_dropdown.clear()
    to_dropdown.clear()

    if unit_type == 'Length':
        units = ['meters', 'kilometers', 'miles', 'foot', 'centimeter', 'inch', 'decimeter', 'millimeter', \
                 'micrometer', 'nautical mile', 'yard']
        
    elif unit_type == 'Weight':
        units = ['grams', 'kilograms', 'pounds', 'ounce', 'ton']

    elif unit_type == 'Temperature':
        units = ['celsius', 'fahrenheit', 'kelvin']

    from_dropdown.addItems(units)
    to_dropdown.addItems(units)


def show_results(value_input, from_dropdown, to_dropdown, units_dropdown, result_label, window):
    try:
        value = float(value_input.text())
        from_unit = from_dropdown.currentText()
        to_unit = to_dropdown.currentText()
        unit_type = units_dropdown.currentText()
        
        if unit_type == 'Length':
            conversion_result = length_converter(value, from_unit, to_unit)

        elif unit_type == 'Weight':
            conversion_result = weight_converter(value, from_unit, to_unit)

        elif unit_type == 'Temperature':
            conversion_result = temp_converter(value, from_unit, to_unit)
            
        result_label.setText(f'Result: {conversion_result}')
        
    except ValueError:
        QMessageBox.warning(window, 'Invalid inputs', 'Please enter a number (Ex. 123)')


if __name__ == "__main__":
    main()