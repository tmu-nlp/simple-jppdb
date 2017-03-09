# Simple PPDB: Japanese
日本語のテキスト平易化のために利用可能な2つの大規模な辞書を構築しました。
Wikipediaから得られる統計情報をもとに、日本語の各単語に[日本語教育語彙表](http://jhlee.sakura.ne.jp/JEV.html)に由来する3段階の難易度（初級・中級・上級）を付与しました。

##1. 単語難易度辞書 (word-level-japanese)
57万単語について`単語 <TAB> 難易度`の情報を収録しました。
ただし、難易度は1が初級、2が中級、3が上級を意味します。
Wikipediaの本文を[MeCab](http://taku910.github.io/mecab/)と[mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)で分割したものを単語とし、出現頻度が5回以上の単語を対象としました。

##2. 平易な言い換え辞書 (simple-ppdb-japanese)
34万単語対について`言い換え確率 <TAB> 難解な単語 <TAB> 平易な単語 <TAB> 難解な単語の難易度 <TAB> 平易な単語の難易度`の情報を収録しました。
ただし、難易度は1が初級、2が中級、3が上級を意味します。
[PPDB: Japanese（日本語言い換えデータベース）](http://ahclab.naist.jp/resource/jppdb/)のうち、上記の単語難易度辞書に掲載されている単語のみからなる言い換え対を対象としました。

## 注意事項
[日本語教育語彙表](http://jhlee.sakura.ne.jp/JEV.html)に掲載されている単語難易度の情報は?に置換して隠しています。
日本語教育語彙表の利用規約に同意できる場合は、まず日本語教育語彙表をダウンロードしてください。
`python complement.py /path/to/日本語教育語彙表.csv`を実行すると、すべての情報が補完されます。

## 参考文献
梶原智之, 小町守. Simple PPDB: Japanese. 言語処理学会第23回年次大会, P8-5, pp.529-532, 2017.

## ライセンス
[Creative Commons Attribution Share-Alike License](http://creativecommons.org/licenses/by-sa/3.0/)での利用が可能です。
ただし、[日本語教育語彙表](http://jhlee.sakura.ne.jp/JEV.html)の単語難易度の情報を使う場合は、日本語教育語彙表のライセンスをご確認ください。

For questions, please contact [Tomoyuki Kajiwara at Tokyo Metropolitan University](https://sites.google.com/site/moguranosenshi/).