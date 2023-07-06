/*
 * Make sure to disconnect RFID shield when uploading code to Arduino UNO, since it is using Hardware serial. 
 * Once code uploaded then Mount RFID shield on Arduino and open serial monitor and set baudrate as 9600 to test code.
 * When card detected, value printed on serial with audio alert and relay state toggled
 */
char input[12];    // variable to hold RFID card value     
int count = 0;        
int buzzerPin = 3;  // Buzzer connected at Digital Pin 3 of Arduino Uno
int relayPin = 2;   // Relay connected at Digital Pin 3 of Arduino Uno
bool statusVal = 0;    // to check previous state


void setup()
{
  Serial.begin(9600);   // START SERIAL AT BAUD RATE OF 9600 BITS/SEC   
  pinMode(buzzerPin, OUTPUT); // set Buzzer pin as OUTPUT
  pinMode(relayPin, OUTPUT);  // set Relay pin as OUTPUT
  
}

void loop()
{      
     
  if(Serial.available())   // CHECK FOR AVAILABILITY OF SERIAL DATA
  {
    count = 0;      // Reset the counter to zero
    /* Keep reading Byte by Byte from the Buffer till the RFID Reader Buffer is empty 
       or till 12 Bytes (the ID size of our Tag) is read */
    statusVal = !statusVal;
    digitalWrite(buzzerPin, HIGH); // Turn on buzzer
    while(Serial.available() && count < 12) 
    {
      input[count] = Serial.read(); // Read 1 Byte of data and store it in the input[] variable
      count++;          // increment counter
      delay(5);
    }
    
     // PRINTING RFID TAG           
    for(int i=0;i<12;i++)
      Serial.print(input[i]);
      
    Serial.println();
    digitalWrite(buzzerPin, LOW); // Turn OFF buzzer
    digitalWrite(relayPin, statusVal); // Toggle relay for each scan of RFID
  }

}
