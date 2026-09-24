# Tactical Edge-AI Walkie-Talkie
Real-time noise cancellation for extreme tactical environments using Rockchip RV1106 and DRA818.

## Project Overview
We built this project to solve a major issue in tactical communication: heavy background noise like wind, machinery, or battlefield sounds. Instead of sending noisy audio over the radio, this walkie-talkie cleans the audio *before* transmission using an AI model running locally on the edge hardware. It requires zero internet connection.

## How It Works (Audio Workflow)
The entire pipeline is optimized for real-time processing. Here is the step-by-step data flow:

1. **Input:** The INMP441 I2S microphone captures raw, noisy audio from the environment.
2. **Edge-AI Processing:** The Rockchip RV1106 takes the audio buffer and runs the RNNoise C-library to filter out background noise instantly.
3. **Transmission:** The clean audio is routed to the analog DRA818 VHF module and broadcasted via the antenna.
4. **Receiving/Output:** Incoming radio signals are processed by the board and played loud and clear through the MAX98357A amplifier and 2W speaker (or routed via Bluetooth).

## Key Features & Optimizations
* **Edge-AI on 256MB RAM:** We managed to run the RNNoise model directly on the RV1106's NPU/CPU without maxing out the system memory.
* **Ultra-Low Latency:** The entire audio pipeline takes <150ms, ensuring real-time communication.
* **Zero Digital Delay:** By integrating the analog DRA818 RF module, we avoided standard digital packetization delays.
* **Fixed Bluetooth Stuttering:** We noticed lag and audio stuttering during wireless output. We fixed this by heavily optimizing the Python chunk size (`CHUNK = 4800` instead of the standard 1920) to maintain a continuous, smooth audio stream.

## Hardware Used
* **Board:** Rockchip RV1106 SoC (256MB RAM)
* **Audio:** INMP441 Microphone (I2S), MAX98357A Amplifier, 2W Speaker
* **Radio:** DRA818V VHF Transceiver + VHF Antenna
* **Power:** 5V Li-Po Battery, TP4056 1A Charging Module, LD117V33 3.3V Regulator
* **Misc:** 0.96" OLED I2C Display, Push-To-Talk (PTT) Switch

## Code Structure
Everything runs through `walkie_demo.py`. This main script handles the I2S microphone capture, passes the audio frames to the C-library for AI processing, manages memory buffers, and routes the final audio to the speaker or Bluetooth output simultaneously.
