from unittest import TestCase, main
from project.student import Student

class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Atanas")
        self.second_student = Student("Plamena", {'math':['x+y=z']})

    def test_correct_init(self):
        self.assertEqual("Atanas", self.student.name)
        self.assertEqual("Plamena", self.second_student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math':'x+y=z'}, self.second_student.courses)

    def test_enroll_same_course_appends_new_notes(self):
        result = self.second_student.enroll("math", ["1+2=3", "3+4=7"])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["x+y=z", "1+2=3", "3+4=7"], self.second_student.courses["math"])

    def test_enroll_in_new_course_without_third_param_adds_notes_to_the_course(self):
        result = self.student.enroll("math", ["x+y=z"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"math":["x+y=z"]}, self.student.courses)

    def test_enroll_in_new_course_with_third_param_Y_adds_notes_to_the_course(self):
        result = self.student.enroll("math", ["x+y=z"], 'Y')
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"math": ["x+y=z"]}, self.student.courses)

    def test_enroll_in_new_course_with_third_param_Y_does_not_adds_notes_to_the_course(self):
        result = self.student.enroll("math", ["x+y=z"], 'N')
        self.assertEqual("Course has been added.", result)
        self.assertEqual({"math": []}, self.student.courses)

    def test_add_notes_to_existing_course_expect_success(self):
        result = self.second_student.add_notes("math", "1+2=3")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["x+y=z","1+2=3"], self.second_student.courses["math"])

    def test_add_notes_to_a_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some_note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course_expect_success(self):
        result = self.second_student.leave_course("math")
        self.assertEqual({}, self.second_student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()