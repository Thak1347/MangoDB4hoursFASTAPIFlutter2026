import 'dart:convert';

import 'package:flutter/foundation.dart' show kIsWeb;
import 'package:http/http.dart' as http;

import '../models/student.dart';

class StudentApiService {
  // Android emulators reach the host through 10.0.2.2; browsers use localhost.
  static String get baseUrl =>
      kIsWeb ? 'http://localhost:8000' : 'http://10.0.2.2:8000';

  Future<List<Student>> getStudents() async {
    final response = await http.get(Uri.parse('$baseUrl/students'));

    if (response.statusCode != 200) {
      throw Exception('Failed to load students: ${response.statusCode}');
    }

    final List<dynamic> data = jsonDecode(response.body);

    return data
        .map((item) => Student.fromJson(item as Map<String, dynamic>))
        .toList();
  }

  Future<Student> createStudent(Student student) async {
    final response = await http.post(
      Uri.parse('$baseUrl/students'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode(student.toJson()),
    );

    if (response.statusCode != 201) {
      throw Exception('Failed to create student: ${response.body}');
    }

    return Student.fromJson(jsonDecode(response.body) as Map<String, dynamic>);
  }
}
