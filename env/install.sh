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
sudo xattr -dr com.apple.quarantine /Applications/Calendars.app
sudo xattr -dr com.apple.quarantine /Applications/LINE.app
sudo xattr -dr com.apple.quarantine /Applications/KakaoTalk.app
