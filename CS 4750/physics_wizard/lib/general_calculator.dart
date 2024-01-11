import 'package:flutter/material.dart';

class GeneralCalculatorScreen extends StatefulWidget {
  @override
  _GeneralCalculatorScreenState createState() =>
      _GeneralCalculatorScreenState();
}

class _GeneralCalculatorScreenState extends State<GeneralCalculatorScreen> {
  String _input = '';

  void _onButtonPressed(String buttonText) {
    setState(() {
      if (buttonText == 'C') {
        _input = '';
      } else if (buttonText == '=') {
        try {
          _input = eval(_input).toString();
        } catch (e) {
          _input = 'Error';
        }
      } else {
        _input += buttonText;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('General Calculator'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Expanded(
            child: Container(
              padding: EdgeInsets.all(16),
              alignment: Alignment.bottomRight,
              child: Text(
                _input,
                style: TextStyle(fontSize: 24),
              ),
            ),
          ),
          _buildCalculatorButtons(),
        ],
      ),
    );
  }

  Widget _buildCalculatorButtons() {
    List<List<String>> buttonRows = [
      ['7', '8', '9', '/'],
      ['4', '5', '6', 'x'],
      ['1', '2', '3', '-'],
      ['C', '0', '=', '+'],
    ];

    List<Widget> buttons = [];
    for (var row in buttonRows) {
      List<Widget> rowButtons = [];
      for (var button in row) {
        rowButtons.add(
          Expanded(
            child: ElevatedButton(
              onPressed: () => _onButtonPressed(button),
              child: Text(button),
            ),
          ),
        );
      }
      buttons.add(
        Expanded(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: rowButtons,
          ),
        ),
      );
    }

    return Column(children: buttons);
  }

  double eval(String expression) {
    try {
      return double.parse(expression);
    } catch (e) {
      return 0;
    }
  }
}
