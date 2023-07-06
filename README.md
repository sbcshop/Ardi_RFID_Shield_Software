# Ardi_RFID_Shield_Software
<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/ArdiRFIDShield.jpg?v=1683884138">
Ardi RFID Shield is based on the EM-18 module, operating at a frequency of 125 KHz. Having onboard single channel optoisolated relay allow you to control lights, motors, or other high-power devices. This shield seamlessly integrates with your Arduino Uno and compatible boards, Ardi32 and ArdiPi. 

This github provides getting started guide and other working details for Ardi RFID Shield 

### Features:
- Onboard 125kHz EM18 RFID small, compact module
- Onboard High-quality relays Relay with Screw terminal and NO/NC interfaces
- Shield compatible with both 3.3V and 5V MCU
- Onboard 3 LEDs power, relay ON/OFF State and RFID Scan status
- Multi-tone Buzzer onboard for Audio alerts
- Mounts directly onto your ArdiPi, Ardi32, and Arduino compatible boards

### Specifications:
- RFID operating Frequency: 125kHz
- Reading distance: 10cm, depending on TAG
- Integrated Antenna
- Relay Max Switching Voltage : 250VAC/30VDC
- Relay Max Switching Current: 7A/10A
  
### Hardware Overview
#### Pinout
<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/ArdiRFIDshieldpinout.jpg?v=1688468860">

- (1) 4 Relay
- (2) Relay ON/OFF status LED

#### Interfacing Details
When RFID shield mounted on Arduino Uno, 
|RFID shield | Arduino UNO| 
|---|---|
| Transmit Pin | D0 (serial Rx of Arduino) | 
| Relay  | D2 | 
| Buzzer | D3 | 

 * Make sure to disconnect RFID shield when uploading code to Arduino UNO, since it is using Hardware serial. 
 * Once code uploaded then Mount RFID shield on Arduino and open serial monitor and set baudrate as 9600 to test code.
 * When card detected, value printed on serial with audio alert and relay state toggled

When RFID shield mounted on Ardi32, 
|RFID shield | Ardi32| 
|---|---|
| Transmit Pin | IO18 (serial Rx of ESP32) | 
| Relay  | IO1 | 
| Buzzer | IO42 | 

When RFID shield mounted on ArdiPi, 
|RFID shield | ArdiPi| 
|---|---|
| Transmit Pin | GP1 (serial Rx of Pico W) | 
| Relay  | GP5 | 
| Buzzer | GP2 | 

### Example Codes
 Also, sample codes are available for Ardi RFID shield
 - [Ardi RFID shield for UNO](https://github.com/sbcshop/Ardi_RFID_Shield_Software/tree/main/examples/ArduinoUno_RFID_shield_interfacing) 
 - [Ardi RFID shield for Ardi32](https://github.com/sbcshop/Ardi_RFID_Shield_Software/tree/main/examples/Ardi32_RFID_shield_interfacing) 
 - [Ardi RFID shield for ArdiPi](https://github.com/sbcshop/Ardi_RFID_Shield_Software/tree/main/examples/ArdiPi_RFID_shield_interfacing)
 
 Using this sample code as a guide, you can modify, build for other boards and share codes!!  
   
## Resources
  * [Schematic](https://github.com/sbcshop/Ardi_RFID_Shield_Hardware/blob/main/Design%20Data/SCH%204CH%20Relay%20Shield.pdf)
  * [Hardware Files](https://github.com/sbcshop/Ardi_RFID_Shield_Hardware/tree/main)
  * [Step File](https://github.com/sbcshop/Ardi_RFID_Shield_Hardware/blob/main/Mechanical%20Data/STEP%204CH%20Relay%20Shield.step)


## Related Products
   * [Ardi-32](https://shop.sb-components.co.uk/products/ardi32-uno-r3-alternative-board-based-on-esp32-s3-wroom?_pos=6&_sid=90d9cefb0&_ss=r) - Arduino Uno Form factor with latest powerful ESP32 S3
   * [ArdiPi](https://shop.sb-components.co.uk/products/ardipi-uno-r3-alternative-board-based-on-pico-w?_pos=5&_sid=5704675c2&_ss=r) - Arduino Uno Form factor with powerful Pico W of Raspberry Pi having onboard WiFi and BLE support.
   * [Ardi Display Shield](https://shop.sb-components.co.uk/products/ardi-display-shield-for-arduino-uno?_pos=5&_sid=961a5887c&_ss=r) - 2.0" Display Shield with onboard Programmable Buttons and Joystick
   * [Ardi UHF Shield](https://shop.sb-components.co.uk/products/ardi-uhf-shield-for-arduino-uno?variant=40791294836819) - UHF based shield with Oled display and Buzzer onboard
   * [Ardi Relay Shield](https://shop.sb-components.co.uk/products/ardi-relay-shield-for-arduino-uno?_pos=4&_sid=961a5887c&_ss=r) - Relay Shield with Screw terminal and Relay ON/OFF Status LED
   
   Shields are compatible with ArdiPi, Ardi-32 and Other Arduino Uno Compatible boards.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
