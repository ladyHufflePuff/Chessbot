
# Chessmate: A Chess-Playing Robot

---

Chessmate is an autonomous chess-playing robot designed to engage human opponents in a game of chess. The project utilizes a [Yahboom Dofbot robotic arm](http://www.yahboom.net/home), controlled by a Raspberry Pi 4, to physically move chess pieces on a standard chessboard. A camera module is integrated to detect and map the chessboard state, while chess logic and AI calculate moves in real time. This combination of computer vision, artificial intelligence, and robotics enables chessmate to play effectively as a human companion.

This guide details the setup process for running the Chessmate robot, including configuring the hardware and software components.


## Features

---

- **Autonomous Gameplay**: Chessmate uses AI to calculate moves and plays chess against a human opponent in real-time.

- **Robotic Piece Manipulation**: A Yahboom Dofbot robotic arm precisely moves chess pieces on a standard chessboard.

- **Real-Time Chessboard Detection**: A camera module captures and processes the chessboard state, mapping piece positions to an 8x8 matrix.

- **Interactive Grid Alignment**: Grid alignment functionality ensures accurate detection and mapping of the physical chessboard.

- **Chess Logic Integration**: Implements chess rules, move validation, and strategies using the Python `chess` library.

## File Structure

---

```
Chessmate/
├── 0.py_install/                       # Dofbot arm library and setup files
├── example_code/                       # Troubleshooting code
│   ├── arm/                            # For Dofbot arm
│   └── cam/                            # For camera module
├── source_code/                        # Main source code
│   ├── arm_position.json               # Arm servo angles for chess squares
│   ├── chessboard_mapping.json         # Coordinates for chess squares
│   ├── grid_overlay.ipynb              # Maps chessboard on live footage
│   ├── main.ipynb                      # Main chess-playing robot code
│   └── output.png                      # GUI of current game state
├── README.md                           # Project documentation
└── .gitignore                          # Files and folders to exclude

```

## Requirements

---

### Hardware
- Yahboom Dofbot AI Vision Robotic Arm with ROS python programming for Raspberry Pi 4
- Raspberry Pi 4 running Raspberry Pi OS
- Camera module for live video capture
- A standard chessboard with chess pieces

### Software
- Python 3.11
- Jupyter notebook
- Stockfish game engine
- Required Python libraries (see installation instruction below)

## Setup Instructions

___

### 1. Clone the Repository
```bash
git clone https://github.com/ladyHufflePuff/Chessmate.git
cd Chessmate
```

### 2. Clone the Stockfish Repository
This step fetches the licenced chess engine
```bash
cd source_code
git clone https://github.com/official-stockfish/Stockfish.git Stockfish
```

### 3. Build the Stockfish Executable
```bash
cd Stockfish/src
make -j profile-build
```

### 4. Create a Virtual Environment
```bash
cd ..
python3 -m venv venv
```

### 5. Activate the Virtual Environment
```bash
source venv/bin/activate
```

### 6. Install Dependencies
```bash
pip install opencv-python chess cairosvg numpy asyncio jupyterlab
```

### 7. Launch Jupyter Lab
```bash
jupyter lab
```

## Usage

---

### Grid Alignment
1. Open the `grid_overlay.ipynb` notebook in Jupyter Lab
2. Follow the instructions to overlay a grid on the live video feed
3. Align the grid with your physical chessboard to ensure accurate mapping

### Run the Chess Program
1. Open the `main.ipynb` notebook
2. Execute the cells step-by-step to start the chess-playing robot
3. The system will detect chessboard changes, calculate moves and execute them using the robotic arm


## Disclaimer

---

This project is intended solely for educational purposes as part of a school project and is not licensed for public or commercial use. The code, scripts, and materials provided are as-is and come without any warranties or guarantees.

The Stockfish library is not included in this repository as it is licensed software. This project does not redistribute or modify the Stockfish library in any way. Users are advised to refer to the [Stockfish GitHub repository](https://github.com/official-stockfish/Stockfish) for more information, including licensing details and instructions on how to download and use the library.

Unauthorized use, modification, or distribution of this code or materials is strictly prohibited without explicit permission from the contributors. By accessing or using the project, you agree to these terms and acknowledge the contributors' intellectual property rights.

# Contributors

---

* [Uchechi Johnson](https://github.com/ladyHufflePuff)
* [Nomsa Kachere](https://github.com/tknomsa)
* [Janice Muthoni](https://github.com/jahneeese)
