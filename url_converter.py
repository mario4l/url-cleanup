import os

url_path_start = "/prepended-start-"
my_str = input("Enter string: ")
print(url_path_start + my_str.replace(' ', '-').lower())
os.system("pause")
