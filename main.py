MOD_NAME = "main"
boolexp = "~B~CD+A~CD+~AB~D+~ABC+A~BC + ~BCD~"

verilog = ""
mainVars = []
boolexp = boolexp.replace(" ", "")
boolexpList = boolexp.split('+')

wCnt = 1;
for ele in boolexpList:
    expStack = []
    for ind in range(len(ele)):
        if(ele[ind] == "~"):
            mainVars.append(ele[ind+1])
            expStack.append("~" + ele[ind+1] )
            ind+=1
        elif(ele[ind].isalpha()):
            mainVars.append(ele[ind])
            expStack.append(ele[ind] )
    verilogGate = "\tand(" + "w" + str(wCnt)
    for exp in expStack:
        verilogGate +=  "," + str(exp)
    verilogGate += ");\n"
    verilog += verilogGate
    wCnt+=1

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
print(verilog)