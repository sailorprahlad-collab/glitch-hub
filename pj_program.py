# pj_program.py - GLITCH HUB - By PJ
# Where System 1 gets confused, System 2 finds the glitch.

def pj_cube_root_2digit(N):
    s = str(N)
    # Group by 3, first group gives a
    groups = []
    while s:
        groups.append(s[-3:])
        s = s[:-3]
    groups = groups[::-1]
    first = int(groups[0])
    a = max([d for d in range(10) if d**3 <= first])
    base = a * 10
    target = N - base**3
    print(f"\nN={N} Groups={groups} a={a} Base={base} Target={target}")
    for b in range(10):
        chain = 30*a + b
        D = chain - b*b
        if D == 0:
            print(f"b={b} chain={chain} D=0 GLITCH - coeff = infinity, use summation only")
            summation = sum(3*n*n + 3*n + 1 for n in range(base, base+b))
            if summation == target:
                return base + b
            continue
        coeff = (base + b) / D
        formula = coeff * (chain*b - b*b) * D + b**3
        summation = sum(3*n*n + 3*n + 1 for n in range(base, base+b))
        match = int(formula) == summation == target
        print(f"b={b} chain={chain} D={D} coeff={coeff:.4f} formula={formula:.0f} summation={summation} match={match}")
        if match:
            return base + b
    return None

def pj_cube_root_3digit_step(N):
    # 1442897 example: 1 -> 11 -> 113, same program, Base changes
    print(f"\nN={N} Groups: 1 | 442 | 897")
    # Step 1: 100 -> 110
    base1 = 100
    target1 = 110**3 - 100**3
    s1 = sum(3*n*n + 3*n + 1 for n in range(base1, base1+10))
    print(f"STEP 1: 100 -> 110 Target={target1} Summation={s1} match={s1==target1}")
    # Step 2: 110 -> 113
    base2 = 110
    target2 = N - base2**3
    print(f"STEP 2: Base={base2} Target={target2}")
    for b in range(10):
        chain = 3*base2 + b
        D = chain - b*b
        coeff = (base2 + b) / D
        formula = coeff * (chain*b - b*b) * D + b**3
        summation = sum(3*n*n + 3*n + 1 for n in range(base2, base2+b))
        match = int(formula) == summation == target2
        print(f"b={b} chain={chain} D={D} coeff={coeff:.4f} formula={formula:.0f} summation={summation} match={match}")
        if match:
            return base2 + b
    return None

print("2-digit proofs:")
print("Answer:", pj_cube_root_2digit(15625))  # 25
print("Answer:", pj_cube_root_2digit(19683))  # 27
print("Answer:", pj_cube_root_2digit(32768))  # 32
print("Answer:", pj_cube_root_2digit(970299)) # 99
print("Answer:", pj_cube_root_2digit(4096))   # 16 - GLITCH D=0

print("\n3-digit proof:")
print("Answer:", pj_cube_root_3digit_step(1442897)) # 113
