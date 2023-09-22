# PythonCryptoTracker 📈

PythonCryptoTracker is a comprehensive tool that leverages the [CryptoCompare.com](http://cryptocompae.com/) API to track cryptocurrency prices. With a user-friendly interface and real-time data fetching capabilities, this tracker is designed for both beginners and seasoned crypto enthusiasts.

## Features 🌟

- **Real-time Data**: Fetches the latest cryptocurrency prices from [CryptoCompare.com](http://cryptocompae.com/).
- **Historic Data**: Access historical data for a comprehensive analysis.
- **Custom Icons**: Customizable icons for MacOS and Windows.
- **Packaging**: Easily package the application using PyInstaller.

## Getting Started 🚀

### Prerequisites

1. Python 3.7+
2. [Free developer API access](https://min-api.cryptocompare.com/) from [CryptoCompare.com](http://cryptocompae.com/).

### Installation

1. Clone the repository.
2. Set up a virtual environment:
   ```bash
   python -m venv _venv
   source _venv/bin/activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
### Running the application
Execute the main script:
```bash
python crypto.py
```

### Packaging the Application 📦
1. Install PyInstaller:
```bash
pip3 install pyinstaller
```
2. Navigate to your project's directory and run:
```bash
pyinstaller crypto.py
```

### Custom Icons 🎨
- For MacOS: Use the makeicns.sh file to generate an .icns bundle. Execute the following:
  ```bash
  chmod +x makeicns.sh
  ./makeicns.sh bitcoin-icon.png
  ```
- For Windows: Generate an .ico file by loading a PNG into Gimp and resizing it to 3 separate layers (64,32,16). Save it as .ico.

### Contributing 🤝
Contributions are welcome! If you have any improvements, features, or bug fixes, feel free to create a pull request.

> Note: This project is an educational example from [LearnPyQT.com](https://www.learnpyqt.com/examples/bitcoin-exchange-tracker/).
