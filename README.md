# My-Arch-Setup

Arch Linux 環境復元用バックアップ

## 保存内容

* Hyprland 設定
* Waybar 設定
* Fcitx5 設定
* Ghostty 設定
* Obsidian 設定
* pkglist.txt (pacman パッケージ一覧)
* aurlist.txt (AUR パッケージ一覧)
* restore.sh

## 新規Archインストール後の復元手順

### 1. リポジトリ取得

```bash
git clone git@github.com:furuike-lab/My-Arch-Setup.git
cd My-Arch-Setup
```

### 2. yay をインストール

```bash
sudo pacman -S --needed git base-devel

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

### 3. 復元実行

```bash
cd ~/My-Arch-Setup
chmod +x restore.sh
./restore.sh
```

### 4. 再ログイン

ログアウトまたは再起動を行う。

## 注意

以下は GitHub に保存していない。

* Google Chrome のログイン情報
* Discord のログイン情報
* rclone の認証情報
* Google Drive のデータ本体

必要に応じて再設定すること。

## 個人データ

Google Drive に保存。

## 最終更新

2026-06-03

