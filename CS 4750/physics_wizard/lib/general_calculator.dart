import 'package:flutter/material.dart';
import 'package:math_expressions/math_expressions.dart';
import 'main.dart';

// Screen for general calculator
class GeneralCalculatorScreen extends StatefulWidget {
  @override
  _GeneralCalculatorScreenState createState() =>
      _GeneralCalculatorScreenState();
}

class _GeneralCalculatorScreenState extends State<GeneralCalculatorScreen> {
  String _input = ''; // Input expression for calculations
  double _result = 0.0; // Result of calculations

  // Functions for button presses
  void _onButtonPressed(String buttonText) {
    setState(() {
      if (buttonText == '=') {
        _calculateResult();
      } else if (buttonText == 'C') {
        _clearInput();
      } else if (buttonText == '+/-') {
        _toggleSign();
      } else {
        _input += buttonText;
      }
    });
  }

  // Function to call to evaluate expression and to update input
  void _calculateResult() {
    try {
      _result = eval(_input);
      _input = _result.toString();
    } catch (e) {
      _input = 'Error';
    }
  }

  // Function to clear inputs
  void _clearInput() {
    _input = '';
    _result = 0.0;
  }

  // Function to toggle sign of input
  void _toggleSign() {
    if (_input.isNotEmpty && _input[0] != '-') {
      _input = '-' + _input;
    } else if (_input.isNotEmpty && _input[0] == '-') {
      _input = _input.substring(1);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('General Calculator'),
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
      body: Column(
        children: [
          Flexible(
            flex: 1,
            child: Container(
              padding: EdgeInsets.all(16.0),
              color: Colors.grey.shade200,
              child: Align(
                alignment: Alignment.bottomRight,
                child: Text(
                  _input,
                  style: TextStyle(fontSize: 64.0),
                ),
              ),
            ),
          ),
          Container(
            height: 500.0,
            width: double.infinity,
            child: Column(
              children: [
                // Make buttons for calculator
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildButton('C', width: 80.0, height: 80.0),
                    _buildButton('+/-', width: 80.0, height: 80.0),
                    _buildButton('+', width: 80.0, height: 80.0),
                    _buildButton('-', width: 80.0, height: 80.0),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildButton('7'),
                    _buildButton('8'),
                    _buildButton('9'),
                    _buildButton('/'),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildButton('4'),
                    _buildButton('5'),
                    _buildButton('6'),
                    _buildButton('*'),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildButton('1'),
                    _buildButton('2'),
                    _buildButton('3'),
                    _buildButton('='),
                  ],
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildButton('.', width: 120.0, height: 80.0),
                    _buildButton('0', width: 240.0, height: 80.0),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // Widget for calculator buttons
  Widget _buildButton(String buttonText,
      {double width = 80.0, double height = 80.0}) {
    return Container(
      width: width,
      height: height,
      margin: EdgeInsets.all(8.0),
      child: ElevatedButton(
        onPressed: () {
          _onButtonPressed(buttonText);
        },
        style: ElevatedButton.styleFrom(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10.0),
          ),
        ),
        child: Text(
          buttonText,
          style: TextStyle(fontSize: 20.0),
        ),
      ),
    );
  }

  // Function to evaluate mathematical expression
  double eval(String expression) {
    Parser p = Parser();
    Expression exp = p.parse(expression);
    ContextModel cm = ContextModel();
    return exp.evaluate(EvaluationType.REAL, cm);
  }
}
