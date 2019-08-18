S=input()
ans =0 
	
ans+=S.count('c=')
S=S.replace('c=','')

ans+=S.count('c-')
S=S.replace('c-','')

ans+=S.count('dz=')
S=S.replace('dz=','')

ans+=S.count('d-')
S=S.replace('d-','')

temp=0
temp+=S.count('lj')
temp+=S.count('nj')

#S=S.replace('lj','')
#S=S.replace('nj','')

ans+=S.count('s=')
S=S.replace('s=','')

ans+=S.count('z=')
S=S.replace('z=','')

print(ans+len(S)-temp)
