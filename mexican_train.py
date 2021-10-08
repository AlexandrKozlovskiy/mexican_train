class die:
 def __init__(self,a,b,change=True):
  if a>b and change: self.a=b,a
  else: self.a=a,b
 def __eq__(self,a): return self.a[0] ==a.a[0] and self.a[1] ==a.a[1]
 def __str__(self): return str(self.a[0])+" "+str(self.a[1])
 def __repr__(self): return self.__str__()
 def __unicode__(self): return self.str()
scores,length,autosorting=0,0,True
def getvariants(number,a,b,c,mexican_train,_scores=0):
 global scores,length
 variants=False
 if len(a)==0:
  if len(c)>length and autosorting: del b[:]; del mexican_train[:]
  scores=_scores
  length=len(c)
  b.append(c)
  return
 for die in range(len(a)):
  die0=a[die]
  if die0.a[0]==number or die0.a[1]==number:
   variants=True
   del a[die]
   new_list=c[:]
   _scores+=die0.a[0]+die0.a[1]
   new_list.append(die0)
   getvariants(die0.a[(die0.a.index(number)+1)%2],a,b,new_list,mexican_train,_scores)
   _scores-=die0.a[0]+die0.a[1]
   a.insert(die,die0)
  if die==len(a)-1 and not variants and len(c)>0 and (not autosorting or (_scores>scores or _scores==scores and len(c)>=length) and autosorting):
   if (len(c) >length or _scores>scores) and autosorting: del b[:]; del mexican_train[:]
   scores=_scores
   length=len(c)
   mexican_train.append(a[:])
   b.append(c)
def getVariants(number,a,b,c,mexican_train,_scores=0):
 global length,scores
 getvariants(number,a,b,c,mexican_train,_scores)
 scores=0
 length=0