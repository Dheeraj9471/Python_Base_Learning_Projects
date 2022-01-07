
# new program for witre mode write from starting oint
# f=open("E://file_handling/file1.txt","w")
# # print(type(f))
# f.write("welocm to my world")
# f.close()

#new program read mode
# f=open("E://file_handling/file1.txt","r")
# data=f.read()
# print(data)
# f.close()

#new program
# f=open("E://file_handling/file1.txt","r")
# data=f.read(5)
# print(data)
# f.close()

#new program
# f=open("E://file_handling/file1.txt","w")
# data="hello thw world wide"
# f.write(data)
# f.close()

#new program
# f=open("E://file_handling/file1.txt","w")
# print(f.tell())
# print(f.read(5))
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(3))
# f.close()

# #new program
# f=open("E://file_handling/file1.txt","r")
# # l1=f.readline()
# # print(l1)
# l1=f.readline(20)
# print(l1)
# f.close()

#new program
# f=open("E://file_handling/file3.txt","w")
# f.write("hello\nsfhs\nwerlcodm teieion\n")
# f.write("welocidn bamk")
# f.write("python is refrance type varisals")
# f.close()

#new program
# f=open("E://file_handling/newf.txt","w")
# f.write("hello")
# print()
# f.write(" ")
# f.write(" ")
# f.write("world")
# f.close()

#new program

# f=open("E://file_handling/file4.txt","w")
# print("my name is Dheeraj kumar",file=f)
# f.close()

#new program
# f=open("E://file_handling/file3.txt","r")
# l1=f.readline()
# print(l1,end=" ")
# l1=f.readline()
# print(l1,end=" ")
# f.close()

#new program
# f=open("E://file_handling/file4.txt","w")
# data=34567
# f.write(data)
# f.close()

#new program
# f=open("E://file_handling/file5.txt","wb")
# data=b"my name is good boy"
# print(type(data))
# f.write(data)
# f.close()

# new program
# f=open("E://file_handling/file5.txt","rb")
# print(f.read(40))
# f.close()

#new program
# f=open("E://file_handling/Dheeraj.mp4","rb")
# print(f.read(100))
# f.close()

# new program
# f1=open("E://file_handling/Dheeraj.mp4","rb")
# f2=open("E://file_handling/Dheeraj2.mp4","wb")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

# new program
# f1=open("E://file_handling/Dheeraj.mp4","rb")
# f2=open("E://file_handling/Dheeraj2.mp4","wb")
# while(1):
#     data=f1.read(100000)
#     if (data==b" "):
#         break
#     f2.write(data)
# f1.close()
# f2.close()

#new program
# f1=open("E://file_handling/Dheeraj2.mp4","rb")
# f2=open("E://file_handling/Dheeraj.mp4","wb")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()

#new program
# f1=open("E://file_handling/Dheeraj2.mp4","rb")
# f2=open("E://file_handling/Dheeraj.mp4","ab")
# data=f1.read()
# f2.write(data)
# f1.close()
# f2.close()