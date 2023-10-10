---
title : How to PSD
Category : Vivration
Author : Makoto Yaugchi
---

# How to PSD

[TOC]

## 基礎からの周波数分析 参考サイト

- 小野測器 コラムより
- <https://www.onosokki.co.jp/HP-WK/eMM_back/backcontents.htm>

- Easy Copy MathJax
- <https://easy-copy-mathjax.nakaken88.com/all/#multiple-line-equations>

## パワースペクトル密度の計算

- フーリエスペクトル: 離散フーリエ変換(Discrete Fourier Transform, DFT)により求める
$$ X_k = \sum_{n=0}^{N-1} x_n e^{-j\frac{2 \pi}{N}kn} $$

- フーリエスペクトルは以下のように複素数(実部 + 虚部)で表される
$$ X(k) = X_R(k) + jX_I(k) $$
$$ or $$
$$ X(k) = |X(k)|e^{j\theta(f)} $$
  
  - $ |X(k)| $ を振幅スペクトル、$ \theta(k) $ を位相スペクトルという

  $$ |X(k)| = \sqrt{X_R^2(k) + X_I^2(k)} $$

  $$ \theta(k) = \tan^{-1} {\frac{X_I(k)}{X_R(k)}}$$

- 複素フーリエ係数: (フーリエスペクトルの実部 / N) + (フーリエスペクトルの虚部 / N)より求める
$$ C_k = \frac{X_R(k)}{N} + \frac{X_I(k)}{N} $$

- パワースペクトル: 2 * (複素フーリエ係数の絶対値 ** 2) で求めることができる
$$ P(k) = 2|C_k|^2$$
  
  - 振幅スペクトルより振幅を求め、振幅 ** 2 / 2 でもパワースペクトル求めることができる
  $$ P(k) = A^2 / 2, \quad A = \frac{|X(k)|}{N} $$

- パワースペクトル密度: パワースペクトル / 周波数分解能により求めることができる
$$ G(k) = \frac{P(k)}{\Delta f} ,\quad  \Delta f = \frac{1}{T} = \frac{f_s}{N} $$

### PSDを求めるスクリプト

```python
# psd.py
from numpy as np

inputData        ## 時系列データ
N = 2 ** 11      ## サンプリング点数
fs = 2000        ## サンプリング周波数
dt = 1 / fs      ## 時間分解能
T = N * dt       ## 時間窓長 
deltaF = fs / N  ## 周波数分解能

freq = np.fft.fftfreq(N, d=dt)
fourierSpectral = np.fft.fft(inputData)
powerSpectrum = 2 * ((fourierSpectral.real / N)**2 + (fourierSpectral.imag / N)**2)
powerSpectrumDensity = powerSpectrum / deltaF

```

## 以下詳細説明

### 数学的な基礎

周波数分析には数が気の知識が少なからず必要になる

- 微積分

$$ \lim_{x \rightarrow 0} \frac{\sin x}{x} = 1 $$

$$ \frac{d}{dx} \sin x = \cos x $$

$$ \frac{d}{dx} \cos x = \sin x $$

- 三角関数

$$ \cos\theta = x, \ \sin\theta = y, \ \tan\theta = \frac{y}{x} $$

$$ \cos^2\theta + \sin^2\theta = 1 $$

- 指数関数

$$ \frac{d}{dx} e^x = e^x $$

$$ \frac{d}{dx} \log_e x = \frac{1}{x} $$

$$ e^x = 1 + \frac{1}{1!}x + \frac{1}{2!}x^2 + \cdots = \sum_{n=0}^{\infty}\frac{1}{n!}x^n $$

- 階乗およびネイピア数を求めるスクリプト

```python
# factrial.py

def factiralFunc(n):
    value = 1
    for i in range(1, n+1):
        value *= i
    return value
value = factiralFunc(5)
```

```python
# NapierNumber.py
# 第13項迄求めると小数点9位まで一致する

from scipy.special import factorial

for i in range(1, 15):
    total = 1
    for j in range(1, i):
        total += (1 / factorial(j))
    print(i, round(total, 9))
```

- 複素数
  $$ i^2 = -1, \ i = \sqrt{-1} $$

  - 直角座標
  $$ z = a + i b $$

  - 複素平面上の絶対値
  $$ r = |z| = \sqrt{a^2 + b^2} = \sqrt{zz^\ast} $$

  - 偏角
  $$ \theta = \arg z = \arctan \frac{b}{a} $$

  - 極座標
  $$ z = r(\cos\theta + i\sin\theta) $$

    - 例

  $$
  z = 1+i\sqrt{3}
  = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2} \right)
  = 2 \left( \cos \frac{\pi}{3} + i \sin \frac{\pi}{3}\right)
  $$

