class Student {
  final String studentCode;
  final String name;
  final int age;
  final String major;
  final int year;
  final bool isActive;

  const Student({
    required this.studentCode,
    required this.name,
    required this.age,
    required this.major,
    required this.year,
    required this.isActive,
  });

  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      studentCode: json['student_code'] as String,
      name: json['name'] as String,
      age: json['age'] as int,
      major: json['major'] as String,
      year: json['year'] as int,
      isActive: json['is_active'] as bool,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'student_code': studentCode,
      'name': name,
      'age': age,
      'major': major,
      'year': year,
      'is_active': isActive,
    };
  }
}
