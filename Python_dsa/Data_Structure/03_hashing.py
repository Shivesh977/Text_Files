# Hashing in python is done by dict 
mp={
    1:1,
    2:3,
    3:4
}

# 
mp={ }

mp[1]=2
mp[2]=3

# to delete key value pair 
del mp[1]  # del mp['key']

mp.clear() # removes everything 

len(mp) # dictionary size 



# ##### Frequency hashing 
l=[1,1,1,1,2,2,2,3,3,3,4,4]

mp={}

for x in l:
  if x not in mp : 
    mp[x]=1
  else : 
    mp[x]+=1

print(mp)


######### set : stores only unique values
st=set()

st.add(10)
st.add(20)
st.add(30)
st.add(30)

# set functions
st.add(x) # to add x in set 
st.remove(x) # removes element x from set 
st.clear() # clears the whole of set 
len(st) # give length of set 


# a | b              # union
# a & b              # intersection
# a - b              # difference
# a ^ b              # symmetric difference