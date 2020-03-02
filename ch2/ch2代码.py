# 2.1 helloworld
print("Hello world!")

#2.2 变量
message = "hello world"
print(message)

#2.2.1 变量的命名和使用
#1.变量名由字母、数字、下划线组成，不能以数字开头
#2.变量名不能有空格
#3.关键字

#动手试一试2-1
a = "hi"
print(a)

#2.3 字符串
#1.单引号和双引号都可以

#2.3.1 修改字符串大小写
name = "ada lovelace"
print(name.title())    #每个单词的首字母大写
print(name.upper())    #每个字母大写
print(name.lower())    #每个字母小写 

#2.3.2 拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

#2.3.3 使用制表符或换行符来添加空白
print("python")  #什么都不加
print("\tpython") #"\t"是缩进一格
print("Language:\n\tPython\n\tC\n\tJavascript")  #"\n"是换行


#2.3.4 删除空白
favorite_language = 'python '
favotite-Language
favorite_language.rstrip()  #删除字符串开头和末尾多余的空白

favorite_language = favorite_language.rstrip() #永久删除多余的空白

favorite_language = ' python '
favorite_language.rstrip() #删除开头和末尾多余的空格
favorite_language.lstrip() #删除字符串开头多余的空格
favorite_language.strip()  #删除字符串末尾多余的空格

#动手试一试 
#2-3 
name1 = 'Eric'  #定义字符串变量时不要忘了引号
print("Hello " + name1 + ", would you like to learn some python today?")  

#2-4
name1 = "lisa"
print(name1.title())   #首字母大写
print(name1.upper())   #大写
print(name1.lower())   #小写

#2-5
name2 = "Albert Einstein"
print(name2+' once said,"A person who never made a mistake never tried anything new."')

#2-6
message =' once said,"A person who never made a mistake never tried anything new."' 
print(name2 + message)

#2-7
name3 = " elsa "
print(name3.lstrip())
print(name3.strip())
print(name3.rstrip())

#2.4 数字
2+3   # 加
3-2   # 剪
2*3   # 乘
3/2   # 除
3 ** 2  # 乘方

0.1 + 0.1
2 *  0.1   #结果包含的小数位数可能不确定

#2.4.3 使用str()函数避免类型错误
#错误代码
age  = 23
message = "Happy " + age + "rd Birthday"
print(message)  #age是整形，需要编程字符串类型显示

#正确代码
age  = 23
message = "Happy " + str(age) + "rd Birthday"  #str（）将age用字符串类型表示
print(message)

#动手试一试
#2-8
print(5+3)
print(10-2)
print(2*4)
print(16/2)

#2-9
num = 1
message = "my favorite number  is:"
print (message + " " + str(num))

#注释 是井号键

#python之禅
import this
