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
print('檔案讀取完了, 總共有', len(data), '筆資料')

#test 算出每筆資料的平均長度

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #sum_len += 1

print('留言的平均長度為', sum_len/len(data))

