# Unity-Unicode-Charset-Generator
> 为 Unity 字体图集生成 Unicode 字符集文本文件的 Python 脚本集合。

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 简介

在 Unity 中制作字体图集时，通常需要指定要包含的字符。手动收集字符既繁琐又容易遗漏。

本仓库提供三个轻量级 Python 脚本，用于按不同场景生成 UTF-8 无 BOM 的字符文本文件，可直接用于 Unity 原生字体或 TextMeshPro 的字体资源创建流程。

## 功能

| 脚本 | 说明 | 默认输出 |
| --- | --- | --- |
| `uniall.py` | 生成所有 Unicode 已分配字符，跳过代理区，排除未分配 `Cn` 和私用 `Co`。适合参考或动态回退。 | `all_unicode_chars_full.txt` |
| `unicommon.py` | 生成 ASCII、常用中文标点、CJK 基本区、扩展 A、兼容表意文字。适合中文项目。 | `unity_all_chinese_chars.txt` |
| `unispecial.py` | 生成箭头、杂项符号、装饰符号、Emoji 等特殊符号。适合 UI 图标和提示符号。 | `unity_symbols.txt` |

## 环境要求

- Python 3.8+
- 无需第三方依赖，使用标准库 `unicodedata`

> 注意：输出字符集取决于当前 Python 所带的 Unicode 数据库版本。

## 使用方法

```bash
# 全量 Unicode 字符（不推荐直接用于静态图集）
python uniall.py

# 常用中文 + ASCII + 中文标点
python unicommon.py

# 特殊符号与 Emoji
python unispecial.py
```

运行后会在当前目录生成对应的 `.txt` 文件。

## 在 Unity 中使用

1. 运行脚本生成 `.txt` 字符文件。
2. 打开 Unity。
3. 对于 TextMeshPro：
   - `Window > TextMeshPro > Font Asset Creator`
   - `Character Set` 选择 `Characters from File`
   - 选择生成的 `.txt` 文件
   - 根据需求调整 Atlas Resolution、Padding、Packing Mode 等参数
4. 对于 Unity 原生字体图集：
   - 在字体资源创建界面中使用 `Custom Characters` 或从文件导入字符集
5. 建议为不同字符集配置 Fallback 字体，避免单个图集过大。

## 自定义

你可以直接修改脚本中的范围与附加字符：

```python
# unicommon.py
cjk_ranges = [
    (0x4E00, 0x9FFF),   # CJK 统一表意文字基本区
    (0x3400, 0x4DBF),   # CJK 扩展 A
    (0xF900, 0xFAFF),   # CJK 兼容表意文字
]
```

```python
# unispecial.py
symbol_ranges = [
    (0x2190, 0x21FF),   # 箭头
    (0x2600, 0x26FF),   # 杂项符号
    (0x2700, 0x27BF),   # 装饰符号
]
```

也可以修改 `extra_chars` 添加项目专用符号。

## 注意事项

- `all_unicode_chars_full.txt` 体积很大，且可能包含控制字符/格式字符，不建议直接用于静态字体图集，否则可能导致 Unity 卡顿或崩溃。
- CJK 全量字符会生成非常大的图集，显存占用高。建议按项目实际用字裁剪。
- 字体文件必须支持对应字符，否则图集中会出现空白或方块。
- Emoji 在 Unity/TextMeshPro 中的支持取决于字体、渲染管线和插件，彩色 Emoji 通常需要额外方案。
- 输出编码为 UTF-8 无 BOM。
- 生成的 `.txt` 文件通常不建议提交到 Git 仓库，除非你需要提供示例。

## 贡献

欢迎提交 Issue 和 Pull Request。

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
