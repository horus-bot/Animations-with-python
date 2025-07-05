# 🎬 Animated GIF Creator

A simple yet powerful Python tool to create animated GIFs from multiple image files using PIL (Pillow).

## ✨ Features

- 🖼️ **Multi-format Support**: Works with various image formats (PNG, JPEG, GIF, etc.)
- 🎥 **Smooth Animations**: Creates seamless animated GIFs with customizable frame duration
- 🔄 **Loop Control**: Infinite loop animations for continuous playback
- 🚀 **Command Line Interface**: Easy-to-use CLI for batch processing
- 📦 **Lightweight**: Minimal dependencies with just PIL/Pillow

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/animated-gif-creator.git
   cd animated-gif-creator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

   Or install Pillow directly:
   ```bash
   pip install pillow
   ```

## 🚀 Usage

### Basic Usage
```bash
python main.py image1.png image2.jpg image3.gif
```

### Example
```bash
python main.py cartoon.gif cartoon2.gif
```

This will create an `animations.gif` file in the same directory.

## 📁 Project Structure

```
animated-gif-creator/
├── main.py              # Main application script
├── requirement.txt      # Python dependencies
├── README.md           # Project documentation
├── animations.gif      # Output animated GIF (generated)
└── example_images/     # Sample images for testing
    ├── cartoon.gif
    └── cartoon2.gif
```

## ⚙️ Configuration

The animation settings can be customized in the `animations()` function:

- **Duration**: Frame duration in milliseconds (default: 200ms)
- **Loop**: Number of loops (0 = infinite, default: 0)

```python
images[0].save(
    "animations.gif",
    save_all=True,
    append_images=[images[1]],
    duration=200,    # Frame duration
    loop=0          # Infinite loop
)
```

## 🔧 How It Works

1. **Input Processing**: Reads image file paths from command line arguments
2. **Image Loading**: Opens each image using PIL/Pillow
3. **Animation Creation**: Combines images into a single animated GIF
4. **Output Generation**: Saves the result as `animations.gif`

## 📋 Requirements

- Python 3.6+
- PIL/Pillow library

## 🎯 Use Cases

- Creating animated avatars
- Making simple animations for web projects
- Converting image sequences to GIFs
- Creating animated banners or logos
- Educational demonstrations

## 🔍 Example Output

Input: Multiple static images
```
image1.png → 🖼️
image2.png → 🖼️
image3.png → 🖼️
```

Output: Animated GIF
```
animations.gif → 🎬 (animated)
```

## 🐛 Troubleshooting

### Common Issues:

1. **"please mention .gif files to be compiled"**
   - Make sure to provide image file paths as arguments
   - Example: `python main.py image1.png image2.jpg`

2. **PIL/Pillow not found**
   - Install Pillow: `pip install pillow`

3. **File not found errors**
   - Ensure image file paths are correct
   - Use absolute paths if needed


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

