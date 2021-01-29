# n1 = 10
# n2 = 0

# try:
#     result = n1 / n2
#     print(f"{n1} / {n2} = {result}")
# except:
#     print("0 can be divided")

# print("program is terminated with normaly")



# s = input("integer: ")

# try:
#     point = int(s) # ValueError 발생 가능
#     print(150 / point) # ZeroDivisionError 발생 가능

# except ValueError:
#     print("input integer only")
# except ZeroDivisionError:
#     print("0 can not be divided")
# except:
#     print("Unknown Error is occured.")


# print("program is terminated with normaly")



# pets = ["cat", "dog", "frog"]

# for i in range(4):
#     try:
#         print(f"I want {pets[i]}!")
#     except:
#         print("there is no pets information")
#     finally:
#         print("I like it!")

# print("program is terminated with normaly")

# def withdraw(money):
#     if money > balance:
#         raise ValueError
#     return balance - money

# balance = 5000

# try:
#     result = withdraw(30000)
#     print(f"rest balance is: {result}")
# except:   
#     print("need more balance")


# file_path = "D:\\Coding\\itbank-python_basic\\py1530\\rdd.txt"
# data = "ring\nding\ndong"

# try:
#     f = open(file_path, "w", encoding='UTF-8')
#     f.write(data)
#     print(f"{data} is written in {file_path}")
# except:
#     print("there is no file or path in your PC")
# finally:
#     f.close()


# file_path = "D:\\Coding\\itbank-python_basic\\py1530\\rdd1.txt"
# added_data = "\nsha sha sha"

# try:
#     f = open(file_path, "a", encoding='UTF-8')
#     f.write(added_data)
#     print(f"{added_data} is appended in {file_path}")
# except:
#     print("there is no file or path in your PC")
# finally:
#     f.close()



# def putTextToFile(file_path, contents):
#     try:
#         f = open(file_path, "a", encoding='UTF-8')
#         f.write("\n"+contents)
#         print(f"{contents} is written into {file_path} well.")
#     except:
#         print(f"can not open the file {file_path}")
#     finally:
#         f.close()

# file_directory = "D:\\Coding\\itbank-python_basic\\py1530\\"
# file_name = ""
# file_text = ""

# while True:
#     print("if you want to exit this program, then put the [exit] into anywhere.")
    
#     file_name = input("please input the file name to put the text: ")
#     if file_name == "exit":
#         print("exiting...")
#         break
    
#     file_text = input("please input the text to put into the file: ")
#     if file_text == "exit":
#         print("exiting...")
#         break
    
#     file_fullpath = file_directory + file_name
#     putTextToFile(file_fullpath, file_text)


# file_path = "D:\\Coding\\itbank-python_basic\\py1530\\rdd.txt"

# try:
#     f = open(file_path, "r", encoding='UTF-8')
#     text = f.read()
#     print(f"{text} is in {file_path}")
# except:
#     print("there is no file or path in your PC")
# finally:
#     f.close()

# print(type(text))




# file_path = "D:\\Coding\\itbank-python_basic\\py1530\\rdd.txt"

# try:
#     f = open(file_path, "r", encoding='UTF-8')
#     text = f.readlines()
#     for i in text:
#         print(f"{i}", end = "")
# except:
#     print("there is no file or path in your PC")
# finally:
#     f.close()


file_path = "D:\\Coding\\itbank-python_basic\\py1530\\"
file_points = "points.txt"
file_result = "result.txt"
full_path_points = file_path + file_points

tot = 0
count = 0

try:
    f = open(file_path + file_points, "r", encoding='UTF-8')
    while True:
        point = f.readline()
        if not point:
            break
        tot += int(point)
        count += 1
except:
    print("there is no file or path in your PC")
finally:
    f.close()    

try:
    f = open(file_path + file_result, "w", encoding='UTF-8')
    f.write(f"Total point is {tot}\nAverage is {tot / count:.2f}")    
except:
    print("there is no file or path in your PC")
finally:
    f.close()    

print(f"Total point is {tot}")
print(f"Average is {tot / count:.2f}")

    