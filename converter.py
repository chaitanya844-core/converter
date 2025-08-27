DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_decimal(s: str, base: int) -> int:
    if not (2 <= base <= 36):
        raise ValueError("from_base must be between 2 and 36")

    s = s.strip().upper()
    if s == "":
        raise ValueError("empty number")

    neg = s.startswith("-")
    if neg:
        s = s[1:]

    value = 0
    for ch in s:
        if ch not in DIGITS[:base]:
            raise ValueError(f"Invalid digit '{ch}' for base {base}")
        value = value * base + DIGITS.index(ch)

    return -value if neg else value

def from_decimal(n: int, base: int) -> str:
    if not (2 <= base <= 36):
        raise ValueError("to_base must be between 2 and 36")
    if n == 0:
        return "0"

    neg = n < 0
    n = abs(n)

    out = []
    while n > 0:
        out.append(DIGITS[n % base])
        n //= base

    if neg:
        out.append("-")

    return "".join(reversed(out))

def convert(number_str: str, from_base: int, to_base: int) -> str:
    return from_decimal(to_decimal(number_str, from_base), to_base)

def main():
    print("Number Converter (bases 2–36). Type 'q' anytime to quit.\n")
    while True:
        number = input("Enter number: ").strip()
        if number.lower() == "q":
            break
        fb = input("From base (2–36): ").strip()
        if fb.lower() == "q":
            break
        tb = input("To base (2–36): ").strip()
        if tb.lower() == "q":
            break

        try:
            fb = int(fb)
            tb = int(tb)
            result = convert(number, fb, tb)
            print(f"→ {number} (base {fb}) = {result} (base {tb})\n")
        except Exception as e:
            print("Error:", e, "\n")

if __name__ == "__main__":
    main()