# TIMER APP

A Pomodoro-style countdown timer application built with Python and Tkinter. The app visually displays the remaining time, supports start and reset functionality, and helps users manage focused work sessions using a clean and interactive GUI.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

This project implements a simple timer application, ideal for productivity techniques like Pomodoro. Users can initiate a countdown, pause or reset it, and visually track the time left on the screen. The project is built entirely using Python’s Tkinter library and demonstrates interactive UI design principles.

## How it Works

1. **Start the Timer**: Click the "Start" button to begin the countdown.
2. **Visual Countdown**: Time is shown in MM:SS format and updates every second.
3. **Reset**: Use the "Reset" button to stop the current session and reset the timer back to its initial state.
4. **Custom Duration** *(optional)*: Code can be adjusted to support different countdown durations like 25-min focus or 5-min break sessions.

## Technologies Used

- **Python**: Core programming logic
- **Tkinter**: Used for GUI components such as buttons, canvas, and labels
- **Math Module**: To format time into minutes and seconds

## Lessons Learned

- **GUI Programming**: Improved understanding of creating interactive desktop apps with Tkinter
- **Time Management**: Used `after()` method for scheduling recurring timer updates
- **Encapsulation**: Organized the timer logic within a class-based structure
- **Dynamic UI Updates**: Learned how to change canvas and label text dynamically during runtime
