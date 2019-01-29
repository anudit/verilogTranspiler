import tt
import os

MOD_NAME = "main"
boolexp = "~B~CD+A~CD+~AB~D+~ABC+A~BC + ~BC~D"

verilog = ""
mainVars = []
nBoolRep = ""
nBoolRepLines = []
wCnt = 1;
fName = "output.txt"

boolexp = boolexp.replace(" ", "")
boolexpList = boolexp.split('+')


for ele in boolexpList:
    
    expStack = []
    ind = 0
    # Construct Expression Stack 
    while (ind < len(ele)):
        if(ele[ind] == "~"):
            mainVars.append(ele[ind+1])
            expStack.append("~" + ele[ind+1] )
            ind+=2
        elif(ele[ind].isalpha()):
            mainVars.append(ele[ind])
            expStack.append(ele[ind])
            ind+=1
        # print(expStack)

    # Change into new representation
    nBoolRepLine = "("
    for ind in range(len(expStack)):
        if (ind == len(expStack)-1):
            nBoolRepLine+=expStack[ind] + ") "
        else:
            nBoolRepLine+=expStack[ind] + " and "
    nBoolRepLines.append(nBoolRepLine)
    

    verilogGate = "\tand(" + "w" + str(wCnt)
    for exp in expStack:
        verilogGate +=  "," + str(exp)
    verilogGate += ");\n"
    verilog += verilogGate
    wCnt+=1

for index in range(len(nBoolRepLines)):
    if (index == len(nBoolRepLines)-1):
        nBoolRep += nBoolRepLines[index]
    else:
        nBoolRep += nBoolRepLines[index] + "or "

mainVars = sorted(list(set(mainVars)))
orGate = "\tor(o"
for n in range(1, wCnt):
    orGate += ",w" + str(n)
orGate += ");\n"
verilog += orGate   

wireLine = "\twire "
for inp in range(1, wCnt):
    wireLine += "w" + str(inp)
    if (inp == wCnt-1):
        wireLine += ";"
    else:
        wireLine += ","
wireLine += "\n"

moduleLine = "module " + MOD_NAME + "("
inputLine = "\tinput "
for inp in range(len(mainVars)):
    moduleLine += str(mainVars[inp]) + ","
    inputLine += str(mainVars[inp])
    if (inp == len(mainVars)-1):
        inputLine += ";"
    else:
        inputLine += ","
moduleLine += "o);\n"
inputLine += "\n"

verilog = moduleLine + inputLine + wireLine + verilog + "endmodule\n"

try:
    b = tt.BooleanExpression(nBoolRep)
except GrammarError as e:
    print("Here's what happened:")
    print(e.message)
    print("Here's where it happened:")
    print(e.expr_str)
    print(' '*e.error_pos + '^')

t = tt.TruthTable(b)

'''
print(nBoolRep+"\n")
print(verilog)
print(t)
'''

with open("out.v", 'w+') as f:
    try:
        f.write(verilog)
        print("[SUCCESS] Verilog File Created")
    except :
        print("[ERROR] File IO Error")

with open("out.txt", 'w+') as f:
    try:
            f.write(nBoolRep+"\n\n")
            f.write(str(t)+"\n\n")
            print("[SUCCESS] Truth Table Created")
            f.write(str(b.tree))
            print("[SUCCESS] Logic Tree Created")
    except :
        print("[ERROR] File IO Error")