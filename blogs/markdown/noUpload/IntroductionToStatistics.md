# 統計学入門

[TOC]

## 第1章 統計学の基礎
## 第2章 1次元のデータ
## 第3章 2次元のデータ
## 第4章 確率
## 第5章 確率変数
## 第6章 確率分布
## 第7章 多次元の確率分布
## 第8章 大数の法則と中心極限定理
## 第9章 標本分布
- 全数調査
- 標本調査
### 母集団と標本
- 母集団
  - 興味がある集団全体を指す
- 標本
  - 分析のために取り出した(抽出という)一部を指す
- 母集団と母集団分布
  - パラメトリック : 母集団分布について全て知ることができる場合
  - ノンパラメトリック : いくつかのパラメータで母集団分布を決定できない場合
- 標本の抽出
  - 単純無作為抽出(単純ランダムサンプリング)
  - 系統抽出法
    - 母集団に番号を付け一番目を無作為に抽出し以後等間隔で抽出する
  - 層化無作為抽出法
    - 母集団の各層(性別、年代別など)ごとにランダムに抽出する
  - 多段抽出法
    - 例として、いくつかの県、いくつかの学校、いくつかの組、そこから生徒を抽出する
  - クラスター(集落)抽出法
    - 母集団を網羅的に分割した小集団から全員を対象とする
### 母数と統計量
- 統計量
  - 標本を要約市母集団の母数のさまざまな推測に使われる
  - 標本の平均、分散、標準偏差、中央値、最小値、最大値、相関係数
  - 統計量の確率分布を標本分布という
- 標本平均と標本分布
  - 標本から計算された平均、分散を言う
  - 母平均$\mu$、母分散$\sigma^2$ を考えていく
$$ \bar{X} = \frac{X_1 + X_2 + \cdots + X_n}{n} $$
  - 標本平均の期待値
$$ E(\bar{X}) = E(X_1 + X_2 + \cdots + X_n / n) = n\mu / n = \mu $$
  - 標本分散
$$ s^2 = \frac{1}{n-1}\{(X_1-\bar{X})^2 + (X_2-\bar{X})^2 + \cdots + (X_n-\bar{X})^2\} $$
  - 標本分散の期待値
$$ E(s^2) = \sigma^2 $$
$$ V(\bar{X}) = \frac{1}{n^2} V((X_1 + X_2 + \cdots + X_n)) = n\sigma^2 / n = \frac{\sigma}{n} $$
### 統計量の標本分布
### 有限母集団と有限母集団修正
## 第10章 正規分布からの標本
### 正規分布の性質
- 正規分布の期待値と分散
$$ E(X) = \mu, \ V(X) = \sigma^2  $$
- 標準正規分布の期待値と分散
$$ E(X) = 0, \ V(X) = 1  $$
### 分散が既知のときの標本平均の標本分布
$$ Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}  N(0, 1) $$
## 第11章 推定
## 第12章 仮説検定
## 第13章 回帰分析