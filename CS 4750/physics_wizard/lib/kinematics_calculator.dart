import 'package:flutter/material.dart';

class KinematicsCalculatorScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Kinematics Calculator'),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => DisplacementEquationScreen()),
              );
            },
            child: Text('Displacement Equation'),
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => VelocityEquationScreen()),
              );
            },
            child: Text('Velocity Equation'),
          ),
        ],
      ),
    );
  }
}

class DisplacementEquationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return EquationScreen(
      equationTitle: 'Displacement Equation',
      equationPlaceholder: 'Enter time, initial velocity, and acceleration',
    );
  }
}

class VelocityEquationScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return EquationScreen(
      equationTitle: 'Velocity Equation',
      equationPlaceholder: 'Enter initial velocity, acceleration, and time',
    );
  }
}

class EquationScreen extends StatelessWidget {
  final String equationTitle;
  final String equationPlaceholder;

  EquationScreen({
    required this.equationTitle,
    required this.equationPlaceholder,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(equationTitle),
        leading: IconButton(
          icon: Icon(Icons.arrow_back),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextField(
              decoration: InputDecoration(
                hintText: equationPlaceholder,
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // TODO: Add logic to evaluate the equation
              },
              child: Text('Evaluate'),
            ),
          ],
        ),
      ),
    );
  }
}
