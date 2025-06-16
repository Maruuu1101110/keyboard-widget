#!/bin/bash

set -e

echo "🛠️ Starting Keystroke-CP setup..."

# Function: Detect Linux distro
detect_distro() {
  if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "$ID"
  else
    echo "unknown"
  fi
}

# Function: Ask Y/n with default N
ask() {
  read -rp "$1 [y/N]: " response
  case "$response" in
  [yY][eE][sS] | [yY]) return 0 ;;
  *) return 1 ;;
  esac
}

# Function: System install for Arch
install_arch_deps() {
  echo "📦 Installing system dependencies for Arch..."
  sudo pacman -S --needed python python-pip gtk4 python-gobject python-evdev git
}

# Function: System install for other distros
install_other_deps() {
  echo "📦 Installing system dependencies (non-Arch)..."
  if command -v apt >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y python3 python3-pip libgtk-4-dev python3-gi python3-evdev git
  else
    echo "⚠️ Package manager not supported. Please install dependencies manually."
    exit 1
  fi
}

# Function: Virtualenv install (isolated)
install_with_venv() {
  echo "📦 Installing with virtualenv..."
  python3 -m venv .temp_env
  source .temp_env/bin/activate
  pip install -r requirements.txt

  INSTALL_DIR="/usr/local/share/keyboard-widget"
  echo "🚚 Copying files to $INSTALL_DIR"
  sudo mkdir -p "$INSTALL_DIR"
  sudo cp -r ./* "$INSTALL_DIR"
  sudo ln -sf "$INSTALL_DIR/run.sh" /usr/local/bin/keyboard-widget

  deactivate
  rm -rf .temp_env
  echo "✅ Installed and cleaned up!"
}

# THEME PLACEMENT
mkdir ~/.config/keyboard-widget
cp -r themes ~/.config/keyboard-widget/themes

# MAIN LOGIC
DISTRO=$(detect_distro)
echo "🧠 Detected distro: $DISTRO"

# UPDATE SYSTEM (RECOMMENDED)
if ask "🔄 Do you want to update your system before continuing?"; then
  if [ "$DISTRO" = "arch" ]; then
    sudo pacman -Syu
  elif [ "$DISTRO" = "debian" ] || [ "$DISTRO" = "ubuntu" ]; then
    sudo apt update && sudo apt upgrade -y
  else
    echo "⚠️ Update not supported for unknown distro."
  fi
fi

# INSTALL METHOD
if ask "📦 Do you want to use a virtual environment (recommended)?"; then
  install_with_venv
else
  if [ "$DISTRO" = "arch" ]; then
    install_arch_deps
  else
    install_other_deps
  fi
  echo "📦 Installing Python packages system-wide..."
  pip install --break-system-packages -r requirements.txt || {
    echo "⚠️ System pip installation failed. Try again with --break-system-packages or use the virtualenv option."
    exit 1
  }
fi


echo "🚀 Done! You can now launch the widget using: run.sh "
