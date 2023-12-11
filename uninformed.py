from sympy import symbols, to_cnf, Or, Not, simplify_logic

def can_resolve(clause1, clause2):
    if simplify_logic(Or(clause1, clause2)) == True:
        return True
    else:
        return False

def resolve(clause1, clause2):
    if (len(clause1.args) == 1 or len(clause1.args) == 0) and (len(clause2.args) == 1 or len(clause2.args) == 0):
        return simplify_logic(clause1 & clause2)
    
    if len(clause1.args) == 1 or len(clause1.args) == 0:
        lst = list(clause2.args)
        for literal in clause2.args:
            if literal == Not(clause1) or clause1 == Not(literal):
                lst.remove(literal)
                return Or(*lst)
            
    if len(clause2.args) == 1 or len(clause2.args) == 0:
        lst = list(clause1.args)
        for literal in clause1.args:
            if literal == Not(clause2) or clause2 == Not(literal):
                lst.remove(literal)
                return Or(*lst)

    list1 = list(clause1.args)
    list2 = list(clause2.args)
    for literal1 in clause1.args:
        for literal2 in clause2.args:
            if literal1 == Not(literal2) or literal2 == Not(literal1):
                list1.remove(literal1)
                list2.remove(literal2)
    return Or(*(list1+list2))

def checks(start, kb, steps):
    count = 0
    while len(kb) >= 1 and count < len(kb):
        count = 0
        i = 0
        while i < len(kb):
            result = can_resolve(start, kb[i])
            if result:
                steps.append({'Clause 1': start, 'Clause 2': kb[i], 'Result': 'Can be resolved'})
                Dict = dict()
                Dict['Clause 1'] = start
                Dict['Clause 2'] = kb[i]
                start = resolve(start, kb[i])
                Dict['Resolvent'] = start
                steps.append(Dict)
                kb.pop(i)
                i = 0
                if start == False:
                    return True
            else:
                steps.append({'Clause 1': start, 'Clause 2': kb[i], 'Result': 'Cannot be resolved'})
                count += 1
                i += 1

    return False

def entails(query, kb, steps):
    length = len(kb)
    temp_kb = kb[:]
    for i in range(length):
        if checks(query, temp_kb, steps) == True:
            return 1
        else:
            temp_kb = kb[:]
            query = temp_kb[i]
            temp_kb.pop(i)

    return 0


if __name__ == "__main__":
    n, m = map(int, input().split())

    A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = symbols('A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z')

    formulas = []
    for _ in range(n):
        formula = input()
        formula = formula.replace('>', '>>').replace('=', '^~').replace('!', '~')
        formulas.append(formula)

    query = input()

    cnf_formulas = []
    for formula in formulas:
        cnf_formula = to_cnf(eval(formula))
        cnf_formula = str(cnf_formula)
        subexpressions = cnf_formula.split(' & ')
        for subexpression in subexpressions:
            cnf_formulas.append(eval(subexpression))

    query = query.replace('>', '>>').replace('=', '^~').replace('!', '~')
    query = Not(eval(query))
    query = to_cnf(query)

    kb = cnf_formulas[:]

    # Removing useless clauses from the knowledge base. For example: A|~A which is a tautology.
    for clause in kb:
        if simplify_logic(clause) == True:
            kb.remove(clause)

    steps = []
    output = entails(query, kb, steps)

    if m == 1:
        for step in steps:
            print(step)

    print(output)