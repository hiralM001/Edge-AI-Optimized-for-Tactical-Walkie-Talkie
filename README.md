# 📻 Tactical Edge-AI Walkie-Talkie
**Real-Time Noise Cancellation for Extreme Environments**

> *A professional-grade Tactical Edge-AI Walkie-Talkie integrating a Rockchip RV1106 SoC, DRA818 RF module, and RNNoise C-library for real-time, negligible-latency noise cancellation with optimized Bluetooth audio streaming.*

---

## 🎯 Project Overview
This project implements a next-generation walkie-talkie solution using the **Rockchip RV1106 SoC** paired with a **DRA818 RF module**, designed specifically for tactical environments requiring crystal-clear communication.

**The Core Innovation:** Integration of **real-time AI-based noise cancellation** running directly on the edge. This cleans up the audio signal at the source before transmission, ensuring high-intelligibility communication even in extreme noise (e.g., heavy machinery, battlefield, high wind).

---

## ✨ Key Features
* 🧠 **Edge-AI Processing:** Powered by the **RV1106's built-in NPU/CPU**, executing the **RNNoise** model (C-library integration) in real-time.
* ⚡ **Low-Latency Performance:** Achieves tactical-grade latency of **<150ms** for the full audio pipeline.
* 📡 **DRA818 RF Integration:** Analog RF module handles transmission with zero digital packetization delay.
* 🎧 **Optimized Bluetooth Streaming:** Supports wireless audio output. The system has been specifically optimized to resolve audio stuttering/lag on wireless devices by optimizing the Python chunk size (`CHUNK = 4800` vs standard `1920`) to ensure a smooth, continuous audio stream.
* 🔋 **Resource Efficient:** Highly optimized Python/C implementation running seamlessly within the constraints of the 256MB RV1106 platform.

---

## 🛠️ Hardware Components

| Category | Component Details |
| :--- | :--- |
| **Core Processing** | Rockchip RV1106 SoC (256MB RAM) |
| **Audio Input** | INMP441 Microphone Module (I2S) |
| **Audio Output** | Speaker Amplifier Module MAX98357A (I2S) + 2W Speaker |
| **Radio System** | DRA818V VHF Transceiver Module + VHF Antenna |
| **Display** | 0.96" OLED I2C Display |
| **Power Management** | 5V Li-Po Battery, TP4056 1A Charger, LD117V33 Regulator & Power Switch |

---

## 💻 Project Code Details
The main processing logic is contained in `walkie_demo.py`. 

This core script efficiently manages:
- 🎤 **Microphone capture**
- 🧠 **C-library AI invocation** 
- 🗄️ **Buffer management**
- 📶 **Simultaneous wireless/wired output**
