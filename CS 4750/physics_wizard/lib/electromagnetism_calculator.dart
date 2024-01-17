import 'package:flutter/material.dart';

class ElectromagnetismCalculatorScreen extends StatefulWidget {
  @override
  _ElectromagnetismCalculatorScreenState createState() =>
      _ElectromagnetismCalculatorScreenState();
}

class _ElectromagnetismCalculatorScreenState
    extends State<ElectromagnetismCalculatorScreen> {
  double result = 0.0;
  String selectedEquation = 'F = k(q1*q2)/r^2';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Electromagnetism Calculator'),
      ),
      body: Container(
        decoration: BoxDecoration(
          color: Colors.grey[200],
        ),
        child: Column(
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
                    DropdownButton<String>(
                      value: selectedEquation,
                      hint: Text('Select Formula'),
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
                        'F = k(q1*q2)/r^2',
                        'E = F/q0',
                        'F = qv*B',
                        'V = I*R',
                        'P = I*V',
                      ].map<DropdownMenuItem<String>>((String value) {
                        return DropdownMenuItem<String>(
                          value: value,
                          child: Text(value),
                        );
                      }).toList(),
                    ),
                    SizedBox(height: 20.0),
                    ElectromagnetismInputForm(
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

class ElectromagnetismInputForm extends StatefulWidget {
  final String selectedEquation;
  final ValueChanged<double> onResultChanged;

  ElectromagnetismInputForm({
    required this.selectedEquation,
    required this.onResultChanged,
  });

  @override
  _ElectromagnetismInputFormState createState() =>
      _ElectromagnetismInputFormState();
}

class _ElectromagnetismInputFormState extends State<ElectromagnetismInputForm> {
  Map<String, double> variables = {
    'k': 8.99e9, // Coulomb's constant
    'q1': 0.0, // Charge 1
    'q2': 0.0, // Charge 2
    'r': 0.0, //Distance
    'q0': 0.0, // Charge
    'F': 0.0, // Force
    'E': 0.0, // Electric field
    'q': 0.0, // Charge
    'v': 0.0, // Velocity
    'B': 0.0, // Magnetic field
    'V': 0.0, // Voltage
    'I': 0.0, // Current
    'R': 0.0, // Resistance
    'P': 0.0, // Power
  };
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

  void updateResult() {
    double result = calculateResult(widget.selectedEquation, variables);
    widget.onResultChanged(result);
  }

  List<String> getRequiredVariables(String equation) {
    switch (equation) {
      case 'F = k(q1*q2)/r^2':
        return ['k', 'q1', 'q2', 'r'];
      case 'E = F/q0':
        return ['F', 'q0'];
      case 'F = qv*B':
        return ['q', 'v', 'B'];
      case 'V = I*R':
        return ['I', 'R'];
      case 'P = I*V':
        return ['I', 'V'];
      default:
        return [];
    }
  }

  double calculateResult(String formula, Map<String, double?> variables) {
    double result = 0.0;

    switch (formula) {
      case 'F = k(q1*q2)/r^2':
        result = (variables['k']! * variables['q1']! * variables['q2']!) /
            (variables['r']! * variables['r']!);
        break;
      case 'E = F/q0':
        result = variables['F']! / variables['q0']!;
        break;
      case 'F = qv*B':
        result = variables['q']! * variables['v']! * variables['B']!;
        break;
      case 'V = I*R':
        result = variables['I']! * variables['R']!;
        break;
      case 'P = I*V':
        result = variables['I']! * variables['V']!;
        break;
    }

    return result;
  }
}
