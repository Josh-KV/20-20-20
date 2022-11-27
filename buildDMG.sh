#!/bin/sh
# AUTHOR: Martin Fitzpatrick
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/20-20-20.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/20-20-20.dmg" && rm "dist/20-20-20.dmg"
create-dmg \
  --volname "20-20-20" \
  --volicon "20-20-20.icns" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "20-20-20.app" 175 120 \
  --hide-extension "20-20-20.app" \
  --app-drop-link 425 120 \
  "dist/20-20-20.dmg" \
  "dist/dmg/"
