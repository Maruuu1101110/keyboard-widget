#!/bin/bash

# === Color Codes ===
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting installation of keyboard-widget...${NC}"

# === Don't run as root ===
if [ "$EUID" -eq 0 ]; then 
    echo -e "${RED}Please do not run this script as root${NC}"
    exit 1
fi

# === Confirm update ===
read -p "Do you want to update the system packages before installing? [y/N]: " update_confirm
if [[ "$update_confirm" =~ ^[Yy]$ ]]; then
    sudo pacman -Syu
fi

# === Check Python version (>= 3.8) ===
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')
required_version="3.8.0"

version_check=$(python3 -c "from packaging import version; print(version.parse('$python_version') >= version.parse('$required_version'))")
if [[ "$version_check" != "True" ]]; then
    echo -e "${RED}Python 3.8 or higher is required. You have $python_version${NC}"
    exit 1
fi

# === Ensure pip is installed ===
if ! command -v pip3 &>/dev/null; then
    echo -e "${YELLOW}Installing pip...${NC}"
    sudo pacman -S --noconfirm python-pip
fi

# === Install system dependencies ===
echo -e "${YELLOW}Installing system dependencies...${NC}"
sudo pacman -S --noconfirm \
    python-gobject \
    gtk4 \
    cairo \
    pkgconf \
    python-pip \
    python-virtualenv

# === Setup virtual environment ===
echo -e "${YELLOW}Setting up virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# === Install Python dependencies ===
echo -e "${YELLOW}Installing Python dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# === Desktop entry setup ===
echo -e "${YELLOW}Creating desktop entry...${NC}"
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/keyboard-widget.desktop << EOL
[Desktop Entry]
Name=Keyboard Widget
Comment=A customizable keyboard overlay widget
Exec=python3 $(pwd)/main.py
Terminal=false
Type=Application
Categories=Utility;
EOL

echo -e "${GREEN}Installation complete!${NC}"
echo -e "${YELLOW}You can now run the widget by:${NC}"
echo -e "1. Using the desktop entry"
echo -e "2. Running 'source venv/bin/activate && python main.py'"
echo -e "\n${YELLOW}Reminder:${NC} Update the keyboard device path in main.py if needed."
