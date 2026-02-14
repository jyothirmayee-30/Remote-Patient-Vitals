#include <WiFi.h>
#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

MAX30105 particleSensor;
const byte RATE_SIZE = 4; 
byte rates[RATE_SIZE]; 
long lastBeat = 0;
float beatsPerMinute;

void setup() {
  Serial.begin(115200);
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) { while (1); }
  particleSensor.setup(); 
  particleSensor.setPulseAmplitudeRed(0x0A); 
  // WiFi setup for Pico W
}

void loop() {
  long irValue = particleSensor.getIR();
  if (checkForBeat(irValue) == true) {
    long delta = millis() - lastBeat;
    lastBeat = millis();
    beatsPerMinute = 60 / (delta / 1000.0);
    
    // Logic to send BPM and SpO2 to Python
    Serial.println(beatsPerMinute);
  }
}
