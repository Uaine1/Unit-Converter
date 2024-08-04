# Unit Converter 

## Description

My application **Unit Converter** has a GUI made in **PyQt5**, I designed to it convert different unit of Length, Weight, and Temperature. The application provides a user friendly interface for selecting unit types, selecting unit, and converting values with so much ease. It offers the user a straightforward way to perform a unit conversion without manually calculating the results. It also useful for students that wants to immediately know the converted value of a specific unit.

## Features

**Unit Type Selection**
Every user of my unit converter has the freedom to select which unit type they want to use. The available
unit changes every time the user select a unit type.

**Dynamic Unit List**
Everytime a user select a unit type, the available unit in the dropdown button of From and To dynamically
changes.

**Unit Conversion**
The application supports conversion between units inside the unit types Length, Weight, and Temperature.
For example a weight conversion between pounds and kilograms.

## Installation

To run my unit converter application you need **Python 3** installed on your PC, also you need to install
PyQt5 using a pip install
```bash
pip install PyQt5
```

## Usage

1. Run the application: You can press the run button on you IDE or execute this script on your
terminal.
```bash
python main.py
```
To run the test file execute this script on your terminal.
```bash
pytest test_main.py
```

2. Unit type selection: You can choose a unit type based on Length, Weight, and Temperature,
you can see the unit types inside the first dropdown button of the application.

3. Choose a unit: You can select which unit you want to convert from and convert into, using the small
dropdown buttons on each section of From and To.

4. Enter the value to convert: Input the numbers or measurements that you want to be converted.
PS. The application is only accepting numbers, strictly no letters.

5. Click the convert button: By click this button, the application will initiate its task. To convert
everything the user inputs in the textbox. After clicking the button the result will show under the input
textbox in red text.


## Contributing

If you would like to contribute or you have suggestions on how should I improve my application.
I would like to discuss it with you, also feel free to submit a pull request. For major changes,
please open an issue first so we can discuss what changes you want to make on my application.

## License

My application is free to use by everyone on the internet just contact me first before doing so.