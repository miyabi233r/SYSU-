import os       # 用于文件和目录操作
import random   # 用于随机点名和打乱顺序
import time     # 用于获取生成考场表的当前时间

# ---------------------------
# 学生类
# ---------------------------
class Student:
    def __init__(self, name, gender, class_, student_id, college):
        # 初始化学生对象属性
        self.name = name            # 学生姓名
        self.gender = gender        # 学生性别
        self.class_ = class_        # 学生班级
        self.student_id = student_id# 学号
        self.college = college      # 学院

    def __str__(self):
        # 返回学生信息的友好字符串表示，用于打印
        return f"{self.name} | {self.gender} | {self.class_} | {self.student_id} | {self.college}"

# ---------------------------
# 考试管理系统类
# ---------------------------
class ExamSystem:
    def __init__(self):
        # 初始化学生列表为空
        self.students = []

    def load_students(self, file_path):
        """
        从指定文件读取学生信息，初始化学生列表
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # 读取所有行
                lines = f.readlines()
                # 跳过标题行，从第二行开始读取学生数据
                for line in lines[1:]:
                    parts = line.strip().split('\t')  # 按制表符分割每列数据
                    if len(parts) >= 6:  # 确保数据完整
                        student = Student(
                            name=parts[1],       # 姓名
                            gender=parts[2],     # 性别
                            class_=parts[3],     # 班级
                            student_id=parts[4], # 学号
                            college=parts[5]     # 学院
                        )
                        self.students.append(student)  # 添加到学生列表
            print(f"成功加载 {len(self.students)} 个学生信息。")
        except FileNotFoundError:
            # 文件不存在时的异常处理
            print(f"错误：文件 {file_path} 未找到！")

    def find_student(self, student_id):
        """
        根据学号查找学生信息，找不到返回 None
        """
        for student in self.students:       # 遍历所有学生
            if student.student_id == student_id:  # 匹配学号
                return student               # 找到返回学生对象
        return None                          # 没找到返回 None

    def random_call(self, num):
        """
        随机点名 num 个学生
        """
        try:
            num = int(num)                  # 尝试将输入转换为整数
            if num > len(self.students):    # 判断输入数量是否超过总人数
                print("输入数量超过总人数！")
                return []
            return random.sample(self.students, num)  # 返回不重复随机学生列表
        except ValueError:
            # 输入无法转换为数字时捕获异常
            print("输入错误，请输入数字！")
            return []

    def generate_exam_table(self, file_name="考场安排表.txt"):
        """
        生成考场安排表，并返回随机打乱后的学生列表
        """
        shuffled_students = self.students[:]  # 复制学生列表，避免打乱原列表
        random.shuffle(shuffled_students)     # 随机打乱学生顺序

        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                # 写入生成时间，放在第一行
                f.write(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                for idx, student in enumerate(shuffled_students, start=1):
                    # 写入座位号、姓名、学号，每行一个学生
                    f.write(f"{idx}\t{student.name}\t{student.student_id}\n")
            print(f"考场安排表已生成：{file_name}")
            return shuffled_students  # 返回打乱后的学生列表，用于生成准考证
        except Exception as e:
            # 捕获所有异常
            print("生成考场安排表出错：", e)
            return []

    @staticmethod
    def generate_admission_cards(shuffled_students, folder="准考证"):
        """
        为每个学生生成单独的准考证文件
        """
        os.makedirs(folder, exist_ok=True)   # 创建准考证文件夹，存在则忽略
        for idx, student in enumerate(shuffled_students, start=1):
            file_path = os.path.join(folder, f"{str(idx).zfill(2)}.txt")  # 生成文件路径
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"座位号：{idx}\n")        # 写入座位号
                    f.write(f"姓名：{student.name}\n") # 写入姓名
                    f.write(f"学号：{student.student_id}\n") # 写入学号
            except Exception as e:
                # 捕获文件写入异常
                print(f"生成准考证 {file_path} 出错：", e)
        print(f"准考证文件已生成在文件夹：{folder}")

# ---------------------------
# 主程序示例
# ---------------------------
def main():
    system = ExamSystem()                       # 初始化考试系统对象
    system.load_students("人工智能编程语言学生名单.txt")  # 加载学生名单

    while True:  # 循环显示菜单
        print("\n1. 查找学生信息  2. 随机点名  3. 生成考场安排表  4. 退出")
        choice = input("请选择操作：")          # 用户输入操作选项
        if choice == "1":
            student_id = input("请输入学号：")  # 用户输入学号
            student = system.find_student(student_id)
            if student:                        # 如果找到学生
                print("学生信息：", student)
            else:
                print("未找到该学号的学生信息。")
        elif choice == "2":
            num = input("请输入点名数量：")     # 用户输入点名数量
            selected = system.random_call(num)
            if selected:                        # 如果有学生被选中
                print("点名结果：")
                for s in selected:
                    print(s)
        elif choice == "3":
            shuffled = system.generate_exam_table()  # 生成考场安排表
            if shuffled:                              # 如果成功生成
                system.generate_admission_cards(shuffled)  # 生成准考证
        elif choice == "4":
            print("退出系统。")
            break
        else:
            print("输入无效，请重新选择！")

if __name__ == "__main__":
    main()
