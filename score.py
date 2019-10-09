print('character y l z j b represent 优 良 中 及格 不及格 respetively')
nums=int(input('Number of courses you want to calc: '))
res=0
scores_test=[]
credits_test=[]
    
scores_nt=[]
credits_nt=[]
trans={'y':95,'l':85,'z':75,'j':60,'b':0}
for i in range(nums):
    print('Course [',i+1,']')
    score=input('input score: ')
    credit=input('input credit: ')
    if score in ['y','l','z','j','b']:
        scores_nt.append(trans[score])
        credits_nt.append(int(credit)*0.35)
    else:
        scores_test.append(int(score))
        credits_test.append(int(credit)*0.65)
    #calc
temp1,temp2=0,0
for sc,cre in zip(scores_test,credits_test):
    temp1+=sc*cre
for sc,cre in zip(scores_nt,credits_nt):
    temp2+=sc*cre
res=(temp1+temp2)/(sum(credits_nt)+sum(credits_test))
print('Your final score is: ',res)
with open('./your score.txt','a+') as f:
    f.write('\nyou score is ')
    f.write(str(res))
flag=input('press Enter if you want to quit')

    

