class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        return total_marks, average_marks

    def display(self):
        total, average = self.compute()
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")


student1 = Student("Alice", [85, 90, 78])
student1.display()

student2 = Student("Bob", [75, 88, 92])
student2.display()
