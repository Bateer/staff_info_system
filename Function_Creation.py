# -*- Coding: utf-8 -*-
# Author: Yu
def creation():
    phone_number = input("Please input your number:")  # 输入手机号码
    if phone_number.isdigit():  # 判断手机号码是否是数字
        if len(phone_number) == 11:  # 判断手机是否是11位
            f = open("staff_table.txt", "r", encoding="utf-8")
            line = f.read()
            if phone_number in line:  # 因为手机号码作为唯一的键值，判断是否之前存在
                print("The phone has been exist!")
            else:
                print("The phone is able to be used!")
                create_list = []  # 用于存放创建新的员工信息的空列表
                # create_list.append(phone_number)
                name = input("Please input your name:")
                # create_list.append(name)
                age = input("Age:")
                dept = input("Dept:")
                enroll_date = input("Enroll_date (Default format \"1990-01-01\"):")
                # 依次输入需要存入的员工的信息

                line_list = line.split("\n")
                staff_id = len(line_list)
                # 根据已经存入的员工信息，依次递增新员工的id

                create_list.append(staff_id)
                create_list.append(name)
                create_list.append(age)
                create_list.append(phone_number)
                create_list.append(dept)
                create_list.append(enroll_date)
                print(create_list)
                f_new = open("staff_table.txt", "a", encoding="utf-8")
                for factor in range(len(create_list)):  # 以相同的格式存入员工信息文件中
                    if factor == 5:
                        f_new.write(create_list[factor])
                        f_new.write("\n")
                    else:
                        f_new.write(str(create_list[factor]))
                        f_new.write(", ")
                f.close()
                f_new.close()
        else:
            print("The number of phone you input should be 11 digits!")
    else:
        print("Please input digit!")
