#! -*- coding: utf-8 -*-
__author__ = 'kensuke-mi'


import unittest
from  src.frequency_summarizer import FrequencySummarizer
from src.mecab_wrapper.mecab_wrapper import MecabWrapper
from src.parsers.parser import Parser

class TestSummarizer(unittest.TestCase):

    def setUp(self):
        print ''

    """
    english mode is now un available
    def test_eng_freqsummarizer(self):
        original_sentences = u"Position information has been frequently used in\
        document summarization. It springs from\
        human’s tendency of writing sentences of\
        greater topic centrality at particular positions in\
        a document. For example, in newswire\
        documents, topic sentences are usually written\
        earlier.\n\n A sentence position hypothesis is then\
        given as: the first sentence in a document is the\
        most important and the importance decreases as\
        the sentence gets further away from the\
        beginning. Based on this sentence position\
        hypothesis, sentence position features are\
        defined by the ordinal position of sentences.\
        These position features have been proved to be\
        very effective in generic document\
        summarization. In more recent summarization\
        tasks, such as query-focused and update\
        summarization tasks, position features are also\
        widely used."

        from nltk.tokenize import sent_tokenize, word_tokenize



        fs = FrequencySummarizer()
        for paragraph in original_sentences.split(u'\n\n'):
            summarized = fs.summarize(paragraph, 2)
            for s in summarized:
                print s
            print u'='* 40
            """


    def test_japanese_summarizer(self):
        # input example
        document = u"AV女優（エーブイじょゆう）は、日本のアダルトビデオ（AV。内容はポルノビデオ）に出演する専門の女優である。非アダルト系メディア出演時にはセクシー女優と言い換えられることがある。本項は日本あるいは日本系の性的映像であるAVの女優について記述するため特記ない場合は日本における状況である。現在（2012時点）、一説には6000 - 8000人のAV女優がおり[1]、また一説には現在（2011年時点）、延べ20万人にものぼると言う[2]。 ※（一時期アダルトビデオに出演する女性を女優と呼ぶのは俳優に失礼だとの意見からAVギャルと呼称する人もいた。）\
        AV女優はビデオカメラの前で何らかの演技を要求されることも多いが、例えば映画やドラマの俳優などとは異なり、特別な演技訓練などを必要としない、誰にでも行えるものである[3]。ただし性的な表現をいかにこなすかについてはやはり大切なところであり、作品の出来にとって重要な要素であることは確かである[3]。例えば1985年頃人気を博したAV女優黒木香はアサヒ芸能のインタビューの中で、カメラの前で行っていることは自身にとってはセックスではなくパフォーマンスであると語ると同時に、あくまで性表現なのであって演技ではないとも語っている[4]。\
        現在（2012年時点）、AV女優はおおよそ「単体」、「企画単体」、「企画」に分類できる[5]。詳しくは後述する。女優のほとんどが本名以外の別名を女優名（芸名）にして出演している。出身地は架空のものである場合が多い[6]。\
        DVD化による作品の長時間化（VHS時代は一般的に1本40 - 60分、たまに90分の作品もあった。DVDでは1本90分から2時間、長いと3、4時間以上）、インターネットの普及（ファン同士の情報交換、オンラインストアの購入者による商品評価によって作品の評判がすぐ広まってしまう）が環境の変化としてあげられる。\
        インターネット利用者の拡大により、日本のAV女優は日本国内はもとより世界各国で人気も高い。アメリカ合衆国や台湾、韓国、中国などで大きな人気を集めている。これと同時にAV女優のアジア進出も進んでいる。\
        なお、性行為は原則としてコンドームを用いて行い[7]、村西 (2011)によれば、特記無き場合暗黙の了解として性行為は3回までとのことである[8]。なお、かつて多く見られていた疑似本番については後述する。\
        \n\n\
        ほとんどのAV女優はAV事務所（AVプロダクション）に所属しており[1]、マネージメントされる立場にある。一般的にAVメーカー（制作会社）からの出演依頼を取り付け、初めて撮影となり、収入が得られる。新人AV女優は仕事を得るためにマネージャーと共にメーカー回りをして、ようやく仕事（収入）が得られる[9]。このメーカー回りのことを業界用語では「面接回り」と言うが、一般的に言えば「オーディション」である。また、プロダクションはマネージメントだけでなく、撮影現場でのトラブルの解決も重要な仕事の一つである[10]。マネージメント料は相当な高額であり、村西 (2011) は折半としているが[11]、いのうえ (2012) では事務所7、女優3が多く中には折半もみられるとしており[12]、中村 (2012) は折半は良心的な方であり、60 - 70%はプロダクションに流れるとしている[9]。プロダクションから独立して独自にAVメーカーと契約することも可能ではあるが、適切な出演料を提示できなかったり、あるいは逆に買い叩かれてしまうなど困難が多い[13]。ただし企画女優においては長期間成功しているケースもみられる[13]。プロダクションはかつてに比べれば健全化しており、ギャラなどもある程度は明らかにされるようになってきているが[14]、ギャラの持ち逃げ[15]や、AV女優に偽って劣悪な撮影現場に送り出すなど[16]といった例もある。また過度のSMプレイにより刑事事件となったバッキー事件などもある[17]。\
        経済評論家の門倉貴史による「風俗産業で働く女性の時給ランキング（2006年版）」によると、風俗産業の中でもAV女優の時間あたりの給料が最も高い。トップは｢単体もの｣のAV出演で時給3万1000円～、｢単体もの｣で、1回のビデオ出演毎に、80万円～150万円程度のギャラを受け取ることが出来ると言う。撮影現場で拘束される時間は2日程度になるから、時給に換算すると、1万7000円～3万1000円程度。ただし、AV業界には、｢出れば出るだけ価値が下がる｣と言う法則があると言われる[18]。元AV女優の峰なゆか、小室友里も同様の指摘をしている[19][20]。 「職業としてのAV女優」の著者・中村淳彦によると、志望者数の増加などで競争率が上がっており、容姿や学歴など採用条件は厳しくなる一方、供給高状態で待遇は悪化傾向であり、企画女優では複数回の本番を行う場合でもプロダクションの取り分を引いた手取りが時給換算で2000円といった例も見られるようになった[21]。\
        前述の峰によれば、一時期と比べるとAV1作あたりの売上本数が減り、その制作費は下がっており、それに伴い真っ先にAV女優の出演料も低下している。ちなみに進行形で出演料は下がり続けているという。また、AV女優人口が増え1人あたりの仕事量が減ったことも背景として挙げている[19]。中村 (2012) によれば出演料は辛うじて横ばいであるものの、長引く不景気により作品のクオリティや内容の過激さが要求されるため、AV女優の仕事内容も以前より過酷となってきている[22]。\
        小室友里は、『くだまき八兵衛』の中でAV界の出演料の裏事情を明かしている。小室は現役時代に出演料のうち3分の2が所属事務所の取り分となっていた。前述の通り、AV女優は出演本数を重ねていくごとに出演料が減る。出演料が減額しても女優には毎月同額を支払えるように、事務所は減額分を補填しているのだ[20]。\
        かつては社会の底辺と言った扱いで女性にとって最後の手段とも取られていたこのAV女優と言う職業[23]は、近年そのネガティブイメージは薄まってきており、業界も健全化してきていると言う[24]。それに伴いAV女優志願者も増え、AV女優の質は概して向上してきている[25]。それに伴い競争率も高くなり、かつてままみられた精神疾患・人格障害、あるいは幼少期の（性的）虐待経験などを持つAV女優[26]を起用する例は少なくなってきているという[27]。ただし、自身及び家族の生活費や弟妹の学資等を稼ぐためにAV女優となる者は存在する。\
        AV女優が所属事務所を変更して芸能活動を継続・再開させる場合、それまで使用していた芸名は使えない（芸名変更）という慣例がある[28]。"

        pathUserDictCsv="../resources/termExtractDict.csv"
        pathNeologd="/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
        osType="mac"
        mecab_wrapper = MecabWrapper(dictType='neologd', osType=osType, pathNeologd=pathNeologd)

        parser_obj = Parser(document=document, mecabTokenizer=mecab_wrapper)
        documentObj = parser_obj.make_document()

        fs = FrequencySummarizer(language='ja', documentObj=documentObj)
        n_sentence = 3
        summarized = fs.summarize(n=n_sentence)
        for summarized_sent in summarized:
            assert len(summarized_sent) == n_sentence
            for s in summarized_sent:
                print s
            print u'-'*30

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSummarizer))

    return suite