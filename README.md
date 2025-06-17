# factorio-wiki-translation-helper

[ [English](README.md) | [日本語](README.ja.md) ]

A tools to support translating the Factorio Wiki.

It replaces internal links in English pages with links to the corresponding pages in the target language, based on the contents of a previously downloaded template file.

## Example

```diff
- [[express transport belt]]
+ [[express transport belt/ja|超高速搬送ベルト]]

- [[belt transport system|transport belts]]
+ [[belt transport system/ja|ベルト輸送]]
```

## Usage

1. Download the template file for translation from:
   [https://wiki.factorio.com/index.php?title=Template\:Translation/ja\&action=edit](https://wiki.factorio.com/index.php?title=Template:Translation/ja&action=edit)

   Replace `ja` in the URL with the language code of the target language you want to translate into.

2. Save the content of the English page you want to translate as a text file.

3. Run `translate_tool.py` with the following command:

   ```shell
   python translate_tool.py <template_file> <language_code> <target_file>
   ```

4. During execution, a log will show what replacements have been made.

   * Replacements will appear at two log levels: `INFO` and `WARNING`.
   * If the original internal link has a link text (i.e., a custom label), it will be logged at the `WARNING` level.
   * If not, it will be logged at the `INFO` level.
   * Be careful with `WARNING` entries, as the original link text will be overwritten.

5. After execution, the content of the input file will be modified.
   The original content will be saved as a `.bak` file.
