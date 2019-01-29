import tt
try:
    b = tt.BooleanExpression('(~B and ~C and D) or (A and ~C and D)or(~A and B and ~D)or(~A and B and C)or(A and ~B and C) or (~B and C and ~D)')
except GrammarError as e:
    print("Here's what happened:")
    print(e.message)
    print("Here's where it happened:")
    print(e.expr_str)
    print(' '*e.error_pos + '^')

mainVars = ["A", "B", "C", "D"]

t = tt.TruthTable(b)
orderedVars = []
for inputs, result in t:
    inputString = str(inputs)
    for ind in range(len(inputString)):
        if (inputString[ind].isalpha()):
            orderedVars.append(inputString[ind])
    break

for inputs, result in t:
    inputString = str(inputs)
    dynEvalString = "b.evaluate(" + inputString + ")"
    print(dynEvalString)
    evalRes = eval(dynEvalString)
    if(evalRes == result):
        print("YES")

print(b.tree)