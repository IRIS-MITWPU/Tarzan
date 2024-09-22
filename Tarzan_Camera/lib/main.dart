import 'package:flutter/material.dart';
import 'camera_page.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Camera Feed App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: CameraPage(),
    );
  }
}
