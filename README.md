# Unit Converter 

#### Video Demo: 

#### Description
This is my final project for CS50's Introduction to Programming with Python Course <br />

My application **Unit Converter** has a GUI made in **PyQt5**, I designed it convert different unit of Length, Weight, and Temperature. The application provides a user friendly interface for selecting unit types, selecting unit, and converting values with so much ease. It offers the user a straightforward way to perform a unit conversion without manually calculating the results. It also useful for students in elementary,highschool, senior highschool and college that wants to immediately know the converted value of a specific measurements to desired unit.

#### Features

**Unit Type Selection** <br />
Every user of my unit converter has the freedom to select which unit type they want to use. The available
unit changes every time the user select a unit type.

**Dynamic Unit List** <br />
Everytime a user select a unit type, the available unit in the dropdown button of From and To dynamically
changes.

**Unit Conversion** <br />
The application supports conversion between units inside the unit types Length, Weight, and Temperature.
For example a weight conversion between pounds and kilograms.

#### Installation

To run my unit converter application you need **Python 3** installed on your mac or windows system, also you need 
to install PyQt5 using a pip install on your terminal.
```bash
pip install PyQt5
```
To run the test file you need to install **PyTest** on your mac or windows system.
```bash
pip install pytest
```
Or you can just type this on your terminal. To install all of the frameworks that I used to make this application.
```bash
pip install -r requirements.txt
```

#### Usage

1. Run the application: You can press the run button on you IDE or execute this script on your
terminal. If you want to manually test the application yourself.
```bash
python main.py
```
To run the test file execute this script on your terminal. If you want to automatically test the application
using **PyTest**
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

#### Code Description 

For the **project.py** <br />

**main()** <br />
The main() has all of my application's GUI configurations and its the one who handles everything. In main you
can change font color, background color, object spacing and etc to change the GUI. It also uses the functions such
as **temp_converter()**, to make sure the application do its intended tasks. <br />

**length_converter(value, from_unit, to_unit)** <br />
Responsible for convertering every unit under the unit type length. It recieves 3 arguments from the
user. <br />

**weight_converter(value, from_unit, to_unit)** <br />
Responsible for convertering every unit under the unit type weight. It recieves 3 arguments from the
user. <br />

**temp_converter(value, from_unit, to_unit)** <br />
Responsible for convertering every unit under the unit type temperature. It receives 3 arguments from the
user. <br />

**get_unit_list(units_dropdown, from_dropdown, to_dropdown)** <br />
It updates the unit list of From and To, depending on the selected unit type by the user. <br />

**show_results(value_input, from_dropdown, to_dropdown, units_dropdown, result_label, window)**
After receiving 4 arguments from the user, the user will finally will get an output for the value they input in
the app <br /> <br />

For the **test_project.py** <br /> 
Here using pytest we can automatically test the code from **project.py**. <br />
**test_length_converter()** <br />
**test_weight_converter()** <br />
**test_temp_converter()** <br />
These functions tests the functionality of the functions inside **project.py**, if they really can convert the inputted values
to the desired output by the user.

#### Contributing

If you would like to contribute or you have suggestions or ideas on how should I improve my application.
I'm open and would like to discuss it with you, also feel free to submit a pull request. For major changes,
please open an issue first so we can discuss what changes you want to make on my application.

#### That's all thank you!