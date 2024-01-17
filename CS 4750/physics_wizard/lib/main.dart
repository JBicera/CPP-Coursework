import 'package:flutter/material.dart';
import 'general_calculator.dart'; // Import General Calculator
import 'kinematics_calculator.dart'; // Import Kinematics
import 'thermodynamics_calculator.dart'; // Import Thermodynamics
import 'electromagnetism_calculator.dart'; // Import Electromagnetism

void main() {
  runApp(PhysicsWizardApp());
}

class PhysicsWizardApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Physics Wizard',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(
          primarySwatch: Colors.grey,
          accentColor: Colors.black,
        ),
        scaffoldBackgroundColor:
            Colors.grey[800], // Darker background color for the scaffold
        textTheme: TextTheme(
          bodyLarge: TextStyle(color: Colors.black), // Text color
        ),
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
        title: Center(
          child: Container(
            margin: EdgeInsets.symmetric(horizontal: 16.0),
            child: Text(
              'Physics Wizard',
              style: TextStyle(
                fontSize: 32.0,
              ),
            ),
          ),
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'AppLogo.png',
              width: 200.0,
              height: 200.0,
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => GeneralCalculatorScreen(),
                  ),
                );
              },
              child: Container(
                width: double.infinity,
                height: 60.0,
                child: Center(
                  child: Text(
                    'General',
                    style: TextStyle(
                      fontSize: 18.0, // Adjust font size
                      color: Colors.black, // Set text color
                    ),
                  ),
                ),
              ),
              style: ElevatedButton.styleFrom(
                primary: Colors.grey[300], // Set button background color
                padding: EdgeInsets.all(0.0),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => KinematicsCalculatorScreen(),
                  ),
                );
              },
              child: Container(
                width: double.infinity,
                height: 60.0,
                child: Center(
                  child: Text(
                    'Kinematics',
                    style: TextStyle(
                      fontSize: 18.0,
                      color: Colors.black,
                    ),
                  ),
                ),
              ),
              style: ElevatedButton.styleFrom(
                primary: Colors.grey[300],
                padding: EdgeInsets.all(0.0),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ThermodynamicsCalculatorScreen(),
                  ),
                );
              },
              child: Container(
                width: double.infinity,
                height: 60.0,
                child: Center(
                  child: Text(
                    'Thermodynamics',
                    style: TextStyle(
                      fontSize: 18.0,
                      color: Colors.black,
                    ),
                  ),
                ),
              ),
              style: ElevatedButton.styleFrom(
                primary: Colors.grey[300],
                padding: EdgeInsets.all(0.0),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => ElectromagnetismCalculatorScreen(),
                  ),
                );
              },
              child: Container(
                width: double.infinity,
                height: 60.0,
                child: Center(
                  child: Text(
                    'Electromagnetism',
                    style: TextStyle(
                      fontSize: 18.0,
                      color: Colors.black,
                    ),
                  ),
                ),
              ),
              style: ElevatedButton.styleFrom(
                primary: Colors.grey[300],
                padding: EdgeInsets.all(0.0),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
