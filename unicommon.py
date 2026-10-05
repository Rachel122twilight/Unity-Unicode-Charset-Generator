import unicodedata

def generate_unity_char_file(output_path, ranges, include_ascii=True, extra_chars=""):
    chars = []
    if include_ascii:
        for cp in range(0x0020, 0x007F):
            chars.append(chr(cp))

    chars.extend(extra_chars)
    for start, end in ranges:
        for cp in range(start, end + 1):
            ch = chr(cp)
            category = unicodedata.category(ch)
            # 跳过未分配(Cn)、私用(Co)、代理(Cs)等无效字符
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

if __name__ == "__main__":
    chinese_punctuation = "，。！？；：“”‘’【】《》〈〉、·—…～￥（）％＋－×÷＝＃＠＆＊"
    
    # 定义要包含的 Unicode 范围
    # 注意：范围越大，生成图集越困难，建议根据实际需求裁剪。
    cjk_ranges = [
        (0x4E00, 0x9FFF),   # CJK 统一表意文字基本区（20992 字）
        (0x3400, 0x4DBF),   # CJK 扩展 A（6582 字）
        (0xF900, 0xFAFF),   # CJK 兼容表意文字（472 字）
        # 如需扩展 B 及以后，可取消注释，但字体通常不支持，且图集会炸
        # (0x20000, 0x2A6DF), # 扩展 B
    ]
    
    generate_unity_char_file(
        output_path="unity_all_chinese_chars.txt",
        ranges=cjk_ranges,
        include_ascii=True,
        extra_chars=chinese_punctuation
    )
