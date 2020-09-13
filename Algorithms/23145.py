def solution(new_id):
    step1=new_id.lower()
    step1_list=list(step1)

    tmp=[]
    for i in range(len(step1_list)):
        val=ord(step1_list[i])
        if (val>=48 and val<=57) or (val>=97 and val<=122) or (val==45) or(val==46) or (val==95):
            pass
        else :
            #step1_list.remove(chr(val))
            tmp.append(chr(val))
    
    for i in tmp:
        step1_list.remove(i)
    tmp.clear()
    step2=''.join(step1_list)
    
    step2_list=list(step2)
    tmp=[0]*len(step2_list)
    
    for i in range(len(step1_list)):
        val=ord(step1_list[i])
        if val==46:
            tmp[i]=1

    flag=0
    step3=''
    for i in range(len(step1_list)):
        if tmp[i]==1:
            flag=1 
            continue
        if tmp[i]==0 and flag==1:
            step3+='.'
            flag=0
        if tmp[i]==0:
            step3+=step1_list[i]
   
    step3_list=list(step3)
    if len(step3_list)==0:
        return 'aaa'
    if step3_list[0]=='.':
        step3_list.remove('.')
    if step3_list[-1]=='.':
        step3_list.pop()
        
    step4=''.join(step3_list)
    
    step4_list=list(step4)
    
    for i in range(len(step4_list)):
        if step4_list[i]==' ':
            step4_list[i]='a'
     
    step5=''.join(step4_list)
   
    step6=step5[0:15]
    step6_list=list(step6)
    if step6_list[-1]=='.':
        step6_list.pop()

    step6=''.join(step6_list)
    
    if len(step6)<=2:
        if len(step6)==1:
            return step6*3
        if len(step6)==2:
             return step6[0]+step6[1]*2
    
     
    answer = step6
    return answer





























s=input()
print(solution(s))
