#write a program that accepts seconds from keyboard as integer. Your program should converts seconds in hours, minutes and seconds.
#Enter seconds: 13400
#Hours: 3
#Minutes: 43
#Seconds: 20

seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)



