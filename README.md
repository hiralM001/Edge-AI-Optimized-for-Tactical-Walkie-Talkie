# Edge-AI Walkie-Talkie (Tactical Real-Time Noise Cancellation)

This project implements a next-generation walkie-talkie solution using the **Rockchip RV1106 SoC** paired with a **DRA818 RF module**, designed for tactical environments requiring clear communication.

The core innovation is the integration of **real-time AI-based noise cancellation** running directly on the edge. This cleans up the audio signal at the source before transmission, ensuring high-intelligibility communication even in extreme noise (e.g., machinery, battlefield, wind).

-> Key Features

*   **Edge-AI Processing:** Powered by the **RV1106's built-in NPU/CPU**, executing the **RNNoise** model (C-library integration) in real-time.
*   **Low-Latency Performance:** Achieves tactical-grade latency of <150ms for the full audio pipeline.
*   **DRA818 RF Integration:** Analog RF module handles transmission with zero digital packetization delay.
*   **Wireless Bluetooth Output (Optimized):** Supports wireless audio output. The system has been specifically optimized to resolve audio stuttering/lag on wireless devices by optimizing the Python chunk size (`CHUNK = 4800` vs standard 1920) to ensure a smooth, continuous audio stream.
*   **Resource Efficient:** Optimized Python/C implementation to run simultaneously within the constraints of the 256MB RV1106 platform.

-> Hardware Components Used

1.  Rockchip RV1106 SoC (256MB RAM)
2.  INMP441 Microphone Module (I2S)
3.  Speaker Amplifier Module MAX98357A (I2S)
4.  Speaker 2W
5.  DRA818V VHF Transceiver Module
6.  0.96" OLED I2C Display
7.  TP4056 1A Charging Module
8.  LD117V33 3.3V Voltage Regulator
9.  VHF Antenna & Power Switch
10.  5V Li-Po Battery

-> Project Code Details
The main processing logic is contained in `walkie_demo.py`. This script manages microphone capture, C-library AI invocation, buffer management, and simultaneous wireless/wired output.
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-Military_AI-red.svg)
![Rockchip](https://img.shields.io/badge/Rockchip-RV1106-green.svg)
![RNNoise](https://img.shields.io/badge/RNNoise-C_Library-orange.svg)
