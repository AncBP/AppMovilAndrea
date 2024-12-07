import 'package:flutter/material.dart';
import 'screen/Login.dart';
import 'screen/Home.dart';
import 'screen/Registro.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Prueba',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/login', 
      routes: {
        '/login': (context) => Login(),
        '/home': (context) => Home(),
        '/registro': (context) => Registro(),
      },
    );
  }
}
