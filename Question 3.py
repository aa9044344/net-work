import json
f=open('C:\\Quiz.json','r')
d= json.load(f)
f.close()

score = 0
Useranswers = []
x=dict(d['Que'])
z=list(d['Ans'])

print("Welcome to the quiz")
for i in x.values():
    print(i)
    useranswer = input("Your answer:")
    Useranswers.append(useranswer)
    for s in z:
       if useranswer == s:
        score=score+1
           
print("Your score:", score ,"out of",len(x))

username = input("Enter your name: ")
result = {}
result["name"]=username
result["score"]=score
result["total_questions"]=len(x)
result["Useranswers"]=Useranswers

f=open('C:\\Result.json','w')
json.dump(result,f)
f.close()
print("Thank you for taking the quiz")