import math
def  lcm(nums):
    a=nums[0]
    b=nums[1]
    result=(a*b)//(math.gcd(a,b))
    for num in nums[2:]:
        result=(result*num)//(math.gcd(result,num))
    return result
    
t=int(input())
t=t//2
points=[0,0]
try:  
    for case in range(t):
    
        ques_in=input()
        ans_in=input()
        

        ques_in=ques_in.split()
        questioner=ques_in[0]
        numstring=ques_in[1]
        nums=list(map(int,numstring.split(",")))
        
        assert(2 <= len(nums) <= 7)
        
        for i in nums:
            
            assert(1<=i<=100)
        ans_in=ans_in.split()
        answerer=ans_in[1]
        
        if case==0:
            first=questioner
            second=answerer
        correct=lcm(nums)
        print(f"{questioner}'s question is : {numstring}")
        if ans_in[2]!="PASS":
            answer=int(ans_in[2])
            
            if correct==answer:
                print("Correct Answer")
                print(f'{answerer}: 10points')
                if answerer=="Darrell":
                    points[0]+=10
                else:
                    points[1]+=10
            else:
                
                print("Incorrect Answer")
                print(f'{answerer}: 0points')
        else:
            print("Question is PASSed")
            print(f'Answer is: {correct}')
            print(f'{answerer}: 0points')
        
        if case==t-1:
            
            print("Total Points:")
            if first=="Darrell":
                print(f"Darrell: {points[0]}points")
                print(f"Sally: {points[1]}points")
            else:
                print(f"Sally: {points[1]}points")
                print(f"Darrell: {points[0]}points")
            if points[0]>points[1]:
                print("Game Result: Darrell is winner")
            elif points[0]==points[1]:
                print("Game Result: Draw")
            else:
                print("Game Result: Sally is winner")
except:
    print("Invalid Input")
                
