markdown
# 任雅文-23354131-第二次人工智能编程作业
## 1. 任务拆解与 AI 协作策略
**步骤 1：设计类结构**  
- 定义 `Student` 类，包含学生基本属性和 `__str__` 方法。  
- 定义 `ExamSystem` 类，封装所有逻辑功能（查找、随机点名、生成考场表、生成准考证）。  

**步骤 2：实现核心功能**  
- 先让 AI 生成读取学生名单和查找学号功能。  
- 再让 AI 实现随机点名和考场表生成。  
- 最后生成准考证文件，并处理异常情况。  

**步骤 3：异常处理与文件操作**  
- 对文件不存在、用户输入非数字、目录创建失败等情况进行异常捕获。  
- 测试每个功能确保程序健壮。  
## 2. 核心 Prompt 迭代记录
**初代 Prompt：**  
> 请帮我写一个 Python 程序，读取学生名单，随机点名，并生成考场安排表。  

**AI 生成的问题/缺陷：**  
- 没有使用面向对象编程（Student/ExamSystem 类）。  
- 没有捕获用户输入错误和文件异常。  
- 没有生成单独准考证文件。  
- 代码没有中文注释，难以理解。  

**优化后的 Prompt：**  
> 请用面向对象写一个学生信息与考场管理系统。要求：  
> 1. 定义 Student 类和 ExamSystem 类；  
> 2. 加入异常处理（文件不存在、输入非数字等）；  
> 3. 使用标准库；  
> 4. 支持随机点名、考场表生成、准考证文件生成；  
> 5. 每行代码加中文注释。  
## 3. Debug 与异常处理记录

**报错类型/漏洞现象：**  
- 初次运行时，如果 `人工智能编程语言学生名单.txt` 文件不存在，会报 `FileNotFoundError`。  
- 输入非数字时随机点名功能报 `ValueError`。  

**解决过程：**  
- 使用 `try-except` 捕获文件不存在异常并提示用户。  
- 将用户输入数字转换包裹在 `try-except ValueError`，并在输入超出人数时提示。  
- 最终 AI 生成的代码中这些异常处理都加上了，并经过我手动测试。
## 4. 人工代码审查 (Code Review)
下面是 AI 生成的 **生成考场安排表** 代码片段，我加了逐行中文注释：

```python
def generate_exam_table(self, file_name="考场安排表.txt"):
    # 复制学生列表并打乱顺序
    shuffled_students = self.students[:]
    random.shuffle(shuffled_students)

    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            # 写入生成时间
            f.write(f"生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            # 写入每个学生的座位号、姓名、学号
            for idx, student in enumerate(shuffled_students, start=1):
                f.write(f"{idx}\t{student.name}\t{student.student_id}\n")
        print(f"考场安排表已生成：{file_name}")
        return shuffled_students
    except Exception as e:
        # 捕获任何异常并打印
        print("生成考场安排表出错：", e)
        return []
