#data=[]
#with open('reviews.txt', 'r') as f:
#	for line in f:
#		data.append(line)
#print(len(data))

#print(data[0])
#print('---------------')
#print(data[1])

#延伸功能-每1000計一次
data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0:  # %餘數7%3=1 , 10%6=4
		    print(len(data))
print(len(data))

print(data[0])
print('---------------')
print(data[1])