import 'package:flutter/material.dart';

class ThermodynamicsCalculatorScreen extends StatefulWidget {
  @override
  _ThermodynamicsCalculatorScreenState createState() =>
      _ThermodynamicsCalculatorScreenState();
}

class _ThermodynamicsCalculatorScreenState
    extends State<ThermodynamicsCalculatorScreen> {
  final String delta = '\u0394';
  double result = 0.0;
  String selectedEquation = 'PV = nRt';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Thermodynamics Calculator'),
      ),
      body: Container(
        decoration: BoxDecoration(
          color: Colors.grey[200], // Lighter overall background color
        ),
        child: Column(
          children: [
            // Display the result at the top of the screen
            Container(
              width: double.infinity, // Full width
              color: Colors.grey[300], // Light grey background color
              padding: EdgeInsets.all(16.0),
              child: Text(
                'Result: $result', // Display the result
                style: TextStyle(fontSize: 24.0), // Larger font size
              ),
            ),
            Expanded(
              child: SingleChildScrollView(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    DropdownButton<String>(
                      value: selectedEquation,
                      hint: Text('Select Thermodynamic Equation'),
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
                        'PV = nRt',
                        '($delta)U = Q - W',
                        'q = mC($delta)T',
                        'W = -p($delta)V',
                      ].map<DropdownMenuItem<String>>((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(value),
                        );
                      }).toList(),
                    ),
                    SizedBox(height: 20.0),
                    ThermodynamicsInputForm(
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

class ThermodynamicsInputForm extends StatefulWidget {
  final String selectedEquation;
  final ValueChanged<double> onResultChanged;

  ThermodynamicsInputForm({
    required this.selectedEquation,
    required this.onResultChanged,
  });

  @override
  _ThermodynamicsInputFormState createState() =>
      _ThermodynamicsInputFormState();
}

class _ThermodynamicsInputFormState extends State<ThermodynamicsInputForm> {
  Map<String, double> variables = {
    'Q': 0.0, // Heat added or removed from the system
    'W': 0.0, // Work done on or by the system
    'n': 0.0, // Number of moles of gas
    'R': 0.0, // Gas constant
    'T': 0.0, // Temperature of the system
    'm': 0.0, // Mass of the substance
    'C': 0.0, // Specific heat capacity
    'Delta T': 0.0, // Change in temperature
  };

  final String delta = '\u0394';

  @override
  Widget build(BuildContext context) {
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
              // Call a function to calculate result based on selected equation
              double result =
                  calculateResult(widget.selectedEquation, variables);
              widget.onResultChanged(
                  result); // Update the result through callback
            },
            child: Text(
              'Calculate',
              style: TextStyle(
                fontSize: 18.0, // Adjust font size
                color: Colors.black, // Set text color
              ),
            ),
          ),
        ],
      ),
    );
  }

  List<String> getRequiredVariables(String equation) {
    const String delta = '\u0394';
    switch (equation) {
      case 'PV = nRt':
        return ['n', 'R', 'T'];
      case '($delta)U = Q - W':
        return ['Q', 'W'];
      case 'q = mC($delta)T':
        return ['m', 'C', 'Delta T'];
      case 'W = -p($delta)V':
        return ['P', 'V'];
      // Add more cases for other thermodynamic equations if needed
      default:
        return [];
    }
  }

  double calculateResult(String equation, Map<String, double?> variables) {
    double result = 0.0;
    const String delta = '\u0394';
    // Implement the calculation based on the selected equation
    switch (equation) {
      case 'PV = nRt':
        result = variables['n']! * variables['R']! * variables['T']!;
        break;
      case '($delta)U = Q - W':
        result = variables['Q']! - variables['W']!;
        break;
      case 'q = mC($delta)T':
        result = variables['m']! * variables['C']! * variables['Delta T']!;
        break;
      case 'W = -p($delta)V':
        result = -variables['P']! * variables['V']!;
        break;
      // Add more cases for other thermodynamic equations if needed
    }

    return result;
  }
}
