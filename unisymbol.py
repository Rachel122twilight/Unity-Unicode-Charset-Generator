import unicodedata

def generate_symbol_char_file(output_path, include_ascii=False, extra_chars=""):
    symbol_ranges = [
        (0x00A0, 0x00FF),   # 拉丁-1 补充
        (0x2000, 0x206F),   # 常用标点
        (0x20A0, 0x20CF),   # 货币符号
        (0x2100, 0x214F),   # 字母式符号
        (0x2190, 0x21FF),   # 箭头
        (0x2200, 0x22FF),   # 数学运算符
        (0x2300, 0x23FF),   # 杂项技术符号
        (0x2500, 0x257F),   # 制表符
        (0x25A0, 0x25FF),   # 几何图形
        (0x2600, 0x26FF),   # 杂项符号（★☆☎☕等）
        (0x2700, 0x27BF),   # 装饰符号（✏✂✅等）
        (0x2B00, 0x2BFF),   # 杂项符号和箭头
        (0x1F300, 0x1F5FF), # 杂项符号和象形文字
        (0x1F600, 0x1F64F), # Emoji 表情
    ]

    chars = []

    if include_ascii:
        for cp in range(0x0020, 0x007F):
            chars.append(chr(cp))

    chars.extend(extra_chars)

    for start, end in symbol_ranges:
        for cp in range(start, end + 1):
            ch = chr(cp)
            category = unicodedata.category(ch)
            if category not in ('Cn', 'Co', 'Cs'):
                chars.append(ch)

    seen = set()
    unique_chars = []
    for c in chars:
        if c not in seen:
            seen.add(c)
            unique_chars.append(c)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(unique_chars))

    print(f"Finished! Output path: {output_path}")
    print(f"Total Characters: {len(unique_chars)}")
    for start, end in symbol_ranges:
        count = sum(
            1 for cp in range(start, end + 1)
            if unicodedata.category(chr(cp)) not in ('Cn', 'Co', 'Cs')
        )
        print(f"  U+{start:04X} - U+{end:04X}: {count} 个字符")


if __name__ == "__main__":
    common_symbols = "©®™§¶°±×÷µ£¥€¢←↑→↓↔↕★☆♠♣♥♦♪♫☀☁☂☃☎☏☑☒✓✔✗✘❤❥❦❧※†‡•‣⁃"

    generate_symbol_char_file(
        output_path="unity_symbols.txt",
        include_ascii=False,
        extra_chars=common_symbols
    )
