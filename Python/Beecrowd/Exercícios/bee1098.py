i = 0
j = 1
while i <= 2:
    if i == 0 or i == 1 or (round(i, 2)) == 2:
        print(f"I={round(i)} J={round(j)}")
        print(f"I={round(i)} J={round(j + 1)}")
        print(f"I={round(i)} J={round(j + 2)}")
    else:
        print(f"I={i:.1f} J={j:.1f}")
        print(f"I={i:.1f} J={j + 1:.1f}")
        print(f"I={i:.1f} J={j + 2:.1f}")
    i += 0.2
    j += 0.2