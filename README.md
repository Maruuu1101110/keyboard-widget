# Keystrokes CP

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
pip install -r requirements.txt
```

3. Install the package:
```bash
pip install -e .
```

## Usage

Run the application with:

```bash
python main.py
```

By default, the application looks for a keyboard device at `/dev/input/by-id/keyboard-kbd`. You can modify this path in the source code to match your keyboard device.

## Configuration

The overlay widget can be customized by modifying the parameters in `overlay_widget.py`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with GTK4
- Inspired by various keystroke visualization tools 