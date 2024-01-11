import 'package:flutter/material.dart';
import 'general_calculator.dart';
import 'kinematics_calculator.dart';
import 'thermodynamics_calculator.dart';

void main() {
  runApp(PhysicsWizardApp());
}

class PhysicsWizardApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Physics Wizard',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MenuScreen(),
    );
  }
}

class MenuScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Physics Wizard'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => GeneralCalculatorScreen()),
                );
              },
              child: Text('General'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => KinematicsCalculatorScreen()),
                );
              },
              child: Text('Kinematics'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => ThermodynamicsCalculatorScreen()),
                );
              },
              child: Text('Thermodynamics'),
            ),
          ],
        ),
      ),
    );
  }
}
