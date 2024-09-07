#list -> data structure whice can hold multiple vales of multiple data type
#array -> data structure whice can hold multiple vales BUT same data type
list_of_cloud = ["aws", "azure","gcp"] #list

print(list_of_cloud)

#add new cloud from end

list_of_cloud.append("oracle")
print(list_of_cloud)

#add new cloud from middel

list_of_cloud.insert(2,"Heroku")
print(list_of_cloud)

#print the count of elemants in list
print("Total elemant of list: ",len(list_of_cloud))



cloud = "amarCloud" #normal variable
for cloud in list_of_cloud:
	print(" ")
	print(cloud)

for i in range(1,11):
	print(i)
