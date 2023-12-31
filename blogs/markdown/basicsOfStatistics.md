---
Title : Basics of statistics
Category : Statistics
Author : Makoto Yaguchi
---

# Basics of statistics

[TOC]

***

## 第1章 データの種類とグラフ表現

### データの種類

- 質的変数
  - 名義尺度 : 他と区別し分類するための名称のようなもの
    - 男女、血液型、郵便番号、住所、本籍地、所属学部、学籍番号
  - 順序尺度 : 順序や大小には意味があるが間隔には意味がないもの
    - 1位, 2位, 3位、1.好き, 2.ふつう, 3.嫌い、1級, 2級, 3級, 4級
- 量的変数
  - 間隔尺度 : 目盛が等間隔になっているもので、その間隔に意味があるもの
    - 気温（摂氏）、西暦、テストの点数
  - 比例尺度 : 0が原点であり、間隔と比率に意味があるもの
    - 身長、速度、睡眠時間、値段、給料、幅跳びの記録

#### データの種類をまとめた表

| 種類     | 尺度     | 説明                                | 例                                      |
| -------- | -------- | ----------------------------------- | --------------------------------------- |
| 質的変数 | 名義尺度 | 分類するための名称                  | 男女、血液型、郵便番号、住所、学籍番号  |
| 質的変数 | 順序尺度 | 順序や大小にのみ意味がある          | 1位, 2位, 3位、1.好き, 2.ふつう, 3.嫌い |
| 量的変数 | 間隔尺度 | 目盛が等間隔で間隔に意味があるもの  | 気温（摂氏）、西暦、テストの点数        |
| 量的変数 | 比例尺度 | 0が原点で間隔と比率に意味があるもの | 身長、速度、睡眠時間、値段、給料        |

#### 異なる視点からの分類

- 離散変数（discrete variable）
  - とびとびの値をとる変数のこと : サイコロの出る目など
- 連続変数（continuous variable）
  - 連続した値をとる変数のこと : 重さや温度など

### 質的変数の要約 → 質的変数の扱い方

