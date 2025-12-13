import random
import csv
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # integer division; use truediv for floats
}

def single_digit_addition(min_val=0, max_val=10):
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    add = OPS['+']
    # avoid division by zero
    expr = f"{a}+{b}"
    result = add(a, b)
    return expr, result

def simple_subtraction(min_val=0, max_val=10):
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, a)
    sub = OPS['-']
    # avoid division by zero
    expr = f"{a}-{b}"
    result = sub(a, b)
    return expr, result

def subtraction(min_val=0, max_val=10):
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    sub = OPS['-']
    # avoid division by zero
    expr = f"{a}-{b}"
    result = sub(a, b)
    return expr, result

def random_simple_expr(min_val=0, max_val=100):
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    op = random.choice(list(OPS.keys()))
    # avoid division by zero
    if op == '/':
        b = random.randint(1, max_val)
        # optional: force exact division so result is integer
        a = b * random.randint(min_val, max_val // max(1, b))
    expr = f"{a}{op}{b}"
    result = OPS[op](a, b)
    return expr, result

def safe_div(op, x, y):
    if op == '/' and y == 0:
        return None  # signal invalid
    return OPS[op](x, y)

def random_parenthesized_expr(min_val=0, max_val=20):
    while True:
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        c = random.randint(min_val, max_val)
        op1 = random.choice(list(OPS.keys()))
        op2 = random.choice(list(OPS.keys()))

        if random.random() < 0.5:
            inner = safe_div(op1, a, b) if op1 == '/' else OPS[op1](a, b)
            if inner is None:
                continue
            if op2 == '/' and c == 0:
                continue
            expr = f"({a}{op1}{b}){op2}{c}"
            result = OPS[op2](inner, c)
        else:
            inner = safe_div(op1, b, c) if op1 == '/' else OPS[op1](b, c)
            if inner is None or (op2 == '/' and inner == 0):
                continue
            expr = f"{a}{op2}({b}{op1}{c})"
            result = OPS[op2](a, inner)

        return expr, result



def generate_dataset(n_simple=10000, n_paren=2000, path="simple_subtraction_dataset.csv"):
    rows = []

    # for _ in range(n_simple):
    #     expr, res = single_digit_addition()
    #     rows.append(f"{expr}={(res)}")

    for _ in range(n_simple):
        expr, res = simple_subtraction()
        rows.append(f"{expr}={(res)}")


    # for _ in range(n_simple):
    #     expr, res = random_simple_expr()
    #     rows.append(f"{expr}={round(res, 2)}")

    # for _ in range(n_paren):
    #     expr, res = random_parenthesized_expr()
    #     rows.append(f"{expr}={round(res, 2)}")

    random.shuffle(rows)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["expression"])
        for row in rows:
            writer.writerow([row])

if __name__ == "__main__":
    generate_dataset()
