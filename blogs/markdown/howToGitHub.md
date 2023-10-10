---
Title : How to Github
Category : python
Author : Makoto Yaugchi
---

# How To GitHub

[TOC]

## Overview

- 簡単にGitHubの使い方をまとめておく
- proxyの設定が必要となる

## GutHubでリモートリポジトリを作成

- GitHubにログイン
- リポートリポジトリ作成

## Gitの設定

- ローカルリポジトリ作成
- ローカルリポジトリにファイルをaddする
- ローカルリポジトリにcommitする
- ローカルリポジトリからリモートリポジトリにremoteする
- リポートリポジトリにファイルをpushする

## command

```PowerShell
# create a new repository on the command line

git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/<userID>/<repositoryName>.git
git push -u origin
# 2回目から
git push
```

```PowerShell
# push an existing repository from the command line

git remote add origin https://github.com/<userID>/<repositoryName>.git
git branch -M main
git push -u origin
```

## note

Category : python
Author : Makoto Yaugchi
