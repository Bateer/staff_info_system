# -*- Coding: utf-8 -*-
# Author: Yu
def delete():
    delete_id = input("Please input the id of the delete staff:")  # 通过输入的员工的id删除员工的信息
    f_delete = open("staff_table.txt", "r+", encoding="utf-8")
    if delete_id.isdigit():  # 判断输入的id是否是数字
        # f_delete = open("staff_table.txt", "r+", encoding="utf-8")
        # delete_list = f_delete.readlines()
        # if int(delete_id) <= len(delete_list):
        #     for delete_line in delete_list:
        #         delete_line_list = delete_line.split(",")
        #         if delete_id in delete_line_list[0]:
        #             delete_s = delete_line.replace(delete_line, "")
        #             f_delete.writelines(delete_s)
        a = []
        for delete_line in f_delete.readlines():
            delete_list = delete_line.split(",")  # 解析出每条员工信息列表
            if delete_id in delete_list[0]:  # 判断员工的id是否和输入的id一致
                delete_s = delete_line.replace(delete_line, "")  # 如果一致，将该条信息代替为""
                f_delete.writelines(delete_s)
            else:
                a.append(delete_line)
        f_delete = open("staff_table.txt", "w", encoding="utf-8")
        for i in a:
            f_delete.write(i)  # 将新的内容再次写入文件中
        f_delete.close()
