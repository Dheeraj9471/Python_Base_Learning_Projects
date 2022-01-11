''' Regular Expression'''
# new program
# import re
# s= """ Abc def mnmn12983 e12e21981246129 89 123456 pasjsdnh dheerj ddjhf 63893478472"""
# p="\d{10}"
# print(re.findall(p.s))

#new program
# import re
# s="welcome to cetpa .cetpa is no1"
# p= "cetpa"
# res= re.findall(p,s)
# print(res)

#new program
# import re
# s=" welcom to cetpa"
# p=r"[abqrstAP]"
# res=re.findall(p,s)
# print(res)

# New program
# import re
# s="cetpa, abc_*^@"
# p= r"[a-zA-Z0-9_*]"
# res=re.findall(p,s)
# print(res)

# New program
# import re
# s="cetpa, abc_*^@"
# p= r"[a-zA-Z0-9_*]"
# res=re.findall(s,p)
# print(res)

# new program
# import re 
# s= "cetpa*.@123 abc*."
# p="."
# res= re.findall(p,s)
# print(res)

# new program
# import re 
# s= "cetpa*.@123 abc*."
# p="\."
# res= re.findall(p,s)
# print(res)

# new program
# import re 
# s= "cetpa*.@123 abc*."
# p="[.]"
# res= re.findall(p,s)
# print(res)

# new program
# import re 
# s= "cetpa*.@123 abc*."
# p="[^a-z]"
# res= re.findall(p,s)
# print(res)


# new program
# import re 
# s= " abc 123 89#$nm78"
# p=r"[0-9]"
# res=re.findall(p,s)
# print(res)

# new program
# import re 
# s= " abc 123 89#$nm78"
# p=r"\d[2]"
# res=re.findall(p,s)
# print(res)

# new program
# import re 
# s= " abc 123 89#$nm78"
# p=r"abc"
# res=re.findall(p,s)
# print(res)

# new program
# import re 
# s= " abc 123 89#$nm78"
# p=r"\d\d"
# res=re.findall(p,s)
# print(res)

# new program
# import re 
# s= " abc 123 89#$nm78"
# p=r"[0-9][0-9]"
# res=re.findall(p,s)
# print(res)

# new program
# import re
# s="abc 7123 89#$ nnabcnn78 777555 12345768"
# p=r"\d\d\d\d\d"
# res=re.findall(p,s)
# print(res)

# new program
# import re
# s= "abc pqr addd ofgh ddlg ab*c DDe 121"
# p="\w\w\w"
# res= re.findall(p,s)
# print(res)

# new program
# import re
# s="1234567899 12abc dheeraj 929283937836373"
# p=r"\d{10}"
# res=re.findall(p,s)
# print(res)

# new program
# import re
# s="99999999999 12abc  2343425678290 1234 Dheeraj 673879765 "
# p=r"\d{5,10}" 
# res=re.findall(p,s)
# print(res)

# new program
# import re
# s="99999999999 12abc  2343425678290 1234 Dheeraj 673879765 "
# p=r"\d{5,}" 
# res=re.findall(p,s)
# print(res)

#new program
# import re
# s="abc de pqr 123 *&abc ##234"
# p= r"[a-z]+"
# res= re.findall(p,s)
# print(res)

#new program
# import re
# s="abc de pqr 123 *&abc ##234"
# p= r"\w +"
# res= re.findall(p,s)
# print(res)

# new program
# import re
# s= "abc@abc pqr & manopdf fh@qpest"
# p=r"[a-z]{3}@[a-z]{3}"
# res= re.findall(p,s)
# print(res)
  

# new program
# import re
# s= "Dhheraj@gamil.com  123@gamail  hello123@ysahu.com hbcfsk@yahp.co.in"
# p=r"\w+@\w+[.]\w+\w+"
# res=re.findall(p,s)
# print(res)


# scrapping

# import re
# import urllib.request
# fun=urllib.request.urlopen("https://www.kaggle.com/")
# data=fun.read()
# # print(data)
# stri=str(data ,"<a>")
# pemail=r"\w+@\w+\.\w+"
# res=re.findall(pemail,stri)
# print(res)
# pmob=r"\d{10}"
# rrs=re.findall(pmob,stri)
# print(rrs)

# pmob=r"\d{10}"
# rrs=re.findall(pmob,stri)
# print(rrs)

#beautifull shop
# import re
# s="Dhheraj is boy 1"
# p="^Dhheraj"
# res= re.findall(p,s)
# print(res)

# new program
# import re
# s="Dhheraj is boy 1"
# p=r"boy&"
# res= re.findall(p,s)
# print(res)

# new program
# import re
# s="Dhheraj is boy \n &^&123#."
# p=r"."
# res= re.findall(p,s)
# print(res)

# new program
# import re
# s="Dhheraj is boy \n &^&123#.""raj"
# p=r"raj"
# res= re.findall(p,s)
# print(res)

#new proram
# import re
# s = "Dheeraj is a good anbd boy"
# p=r"is|Dheeraj"
# res= re.findall(p,s)
# print(res)

#new proram
# import re
# s = "783_7r327 r6rt27r_t265 123_"
# p="(\d+)_"
# res= re.findall(p,s)6fr4
# print(res)

#new programing
# import re
# s= "abc def ab@12 fghr"
# p="[a-z]{3}"
# res=re.split(p,s)
# print(res)


