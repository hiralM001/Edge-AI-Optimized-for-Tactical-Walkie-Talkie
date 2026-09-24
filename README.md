# 📻 Tactical Edge-AI Walkie-Talkie

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-Military_AI-red.svg)
![Rockchip](https://img.shields.io/badge/Rockchip-RV1106-green.svg)
![RNNoise](https://img.shields.io/badge/RNNoise-C_Library-orange.svg)
![SIH 2026](https://img.shields.io/badge/Smart_India_Hackathon-2026-blueviolet.svg)

> **A professional-grade Tactical Edge-AI Walkie-Talkie integrating a Rockchip RV1106 SoC and DRA818V Transceiver for Real-Time (<150ms) Military Noise Cancellation.**

---

## 🚀 Project Overview
*(Drag and drop your final hardware prototype or component photo here)*

This project demonstrates an advanced Edge-AI communication device designed for extreme tactical environments. By utilizing highly optimized C-libraries (**RNNoise**) and custom **PyTorch-trained models**, the system effectively filters out heavy military background noises—such as helicopters, tanks, bomb blasts, and gunshots—directly on the edge hardware with zero internet dependency.

---

## 🧠 System Architecture & Data Flow

```mermaid
graph TD
    A["🎤 INMP441 Mic"] -->|Raw Audio| B("Rockchip RV1106 SoC")
    B -->|Noisy Data| C{"RNNoise AI Filter"}
    C -->|Clean Voice| D["DRA818V Module"]
    D -->|Radio Signal| E(("Antenna"))

    F["Incoming Radio"] -->|Receives| D
    D -->|Radio Audio| B
    B -->|Output Voice| G["🔊 2W Speaker"]

    style B fill:#007acc,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#e63946,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#2a9d8f,stroke:#fff,stroke-width:2px,color:#fff
