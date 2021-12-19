
# We use Google's Constraint Programming solver to solve each puzzle in a second or two.
# Find it at https://developers.google.com/optimization/cp/
from ortools.constraint_solver import pywrapcp

# Create the solver.

solver = pywrapcp.Solver("")

# Create the variables.

Vars = []

## Island values (number of bridges)
Value = {}
for Island in Islands:
  Value[Island] = solver.IntVar(1,8,"IslandValue_"+str(Island[0])+"_"+str(Island[1]))
  Vars.append(Value[Island])

G = [[0 for x in range(12)] for y in range(12)]

for x in range(12):
  for y in range(12):
    G[x][y] = solver.IntVar(0,1,"Xed_"+str(x)+"_"+str(y))
    Vars.append(G[x][y])

# ## Number of bridges between pairs of islands
# BridgesBetween = {}
# for Island in Islands:
#   x,y = Island
#   for Neighbor in Neighbors[Island]:
#     x1,y1 = Neighbor
#     if x<x1 or (x==x1 and y<y1):
#       BridgesBetween[(Island,Neighbor)] = solver.IntVar(0,2,"BridgesBetween_"+str(x)+"_"+str(y)+"_"+str(x1)+"_"+str(y1))
#       Vars.append(BridgesBetween[(Island,Neighbor)])

# Constraints

## Island value is number of bridges to neighbors.

for Island in Islands:
  Bridges = []
  for Neighbor in Neighbors[Island]:
    if (Island,Neighbor) in BridgesBetween:
      Bridges.append(BridgesBetween[(Island,Neighbor)])
    else:
      Bridges.append(BridgesBetween[(Neighbor,Island)])
  solver.Add(Value[Island] == sum(Bridges))

## Sign sums are correct, and all addends differ

def FindAddends(x1,x2,y1,y2,xStep,yStep,Tot):
  Addends = []
  xx,yy = x1,y1
  while not (xx==x2 or yy==y2):
    if (xx,yy) in Signs:
      break
    if (xx,yy) in Islands:
      Addends.append(Value[(xx,yy)])
    xx += xStep
    yy += yStep
  solver.Add(sum(Addends) == Tot)
  solver.Add(solver.AllDifferent(Addends))

for Sign in Signs:
  x,y = Sign
  N,S,E,W = Signs[Sign]
  if not N == 0:
    FindAddends(x,x+1,y+1,Height,0,1,N)
  if not S == 0:
    FindAddends(x,x+1,y-1,-1,0,-1,S)
  if not E == 0:
    FindAddends(x+1,Width,y,y+1,1,0,E)
  if not W == 0:
    FindAddends(x-1,-1,y,y+1,-1,0,W)

## Bridges do not cross

for Island1,Island2,Island3,Island4 in CrossThreats:
  solver.Add(BridgesBetween[(Island2,Island1)]*BridgesBetween[(Island3,Island4)] == 0)

# Create the "decision builder"

db = solver.Phase(Vars, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

# Test whether the map is a connected graph.
def Connected(BridgesBetween):
  global Islands, Neighbors
  
  def Explore(Island):
    Remaining.remove(Island)
    if Remaining == []:
      return
    else:
      for Neighbor in Neighbors[Island]:
        if not Neighbor in Remaining:
          continue
        if (Island,Neighbor) in BridgesBetween:
          Pair = (Island,Neighbor)
        else:
          Pair = (Neighbor,Island)
        if BridgesBetween[Pair].Value() == 0:
          continue
        Explore(Neighbor)

  Remaining = list(Islands)
  Explore(Remaining[0])
  return (Remaining == [])

# Call the solver and display the solution.

if solver.Solve(db):
  while solver.NextSolution():
    if Connected(BridgesBetween):
      print("Solution:")
      for Island in Islands:
        print("Island", Island, "=",Value[Island].Value())
      for B in BridgesBetween:
        if not BridgesBetween[B].Value() == 0:
          print(B,BridgesBetween[B].Value(), "bridges")
      break
else:
  print("No solution found.")
