# 簡易文章洗稿工具 ( Article Spinner)

## 簡介
您可以透過以下Colab筆記本直接使用本工具:
- 初版: https://colab.research.google.com/drive/1O5DQT4_gSuBc3uh6tQHkYGnHv3sEzhP9
  
這是一個基於Python的文章洗稿工具，透過Word2Vec模型和中文分詞技術，能夠智慧替換文章中的關鍵字，產生相似但不完全相同的內容。該工具特別適用於內容創作者、SEO優化和文章改寫需求。
***此為期末專案，功能較不完善，僅做學術與娛樂用途。***

## 使用的語言模型

本工具使用北醫大學 (TMU) 自然語言處理實驗室開發的「語詞等級之預訓練詞嵌入模型」:
- 模型連結: [https://nlp.tmu.edu.tw/word2vec/index.html](https://nlp.tmu.edu.tw/word2vec/index.html)
- 模型說明: 此模型針對中文語言最佳化，提供高品質的詞向量表示

## 功能特點

- 基於Word2Vec模型進行相似詞替換
- 可調節替換詞的相似度閾值
- 可控修改幅度百分比
- 直觀顯示修改前後的文章對比

## 安裝需求

```bash
pip install gensim
pip install opencc-python-reimplemented
pip install jieba
```

## 使用方法

1. 下載TMU NLP實驗室的Word2Vec模型檔案並放置於指定位置
2. 配置模型路徑：`model = gensim.models.KeyedVectors.load_word2vec_format('路徑/qqqq.model.bin', unicode_errors='ignore', binary=True)`
3. 設定參數：
 - `turnout`: 詞語相似度閾值(預設0.7)
 - `spread`: 修改幅度上限(預設0.25)
4. 執行程式並輸入需要改寫的文章內容

## 參數說​​明

- **turnout**: 控制替換詞的相似度閾值，值越高替換的詞語越相似
- **spread**: 控製文章的修改幅度百分比，數值越高修改越多

## 使用範例
### 輸入
```python
有對老夫妻年逾五十，經濟條件不錯，理當是安享退休生活的時候，卻相偕到律師那兒要辦離婚。原因是自從結婚以來，兩人爭吵不斷，老是意見不合，個性上又南轅北轍十分不和諧， 二十多年的婚姻生活，要不是為了孩子著想，早就勞燕紛飛了。  好不容易總算盼到孩子們成年，再不需要父母操心，為了讓彼此在晚年能自由的生活，
不用再忍受那麼多無謂的爭吵，決定辦離婚。  這一刻在律師面前，讓律師也面有難色，律師費都有點不好意思收了，  於是他提議辦完手續後，三人一起吃頓飯。老夫妻想了想，雖然離了婚，兩人又沒什麼深仇大恨，吃頓飯總可以吧！
餐廳裡三人氣氛非常尷尬（想也難怪，陌生的律師和兩個剛離婚的人）。正巧服務生送來一道烤雞，老先生馬上挾起一塊雞腿給老太太說： 「吃吧！你最喜歡吃的雞腿。」  律師眼精一亮，心想事情也許有了轉機哦！  未料老太太紅著雙眼說：「我很愛你，但你這個人就愛自以為是，什麼事都自己說了就算，
從來不管別人的感受，難道你不知道，我這輩子最討厭吃的就是雞腿嗎？」  這時老先生也有點哽咽的說：「你．．．總是不了解我愛你的心，時時刻刻我都在想， 要如何討你的歡心，總是把最好的留給你，你知道嗎？  這輩子我最喜歡吃的就是．．．雞腿。」  律師看在眼裡，不免鼻頭一酸，兩個如此深愛著彼此的人，
卻因為溝通出了問題而面臨分開的局面。  這一晚兩人心中都有著無限的感慨，這麼多年的感情卻要面對如此殘酷的結局。  老先生整晚翻來覆去睡不著，心中陣陣如火燃燒般的痛在心底無情的煎熬著。他考慮了很久，強忍著痛苦打電話給老太太，想要表達他內心的後悔， 他想告訴老太太，他是多麼的愛她。
電話聲響了，老太太知道一定是老先生打來的，但是她心中充滿了恨，  她覺得是老先生負了她一生，她不想再聽到他的聲音。電話不知響了多久，老太太就是不接，婚都離了，面子重要，怎能接電話， 甚至她把電話線都拆了。
老先生手握著冰冷的話筒，聽不到老太太的聲音，心中有如刀割一般，久久無法釋懷。其實這一天晚上老太太也是在傷心中輾轉難眠，而且她忘了．．．老先生他有心臟病。  隔天，老先生被發現死在自已家客廳，手裡還緊握著電話筒。  老太太知道這個消息後簡直無法相信，為了賭一口氣，竟然讓自己深愛的人在心碎中死去，
這時候任她如何大聲的呼喊也喚不回老先生的回眸一笑。  老太太柔腸寸斷的整理老先生的遺物，突然發現抽屜裡的一張保險單，  投保日期就是當年他們倆的結婚日，受益人當然是老太太的名字，雖然金額只有一佰萬元， 但是當中夾著一張字條－－
「親愛的，當你發現這張保單時，也許我已經不在這人世了，但我愛你的心不會改變， 照顧你的責任更不會終止，這些保險金將代替我，繼續給你無微不至的愛與關懷， 一如我仍然在你身旁，永遠愛你的．．．」  看到這裡老太太早已淚如雨下，她真的沒看走眼，他是真心願意照顧自已一輩子的人。
千萬不要讓生命中有這樣的遺憾，早早放下心中無謂的面子、成見，用愛與包容， 真心的對待，否則你可能錯過這一生深愛你的人最後一次所說的：「我愛你！」到時再多的悔恨也無法挽回這樣的遺憾。
更提醒您，要把握住機會，讓心愛的人知道你有多在乎她，勇敢的說出來吧！假若你真的說不出「我愛你」這三個字，只要你用心，總有一天她終會了解的。

```
### 分析
```python
老婆婆 0.9188786149024963
雞翅 0.8986236453056335
律師團 0.8173761963844299
不平凡 0.7165327668190002
分手 0.8922234177589417
仰慕 0.7917875051498413
曉得 0.8906570672988892
不必要 0.8908231258392334
自己 0.8643238544464111
夜宵 0.8249589204788208
父女 0.7248302698135376
爭執 0.9398536682128906
真誠 0.8223602175712585
裡子 0.7264276146888733
惋惜 0.8327012658119202
是 0.8551662564277649
照料 0.7810742855072021
分飛 0.8337294459342957
Jaspp 0.7166228294372559
互相 0.9120839834213257
鄭恩 0.7484172582626343
訂婚 0.8709983825683594
發覺 0.8264264464378357
人生 0.8135207295417786
張照 0.71079021692276
舀進 0.7456400394439697
眼晴 0.716331422328949
不料 0.9524697661399841
制於 0.7336809635162354
3823萬 0.8615784049034119
熱線 0.8167982697486877
訴訟費 0.8521071076393127
現烤 0.8695183992385864
侍者 0.8715914487838745
第二天 0.9121532440185547
話筒 0.7900850176811218
偏愛 0.7905985116958618
更盟 0.7122007608413696
卻 0.7359343767166138
實在 0.8941600918769836
太 0.8426709175109863
整夜 0.7216288447380066
或許 0.9643462300300598
保證書 0.7627495527267456
忘懷 0.7957392334938049
大不相同 0.8274942636489868
頤養 0.8230069875717163
難以 0.8810994029045105
終將 0.7933441400527954
聲響 0.7810978889465332
舒心 0.772315263748169
網路線 0.855282723903656
飄落 0.8244326114654541
小孩 0.8888149261474609
噴淚 0.7605851292610168
繼承人 0.7791741490364075
了解 0.9748266935348511
顴骨 0.8260535001754761
澎拜 0.7227017283439636
絕望 0.8438405394554138
恰巧 0.9057871103286743
清高 0.7379544377326965
保額 0.8389978408813477
然而 0.7438419461250305
時時 0.8468157052993774
理應 0.7516596913337708
蒼翠山 0.7208415865898132
偏見 0.8136572241783142
壽險 0.8230671882629395
紙條 0.8989315032958984
怎樣 0.8356188535690308
怨恨 0.8530154228210449
芳心 0.7028205990791321
打過去 0.7862455248832703
寬容 0.8575817942619324
掌握住 0.8653125762939453
去辦 0.8028457760810852
忍著 0.7734946012496948
麥克風 0.8054083585739136
假使 0.8303011655807495
在意 0.8981719613075256
折磨 0.8602111339569092
櫃子 0.9509977102279663
承保 0.8694785237312317
不至於 0.8928521871566772
為之一亮 0.8167832493782043
數年里 0.7393890619277954
離世 0.7456066012382507
摯愛 0.7427828311920166
關愛 0.8066178560256958
儘管 0.8650476932525635
常常 0.7059000730514526
猶如 0.9643808007240295
餐館 0.9250268936157227
手稿 0.8239649534225464
一陣陣 0.8840038180351257
蒼白 0.7577139735221863
但 0.924171507358551
依歸 0.7445711493492126
高呼 0.8556896448135376
小看 0.7156545519828796
打給 0.8420305252075195
四十 0.9817777276039124
高血壓 0.88443922996521
睡不著覺 0.9052262306213379
痛恨 0.8716013431549072
邪惡 0.8034469485282898
一清二楚 0.7335363030433655
相左 0.7636154890060425
淚流滿面 0.8608664870262146
熱誠 0.7642127871513367
趕著 0.7345274686813354
豈能 0.8440055847167969
承受 0.8527333736419678
臥室 0.8633702397346497
怪不得 0.8112710118293762
成年人 0.7672233581542969
內心 0.7951148748397827
關頭 0.7333523035049438
提案 0.7244804501533508
眼角 0.8431395888328552
終於 0.8211145401000977
苛責 0.7809733748435974
熟悉 0.8489698767662048
身邊 0.8761498332023621
劇情 0.7062088251113892
留下來 0.727564811706543
入職 0.7858092784881592
勇氣 0.793412446975708
這樣子 0.8305128812789917
感嘆 0.9034942388534546
響聲 0.8981431722640991
歹勢 0.8383806943893433
終老 0.7885191440582275
暖意 0.7043383717536926
難過 0.9217855930328369
太久 0.7010933756828308
性格 0.9095984697341919
倖存 0.8105365633964539
無奈 0.8647724986076355
悲慘 0.8372344970703125
終於 0.9341779351234436
中止 0.894512951374054
打來 0.8067781925201416
傷心 0.7385833859443665
祥和 0.7868358492851257
寄來 0.8430265188217163
分離 0.7434297800064087
證件 0.7274680733680725
尊重 0.7518618106842041
心底 0.7951148152351379
不禁 0.8156865835189819
無窮 0.7549728751182556
別人 0.9064468145370483
冷卻 0.7874945402145386
笑道 0.7584916353225708
協調 0.7694194316864014
想 0.8552100658416748
體會 0.8430704474449158
沒甚麼 0.8968309760093689
一生 0.7795103788375854
傳達 0.8357791900634766
氛圍 0.8438988924026489
那裡 0.9257088303565979
真 0.7547945976257324
卸下 0.7354922890663147
要是 0.8859107494354248
之中 0.8080942630767822
小聲 0.7939817905426025
沮喪 0.8329600095748901
壓根 0.7220488786697388
父母親 0.9376999139785767
繼 0.7356211543083191
情感 0.8130792379379272
何等 0.8097331523895264
洋溢 0.849967360496521
梳理 0.7012053728103638
不然 0.8091394305229187
數額 0.8305824398994446
一輩子 0.7175514698028564
己經 0.7449067831039429
不賴 0.8356958627700806
新北產業園區 0.701815128326416
交心 0.7566284537315369
名子 0.8790687918663025
一生 0.755290150642395
已然 0.7983443140983582
職責 0.7180650234222412
為什麼 0.8633413910865784
不必 0.9141397476196289
居然 0.9833400845527649
態勢 0.8088149428367615
遲遲未 0.7052690982818604
早上 0.9692776203155518
應對 0.7173097133636475
愿意 0.8432328701019287
當時 0.7671827673912048
建言 0.7309701442718506
無論 0.9006590247154236
聽見 0.8658251762390137
趕緊 0.8295173048973083
堅信 0.7792050242424011
陷入 0.8165144324302673
自己 0.9064468145370483
十余年 0.7547550797462463
眼前 0.7401187419891357
星期天 0.7948307394981384
兩萬四 0.7855777740478516
轉變 0.7917324304580688
此時 0.8286126255989075
畢竟 0.8372727632522583
4738.59 0.8114898204803467
考量 0.773297131061554
後來 0.7796341180801392
畢竟 0.8120148181915283
依然 0.9496681690216064
反問 0.8083614706993103
良機 0.7762030363082886
知 0.7555286288261414
忽然 0.9605013132095337
成因 0.797487199306488
事 0.8934470415115356
很 0.941316545009613
前提 0.7704852223396301
別 0.8869559168815613
一同 0.8616647124290466
看見 0.8945684432983398
頗為 0.9425191283226013
感覺 0.7876816987991333
迅速 0.7960790395736694
定奪 0.7162927985191345
那麼 0.9182523488998413
反而 0.7230122685432434
去年 0.7237376570701599
這麼 0.9182524681091309
這兒 0.8156628012657166
但是 0.8758367300033569
上去 0.8011671900749207
衹有 0.736136257648468
須要 0.8069459199905396
通常 0.7464718222618103
時侯 0.8653978705406189
盡快 0.7307333946228027
如果 0.8005235195159912
其實 0.8013498187065125
有意思 0.7879040241241455
難題 0.7824379801750183
那些 0.8635151982307434
會不會 0.7795959115028381
甚麼 0.9597721695899963
自己 0.8903271555900574
能 0.8875210285186768
早已 0.7557728290557861
```
### 輸出:
```
有對老夫妻年逾[四十]，經濟[前提][不賴]，[理應][是][頤養][入職]生活的[時侯]，[卻]相偕到[律師團][那裡]要辦[分手]。[成因][是][繼][訂婚][去年]，[父女][爭執][迅速]，[常常][建言][相左]，[性格]上又[大不相同][頗為]不[祥和]， [數年里]的婚姻生活，要不[是]為了[小孩][依歸]，[己經][分飛][飄落]了。  [終於][終於]盼到[小孩]們[成年人]，再不[須要][父母親][苛責]，為了讓[互相]在[終老][能]自由的生活，
[不必]再[承受][這麼]多[[不必]要]的[爭執]，[定奪]辦[分手]。  這[關頭]在[律師團][眼前]，讓[律師團]也面有難色，[律師團]費都[太][歹勢]收了，  [後來]他[提案][去辦][證件]後，[鄭恩][一同]吃[夜宵]。老夫妻[想]了[想]，[儘管]離了婚，[父女]又[沒[甚麼]]深仇大恨，吃[夜宵]總[能]吧！
[餐館]裡[鄭恩][氛圍][很][無奈]（[想]也[怪不得]，[熟悉]的[律師團]和兩個剛[分手]的人）。[恰巧][侍者][寄來][交心][現烤]，老先生[趕緊][舀進]一塊[雞翅]給[老婆婆]說： 「吃吧！你最[偏愛]吃的[雞翅]。」  [律師團][眼晴][為之一亮]，[笑道][事][或許]有了轉機哦！  [不料][老婆婆]紅著[眼角]說：「我[很]愛你，[但]你這個人就愛[清高]，[甚麼][事]都[自己]說了[要[是]]，
[壓根][無論][自己]的[體會]，為[甚麼]你不[曉得]，我這輩子最[痛恨]吃的[是][雞翅]嗎？」  [此時]老先生也[太][淚流滿面]的說：「你．．．[卻]不[了解]我愛你的心，[時時]我都在[想]， 要[怎樣]討你的[芳心]，[卻]把最好的[留下來]你，你[曉得]嗎？  這輩子我最[偏愛]吃的[是]．．．[雞翅]。」  [律師團]看在眼裡，[不禁][顴骨]一酸，兩個[然而][仰慕]著[互相]的人， [卻][其實][協調]出了[難題]而[陷入][分離]的[態勢]。
這一晚[父女][不平凡]都有著[無窮]的[感嘆]，[這麼][十余年]的[情感][卻]要[應對][然而][悲慘]的[劇情]。  老先生[整夜]翻來覆去[睡不著覺]，[不平凡][一陣陣][澎拜][冷[卻]]般的痛在[心底][邪惡]的[折磨]著。他[考量]了[很]久，[忍著]著[沮喪]打[熱線]給[老婆婆]，[想][傳達]他[心底]的[傷心]， 他[想][反問][老婆婆]，他[是][何等]的愛她。  [熱線][響聲]了，[老婆婆][曉得][如果][是]老先生[打給]的，[但]她[不平凡][洋溢]了恨，
她[感覺][是]老先生負了她[人生]，她[遲遲未]再[聽見]他的[響聲]。[熱線][知]響了[[太]久]，[老婆婆][是][制於]，婚都離了，[裡子][有意思]，[豈[能]]接[熱線]， [反而]她把[熱線]線都拆了。  老先生手握著[蒼白]的[麥克風]，聽不到[老婆婆]的[響聲]，[不平凡][猶如][蒼翠山][通常]，久久[難以][忘懷]。[畢竟]這[星期天][早上][老婆婆]也[是]在傷[不平凡]輾轉難眠，[但][是]她忘了．．．老先生他有[高血壓]。
[第二天]，老先生被[發覺]死在[自己]家[臥室]，手裡還緊握著[熱線]筒。  [老婆婆][曉得]這個消息後[真][難以][堅信]，為了賭一口氣，[居然]讓[自己][仰慕]的人在[絕望]中[倖存]， [此時]侯任她[怎樣][小聲]的[高呼]也喚不回老先生的回眸一笑。  [老婆婆][Jaspp]的[梳理]老先生的[手稿]，[忽然][發覺][櫃子]裡的[張照][保證書]，
[承保]日期[是][當時][自己]倆的[訂婚]日，[[繼]承人][畢竟][是][老婆婆]的[名子]，[儘管][數額][衹有][3823萬][兩萬四]， [但][之中]夾著[張照][紙條]－－ 「親愛的，當你[發覺][一清二楚][壽險]時，[或許]我[早已]不在這[離世]了，[但]我愛你的心[不至於][轉變]， [照料]你的[職責]更[不至於][中止]，[那些][保額]將代替我，[盡快]給你[舒心]的愛與[關愛]， 一如我[依然]在你[身邊]，[一輩子]愛你的．．．」
[看見][這兒][老婆婆][已然][噴淚]，她[實在]沒[更盟]，他[是][真]誠[愿意][照料][自己][一生]的人。  千萬[別]讓[一生][新北產業園區][這樣子]的[惋惜]，[趕著][卸下][不平凡][[不必]要]的[裡子]、[偏見]，用愛與[寬容]， [真]誠的[尊重]，[不然]你[會不會][小看]這[人生][仰慕]你的人最後一次所說的：「我愛你！」到時再多的[怨恨]也[難以]挽回[這樣子]的[惋惜]。
更提醒您，要[掌握住][良機]，讓[摯愛]的人[曉得]你有多[在意]她，[勇氣]的說[上去]吧！[假使]你[實在][暖意]「我愛你」這[4738.59]字，只要你[熱誠]，總有[星期天]她[終將][了解]的。

```

## 輸出格式

程式將顯示三部分資訊：
1. 提取出的關鍵字列表
2. 每個關鍵字的替換詞及相似度數值
3. 修改前後的文章對比，替換的字詞會用方括號標記，如：[替換字]

## 注意事項

- 需預先下載北醫大學 NLP實驗室的Word2Vec模型
- 替換品質取決於Word2Vec模型的品質和覆蓋範圍

## 許可證

詳情請參閱LICENSE文件。

