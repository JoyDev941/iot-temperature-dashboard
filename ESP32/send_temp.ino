#include <WiFi.h>
#include <DHT.h>
#include <HTTPClient.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "x";
const char* pass = "x";
const int ledPin = 2;

void connect(){

  WiFi.begin(ssid, pass);
  pinMode(ledPin, OUTPUT);


  while(WiFi.status() != WL_CONNECTED){
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
    Serial.print("Connecting...");
  }

  if(WiFi.status() == WL_CONNECTED){
    digitalWrite(ledPin, HIGH);
    Serial.print("Wifi connected");
  }

}

void STempData(float T){

  HTTPClient http;
  http.begin("http://192.168.68.120:2004/set?msg="+String(T));
  int httpCode = http.GET();
  http.end();

}


void setup() {
  connect();
  dht.begin();

}

void loop() {

  float temp = dht.readTemperature();

  if (!isnan(temp)) {
    
    STempData(temp);
    
    }
    
  delay(10000);

  
}