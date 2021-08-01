student_ids=['B01','B02','B03','B05','B08','B10']

# method 1
student_num=len(student_ids)
print('方法1：学生有{}名'.format(student_num))

# method 2
count=0
for i in student_ids:
    count+=1
print('方法2：学生有{}名'.format(count))


