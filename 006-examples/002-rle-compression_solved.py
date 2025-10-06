
def validate_string(s):
    for ch in s:
        if not ch.isalpha():
            return False

    return True


def rle_encode(s):
    if s == "":
        return ""

    if not validate_string(s):
        raise ValueError(
            "Invalid input: only letters A-Z or a-z are allowed")

    out = ""
    current = s[0]
    count = 1

    for ch in s[1:]:
        if ch == current:
            count += 1
        else:
            out += f"{current}{count}"
            current = ch
            count = 1

    out += f"{current}{count}"

    return out


def compression_ratio(original, compressed):
    if len(original) == 0:
        return 1.0

    return round(len(compressed) / len(original), 2)


def rle_decode(encoded):
    i = 0
    n = len(encoded)
    out = ""

    while i < n:
        ch = encoded[i]

        if not ch.isalpha():
            raise ValueError("Invalid encoding: expected a letter")

        i += 1
        if i >= n or not encoded[i].isdigit():
            raise ValueError(
                "Invalid encoding: expected count digits after letter")

        digits_str = ""
        while i < n and encoded[i].isdigit():
            digits_str += encoded[i]
            i += 1

        try:
            count = int(digits_str)
        except ValueError:
            raise ValueError(
                "Invalid encoding: expected integer count after letter")

        out += ch * count

    return out


def first_diff_index(a, b) -> int:
    m = min(len(a), len(b))

    for i in range(m):
        if a[i] != b[i]:
            return i

    if len(a) != len(b):
        return m

    return -1


samples = [
    "aaabbbbccaaaaA",
    "aahhhhhhhhhhhhsivaaaa",
    "abAB",
    "AAAAA123",
    "zzzzzzzzzz",
    "A",
    "",
]

print("RLE Compression\n")

for s in samples:
    print(f"input: {s}")

    try:
        encoded = rle_encode(s)
        decoded = rle_decode(encoded)
        ratio = compression_ratio(s, encoded)
        diff_idx = first_diff_index(s, decoded)
        ok = diff_idx == -1

        print(f"encoded: {encoded}")
        print(f"decoded: {decoded}")
        print(f"ratio: {ratio}")
        print(f"ok: {ok}{'' if ok else f' (first diff at index {diff_idx})'}")
        print()
    except ValueError as e:
        print(f"error: {e}")
        print()
