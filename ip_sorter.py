def ip_sorted():
	ip_address = ["192.168.43.114","192.168.43.114","192.168.43.114","192.168.43.114"]
	last_no=[]
	for ip in ip_address:
		x = ip.split(".")[-1]
		last_no.append(int(x))
	sort_last=sorted(last_no)
	indices = []

	for x in sort_last:
		for y in last_no:
			if x==y:
				indices.append(last_no.index(y))

	ordered_ip=[]
	for i in range(len(indices)):
		ordered_ip=ip_address[indices[i]]
	return ordered_ip
