import unicodedata

def generate_symbol_char_file(output_path, include_ascii=False, extra_chars=""):
    """
    生成包含常用特殊符号的 Unity 字符文件。
    包含：箭头、杂项符号、装饰符号、Emoji 等。
    """
    symbol_ranges = [
        (0x2190, 0x21FF),   # 箭头 Arrows
        (0x2600, 0x26FF),   # 杂项符号 Miscellaneous Symbols（★☆☎☕等）
        (0x2700, 0x27BF),   # 装饰符号 Dingbats（✏✂✅等）
        (0x2B00, 0x2BFF),   # 杂项符号和箭头 Miscellaneous Symbols and Arrows
        (0x1F300, 0x1F5FF), # 杂项符号和象形文字 Miscellaneous Symbols and Pictographs
        (0x1F600, 0x1F64F), # Emoji 表情 Emoticons
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
            # 跳过未分配(Cn)、私用(Co)、代理(Cs)
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
    # 额外的常用符号
    extra_symbols = "★☆♠♣♥♦♪♫☀☁☂☃☎☏☑☒✓✔✗✘❤❥❦❧※§¶†‡•‣⁃←↑→↓↔↕"

    generate_symbol_char_file(
        output_path="unity_symbols.txt",
        include_ascii=False,   # 符号文件通常不需要 ASCII，可按需开启
        extra_chars=extra_symbols
    )
