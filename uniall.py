import unicodedata
import sys

def generate_all_unicode_chars(output_path):
    chars = []
    # Unicode 最大码点为 0x10FFFF，但大部分区域未分配。
    # 遍历所有有效码点，跳过代理对区域。
    for cp in range(0x0000, 0x110000):
        # 跳过代理对区域 (U+D800 - U+DFFF)
        if 0xD800 <= cp <= 0xDFFF:
            continue
        try:
            ch = chr(cp)
            # 过滤掉未分配(Cn)、私用(Co)字符
            category = unicodedata.category(ch)
            if category in ('Cn', 'Co'):
                continue
            chars.append(ch)
        except ValueError:
            continue
    
    # 去重并写入（UTF-8 无 BOM）
    unique_chars = list(dict.fromkeys(chars))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(''.join(unique_chars))
    
    print(f"Finished! Output path: {output_path}")
    print(f"Total Characters: {len(unique_chars)}")
    print("WARNING! This file is only recommended for reference or dynamic fallback. Using it directly for static atlas generation may cause Unity to crash.")

if __name__ == "__main__":
    generate_all_unicode_chars("all_unicode_chars_full.txt")
