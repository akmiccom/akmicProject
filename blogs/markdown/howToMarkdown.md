---
title : How to markdown
Category : python
Author : Makoto Yaugchi
---

# How to markdown

markdown記法のまとめ

[TOC]


## Overview
自分が調べた順番に記載していく。

## Basic Syntax
[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
|     Element     | Markdown Syntax                  |
| :-------------: | :------------------------------- |
|  comment out    |  \<!-- -->                       |
|     Heading     | # h1 <br> # h2                   |
|      Bold       | \*\*bold text\*\*                |
|     italic      | \*italicezed text\*              |
|   Blockquote    | > blockquote                     |
|  Ordered List   | 1. <br> 2. <br> 3.               |
| unordered List  | - <br> - <br> -                  |
|      Code       | \`code` <br>  \```python<br>```  |
|      Link       | \[title](http://www.example.com) |
|      Image      | \!\[alt text](img/image.jpg)     |
|     Escape      | \                                |
| Hoeizontal Rule | --- *** ___                      |
| Space | \&thinsp;&nbsp; <br> &nbsp <br> &ensp <br> &emsp |

## Extended Syntax
|   Element   | Markdown Syntax |
| :---------: | :------- |
|    Table    | \| syntax \| description \| <br> \| ---- \| ---- \| <br> \| Header \| Title \|  <br> \| Paragraph \| Text \| |
|  Footnote   | Here's a sentence with a footnote.[^1] <br> [^1]: This is the footnote                                        |
| Heading ID  | ### My Greate Heading {# custom-id } |
|  Highlight  | \==very important words.== |
| Strikethrogh | \~~The world is flat~~ |
| Emoji | \:joy: &thinsp;&nbsp; [Copying and Pasting Emoji](https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji) |
| Note | \:::note info <br> Information <br> :::|
|  Subscript  | h~2~0 |
| SuperScript | X^2^ |

## Mathjax Syntax
- [Mathjaxの使い方](https://www.eng.niigata-u.ac.jp/~nomoto/download/mathjax.pdf)
- \$\$ \\frac{1}{2} \$\$
- \\[ \\frac{1}{2} \\]
- \frac{1}{2} と書くと以下のように分数が表現できる

$$ \frac{1}{2} $$

## Features

### markdownの特徴

- 覚えやすい
- HTMLに変換可能
- 対応ツールが多い

### 使えるEditor

- Visual Studio Code
- Atom
- MacDown

## note

Category : python
Author : Makoto Yaugchi
