import sys
file=open('list.txt, 'r'')
list1=file.read()
while True :
	word=input()
	if(word in list1):
		print(True)
	else:
		print(False)