[統計Webより](https://bellcurve.jp/statistics/course/5414.html)

- クロス集計表1
  - 性別×好きなスポーツのクロス集計表 (2×4のクロス集計表)
    | 性別 | サッカー | 野球 | テニス | 水泳 | 合計 |
    | -------- | ---- | ------ | ---- | ---- | --- |
    | 男子     | 7    | 5      | 2    | 1    | 15  |
    | 女子     | 5    | 3      | 5    | 2    | 15  |
    | 合計     | 12   | 8      | 7    | 3    | 30  |

- クロス集計表2
  - 好きなスポーツ×性別のクロス集計表 (4×2のクロス集計表)
    | スポーツ | 男子     | 女子 | 合計 |
    | -------- | ---- | ---- | --- |
    | サッカー | 7    | 5    | 12  |
    | 野球     | 5    | 3    | 8   |
    | テニス   | 2    | 5    | 7   |
    | 水泳     | 1    | 2    | 3   |
    | 合計     | 15   | 15   | 30  |

### グラフによるデータの要約

- 棒グラフ: ----------------> 量の大小を比較
- 折れ線グラフ: ----------> 数量の時間的・空間的変化を表現
- 円グラフ: ----------------> カテゴリの割合を表す
- 帯グラフ: ----------------> 割合の比較、年次変化
- レーダーチャート: ----> 複数の値をまとめて表現
- 幹葉図: -------------------> データを幹と葉に分類して表す

[幹葉図の例](https://bellcurve.jp/statistics/course/5228.html)

| 幹  | 葉      | 実際の数値  |
| --- | ------- | ----------- |
| 1   | 7       | 17          |
| 2   | 0 3 3 7 | 20 23 23 27 |
| 3   | 1 5     | 31 35       |

### グラフ表現の工夫と注意点

- 積み上げ棒グラフ
- 年度比較などの時点の異なる複数の帯グラフ
- レンジを適切に表現しないと間違った解釈となる

### 時系列データの記述と分析

- 時系列データとは時間順に示されたデータのこと
- 指数化と幾何平均
  - 指数化：ある時点を基準とし時系列間の値の大きさをそろえる
  - 幾何平均：平均伸び率の計算に用いる
  $$ r_G = (r_1 \times r_2 \times \cdot \times r_{T-1} \times r_T )^{1/T} = (\Pi_{t=1}^T r_t)^{1/T} $$

### 時系列データの変動分解

- 傾向変動
- 季節変動
- 不規則変動

- トレンド抽出
  - 移動平均法
  - 指数平滑法

### 指数の作成と利用

- ラスパイレス指数
  $$ P_{Lasperyes} = \frac{\sum_{i=1}^n p_t q_0}{\sum_{i=1}^n p_0 q_0} $$
- パーシェ指数
  $$ P_{Paasche} = \frac{\sum_{i=1}^n p_t q_t}{\sum_{i=1}^n p_0 q_t} $$
- フィッシャー指数
  $$ P_{Fisher} = \sqrt{P_{L(0, t)} \times P_{P(0, t)}} $$


### 時系列グラフ作成上の注意点

- 時間の間隔に注意する
- 時系列データに対する対数の利用

***

## 第2章 量的変数の要約方法

- 度数分布表の作成
- ヒストグラムと度数分布多角形
- 分布の特徴の把握
- 分位数と5数要約
- データの散らばり
- 箱ひげ図

***

## 第3章 1変数データの分析

### 位置に関する代表値

- 平均値
  - 観測値の合計/観測値の個数
  - 度数分布表からの平均値
    - 観測値 ≒ 階級値 として計算する
- 中央値
  - 観測値を大きさの順に並べたときの中央に繰る値
  - 観測値が偶数個の場合、2つの平均をとる
    - 1,2,3,4,5,6,7,8,9,10の時は5.5
- 最頻値、モード
  - 最も多く出現する観測値

#### 3つの代表値の関係性

- 分布が左右対称
  - 3つの値はそれほど違わない
- 右の裾が長い
  - 中央値は平均値より小さい値
  - 最頻値はさらに小さい値となる

### 観測値の散らばりの尺度

- 偏差
  - 観測値から平均値を引いたもの

\[ x_i = \bar{x} \]

- 平均偏差
  - 偏差の絶対値の平均値

\[ \frac{1}{n} \sum_{i=1}^n |x_i - \bar{x}| \]

- 分散
  - 偏差の2乗の平均値

\[ s^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \]

- 標準偏差
  - 分散の平方根
  - \(s\) は標本の標準偏差で使い \( \sigma \) は母集団の標準偏差で使われることが多い

\[ s = \sqrt{s^2}, \quad \sigma = \sqrt{\sigma^2} \]

- 特徴
  - これらの値が小さい時は平均値のまわりに値が集中している

### 変数の変換と平均値、分散、標準偏差

- 平均値と分散を以下とおく
  \[ \bar{x} = \frac{1}{n} \sum_{i=1}^n x_i , \quad s^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2 \]
- ここで\(a, b\)を定数として \(y = a + bx\) のように変数の変換を考える
- 平均値\(\bar{y}\)と分散\(s_y^2\)は以下のように表せる
  \[ \bar{y} = \frac{1}{n} \sum_{i=1}^n (a + bx_i) = \frac{1}{n} (na + b\sum_{i=1}^n x_i ) = a + b\bar{x} \]

\[
  s^2
  = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2
  = \frac{1}{n} \sum_{i=1}^n (a+bx_i-a-b\bar{x})^2
  = b^2 \frac{1}{n} \sum_{i=1}^n (x_i-\bar{x})^2
  = b^2 s_x^2
\]

- 分散から標準偏差を求める
  \[ s_y = |b|s_x \]
- 変動係数

  - 標準偏差を平均値で割ったもの
  - 散らばり度合を考える際に平均値の大きさを考慮する
  - 単位が異なる標準偏差では正しい散らばりを見ることができない
    \[ cv = \frac{s}{\bar{x}} \]

### 「進んだ話題」探索的データ解析法と外れ値

- 調査や実験によって得られたデータの分布を確認せずに平均値や標準偏差を求めることは誤った解釈につながる恐れがあるため注意が必要である
- ヒストグラムや箱ひげ図などの統計グラフを用いてデータ全体の分布を確認し、適切なデータ分析を心がける必要がある
  - 複数の分布が混ざったデータになっていないか
  - 他の観測値と比べ大きくはずれている観測値がないか
  - 誤って混入した観測値を除いて計算するべきか

#### 探索的データ解析

- EDA, Exploratory Data Analysis
  [探索的データ解析](https://www.msi.co.jp/solution/splus/products/eda.html)
  - 外れ値の影響を受けにくく、かつ実用的な一連の手法
    - 全体として分布の形が左右対称か右か左のすそが長いか
    - その長さを中央値、四分位等の数値を求める
    - 外れ値を四分位範囲の1.5倍離れたものや3倍離れたもので判定
    - 外れ値がどのような原因で発生したのかを考えることが大切となる
- 外れ値の検出と対策
  - 分布が対称でない場合は箱ひげ図による形式的な外れ値の検出は有効でない
  - 対数変換などで対称に近づけてから外れ値を特定する
  - 判断が難しい場合は、頑健統計学 (robust statistics) を用いる
    - データに外れ値が混入している場合でも、妥当な統計的解析を行う手法
    - (例)中央値が外れ値に頑健である

***

## 第4章 2変数データの分析

### 2つの変数の関係

- 質的変数
  - クロス集計表
- 量的変数
  - 相関関係

### 層別散布図

- 複数のグループを描いた散布図
  - 全体ではなくグループに分けることで相関関係等を導き出すことができる

### 相関係数

- 共分散

\[ s_xy = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) \]

### 相関係数の注意点

### 相関と因果

***

## 第5章 回帰直線と予測

### 回帰分析

- 相関係数
  - 2つの変数の間の直線的な関係の強さを測る尺度で-1～1の間を取る
  - 変数を入れ替えてもへんかはない
- 回帰分析
  - 2つの変数の間に何らかの因果関係を想定し、変数 \(x\) から変数 \(y\) を予測する
  - \(x\): 説明変数
  - \(y\): 被説明変数、目的変数
- 回帰直線
  - 直線の式 \(y= \hat{\beta} + \hat{\alpha}x \) により予測する
  - \( \alpha, \ \beta \) : 回帰係数


### 最小二乗法

- 観測値 \( x_i, \ y_i \) に対して、予測値 \(y= \hat{\beta} + \hat{\alpha}x \) を考える
- 残差
  - \( y \) に関する観測値 \( y_i \) と予測値 \( \hat{y_i} \) の差より残差平方和を求める

\[
  \sum_{i=1}^n (y_i - \hat{y_i})^2
\]

- 式に直線の式 \(y= \hat{\beta} + \hat{\alpha}x \) を代入する

\[
  S(\hat{\alpha} \hat{\beta}) = \sum_{i=1}^n (y_i - \hat{\alpha} - \hat{\beta} x_i)^2
\]

#### 最小二乗法の導出

<https://taketake2.com/P7.html>

$$ J = \sum_{i=1}^n (y_i - \hat{\alpha} - \hat{\beta} x_i)^2 $$
$$ J = \sum_{i=1}^n (y_i^2 - 2y_i(\hat{\alpha} + \hat{\beta} x_i) + \hat{\beta}^2 x_i^2 + 2\hat{\beta}x_i\hat{\alpha} + \hat{\alpha}^2) $$
$$ \frac{\partial J}{\partial\hat{\beta}} = \sum_{i=1}^n (-2y_i x_i + 2\hat{\beta} x_i^2 + 2x_i\hat{\alpha}) = 0 $$
$$ \frac{\partial J}{\partial\hat{\alpha}} = \sum_{i=1}^n (-2y_i + 2\hat{\beta} x_i + 2\hat{\alpha}) = 0 $$
下の式より
$$ -\sum_{i=1}^n y_i + \sum_{i=1}^n \hat{\beta}x_i + \hat{\alpha} = 0 $$

### 線形回帰モデル



### 「進んだ話題」回帰直線に関する歴史

### 「進んだ話題」決定係数

***

## 第6章 確率

### 事象と確率

#### 事象とその分類

試行の結果起こる事柄で、サイコロを振るという試行に対しての事象などが考えることができる

- 全事象 : すべての事象 \( U_{dice} = \{1, 2, 3, 4, 5, 6\} \)
- 事象 : それぞれの事象   \( A_{even} = \{1, 3, 5\}, \ B_{odd} = \{2, 4, 6\} \)
- 根元事象 : それ以上分割できない事象 \( a = \{1\}, \ b = \{2\} \)
- 和事象 : 事象AとBのいずれかが起こる \(A \cap B\)
- 積事象 : 事象AとBが両方同時におこる \(A \cup B\)
- 余事象 : 事象AとBが起こらない \(\bar{A}, \ \bar{B}\)
- 空事象 : 起こりえない事象 \(\phi\)

ベン図
![ベン図](jpg/probability003-1024x433.webp)

> [DXCEL WAVE](https://di-acc2.com/analytics/statistics/17069/)より

#### 確率の定義

確率(probability) : 偶然起こる現象に対する頻度（起こりやすさの指標）のこと

##### 古典的確率

- 同様に確からしいと仮定できる根元事象が \(n\) 個で、
- ある事象 \(A\) に含まれる根元事象が \(k\) 個あるときの- \(A\) の起こる確率
  \[P(A) = \frac{k}{n} \]
  - \( P \) : 確率(probability)

##### 頻度確率

- 同じ条件の下で繰り返すことができるような実験や観測(反復試行)
- それらによって得られた根元事象の相対頻度に基づき確率を決める
- コインの表裏の確率のように投げる回数を増やすことで事象の起こりやすさを判断する
  \[P(A) = \sum_{a_i \in A} p_i \]
  - \( A \) : 事象(2 and 4 and 6)
  - \( a_i \) : 根元事象(2 or 4 or 6)
  - \( a_i \in A \) : 事象において根元事象が起きた場合
  - \( p \) : 根元事象の起こる確率

##### 公理的確率

- 確率の公理
  - 任意の事象 \( A(\subset U) \) は、 \( 0 \leqq P \leqq 1\) をみたす
  - 全事象 \( U \) は、 \( P(U)=1 \) をみたす
  - **無限個**の事象 \( A_1, A_2, \cdots \) が互いに排反なとき、すなわち \(A_i \cap A_j = \phi(i \neq j) \) が成り立つとき以下をみたす
  - 言い方を変えると \(A_i \) かつ \( A_j \) が 空事象のとき以下が成り立つ
    \[P(A_1 \cup A_2 \cup \cdots ) = P(A_1) + P(A_2) + \cdots \]
- **有限個**の排反な事象 \( A_i(1, \cdots, k), \ A_i \cap A_j = \phi(i \neq j) \) に対しても成り立つ
  \[P(A_1 \cup A_2 \cup \cdots \cup A_k ) = P(A_1) + P(A_2) + \cdots + P(A_k) \]
- これより古典的確率や頻度確率がみたす性質なども成立することが示せる
  \[ P(\bar{A}) = 1 - P(A), \ P(\phi) = 0 \]

### 事象の独立性と試行の独立性

- 2つの事象について
- 一方の事象が変化したときにもう一方の事象が変化せず
- それが相互に言える場合、この2つの事象は独立であると言う(⇔関連がある)
- 事象 \( A \) と \( B \) が独立である場合は以下の式が成り立つ
  \[ P(A \cap B ) = P(A)P(B) \]

#### 反復試行の確率

ある事象 \( A \) が起こる確率を \( p(0 \leqq p \leqq 1 ) \) とすると同じ試行を \( n \) 回独立に繰り返したときに事象 \( A \) が起こる確率は以下の式で求めることができる
\[ {}_n C_k \ p^x \ (1-p)^{n-k} \]

### 条件付き確率

#### 条件付き確率とは

2つの事象 \( A \) と \( B \) に対して、 \( A \) が起こった条件の下で \( B \) が起こる確率
\[ P(B|A) = \frac{P(A \cap B)}{P(A)}, \quad P(A) > 0 \]

例題6.11
ある高校のク**ラス**を性別と出身中学校で分けたクロス集計表がある。無作為に選んだ1人が、A中学校から選ばれたことがわかっている場合に、男子である(条件付)確率を求める

|      | A中学 | B中学 | C中学 | 合計 |
| ---- | ----- | ----- | ----- | ---- |
| 男子 | 10    | 7     | 5     | 22   |
| 女子 | 5     | 7     | 6     | 18   |
| 合計 | 15    | 14    | 11    | 40   |

- 事象 \( A \) : A中学出身, ---> \( P(A) = 15/40 \)
- 事象 \( B \) : 男子, -----------> \( P(A \cap B) = 10/40 \)

\[ P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{10/40}{15/40} = \frac{2}{3} \]

#### 乗法定理とは

\( A \) 条件下で \( B \) が起きた場合に\( A \cap B \) を求める
\[ P(A \cap B) = P(A)P(B|A) \]

例題6.12
10本のくじで当たりが3本ある。2人が順番にくじを引く場合、1人目が当たり、2人目がはずれとなる確率を求める。一度引いたくじは元に戻さない。

- 事象 \( A \) : 1人目があたり, ---> \( P(A) = 3/10 \)
- 事象 \( B \) : 2人目がはずれ, ---> \( P(B) = 7/9 \)

\( B \) は \( A \) のもとで起きているので、条件付確率で考えると \( P(B|A) = 7/9 \) となる
\[ P(A \cap B) = P(A)P(B|A) = 3/10 \times 7/9 = 7/30 \]

### ベイズの定理

ベイズの定理
\[ P(B_1|A) = \frac{P(B_1)P(A|B_1)}{P(B_1)P(A|B_1) + P(B_2)P(A|B_2)} \]

日本人の0.01%が罹患(りかん)しているある病気について考える。以下のような条件において、ある人がこの病気の検査を受けて陽性という判定を受けた時の病気に罹患している確率を求める

- 病気に罹患している人 -----> 陽性と判定される確率が95%
- 病気に罹患していない人 --> 陰性と判定される確率は80%

![ベイズの定理](jpg/ベイズの定理.jpg)

> [統計Web](https://bellcurve.jp/statistics/course/6448.html/)より

#### ベイズの定理を使って確率を求める

- 検査で陽性: 事象 \( A \)
- 検査で陰性: 事象 \( \bar{A} \)（事象Aの余事象）
- 罹患している: 事象 \( B_1 \)
- 罹患していない: 事象 \( B_2 \)

\[
\begin{align}
P(B_1|A) &= \frac{P(B_1)P(A|B_1)}{P(B_1)P(A|B_1) + P(B_2)P(A|B_2)} \\
&= \frac{0.0001 \times 0.95}{0.0001 \times 0.95 + 0.9999 \times 0.20} \\
&= 0.000475 \\
\end{align}
\]

- 罹患している確率：\( P(B_1) = 0.0001 \)
- 罹患していない確率：\( P(B_2) = 0.9999 \)
- 罹患かつ陽性となる確率：\( P(A|B_1) = 0.95 \)
- 罹患かつ陰性となる確率：\( P(\bar{A}|B_1) = 0.05 \)
- 非罹患かつ陰性となる確率：\( P(\bar{A}|B_2) = 0.80\)
- 非罹患かつ陽性となる確率：\( P(A|B_2) = 0.20 \)

### 「進んだ話題」独立性に関する注意

***

## 第7章 確率変数と確率分布

### 確率変数と確率分布の考え方

- サイコロの確率変数\( X \)は1から6
- サイコロの確率分布は全て1/6
- 離散型確率変数と連続型確率変数
- 1から6の目を出すサイコロや表裏を出すコイン
- 身長、体重など

<例1>

- ゆがみの**ない**サイコロの確率分布

| \( x \)    | 1   | 2   | 3   | 4   | 5   | 6   | 合計 |     |
| ---------- | --- | --- | --- | --- | --- | --- | ---- | --- |
| \( p(x) \) | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1/6 | 1    |     |

<例2>

- ゆがみの**ある**サイコロの確率分布

| \( x \)    | 1    | 2    | 3   | 4    | 5    | 6   | 合計 |     |
| ---------- | ---- | ---- | --- | ---- | ---- | --- | ---- | --- |
| \( p(x) \) | 1/12 | 1/12 | 1/3 | 1/12 | 1/12 | 1/3 | 1    |     |

### 平均、分散、標準偏差

- 確率変数 \( X \) の平均 \( E(X) \) は \( X \) の期待値とも言う
  \[ E(X) = x_1p_1 + x_2p_2 + \cdots + x_kp_k = \sum_{i=1}^k x_ip_i \]
- 確率変数 \( aX + b \) と \( X^2 \) の平均
- 確率変数の分散と標準偏差
- 確率変数 \( aX + b \) と \( X^2 \) の分散と標準偏差

### 二項分布と正規分布

- 二項分布

  - 成功確率 \( p \) が一定の反復試行を \( n \) 回行ったとき、成功回数 \( X \) を確率変数とする離散型確率分布をいう
  - 成功確率 \( p \) が一定の場合、成功が \( x \) 回、失敗が \( n-x \) 回である確率は以下の式となる
    \[ P(X = x) = {}_n C_k p^x (1-p)^{n-k} \]
- 二項分布の性質

  - 確率変数 \( X \) は二項分布 \( B(n, p) \) に従うと言う
  - その時の平均、分散、標準偏差は以下となる
    \[ \mu = np, \sigma^2 = np(1-p), \sigma = \sqrt{np(1-p)} \]
- 正規分布

  - 連続型確率分布は確率変数 \(X\) に対し、ある値 \(x\) を取る確率が \(P(X = x)\) で決まるのではなく、関数 \(f(x) \geqq 0\) で分布全体を表す
  - この関数 \(f(x) \geqq 0\) を確率変数 \(X\) の確率密度関数という
  - 連続型確立変数 \(X\) が区間 \(|a, b|\) 内の値を取る確率を関数 \(f(x)\) で書く
    \[P(a \leqq X \leqq b) = \int_a^b f(x)dx \quad , \quad \int_\infty^\infty f(x)dx = 1\]
  - 最も重要な連続型確率密度関数である正規分布(ガウス分布)は、\(\mu \) と \(\sigma^2 \) で以下のように定まる
    \[f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} \quad (-\infty  \lt x \lt \infty)\]
- 正規分布の性質

  - 確率変数 \(X\) が正規分布 \(N(\mu, \ \sigma^2)\) に従うとき
    \[X, \ N(\mu, \ \sigma^2) \]
  - \(X\) の1次関数 \(Y = aX + b\)は、正規分布 \(N(a\mu + b, \ a^2\sigma^2)\) に従う
    \[Y = aX + b, \ N(a\mu + b, \ a^2\sigma^2) \]
  - 標準化のために、\(a = 1/\sigma ,\ b = -\mu/\sigma \) としたときの確率変数を \(Z\) とすると、 \(Z = X/\sigma -\mu/\sigma\) は、正規分布 \(N(0, \ 1)\) に従う
    \[Z = \frac{1}{\sigma} X -\frac{\mu}{\sigma} = \frac{X-\mu}{\sigma}, \ N(0, \ 1) \]
  - 確率変数 \(X\) が二項分布 \( B(n, p) \) に従い、\( n \) が大きい時、確率変数が従う分布は正規分布 \(N(np, \ np(1-p))\) で近似できる
    \[X, \ B(n, p), \ n\gg0,  \ N(np, \ np(1-p)) \]
    - \( n \) : 試行回数
    - \( p \) : 成功確率
  - 正規分布 \(N(0, \ 1)\) を標準正規分布といい、標準正規分布の上側確率を使って次節の正規分布の確率を求めることができる

### 正規分布の確率と計算

#### 標準正規分布 \(N(0, \ 1) \) の確率

標準正規分布について、\( u = 1.96 \) として、縦線 \( z = 1.96 \) から上側の面積である \( Q(1.96) = P(Z \geqq 1.96) \) の値を標準正規分布表より求める

![標準正規分布表](jpg\標準正規分布.jpg)
[標準正規分布表](https://bellcurve.jp/statistics/course/7805.html)

\[ Q(1.96) = P(Z \geqq 1.96) = 0.0250 \]

\[Z = \frac{X-\mu}{\sigma}, \quad X:確率変数,\ \mu : 平均,\ \sigma : 標準偏差 \]

- 標準正規分布でよく使われるケース

\[ P(Z \geqq 1.28) = 0.10 \]

\[ P(Z \geqq 1.645) = 0.05 \]

\[ P(Z \geqq 1.96) = 0.025 \]

\[ P(-1.645 \geqq Z \geqq 1.645) = 0.90 \]

\[ P(-1.96 \geqq Z \geqq 1.96) = 0.95 \]

#### 一般の正規分布 \( N(\mu, \ \sigma^2) \) の確率

確率変数 \(X\) が正規分布 \( N(\mu, \ \sigma^2) \) に従うとき、標準化と標準正規分布の表を使い \(X\) がある区間に入る確率を求めることができる

確率変数 \(X\) が正規分布 \( N(50, \ 10^2) \) に従う場合、\(P(X \geqq 65)\) を標準化へ変換をして計算すると以下のようになる
\[ P(\frac{X-50}{10} \geqq \frac{65-50}{10}) = P(Z \geqq 1.5) = 0.0668 \]

#### 二項分布の正規近似

確率変数 \(X\) が二項分布 \( B(n, p) \) に従い、\( n \) が大きい時、確率変数が従う分布は正規分布 \(N(np, \ np(1-p))\) で近似できる

\[ \ B(n, p), \ \approx \ N(np, \ np(1-p)) \]

![二項分布と正規分布](jpg\bnomial.png)

この性質を用いて、二項分布の確率を正規分布の確率を用いて求めることができる

## 第8章 データの収集: 実験・観察・調査

### 統計的問題解決におけるデータの収集

- PPDACサイクル
  - Problem 問題
  - Plan 実験や調査の計画
  - Data 収集
  - Analysis 分析
  - Conclusion 結論
- 問題の明確化
  - 得られたデータで結論が出せるレベルまで具体化する

### 実験研究と観察研究

- 実験研究
  - 研究対象に対して何らかの介入を行い、その効果を検証するための研究
  - 新しい治療法の有効性や安全性を検証する場合など
    - ある降圧剤の効果を検証するために、薬投与群とプラセボ投与群との間で血圧の比較を行う
    - 新しい肥料の効果を検証するために、新しい肥料投与群と古い肥料投与群との間で作物の収量を比較する
- 観察研究
  - 研究対象に対して介入を行わず、自然の状態を観察する研究
  - 現行の治療法やその予後を検証する場合など
  - 寿命調査やアンケート調査
- 処理群と対照群
  - 2グループの研究対象について
    - 処理群: 一方にだけ興味の対象とする何らかの処理を加える
    - 対照群: 何も処理を加えず、比較の対象とする
- 実験・調査の計画の立案
  - どのような研究方法を取るのか
    - 実験 or 研究
  - 対象者としてどのような人を選ぶのか
    - 標本調査の方法
  - どのような測定を行うのか

[フィッシャーの三原則][https://bellcurve.jp/statistics/course/12744.html](https://bellcurve.jp/statistics/course/12744.html)

- 局所管理（local control）
- 無作為化（randomization）
- 反復（replication）

### 全数調査と標本調査

- 母集団と標本

  - 母集団: 特徴や傾向を知りたい集団全体
  - 標本: 実際に調査を実施する母集団の一部
    - 標本の大きさ: 標本の人数や個数
- 全数調査

  - 集団のすべてを調査するもの
    - 国勢調査
  - 一部を取り出して調査するもの
- 標本調査

  - 母集団の一部を取り出して調査し、母集団の特性値に対して統計的推測を行う
  - 母集団と標本の間には一般には誤差が発生する
    - 標本誤差: 標本調査により発生する誤差
    - 非標本誤差: 計画、調査、結果の整理、解析、発表段階での誤差
    - 精度の大小を比較するのは困難と言われている

|            | 全数調査   | 標本調査       |     |
| ---------- | ---------- | -------------- | --- |
| 標本誤差   | 発生しない | 発生する       |     |
| 非標本誤差 | 発生する   | 発生する       |     |
| 精度の大小 | 管理が困難 | 両方が混在する |     |

### 無作為抽出法

- くじやサイコロを用いる
- 乱数表を用いる
- コンピュータで乱数を発生させる

## 第9章 統計的な推測

### 統計的な推測

- 統計学では知見を得たい母集団を明確に設定し、適切に計画された実験や調査により標本を抽出する
  - 一般に、単純無作為抽出が好ましい
- 標本平均や標本比率等より母集団の特徴を表す母平均や母比率等の統計的な推測を行う
  - 統計的推定
  - 統計的仮説検定
    ![標本調査](jpg/標本調査.jpg)

#### 単語の整理

- 母平均

  - 母集団の平均値・期待値

- 母比率

  - 個々のカテゴリーが母集団で占めるであろう割合
 
- 標本平均

  - 標本の平均値・期待値
 
- 標本比率

  - 個々のカテゴリーが標本で占めるであろう割合
 
- 標本分布

  - 標本平均や標本比率などの推定された量に関する分布
  - 母平均や母比率の値のまわりに分布する
    - 母集団から繰り返し大きさ \(n\) の標本を無作為に抽出すると
    - 標本平均は母平均のまわりに分布する
    - 標本比率も母比率のまわりに分布する

#### 標本平均 \( \bar X \) の標本分布

- 母平均 \(\nu\) 、母分散 \(\sigma^2\) をもつ母集団から
- 大きさ \(n\) の標本として \(X_1, X_2, \dot,X_n\) を無作為に抽出する
- これらは \(n\) 個の確率変数であり、それらの標本平均である以下の式も確率変数である
- 標本平均の実現値は標本ごとに異なる
- 標本を無限回得ることができるなら、標本平均は何らかの分布に従う

\[
  \bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
\]

- 標本平均の性質 ※重要な性質1
  - \(n\) 個の確率変数 \(X_1, X_2, \dot,X_n\) が互いに独立に母平均 \(\mu\) 、母分散 \(\sigma^2\) の分布に従い、\(n\) が十分に大きい時

\[
  標本平均 \bar{X} は正規分布 N( \mu, \frac{\sigma^2}{n}) に近似的に従う
\]

- 以上より、\(n\) が大きくなるほど標準偏差が小さくなり、分布の山が際立つことがわかる
- さらに、を \( \bar{X} \) 標準化した確率変数 \(Z\) を考えると、\(n\) が大きい時

\[
  Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n} } は標準正規分布 N( 0, 1) に近似的に従う
\]

#### 標本比率 \( \hat p \) の標本分布

母集団における興味のある事象 \(A\) の出現比率 \(p\)について考える
n回の反復試行で \(A\) が起こる回数 \(X\) は確率変数であり、二項分布 \(B(n, p)\) に従う

- 非復元抽出
  - これに対し、母集団から一つ抽出しそれを元に戻さず試行を続けた場合、次の事象 \(A\) の出現比率は \(p\) となる
  - 母集団の大きさが大きい場合、非復元抽出であっても近似的に二項分布 \(B(n, p)\) に従うと考えてよい

母比率 \(p\) の推定に標本比率 \( \hat{p} = X / n \) を用いるとき、標本比率 \( \hat{p} \) も確率変数である。 \( \hat{p} \) が従う分布を標本比率 \( \hat{p} \) の標本分布という

- 標本比率の性質 ※重要な性質2
  - 二項分布 \(B(n, p)\) に従う確率変数 \(X\) の平均と分散は \( np, np(1-p) \)
  - 標本比率の平均と分散は \( p, p(1-p) / n \) となる
- \(n\) が大きい時、二項分布は正規分布に近似できることから以下のことが言える

\[
  標本比率 \hat{p} は正規分布 N( p, \frac{p(1-p)}{n}) に近似的に従う
\]

- \(p\) を標準化下確率変数 \(Z\) を考えると \(n\) が大きい時

\[
  Z = \frac{\hat{p} - p}{\sqrt{p(1-p) / n} } は標準正規分布 N( 0, 1) に近似的に従う
\]

### 区間検定

- \(n\) 世帯であるドラマを観ていた世帯数を \(X\) とし、視聴率(母比率) \(p\) の推定を考える
- 視聴世帯数は確率変数であり、二項分布に従う

#### 点推定

- 900世帯中180世帯が観ていた場合は、以下のように一つの値に推定することができる

\[
  \hat{p} = \frac{X}{n} = \frac{180}{900} = 0.2
\]

#### 区間推定

- 点推定に対し、以下のように幅を持たせて推定を行うことを区間推定という
- 関東地区の視聴率調査では、約1800万世帯という大きな母集団から900世帯と標本として調査を行う
- 標本の大きさが小さい時に信頼区間を用いて、信頼性を評価する

\[
  1.73 \leqq p \leqq 0.23
\]

### 仮説検定

***


## 数学の補足

1. 総和記号
2. 階乗、順列、組み合わせ
3. 対数
4. 最小二乗法による1次式のあてはめ

## 第6章の練習問題

### Question 6.3

- コインを3回投げて少なくとも1回表が出る確率は？

**Answer**
以下解説

- コインを3回投げて表裏の出方は \(2^3\) で8通り
- 少なくとも1回表が出るに対する余事象は、1回も表がでないこと
- 1回も表がでないのは裏裏裏の1通りのみとなる
- 全体から余事象を引くことで必要な確率を求めることができる
  \[ 1 - \frac{1}{8} = \frac{7}{8} \]

### Question 6.7

- ある病気にかかる確率は喫煙者で0.3%、非喫煙者で0.1%
- ある集団の喫煙者の割合が20%のとき病気にかかった人が喫煙者である確率は？

**Answer**
以下、それぞれの確率を算出

- 喫煙者で病気に掛かる確率 \( 0.2 \times 0.003 = 0.0006 \)
- 非喫煙者で病気に掛かる確率 \( 0.8 \times 0.001 = 0.0008 \)
- 全体で病気に掛かる確率 \( 0.0006 + 0.0008 = 0.0014 \)
- 病気に掛かり、喫煙者である確率 \( 0.0006 / 0.0014 = 3/7 \)

### Question 6.8

大小のサイコロを同時に投げる試行において、以下の事象における確率を求める

- \( A \): 大きいサイコロが4の目が出る
- \( B \): 2個のサイコロの和が7である
- \( C \): 2個のサイコロの和が9である

1. 事象 \( A, \ B, \ C \) それぞれの確率
2. 事象 \( C \) が起こった時の事象 \( A \) が起こる条件付き確率
3. 事象 \( A \) が起こった時の事象 \( C \) が起こる条件付き確率
4. \( P(A \cap B), \ P(A)P(B) \) の大小関係 \( <, =, > \)
5. \( P(A \cap C), \ P(A)P(C) \) の大小関係 \( <, =, > \)
6. 大小のサイコロを2個同時に投げる試行を2回繰り返す
   1. 1回目に\( P(A \cap B) \) が起こり、2回目に\( P(\bar{A} \cap B) \) が起こる確率
   2. 3つの事象がいずれも1回ずつ起こる確率

**Answer**
大小のサイコロの組合せ
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)
(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)
(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)
(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6)
(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)
(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)

大小のサイコロの和

| big \ small |   Ⅰ   |   Ⅱ   |   Ⅲ   |   Ⅳ   |   Ⅴ   |   Ⅵ    | ↙事象B     |
| ----------: | :---: | :---: | :---: | :---: | :---: | :----: | ---------- |
|       **Ⅰ** |   2   |   3   |   4   |   5   |   6   | **7**  |            |
|       **Ⅱ** |   3   |   4   |   5   |   6   | **7** |   8    | **↙事象C** |
|       **Ⅲ** |   4   |   5   |   6   | **7** |   8   | **9**  |            |
|       **Ⅳ** | **5** | **6** | **7** | **8** | **9** | **10** | **←事象A** |
|       **Ⅴ** |   6   | **7** |   8   | **9** |  10   |   11   |            |
|       **Ⅵ** | **7** |   8   | **9** |  10   |  11   |   12   |            |

大小のサイコロの組合せ表より
\[ P(A) = 6/36 = 1/6 \]

大小のサイコロの和の表より
\[ P(B) = 6/36 = 1/6 \]

\[ P(C) = 4/36 = 1/9 \]

条件付き確率の式より
\[ P(C|A) = \frac{P(A \cap C)}{P(A)} = \frac{1/36}{1/9} = 1/4 \]

\[ P(A|C) = \frac{P(A \cap C)}{P(C)} = \frac{1/36}{1/6} = 1/6 \]

それぞれの確率を比較する
\[ P(A \cap B) = \ P(A)P(B) \]

\[ P(A \cap C) > \ P(A)P(C) \]

1回目と2回目の確率を掛け合わせる
\[ P(A \cap B) \times P(\bar{A} \cap B) = 1/36 \times 3/36 \]

3つの事象のうち \(B\) と \(C\) は同時に起こらないので2回の試行で3つの事象がいずれも1回ずつ起こるのは以下の場合となる

- 2回のうちどちらかで \( P(A \cap B) \) が起こり、他の試行で \(C\) が起こるので、\( P(\bar{A} \cap C) \) となる
  \[ P(\bar{A} \cap C) = 1/36 \times 1/12 \times 2 = 1/216 \]
- 2回のうちどちらかで \( P(A \cap C) \) が起こり、他の試行で \(B\) が起こるので、\( P(\bar{A} \cap B) \) となる
  \[ P(\bar{A} \cap B) = 1/36 \times 5/36 \times 2 = 5/648 \]

## 第7章の練習問題

## 第8章の練習問題

## 第9章の練習問題

## note
<!-- 変更すると新しいBlogが作成される -->
Category : python
Author : Makoto Yaugchi
