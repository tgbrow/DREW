#include <RFM12B.h>

// You will need to initialize the radio by telling it what ID it has and what network it's on
// The NodeID takes values from 1-127, 0 is reserved for sending broadcast messages (send to all nodes)
// The Network ID takes values from 0-255
// By default the SPI-SS line used is D10 on Atmega328. You can change it by calling .SetCS(pin) where pin can be {8,9,10}
#define NODEID           1  //network ID used for this unit
#define NETWORKID       99  //the network ID we are on
#define GATEWAYID     1  //the node ID we're sending to
#define SERIAL_BAUD 9600

// Need an instance of the Radio Module
RFM12B radio;

// "regular operation"
typedef struct {		
  byte          messageType; //2 for zone to USB
  byte          wearableID; //1-255
  byte          zoneID; //1-255
  byte          signalStrength; //arssi
} ZonePayload;

// "discover a wearable device"
typedef struct {		
  byte          messageType; //1 for wearable
  byte          wearableID; //1-255
} WearablePayload;

// "discover a new zone ID"
typedef struct {		
  byte          messageType; //4 for wearable
  byte          zoneID; //1-255
} ZoneACK;
ZoneACK zoneACK;

// "never gets sent over serial"
typedef struct {		
  byte          messageType; // 3 
} USBPayload;
USBPayload usbPayload;

void setup()
{
  radio.Initialize(NODEID, RF12_915MHZ, NETWORKID);
  Serial.begin(SERIAL_BAUD);
  //Serial.println("Listening...");
  usbPayload.messageType = 3;
}

void loop()
{
  if (Serial.available()) {
    if (Serial.read() == '1') {
      radio.Send(GATEWAYID, (const void*)(&usbPayload), sizeof(usbPayload), 0);
    }
  }
      
  if (radio.ReceiveComplete())
  {
    if (radio.CRCPass())
    {
      if (radio.Data[0] == 1)
      {
        WearablePayload wearableData;
        wearableData = *(WearablePayload*)radio.Data;
        Serial.print(wearableData.messageType);
        Serial.print(',');
        Serial.println(wearableData.wearableID);
      } else if (radio.Data[0] == 2)
      {
        ZonePayload zoneIncoming;
        zoneIncoming = *(ZonePayload*)radio.Data;
        Serial.print(zoneIncoming.messageType);
        Serial.print(',');
        Serial.print(zoneIncoming.wearableID);
        Serial.print(',');
        Serial.println(zoneIncoming.zoneID);
        Serial.print(',');
        Serial.println(zoneIncoming.signalStrength);
      } else if (radio.Data[0] == 4){
        ZoneACK zoneACK;
        zoneACK = *(ZoneACK*)radio.Data;
        Serial.print(zoneACK.messageType);
        Serial.print(',');
        Serial.println(zoneACK.zoneID);
      } else {
        //ignore
      }
    }
    else {
      //Serial.print("BAD-CRC");
    }
  }
}
