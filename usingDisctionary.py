my_dict={'Afghanistan' : 93, 'Albania' : 355, 'Algeria' : 213, 'Andorra' : 376, 'Angola' : 244, 'Antarctica' : 672}
new_dict=list(my_dict.keys())
#print(new_dict)
Member_name=new_dict[1]
#print(Member_name)
Member_value=my_dict['Albania']
print("Member name:{first} Member Value:{second}".format(first=Member_name,second=Member_value))
