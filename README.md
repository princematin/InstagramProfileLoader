# Instagram Profile Loader

A simple Python desktop application built with Tkinter that retrieves and displays public Instagram profile information using Instaloader.

## Features

- Retrieve an Instagram profile by username.
- Display the profile picture.
- Show the username and biography.
- Display follower and following counts.
- Simple graphical user interface.

## Technologies Used

- **Python** — Core programming language
- **Tkinter** — Graphical user interface
- **Instaloader** — Instagram profile data retrieval
- **Pillow (PIL)** — Image processing
- **urllib** — Downloading profile images
- **io** — Handling image data in memory

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd InstagramProfileLoader
   ```

3. Install the required dependencies:

   ```bash
   python -m pip install instaloader pillow
   ```

4. Run the application:

   ```bash
   python main.py
   ```

Replace `main.py` with your Python filename if it is different.

## How to Use

1. Launch the application.
2. Enter an Instagram username.
3. Click **Click to show**.
4. View the profile picture, biography, followers, and following count.

## Notes

- Profile information availability depends on Instagram's access restrictions and the Instaloader library.
- Private profiles and temporary access restrictions may prevent the application from retrieving information.
- The current version does not include error handling for invalid usernames or network failures.

## Future Improvements

- Add error handling and user-friendly error messages.
- Improve the interface layout and responsiveness.
- Add loading indicators.
- Improve image sizing and display.

## License

This project is available for learning and personal use. Add a specific open-source license if you intend to distribute it under defined terms.