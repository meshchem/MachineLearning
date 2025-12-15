import random 

def random_and_expr():
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    expr = f"{a}&{b}"
    res = a & b
    return expr, res


def random_or_expr():
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    expr = f"{a}|{b}"
    res = a | b
    return expr, res

def generate_dataset(n_and=5000, n_or=5000, path="binary_and_boolean_dataset.txt"):
    rows = []

    for _ in range(n_and):
        expr, res = random_and_expr()
        rows.append(f"{expr}={res}")

    # for _ in range(n_or):
    #     expr, res = random_or_expr()
    #     rows.append(f"{expr}={res}")

    # random.shuffle(rows)

    with open(path, "w") as f:
        for row in rows:
            f.write(row + "\n")

if __name__ == "__main__":
    generate_dataset()
