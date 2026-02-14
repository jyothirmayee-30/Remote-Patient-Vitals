# 🏥 Remote Patient Vitals Monitor

A professional-grade healthcare IoT solution designed for remote patient monitoring. It captures critical biometric data and streams it securely to healthcare providers.

## 🚀 Features
- **Biometric Streaming:** Real-time Heart Rate (BPM) and Blood Oxygen (SpO2).
- **Abnormal Rhythm Detection:** Flags tachycardia or bradycardia events.
- **Wireless Portability:** Utilizes the Pico W's low-power WiFi for untethered use.
- **Medical Dashboard:** A clean, high-visibility UI for clinical data review.

## ⚙️ Engineering Logic
- **Hardware:** Raspberry Pi Pico W interfaces with the MAX30102 sensor via I2C.
- **Software:** Python implements a moving average filter to smooth raw PPG (Photoplethysmogram) data for accurate heart rate calculation.
