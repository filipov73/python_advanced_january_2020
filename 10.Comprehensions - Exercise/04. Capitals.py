print("\n".join([f"{k} -> {v}" for k, v in {el[0]: el[1] for el in zip(input().split(", "), input().split(", "))}.items()]))
