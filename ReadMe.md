# What's this?

ウルトラ簡易テキスト要約システムです。

要約と言っているけど、実際は、「段落中でもっとも段落中の単語を含む」文を探索するだけです。

# 類似プロジェクト

類似というか、かなり進んでいるプロジェクトの紹介です。

* [sumy](https://github.com/miso-belica/sumy)

本リポジトリの段落データモデルはsumyを参考にして作りました。


# インストール

```
[sudo] python setup.py install
```

でインストールできます。

## 依存パッケージ

Mecab本体とMecab-pythonパッケージに依存します。

この２つは手動インストールしなくてはいけません。がんばってください。


# 使いかた

```
#! -*- coding: utf-8 -*-


from  src.frequency_summarizer import FrequencySummarizer
from src.mecab_wrapper.mecab_wrapper import MecabWrapper
from src.parsers.parser import Parser

# input example
# wikipedia https://ja.wikipedia.org/wiki/AV%E5%A5%B3%E5%84%AA より作成
document = u"AV女優（エーブイじょゆう）は、日本のアダルトビデオ（AV。内容はポルノビデオ）に出演する専門の女優である。非アダルト系メディア出演時にはセクシー女優と言い換えられることがある。本項は日本あるいは日本系の性的映像であるAVの女優について記述するため特記ない場合は日本における状況である。現在（2012時点）、一説には6000 - 8000人のAV女優がおり[1]、また一説には現在（2011年時点）、延べ20万人にものぼると言う[2]。 ※（一時期アダルトビデオに出演する女性を女優と呼ぶのは俳優に失礼だとの意見からAVギャルと呼称する人もいた。）\
\n\n\
AV女優はビデオカメラの前で何らかの演技を要求されることも多いが、例えば映画やドラマの俳優などとは異なり、特別な演技訓練などを必要としない、誰にでも行えるものである[3]。ただし性的な表現をいかにこなすかについてはやはり大切なところであり、作品の出来にとって重要な要素であることは確かである[3]。例えば1985年頃人気を博したAV女優黒木香はアサヒ芸能のインタビューの中で、カメラの前で行っていることは自身にとってはセックスではなくパフォーマンスであると語ると同時に、あくまで性表現なのであって演技ではないとも語っている[4]。\
\n\n\
現在（2012年時点）、AV女優はおおよそ「単体」、「企画単体」、「企画」に分類できる[5]。詳しくは後述する。女優のほとんどが本名以外の別名を女優名（芸名）にして出演している。出身地は架空のものである場合が多い[6]。\
DVD化による作品の長時間化（VHS時代は一般的に1本40 - 60分、たまに90分の作品もあった。DVDでは1本90分から2時間、長いと3、4時間以上）、インターネットの普及（ファン同士の情報交換、オンラインストアの購入者による商品評価によって作品の評判がすぐ広まってしまう）が環境の変化としてあげられる。\
\n\n\
インターネット利用者の拡大により、日本のAV女優は日本国内はもとより世界各国で人気も高い。アメリカ合衆国や台湾、韓国、中国などで大きな人気を集めている。これと同時にAV女優のアジア進出も進んでいる。\
\n\n\
なお、性行為は原則としてコンドームを用いて行い[7]、村西 (2011)によれば、特記無き場合暗黙の了解として性行為は3回までとのことである[8]。なお、かつて多く見られていた疑似本番については後述する。"

# mecabの設定をここでやってください
pathUserDictCsv="../resources/termExtractDict.csv"
pathNeologd="/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
osType="mac"
mecab_wrapper = MecabWrapper(dictType='neologd', osType=osType, pathNeologd=pathNeologd)

parser_obj = Parser(document=document, mecabTokenizer=mecab_wrapper)
documentObj = parser_obj.make_document()

fs = FrequencySummarizer(language='ja', documentObj=documentObj)
n_sentence = 1
summarized = fs.summarize(n=n_sentence)
for summarized_sent in summarized:
    for s in summarized_sent: print s
```

これを実行すると、こんな結果が帰ってきます。

```
※（一時期アダルトビデオに出演する女性を女優と呼ぶのは俳優に失礼だとの意見からAVギャルと呼称する人もいた
例えば1985年頃人気を博したAV女優黒木香はアサヒ芸能のインタビューの中で、カメラの前で行っていることは自身にとってはセックスではなくパフォーマンスであると語ると同時に、あくまで性表現なのであって演技ではないとも語っている[4]
DVDでは1本90分から2時間、長いと3、4時間以上）、インターネットの普及（ファン同士の情報交換、オンラインストアの購入者による商品評価によって作品の評判がすぐ広まってしまう）が環境の変化としてあげられる
インターネット利用者の拡大により、日本のAV女優は日本国内はもとより世界各国で人気も高い
なお、性行為は原則としてコンドームを用いて行い[7]、村西 (2011)によれば、特記無き場合暗黙の了解として性行為は3回までとのことである[8]
```

# 探索アルゴリズムについて

ざっくり解説すると
* 各段落で単語の一覧を作成する
* 段落内で、もっとも多くの単語を含む文を探し、ランキングにする
* ランキング順に表示する

これだけです。

メイン部分は[この記事](http://glowingpython.blogspot.jp/2014/09/text-summarization-with-nltk.html)から流用しています。