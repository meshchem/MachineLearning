import random 

def and_expr():
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    expr = f"{a}&{b}"
    res = a & b
    return expr, res


def or_expr():
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    expr = f"{a}|{b}"
    res = a | b
    return expr, res

def to_words(expr, res):
    expr = expr.replace("0", "FALSE").replace("1", "TRUE")
    expr = expr.replace("&", " AND ").replace("|", " OR ")
    return f"{expr} IS {'TRUE' if res == 1 else 'FALSE'}"

def generate_dataset(n_and=5000, n_or=5000, path="linguistic_boolean_dataset.txt"):
    rows = []

    for _ in range(n_and):
        expr, res = and_expr()
        rows.append(to_words(expr, res))

    for _ in range(n_or):
        expr, res = or_expr()
        rows.append(to_words(expr, res))

    random.shuffle(rows)

    with open(path, "w") as f:
        for row in rows:
            f.write(row + "\n")

if __name__ == "__main__":
    generate_dataset()
