# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter = ",",skip_header=1 )
print ("\nData: \n\n",data)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((new_record,data))
print (census)



#Code starts here



# --------------
#Code starts here
age = np.array(census[:,0])
print(age) 
max_age =np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print (age_mean)
age_std = np.std(age)
print (age_std)


# --------------
#Code starts here
#race 0
race_0 = np.array(census[census[:,2]==0],dtype=int)
print(race_0)
len_0 = len(race_0)
print(len_0)

#race 1
race_1 =np.array(census[census[:,2]==1], dtype=int)
print(race_1)
len_1 =len(race_1)
print(len_1)

#race 2
race_2 = np.array(census[census[:,2]==2],dtype= int)
# print(race_2)
len_2=len(race_2)
print (len_2)

#race 3
race_3 = np.array(census[census[:,2]==3],dtype= int)
# print(race_3)
len_3 = len(race_3)
print (len_3)

#race 4
race_4 = np.array(census[census[:,2]==4],dtype= int)
# print(race_4)
len_4 = len(race_4)
print(len_4)
#Minority Race
minor_race= np.array([len_0,len_1,len_2,len_3,len_4])
print(minor_race)
minority_race = 3
print(minority_race)


# --------------
#Code starts here
senior_citizens = np.array(census[census[:,0]>60], dtype=int)
senior_citizens_len=len(senior_citizens)
working_hours_sum = sum(senior_citizens[:,6])
avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)
# print(working_hours_sum)
# print(senior_citizens_len)
# print(senior_citizens)



# --------------
#Code starts here
high = np.array(census[census[:,1]>10],dtype=int)
low = np.array(census[census[:,1]<=10],dtype=int)
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)
# print(high)
# print(low)


