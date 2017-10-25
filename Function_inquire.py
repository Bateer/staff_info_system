# -*- Coding: utf-8 -*-
# Author: Yu
# count = 1
def Analysis_sentence (Input_sentence):
    sentence_1 = Input_sentence.split("select")
    # print(sentence_1)
    sentence_2 = sentence_1[1].split("from")
    # print(sentence_2)
    sentence_3 = sentence_2[1].split("where")
    # print(sentence_3)
    sentence_4 = sentence_3[1].split(" ")
    # print(sentence_4)
    # 利用语句中关键字"select","from","where"来解析输入的句子，分成不同的列表

    def Index_found (list_new):  # 用来打印查询结果以及查询到的条数
        count_items = 0
        for index in range(len(list_new)):
            number = dict_staff[sentence_4[1]].index(list_new[index])
            # 找出筛选出数据在字典中对应key中的列表对应的序号，对应的序号也对应员工信息表中id
            # print(number)
            if sentence_2[0].strip(" ") == "*":  # 直接将员工信息全部打印
                print(staff_info_list[number])
            else:
                select_list = sentence_2[0].split(",")  # 解析语句中查询需要找到信息，比如 name，age
            # print(select_list)
                Info_py_list = []
                for b in range(len(select_list)):
                    info_py = dict_staff[select_list[b].strip(" ")][number]
                    Info_py_list.append(info_py)
                print(Info_py_list)  # 从字典中读取对应的值
            count_items += 1  # 打印一条，加一，记录下打印的条数
        print("The number of information found is %d!" % count_items)
    # sentence_3[0].strip(" ")

    staff_info_list = []  # 创建一个用于存放员工信息列表的空列表
    f_staff = open(sentence_3[0].strip(" "), "r", encoding="utf-8")
    # 打开输入查询句子中关于员工信息文件的部分
    info_f = f_staff.read()
    info_f_first = info_f.split("\n")
    info_f_first_new = info_f_first[:-1]
    # 将文件中的信息以\n分割为一个列表，因为最后一个为空，所以截取列表中有用的元素
    for number_first in range(len(info_f_first_new)):
        info_f_second = info_f_first_new[number_first].split(",")
        info_list = []
        for number_second in range(1, len(info_f_second)):
            info_list.append(info_f_second[number_second].strip(" "))
        staff_info_list.append(info_list)
    # 两个for循环，将文件中的员工信息存入列表中，每一条都以列表的形式存入，没有员工的id
    # print(staff_info_list)
    # staff_info_list = [["Alex Li", "22", "13651054608", "IT", "2013-04-01"]
    #                    , ["Jack Wang", "30", "13304320533", "HR", "2015-05-03"]
    #                    , ["Rain Liu", "25", "1383235322", "Sales", "2016-04-22"]
    #                    , ["Mack Cao", "40", "1356145343", "HR", "2009-03-01"]]

    dict_staff = {"name": [], "age": [], "phone": [], "dept": [], "enroll_date": []}
    # 将员工信息以name，age等列的形式存入字典中，方便下面的查找

    for (i, j, x, y, z) in zip(range(len(staff_info_list)), range(len(staff_info_list)), range(len(staff_info_list))
            , range(len(staff_info_list)), range(len(staff_info_list))):
        dict_staff["name"].append(staff_info_list[i][0])
        dict_staff["age"].append(staff_info_list[j][1])
        dict_staff["phone"].append(staff_info_list[x][2])
        dict_staff["dept"].append(staff_info_list[y][3])
        dict_staff["enroll_date"].append(staff_info_list[z][4])
    # print(dict_staff)
    # 每一条列表中的staff_info_list[i][0]即名字，都存入在字典中name中的列表，其他的同理，将员工信息分类存起来

    # new_1 = list(filter(lambda o: o == "22", dict_staff["age"]))
    # print(new_1)
    if sentence_4[2] == ">":  # 根据解析出来的语句，判断需要查找的条件
        new_1 = list(filter(lambda o: o > sentence_4[-1], dict_staff[sentence_4[1]]))
        # 利用list中的塞选器对列表中的元素进行比较查询
        # print(new_1)
        # for index in range(len(new_1)):
        #     number = dict_staff[sentence_4[1]].index(new_1[index])
        #     print(number)
        #     print(staff_info_list[number])
        #     select_list = sentence_2[0].split(",")
        #     # print(select_list)
        #     Info_py_list = []
        #     for b in range(len(select_list)):
        #         Info_py = dict_staff[select_list[b].strip(" ")][number]
        #         Info_py_list.append(Info_py)
        #     print(Info_py_list)
        Index_found(new_1)  #调用上面Index_found（）来打印查询的结果

    elif sentence_4[2] == "<":
        new_2 = list(filter(lambda o: o < sentence_4[-1], dict_staff[sentence_4[1]]))
        # print(new_2)
        Index_found(new_2)

    elif sentence_4[2] == "<=":
        new_3 = list(filter(lambda o: o <= sentence_4[-1], dict_staff[sentence_4[1]]))
        # print(new_3)
        Index_found(new_3)

    elif sentence_4[2] == ">=":
        new_4 = list(filter(lambda o: o >= sentence_4[-1], dict_staff[sentence_4[1]]))
        # print(new_4)
        Index_found(new_4)

    elif sentence_4[2] == "=":
        new_5 = list(filter(lambda o: o == sentence_4[-1], dict_staff[sentence_4[1]]))
        # print(new_5)
        Index_found(new_5)

    elif sentence_4[2] == "like":
        new_6 = []
        for element in dict_staff[sentence_4[1]]:
            if sentence_4[-1] in element:
                new_6.append(element)
        # 判断列表中的每个元素是否含有like后面的元素
        Index_found(new_6)

# while count == 1:
#     Input_sentence = input("Please input:")
#     if "select" and "from" and "where" in Input_sentence:
#         #  print("Yes!")
#         Analysis_sentence(Input_sentence)
#         count = 0
#     else:
#         print("Your sentence is wrong, Please input again!")
