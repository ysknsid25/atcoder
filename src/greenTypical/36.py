s=list(input())
k=int(input())

dot_cnt_list=[0 for i in range(len(s)+1)]
dot_cnt=0
for i in range(len(s)):
  span = i+1
  if s[i]==".":
    dot_cnt+=1
  dot_cnt_list[span]=dot_cnt

#! 尺取法
l=1
r=1
ans=0
while r<=len(s):
  dot_cnt=dot_cnt_list[r]-dot_cnt_list[l-1]
  if dot_cnt <= k:
    r+=1
  else:
    ans=max(ans,r-l)
    l+=1
ans=max(ans,r-l) #最後の一回

print(ans)