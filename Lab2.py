import math
def display_main_menu():
    print("display main menu")

def get_user_input():
    print("sequence of numbers please")
    x=input()
    
    
    num_list=[float(i) for i in x.split(",") ]
    print(num_list)
    return num_list
   
def calc_average(num_list):
    average=sum(num_list)/len(num_list)
    return average
def calc_min_and_max_temp(num_list):
    min_max_list=[]
    min_max_list.append(min(num_list))
    min_max_list.append(max(num_list))
    print(min_max_list)
    print("The min is "+str(min(num_list))+" and the max is "+str(max(num_list)))
def calc_median(num_list):
    if (len(num_list)%2==0):
        median_index=(len(num_list)-1)/2
        print("median is "+str(num_list[int(median_index)]))
    else:
        median_index=math.floor(len(num_list)/2)
        print("median is "+str(num_list[int(median_index)]))





def calculate_bmi(height,weight):
    print ("Height= "+str(height))
    print ("weight= "+str(weight))
    return height,weight



def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    average=calc_average(num_list)
    calc_min_and_max_temp(num_list)
    calc_median(num_list)
    height, weight=calculate_bmi(weight=75, height=1.85)

    bmi= weight/(height*height)
    print("bmi= "+str(bmi))
    if bmi<18.5:
        delta=-1
        print("Bulk up twig and Weight classification is "+str(delta))
        
        
    elif 18.5<=bmi<=25.0:
        delta=0
        print("you could be better and Weight classification is "+str(delta))
        
    else:
        delta=1
        print("Hit the gym Buddy and Weight classification is "+str(delta))
    print("Average = "+str(average))

if __name__ == "__main__":
    main()