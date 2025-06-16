# Keyboard Overlay

A customizable keystroke overlay widget for Linux that displays your keyboard inputs in real-time. Built with GTK4 and Python.

## Features

- Real-time keystroke visualization
- Customizable overlay widget
- Low-latency input detection
- GTK4-based modern interface

## Requirements

- Python 3.8+
- GTK4
- Linux OS
- Input device access permissions

## Installation

### From source

1. Clone the repository:
```bash
git clone https://github.com/Maruuu1101110/keyboard-widget.git
cd keyboard-widget
```

2. Install dependencies:
```bash
sh setup.sh
```
3. Run widget:
```bash
sh run.sh
```
## Usage

You can run the widget via:
```bash
python main.py
```

or 

```bash
sh run.sh
```

You can also bind it to your systems config, Hyprland for example:
```bash
bind = $mainMod, K, exec, /path/to/run.sh
```

## Configuration

### Themes

To customize the appearance, open any `.css` file in:
`~/.config/keyboard-widget/themes`, you can even add your own theme.

### Device Configuration
If the `run.sh` can't detect your device: 

You can check for it by yourself:
```bash
ls -l /dev/input/by-id
```
and check for your keyboard and edit this line `"device_path": "your/device/path"` in `~/.config/keyboard/config.json`.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with GTK4
- Inspired by various keystroke visualization tools 