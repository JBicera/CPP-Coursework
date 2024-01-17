import 'package:flutter/material.dart';
import 'dart:math';
import 'main.dart';

// Widget representing the calculator screen
class KinematicsCalculatorScreen extends StatefulWidget {
  @override
  _KinematicsCalculatorScreenState createState() =>
      _KinematicsCalculatorScreenState();
}

class _KinematicsCalculatorScreenState
    extends State<KinematicsCalculatorScreen> {
  String selectedEquation = 'V = V0 + at'; //Default selected equation
  double result = 0.0;
  final String delta =
      '\u0394'; // Save greek letter delta for "Change in" symbol

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Kinematics Calculator'),
        leading: IconButton(
            icon: Icon(Icons.arrow_back),
            onPressed: () {
              // Navigate directly to the MenuScreen
              Navigator.pushReplacement(
                context,
                MaterialPageRoute(
                  builder: (context) => MenuScreen(),
                ),
              );
            }),
      ),
      body: Container(
        decoration: BoxDecoration(
          color: Colors.grey[200],
        ),
        child: Column(
          // Display the result at the top of the screen
          children: [
            Container(
              width: double.infinity,
              color: Colors.grey[300],
              padding: EdgeInsets.all(16.0),
              child: Text(
                'Result: $result',
                style: TextStyle(fontSize: 24.0),
              ),
            ),
            Expanded(
              child: SingleChildScrollView(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Dropdown for selecting equations
                    DropdownButton<String>(
                      value: selectedEquation,
                      hint: Text('Select Kinematic Equation'),
                      onChanged: (String? newValue) {
                        setState(() {
                          selectedEquation = newValue!;
                        });
                      },
                      style: TextStyle(
                        fontSize: 24.0,
                        color: Colors.black,
                      ),
                      items: [
                        // All available equations
                        'V = V0 + at',
                        '($delta)x = Vi*t + 0.5at^2',
                        'Vf^2 = Vi^2 + 2a($delta)x',
                        '($delta)x = 0.5(Vi + Vf)t',
                      ].map<DropdownMenuItem<String>>((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(value),
                        );
                      }).toList(),
                    ),
                    SizedBox(height: 20.0),
                    // Input form for entering variables and calculating result
                    KinematicsInputForm(
                      selectedEquation: selectedEquation,
                      onResultChanged: (double newResult) {
                        setState(() {
                          result = newResult;
                        });
                      },
                    ),
                    SizedBox(height: 20.0),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

// Widget representing the input form for kinematics equations
class KinematicsInputForm extends StatefulWidget {
  final String selectedEquation;
  final ValueChanged<double> onResultChanged;

  KinematicsInputForm({
    required this.selectedEquation,
    required this.onResultChanged,
  });

  @override
  _KinematicsInputFormState createState() => _KinematicsInputFormState();
}

class _KinematicsInputFormState extends State<KinematicsInputForm> {
  // Map to store variable values for the selected equation
  Map<String, double> variables = {
    'V0': 0.0, // Initial velocity
    'a': 0.0, // Acceleration
    't': 0.0, // Time
    'Vi': 0.0, // Initial velocity
    'Vf': 0.0, // Final velocity
    'Delta x': 0.0, // Change in position
  };

  @override
  Widget build(BuildContext context) {
    // Get the required variables for the selected kinematic equation
    List<String> requiredVariables =
        getRequiredVariables(widget.selectedEquation);

    return Padding(
      padding: EdgeInsets.all(16.0),
      child: Column(
        children: [
          for (String variable in requiredVariables)
            TextFormField(
              decoration: InputDecoration(labelText: variable),
              keyboardType: TextInputType.number,
              onChanged: (value) {
                setState(() {
                  variables[variable] = double.tryParse(value) ?? 0.0;
                });
              },
            ),
          SizedBox(height: 20.0),
          ElevatedButton(
            onPressed: () {
              double result =
                  calculateResult(widget.selectedEquation, variables);
              widget.onResultChanged(result);
            },
            child: Text(
              'Calculate',
              style: TextStyle(
                fontSize: 18.0,
                color: Colors.black,
              ),
            ),
          ),
        ],
      ),
    );
  }

  // Function to get the required variables
  List<String> getRequiredVariables(String equation) {
    const String delta = '\u0394';
    switch (equation) {
      case 'V = V0 + at':
        return ['V0', 'a', 't'];
      case '($delta)x = Vi*t + 0.5at^2':
        return ['Vi', 't', 'a'];
      case 'Vf^2 = Vi^2 + 2a($delta)x':
        return ['Vi', 'a', 'Delta x'];
      case '($delta)x = 0.5(Vi + Vf)t':
        return ['Vi', 'Vf', 't'];
      default:
        return [];
    }
  }

  // Function to calculate the result
  double calculateResult(String equation, Map<String, double?> variables) {
    double result = 0.0;
    const String delta = '\u0394';

    switch (equation) {
      case 'V = V0 + at':
        result = variables['V0']! + variables['a']! * variables['t']!;
        break;
      case '($delta)x = Vi*t + 0.5at^2':
        result = variables['Vi']! * variables['t']! +
            0.5 * variables['a']! * pow(variables['t']!, 2);
        break;
      case 'Vf^2 = Vi^2 + 2a(Change of x)':
        result = sqrt(
          pow(variables['Vi']!, 2) +
              2 * variables['a']! * variables['Delta x']!,
        );
        break;
      case '($delta)x = 0.5(Vi + Vf)t':
        result = 0.5 * (variables['Vi']! + variables['Vf']!) * variables['t']!;
        break;
    }

    return result;
  }
}
