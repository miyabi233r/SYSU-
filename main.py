import os
import random
import time

# ---------------------------
# 学生类
# ---------------------------
class Student:
    def __init__(self, name, gender, class_, student_id, college):
        self.name = name
        self.gender = gender
        self.class_ = class_
        self.student_id = student_id
        self.college = college

    def __str__(self):
        # 用于友好打印学生信息
        return f"{self.name} | {self.gender} | {self.class_} | {self.student_id} | {self.college}"
        
# ---------------------------
# 考试管理系统类
# ---------------------------
class ExamSystem:
    def __init__(self):
        self.students = []

    # -----------------------
    # 读取学生名单文件
    # -----------------------
    def load_students(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines[1:]:  # 跳过标题行
                    parts = line.strip().split('\t')
                    if len(parts) >= 6:
                        student = Student(
                            name=parts[1],
                            gender=parts[2],
                            class_=parts[3],
                            student_id=parts[4],
                            college=parts[5]
                        )
                        self.students.append(student)
            print(f"成功加载 {len(self.students)} 个学生信息。")
        except FileNotFoundError:
            print(f"错误：文件 {file_path} 未找到！")

    # -----------------------
    # 查找学生信息
    # -----------------------
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None  # 没找到返回 None

    # -----------------------
    # 随机点名
    # -----------------------
    def random_call(self, num):
        try:
            num = int(num)
            if num > len(self.students):
                print("输入数量超过总人数！")
                return []
            return random.sample(self.students, num)  # 返回不重复随机学生
        except ValueError:
            print("输入错误，请输入数字！")
            return []

    # -----------------------
    # 生成考场安排表
    # -----------------------
    def generate_exam_table(self, file_name="考场安排表.txt"):
        shuffled_students = self.students[:]
        random.shuffle(shuffled_students)

        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                for idx, student in enumerate(shuffled_students, start=1):
                    f.write(f"{idx}\t{student.name}\t{student.student_id}\n")
            print(f"考场安排表已生成：{file_name}")
            return shuffled_students
        except Exception as e:
            print("生成考场安排表出错：", e)
            return []

    # -----------------------
    # 生成准考证文件
    # -----------------------
    @staticmethod
    def generate_admission_cards(shuffled_students, folder="准考证"):
        # 创建文件夹
        os.makedirs(folder, exist_ok=True)
        for idx, student in enumerate(shuffled_students, start=1):
            file_path = os.path.join(folder, f"{str(idx).zfill(2)}.txt")
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"座位号：{idx}\n")
                    f.write(f"姓名：{student.name}\n")
                    f.write(f"学号：{student.student_id}\n")
                # print(f"生成准考证：{file_path}")
            except Exception as e:
                print(f"生成准考证 {file_path} 出错：", e)
        print(f"准考证文件已生成在文件夹：{folder}")