- オイラーの公式
  $$ e^{ix} = \cos x + i \sin x $$

- 複素指数関数
  $$ z = r e^{i \theta} $$

- $ \pi, e, iの関係式$
  $$ e^{i\pi} = -1 $$

### フーリエ級数展開

どんな複雑な周期時間関数でも、その基本周波数およびその整数倍の周波数の三角関数の和で表すことができる

- $x(t)$を周期$T$の周期関数とする
  - 基本周波数$f_0$と基本角周波数$\omega_0$は

  $$ f_0 = \frac{1}{T}, \quad \omega_0 = 2 \pi f_0 = \frac{2\pi}{T} $$

  - 通常の三角関数による級数展開

  <!-- $$ \begin{align*}
  x(t)
  &= a_0 + \sum_{n=1}^{\infty} (a_n \cos n \omega_0 t + b_n \sin n \omega_0 t) \\
  &= a_0 + \sum_{n=1}^{\infty} X_n \cos (n \omega_0 t + \varphi_n),
  \ X_n = \sqrt{a_n^2 + b_n^2},
  \ \varphi_n = -\tan^{-1} \frac{b_n}{a_n}  \\
  \end{align*} $$ -->

  $$ a_n = \frac{2}{T}\int_0^\infty x(t) \cos n \ \omega_0 \ t \ dt $$

  $$ b_n = \frac{2}{T}\int_0^\infty x(t) \sin n \ \omega_0 \ t \ dt $$

  $$ a_0 = \frac{1}{T}\int_0^\infty x(t) \ dt $$

- 複素フーリエ級数展開

$$ x(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t} $$

$$ c_n = \frac{1}{T} \int_0^T x(t) e ^{-jn \omega_0 t} dt \quad (n = 0, \pm1, \pm2 \cdots) $$

### フーリエ変換

$$ (f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt $$

### デルタ関数

### フーリエ変換と畳み込み

### 時間信号のサンプリング

### 離散フーリエ変換 DFT その1

$$ X_k = \sum_{n=0}^{N-1}x_n e^{-j\frac{2\pi}{N}kn} $$
$$ n = 0, \pm1, \pm2 \cdots $$

### 高速フーリエ変換 FFT

### 離散フーリエ変換 DFT その2

### フーリエスペクトル

- スペクトル解析(フーリエ解析)
  - 音や振動などのような複雑な信号波形を基本的な周波数に分解してその強さを求めること
  - これを実行する際に最も一般的な方法がフーリエ変換技術

- フーリエスペクトル $ X(f) $
  - 周波数後tの振幅と位相情報を持つ複素数
  - 次元[mm × t] = 時間波形の次元[mm] × 時間の次元[t]
  - 通常は有限時間長 $T$ で除算した値をフーリエスペクトルとしている

$$ X(f) = X_R(f) + jX_I(f)  $$

$$ |X(f)| = \sqrt{X_R^2(f) + X_I^2(f)} $$

$$ \theta(f) = \tan^{-1}\frac{X_I(f)}{X_R(f)} $$

$$ X(f) = | X(f) |e^{j\theta(f)}  $$

$$ | X(f) | : 振幅スペクトル $$

$$ e^{j\theta(f)} : 位相スペクトル $$

### パワースペクトル

- パワースペクトル
  - 周波数の関数で元の時間信号に含まれる周波数毎の単位時間当たりのエネルギー(パワー)
  - スペクトル解析などの信号処理の分野のパワーは時間信号の2乗平均値を指す

周期Tの時間信号の2乗平均値
$$ \bar{x^2} = \frac{1}{T} \int_0^T x^2(t) \ dt $$

周期の内時間信号の2乗平均値
$$ \bar{x^2} = \lim_{T\rightarrow\infty} \frac{1}{T} \int_0^T x^2(t) \ dt $$

### パワースペクトル密度の求め方

- ランダム信号をFFT解析するとパワースぺクトルの各成分の振幅の値が得られる
- 値は、FFT計算の周波数分解能Δfに依存し、解析条件を変更すると値が変化する
- 解析結果の値がΔfに依存しない様に単位周波数幅あたりのパワー値で表現する

#### パワースペクトルと周波数分解能の関係

FFT解析を行う際の周波数レンジ、サンプル点数と周波数分解能の間には次の関係がある

- $$ ライン数[点] = サンプル点[点] / 2.56 $$
- $$ 周波数分解能 \Delta f [Hz] = 周波数レンジ[Hz] / ライン数[点] $$

図1に連続スペクトルを持つ信号をFFT解析して得られたパワースペクトルを示す



$$ \Delta f : 周波数分解能 $$

$$ f_s : サンプリング周波数 $$

$$ \Delta f = \frac{1}{T} = \frac{f_s}{N} $$


## note

Category : python
Author : Makoto Yaugchi
