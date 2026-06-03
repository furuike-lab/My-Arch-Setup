#!/bin/bash

set -e

echo "=== Restoring Arch environment ==="

# ~/.config 作成
mkdir -p ~/.config

echo "=== Restoring dotfiles ==="
cp -r .config/* ~/.config/

if [ -f .zshrc ]; then
    cp .zshrc ~/
fi

echo "=== Installing pacman packages ==="
sudo pacman -Syu --needed - < pkglist.txt

echo "=== Checking yay ==="

if ! command -v yay >/dev/null 2>&1; then
    echo "yay is not installed."
    echo "Install yay manually, then run this script again."
    exit 1
fi

echo "=== Installing AUR packages ==="
yay -S --needed - < aurlist.txt

echo "=== Done ==="
echo "Please log out and log back in."
