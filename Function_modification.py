# -*- Coding: utf-8 -*-
# Author: Yu

def modification():
    while True:
        update_input_sentence = input("Please input sentence about updating the information:\n")
        if "UPDATE" and "SET" and "WHERE" in update_input_sentence:  # 判断输入更新语句是否语法正确
            # print("Yes")
            sentence_1 = update_input_sentence.split("UPDATE")
            # print(sentence_1)
            sentence_2 = sentence_1[1].split("SET")
            # print(sentence_2)
            sentence_3 = sentence_2[1].split("WHERE")
            # print(sentence_3)
            sentence_4 = sentence_3[0].split("=")
            # print(sentence_4)
            sentence_5 = sentence_3[1].split("=")
            # print(sentence_5)
            # 解析输入的更新语句
            if sentence_4[0] == sentence_5[0]:  # 判断输入的语句的语法是否正确
                staff_info_list = []
                f_staff = open(sentence_2[0].strip(" "), "r", encoding="utf-8")
                info_f = f_staff.read()
                info_f_first = info_f.split("\n")
                info_f_first_new = info_f_first[:-1]
                for number_first in range(len(info_f_first_new)):
                    info_f_second = info_f_first_new[number_first].split(",")
                    info_list = []
                    for number_second in range(1, len(info_f_second)):
                        info_list.append(info_f_second[number_second].strip(" "))
                    staff_info_list.append(info_list)
                # 上面部分是把文件中过的员工信息转变成下面形式的列表
                # print(staff_info_list)
                # staff_info_list = [["Alex Li", "22", "13651054608", "IT", "2013-04-01"]
                #                    , ["Jack Wang", "30", "13304320533", "HR", "2015-05-03"]
                #                    , ["Rain Liu", "25", "1383235322", "Sales", "2016-04-22"]
                #                    , ["Mack Cao", "40", "1356145343", "HR", "2009-03-01"]]

                dict_staff = {"name": [], "age": [], "phone": [], "dept": [], "enroll_date": []}

                for (i, j, x, y, z) in zip(range(len(staff_info_list)), range(len(staff_info_list)),
                                           range(len(staff_info_list))
                        , range(len(staff_info_list)), range(len(staff_info_list))):
                    dict_staff["name"].append(staff_info_list[i][0])
                    dict_staff["age"].append(staff_info_list[j][1])
                    dict_staff["phone"].append(staff_info_list[x][2])
                    dict_staff["dept"].append(staff_info_list[y][3])
                    dict_staff["enroll_date"].append(staff_info_list[z][4])
                # 将staff_info_list中的内容分类存入字典
                # print(dict_staff)
                dict_staff_key = dict_staff[sentence_5[0].strip(" ")]  # 找到需要更新的列所在的列表 比如age对应的列表
                for item in dict_staff_key:
                    if item == sentence_5[1].strip(" "):
                        index_where = dict_staff_key.index(item)
                        dict_staff_key[index_where] = sentence_4[1].strip(" ")
                # 找到需要更改的元素，将其替换为更新的结果
                print(dict_staff_key)
                dict_staff[sentence_4[0].strip(" ")] = dict_staff_key
                print(dict_staff)
                f_new = open("staff_new.txt", "w", encoding="utf-8")
                for b in range(len(dict_staff["name"])):  # 将更新后的字典重新按文件格式写入staff_new文件中
                    f_new.write(str(int(b+1)))
                    f_new.write(", ")  # 写入员工编号
                    for a in dict_staff:  # a = name, age, phone, dept, enroll_date
                        print(dict_staff[a][b])
                        if a == "enroll_date":
                            f_new.write(dict_staff[a][b])
                            f_new.write("\n")  # 每一条员工信息最后跳一行开始新的一行
                        else:
                            f_new.write(dict_staff[a][b])
                            f_new.write(", ")  # 除开编号其他信息用逗号隔开
                f_staff.close()
                f_new.close()
            f_staff_new = open("staff_new.txt", "r", encoding="utf-8")
            f_staff_table = open("staff_table.txt", "r+", encoding="utf-8")
            f_str = f_staff_new.read()
            f_staff_table.write(f_str)  # 将文件staff_new.txt中的内容重新写回staff_table.txt
            break
        else:
            print("Syntax Error!")


    # sentence_1 = update_input_sentence.split("UPDATE")
    # print(sentence_1)
    # sentence_2 = sentence_1[1].split("SET")
    # print(sentence_2)
    # sentence_3 = sentence_2[1].split("WHERE")
    # print(sentence_3)
    # sentence_4 = sentence_3[0].split("=")
    # print(sentence_4)
    # sentence_5 = sentence_3[1].split("=")
    # print(sentence_5)
