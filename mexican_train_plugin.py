from .mexican_train import *
from globalPluginHandler import GlobalPlugin
try: unicode
except NameError: unicode=strfrom api import getFocusObject,copyToClip
from ui import message
class GlobalPlugin(GlobalPlugin):
 def __init__(self, *args, **kwargs):
  super(GlobalPlugin, self).__init__(*args, **kwargs)
  self.a=[]
  self.b=[]
  self.mexican_train=[]
 def terminate(self):
  pass
 def script_getbestvariant(self,gesture):
  gesture=gesture._get_displayName()
  index=int(gesture.split("+")[-1])
  object=getFocusObject()
  children=object.parent.children
  for child in children: self.a.append(die(int(child.name.split("/")[0]),int(child.name.split("/")[1])))
  number=int(object.name.split("/")[0 if index==1 else 1])
  getVariants(number,self.a,self.b,[],self.mexican_train)
  if len(self.b)>0:
   message(str(number))
   c=u""
   if len(self.b)>1: c="Количество вариантов "+str(len(self.b))+".\n"
   for e in range(len(self.b)):
    c+="Вариант - "+str(e)+". Длинна варианта - "+str(len(self.b[e]))+".\n"
    for f in self.b[e]: c+=unicode(f.a[0])+" "+unicode(f.a[1])+"\n"
    if len(self.a)>len(self.b[e]): c+="Кости для мексиканского поезда при варианте "+str(e)+",длинна которых "+str(len(self.mexican_train[e]))+": "+str(self.mexican_train[e])+"\n"
   del self.a[:]
   del self.b[:]
   del self.mexican_train[:]
   copyToClip(c)
   message(c)
 __gestures={"kb:NVDA+control+1":"getbestvariant","kb:NVDA+control+2":"getbestvariant"}