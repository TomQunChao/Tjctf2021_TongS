a=0
b=0
c=0


n=None
k=print
r=int
d=len
class b:
 def __init__(F)->n:
  F.mem=[0]*256
  F.reg=[0]*4
  F.res=0
  F.parsers=[n,F.N,F.R,F.E,F.t,F.J,F.h,F.H,F.i,F.y,F.s,F.w]
 def y(F,op):
  to=op[1]
  fr=op[2]+F.reg[op[3]]+F.reg[op[4]]
  F.reg[to]=F.mem[fr]
  return 1
 def i(F,op):
  fr=op[1]
  to=op[2]+F.reg[op[3]]+F.reg[op[4]]
  F.mem[to]=F.reg[fr]
  return 1
 def E(F,op):
  F.res=F.reg[op[1]]+F.reg[op[2]]
  F.reg[op[1]]=F.res
  return 1
 def s(F,op):
  F.res=F.reg[op[1]]*F.reg[op[2]]
  F.reg[op[1]]=F.res
  return 1
 def H(F,op):
  r=op[1]
  F.reg[0]=r
  return 1
 def w(F,op):
  to=op[1]
  fr=op[2]
  F.reg[to]=F.reg[fr]
  return 1
 def h(F,op):
  S=op[1]
  return S
 def t(F,op):
  S=op[1]
  if F.res==0:
   return S
  return 1
 def J(F,op):
  S=op[1]
  if F.res!=0:
   return S
  return 1
 def N(F,op):
  k('please input a number')
  F.reg[0]=r(input())
  return 1
 def R(F,op):
  k(F.reg[0])
  return 1
 def v(F):
  G=1
  while G<d(F.code):
   Y=F.code[G]
   T=F.parsers[Y[0]](Y)
   G+=T
 def X(F,p):
  F.code=p
  F.v()
p=[[7,0,1],[11,1,0,2],[7,'"正确！请提交tjctf{md5(input)}，input为你输入的数字空格分隔，不要多出空格，例如1 2 3"',3],[8,0,10,1,1,4],[7,'"Oops... wrong"',5],[8,0,11,1,1,6],[7,2,8],[8,0,64,1,1,9],[7,-1,10],[8,0,65,1,1,11],[7,4,12],[8,0,66,1,1,13],[7,5,14],[8,0,67,1,1,15],[7,6,16],[8,0,68,1,1,17],[7,1,18],[8,0,69,1,1,19],[7,3,20],[8,0,70,1,1,21],[7,4,22],[8,0,71,1,1,23],[7,5,24],[8,0,72,1,1,25],[7,-1,26],[8,0,73,1,1,27],[7,1,28],[8,0,74,1,1,29],[7,2,30],[8,0,75,1,1,31],[7,4,32],[8,0,76,1,1,33],[7,5,34],[8,0,77,1,1,35],[7,-1,36],[8,0,78,1,1,37],[7,1,38],[8,0,79,1,1,39],[7,2,40],[8,0,80,1,1,41],[7,3,42],[8,0,81,1,1,43],[7,1,44],[8,0,82,1,1,45],[7,2,46],[8,0,83,1,1,47],[7,3,48],[8,0,84,1,1,49],[7,4,50],[8,0,85,1,1,51],[7,5,52],[8,0,86,1,1,53],[7,-1,54],[8,0,87,1,1,55],[7,-1,56],[8,0,88,1,1,57],[7,6,58],[8,0,89,1,1,59],[7,1,60],[8,0,90,1,1,61],[7,2,62],[8,0,91,1,1,63],[7,-1,64],[8,0,92,1,1,65],[7,4,66],[8,0,93,1,1,67],[7,6,68],[8,0,94,1,1,69],[7,1,70],[8,0,95,1,1,71],[7,-1,72],[8,0,96,1,1,73],[7,3,74],[8,0,97,1,1,75],[7,4,76],[8,0,98,1,1,77],[7,5,78],[8,0,99,1,1,79],[7,0,82],[11,3,0,83],[11,2,0,84],[11,1,0,85],[7,-36,89],[3,0,1,90],[4,21,91],[7,0,92],[11,2,0,93],[7,-6,95],[3,0,2,96],[4,13,97],[8,1,32,3,3,98],[9,1,64,1,2,99],[7,1,100],[3,0,1,101],[5,4,102],[1,103],[9,1,32,3,3,104],[8,0,64,1,2,105],[9,1,32,3,3,107],[7,1,108],[3,2,0,109],[6,-14,110],[7,6,112],[3,1,0,113],[6,-22,114],[7,0,118],[11,1,0,119],[11,2,0,120],[11,3,0,121],[7,-36,125],[3,0,1,126],[4,44,127],[7,0,128],[11,2,0,129],[7,-6,131],[3,0,2,132],[4,6,133],[7,0,134],[8,0,40,0,2,135],[7,1,136],[3,2,0,137],[6,-7,138],[7,0,141],[11,2,0,142],[7,-6,144],[3,0,2,145],[4,13,146],[9,3,64,1,2,147],[7,0,148],[8,1,32,0,0,149],[7,0,150],[11,1,0,151],[7,1,152],[8,0,40,3,1,153],[7,0,154],[9,1,32,0,0,155],[7,1,156],[3,2,0,157],[6,-14,158],[7,0,161],[11,2,0,162],[7,-6,165],[3,0,2,166],[4,9,167],[7,0,168],[9,3,41,2,0,169],[7,-1,170],[3,0,3,171],[5,64,172],[7,1,173],[3,2,0,174],[6,-10,175],[7,6,178],[3,1,0,179],[6,-45,180],[7,0,183],[11,2,0,184],[11,3,0,185],[11,1,0,186],[7,-6,189],[3,0,1,190],[4,46,191],[7,0,192],[11,2,0,193],[7,-6,195],[3,0,2,196],[4,6,197],[7,0,198],[8,0,40,0,2,199],[7,1,200],[3,2,0,201],[6,-7,202],[7,0,205],[11,2,0,206],[7,-6,208],[3,0,2,209],[4,15,210],[7,6,211],[10,0,2,212],[9,3,64,1,0,213],[7,0,214],[8,1,32,0,0,215],[7,0,216],[11,1,0,217],[7,1,218],[8,0,40,3,1,219],[7,0,0,220],[9,1,32,0,0,221],[7,1,222],[3,2,0,223],[6,-16,224],[7,0,227],[11,2,0,228],[7,-6,230],[3,0,2,231],[4,9,232],[7,0,233],[9,3,41,2,0,234],[7,-1,235],[3,0,3,236],[5,12,237],[7,1,238],[3,2,0,239],[6,-10,240],[7,1,243],[3,1,0,244],[6,-47,245],[7,0,248],[11,1,0,249],[9,0,10,1,1,250],[2,251],[6,5,252],[7,0,254],[11,1,0,255],[9,0,11,1,1,256],[2,257]]
b().X(p)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

