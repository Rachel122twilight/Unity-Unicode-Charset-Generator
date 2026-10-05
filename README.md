# Unity-Unicode-Charset-Generator

[中文](https://github.com/Rachel122twilight/Unity-Unicode-Charset-Generator/blob/main/README_cn.md)

> A collection of Python scripts for generating Unicode charset text files for Unity font atlases.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Introduction

When creating a font atlas in Unity, you usually need to specify which characters to include. Manually collecting characters is both tedious and prone to omissions.

This repository provides three lightweight Python scripts to generate UTF-8 (no BOM) character text files for different scenarios. These files can be used directly in Unity's native font or TextMeshPro font asset creation workflows.

## Features

| Script | Description | Default Output |
|--------|-------------|----------------|
| `uniall.py` | Generates all assigned Unicode characters, skipping surrogates and excluding unassigned `Cn` and private use `Co`. Suitable for reference or dynamic fallback. | `all_unicode_chars_full.txt` |
| `unicommon.py` | Generates ASCII, common Chinese punctuation, CJK Unified Ideographs, Extension A, and CJK Compatibility Ideographs. Suitable for Chinese projects. | `unity_all_chinese_chars.txt` |
| `unispecial.py` | Generates arrows, miscellaneous symbols, dingbats, Emoji, and other special symbols. Suitable for UI icons and prompt symbols. | `unity_symbols.txt` |

## Requirements

- Python 3.8+
- No third-party dependencies; uses the standard library `unicodedata`

> Note: The output character set depends on the Unicode database version bundled with the current Python installation.

## Usage

```bash
# All Unicode characters (not recommended for direct use in static atlases)
python uniall.py

# Common Chinese + ASCII + Chinese punctuation
python unicommon.py

# Special symbols and Emoji
python unispecial.py
```

After running, the corresponding `.txt` files will be generated in the current directory.

## Using in Unity

1. Run a script to generate the `.txt` character file.
2. Open Unity.
3. For TextMeshPro:
   - `Window > TextMeshPro > Font Asset Creator`
   - Set `Character Set` to `Characters from File`
   - Select the generated `.txt` file
   - Adjust Atlas Resolution, Padding, Packing Mode, etc. as needed
4. For Unity's native font atlas:
   - Use `Custom Characters` in the font asset creation interface or import the character set from a file
5. It is recommended to configure Fallback fonts for different character sets to avoid oversized atlases.

## Customization

You can directly modify the ranges and additional characters in the scripts:

```python
# unicommon.py
cjk_ranges = [
    (0x4E00, 0x9FFF),  # CJK Unified Ideographs
    (0x3400, 0x4DBF),  # CJK Extension A
    (0xF900, 0xFAFF),  # CJK Compatibility Ideographs
]
```

```python
# unispecial.py
symbol_ranges = [
    (0x2190, 0x21FF),  # Arrows
    (0x2600, 0x26FF),  # Miscellaneous Symbols
    (0x2700, 0x27BF),  # Dingbats
]
```

You can also modify `extra_chars` to add project-specific symbols.

## Notes

- `all_unicode_chars_full.txt` is very large and may contain control/format characters. It is not recommended for direct use in static font atlases, as it may cause Unity to lag or crash.
- Full CJK character sets generate very large atlases with high VRAM usage. It is advisable to trim them based on the actual characters used in your project.
- The font file must support the corresponding characters; otherwise, blank spaces or squares will appear in the atlas.
- Emoji support in Unity/TextMeshPro depends on the font, render pipeline, and plugins. Color Emoji typically requires additional solutions.
- The output encoding is UTF-8 without BOM.
- The generated `.txt` files are generally not recommended for committing to Git repositories, unless you need to provide examples.

## Contributing

Issues and Pull Requests are welcome.

## License

This project is open-sourced under the [MIT License](LICENSE).
