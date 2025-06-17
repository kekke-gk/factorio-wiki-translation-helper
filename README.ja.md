# factorio-wiki-translation-helper

[ [English](README.md) | [日本語](README.ja.md) ]

Factorio Wikiの翻訳作業をサポートするツールです。

事前にダウンロードしたテンプレートファイルの内容にしたがって、英語ページ内にある内部リンクを日本語ページへのリンクに置換します。

## 実行例

```diff
- [[express transport belt]]
+ [[express transport belt/ja|超高速搬送ベルト]]

- [[belt transport system|transport belts]]
+ [[belt transport system/ja|ベルト輸送]]
```

## 使い方

1. 翻訳用のテンプレートファイルを https://wiki.factorio.com/index.php?title=Template:Translation/ja&action=edit からダウンロードします。ただし、`ja`の部分は翻訳したい言語によって変更します。
2. 翻訳したい英語ページの内容をテキストファイルとして保存します。
3. `translate_tool.py`を以下のように実行します。

    ```shell
    python translate_tool.py <テンプレートファイル> <言語コード> <対象ファイル>
    ```

4. 実行中はどのような置換が実行されたかが、`INFO`と`WARNING`の2つのレベルのログで表示されます。置換元の内部リンクがリンクテキストを持っていたら`WARNING`レベル、持っていなければ`INFO`レベルで出力されます。`WARNING`の場合は元々のリンクテキストを上書きすることになるので注意が必要です。
5. 実行が完了すると、入力したテキストファイルの内容が変更され、変更前の内容は`.bak`ファイルとして保存されます。
