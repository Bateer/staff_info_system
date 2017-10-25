# -*- Coding: utf-8 -*-
# Author: Yu
import Function_inquire
import Function_Creation
import Function_Delete
import Function_modification
# 调用查询（inquire）函数， 创建（Creation）函数，删除（Delete）函数， 修改（modification）函数

while True:
    screen = "----------Welcome----------\n" \
             "1. Inquire the information of staffs.\n" \
             "\033[1;31;0m" \
             "(You can use fuzzy sentence to inquire, For example: select name,age from staff_table.txt where age > 22.)" \
             "\033[0m\n" \
             "2. Create a new staff.\n" \
             "3. Delete staff.\n" \
             "4. Modification the information of staff.\n" \
             "\033[1;31;0m(The syntax is: UPDATE staff_table.txt SET dept = Market WHERE where dept = IT)\033[0m\n" \
             "5. Exit.\n"

    print(screen)  # 打印用户交互界面
    user_number = input("\033[1;31;0m Please your choice:\033[0m")
    if user_number == "1":  # 选择1调用查询函数，并判断语法是否正确
        while True:
            Input_sentence = input("Please input:")
            if "select" and "from" and "where" in Input_sentence:
                print("Yes!")
                Function_inquire.Analysis_sentence(Input_sentence)
                break
            else:
                print("Your sentence is wrong, Please input again!")
    elif user_number == "2":  # 选择2调用创建函数创建新的员工信息
        Function_Creation.creation()
    elif user_number == "3":  # 选择3调用删除函数来删除其中员工信息
        Function_Delete.delete()
    elif user_number == "4":  # 选择4调用修改函数来修改员工信息
        Function_modification.modification()
    elif user_number == "5":  # 选择5来退出程序
        break