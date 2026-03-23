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
