#!/bin/bash

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew bundle --file=./Brewfile

sudo xattr -dr com.apple.quarantine /Applications/iTerm.app
sudo xattr -dr com.apple.quarantine /Applications/KeepingYouAwake.app
sudo xattr -dr com.apple.quarantine /Applications/Google\ Chrome.app
sudo xattr -dr com.apple.quarantine /Applications/Firefox.app
sudo xattr -dr com.apple.quarantine /Applications/AppCleaner.app
sudo xattr -dr com.apple.quarantine /Applications/Spectacle.app
sudo xattr -dr com.apple.quarantine /Applications/Dropbox.app
sudo xattr -dr com.apple.quarantine /Applications/CalendarFree.app
sudo xattr -dr com.apple.quarantine /Applications/LINE.app
sudo xattr -dr com.apple.quarantine /Applications/KakaoTalk.app
sudo xattr -dr com.apple.quarantine /Applications/JetBrains\ Toolbox.app
sudo xattr -dr com.apple.quarantine /Applications/Docker/Docker\ Quickstart\ Terminal.app
sudo xattr -dr com.apple.quarantine /Applications/Docker/Kitematic.app

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

# zsh-autosuggestions
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

npm install --global pure-prompt

curl -sLf https://spacevim.org/install.sh | bash
