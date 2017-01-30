import os



def remove_element(mac):
	mac=mac.upper()
	os.system('sudo iptables -L -t mangle --line-numbers > abc.txt')
	flag=0
	rule_list=[]
	with open('abc.txt') as f:
    		for line in f:
        		#print line
			mylist=line.split()
			#print mylist
			if len(mylist)>1:
				if mylist[1]=='internet' and mylist[0]=='Chain':
					flag=1
		
			if flag==1:
		
				if mylist[1]=='RETURN':
					if mylist[7]==mac:
						rule_list.append(mylist[0])
				
	for i in rule_list:
		command="echo 'copenhagen1996' | sudo -S iptables -t mangle -D internet "+i
		os.system(command)	
	print rule_list



	os.system('rm abc.txt')
	       
