from PyQt6 import QtWidgets, uic

class AddNewStudentForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("addNewStudentForm.ui", self) 
        self.setWindowTitle("Add New Student")
        self.saveBtn.clicked.connect(self.addStudent)
        self.cancelBtn.clicked.connect(self.close)
        self.setModal(True)

        from generateId import generateId
        self.txtId.setText(generateId().generate_id())
        self.txtId.setReadOnly(True)


    def addStudent(self):
        student_id = self.txtId.text()
        name = self.txtName.text()
        birthday = self.txtDob.date().toString("yyyy-MM-dd")
        department = self.txtDepartment.text()
        type = self.txtType.currentText()

        if not student_id or not name or not birthday or not department or not type:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return
        from studentDAO import StudentDAO
        from Student import Student
        from ManagerStudent import ManagerStudent
        stu = Student(student_id, name, birthday, department, type)
        ManagerStudent().add_student(stu)
        QtWidgets.QMessageBox.information(self, "Success", "Student added successfully.")
        self.close()