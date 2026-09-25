# Tactical Edge-AI Walkie-Talkie (Prototype Phase)
Real-time noise cancellation for extreme tactical environments using Rockchip RV1106 and DRA818.

## ⚠️ Note :
This repository contains the **Proof of Concept (PoC) prototype** code for our Smart India Hackathon project. 
* **Current Prototype Code:** In `walkie_demo.py`, you will notice Bluetooth connectivity logic. We temporarily implemented Bluetooth audio routing to test edge-AI latency, buffer management, and chunk optimizations without needing full radio licenses during the initial software phase.
* **Final Physical Build:** In the actual hardware deployment, the Bluetooth logic will be completely bypassed. The system will rely strictly on the **DRA818 VHF/UHF RF module** for secure, analog radio transmission with negligible digital packetization delay.

## 🎥 Prototype Demonstration Video
Watch our working prototype and real-time noise cancellation test here:
👉 **https://drive.google.com/file/d/1q5VB-f_a27Qz8xjuAoVx6N8-TtIMXN7g/view**

## Project Overview
We built this project to solve a major issue in tactical communication: heavy background noise like wind, machinery, or battlefield sounds. Instead of sending noisy audio over the radio, this walkie-talkie cleans the audio *before* transmission using an AI model running locally on the edge hardware. It requires zero internet connection.

## How It Works (Audio Workflow)
The entire pipeline is optimized for real-time processing. Here is the exact data flow:

[ Environment Noise + Voice ]
            |
            v
   ( INMP441 I2S Mic )
            |
            |--- Raw Noisy Audio Buffer
            v
 [ Rockchip RV1106 SoC ]  <====>  [ RNNoise C-Library ]
            |                     *Filters noise in <150ms*
            |
            |--- Clean Voice Output
            v
 [ DRA818 VHF RF Module ]
            |
            |--- Analog Radio Transmission
            v
     (( VHF Antenna ))
            |
            v
 [ Receiving Walkie-Talkie ] ---> [ MAX98357A Amp ] ---> ( 2W Speaker )

## Key Features & Optimizations
* **Edge-AI on 256MB RAM:** We managed to run the RNNoise model directly on the RV1106's NPU/CPU without maxing out the system memory.
* **Ultra-Low Latency:** The entire audio pipeline takes <150ms, ensuring real-time communication.
* **Audio Stuttering Fix:** During our prototype wireless testing, we fixed audio lag/stuttering by heavily optimizing the Python chunk size (`CHUNK = 4800` instead of the standard 1920) to maintain a continuous stream.

## Hardware Used (Prototype)
* **Board:** Rockchip RV1106 SoC (256MB RAM)
* **Audio:** INMP441 Microphone (I2S), MAX98357A Amplifier, 2W Speaker
* **Radio:** DRA818V VHF Transceiver + VHF Antenna
* **Power:** 5V Li-Po Battery, TP4056 1A Charging Module, LD117V33 3.3V Regulator
* **Misc:** 0.96" OLED I2C Display, Push-To-Talk (PTT) Switch
