#!/bin/bash

WIDGET_PATH="/usr/local/share/keyboard-widget/main/main.py"

if [ ! -f "$WIDGET_PATH" ]; then
  echo "❌ Keystroke widget not found. Please install it first using setup.sh"
  exit 1
fi

python3 "$WIDGET_PATH"
