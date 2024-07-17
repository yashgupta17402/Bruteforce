// Mux control pins for analog signal (SIG_pin) default for Arduino Mini Pro
const byte s0 = A4; 
const byte s1 = A3; 
const byte s2 = A2; 
const byte s3 = A1;

// Mux control pins for Output signal (OUT_pin) default for Arduino Mini Pro 
const byte w0 = 6;  
const byte w1 = 5; 
const byte w2 = 4; 
const byte w3 = 3;

// Mux in "SIG" pin default for Arduino Mini Pro  
const byte SIG_pin = 0; 

// Mux out "SIG" pin default for Arduino Mini Pro 
const byte OUT_pin = 2;

// Status and Column pins default for Arduino Mini Pro 
const byte STATUS_pin = 8; 
const byte COL_pin = 9;

// Mux channel control signals
const boolean muxChannel[16][4] = {
    {0,0,0,0}, // channel 0
    {1,0,0,0}, // channel 1
    {0,1,0,0}, // channel 2
    {1,1,0,0}, // channel 3
    {0,0,1,0}, // channel 4
    {1,0,1,0}, // channel 5
    {0,1,1,0}, // channel 6
    {1,1,1,0}, // channel 7
    {0,0,0,1}, // channel 8
    {1,0,0,1}, // channel 9
    {0,1,0,1}, // channel 10
    {1,1,0,1}, // channel 11
    {0,0,1,1}, // channel 12
    {1,0,1,1}, // channel 13
    {0,1,1,1}, // channel 14
    {1,1,1,1}  // channel 15
};

int valor = 0; // Variable for reading sensor values
int butt=11;
void setup() {
  pinMode(s0, OUTPUT); 
  pinMode(s1, OUTPUT); 
  pinMode(s2, OUTPUT); 
  pinMode(s3, OUTPUT); 
  
  pinMode(w0, OUTPUT); 
  pinMode(w1, OUTPUT); 
  pinMode(w2, OUTPUT); 
  pinMode(w3, OUTPUT); 
  
  pinMode(OUT_pin, OUTPUT); 
  pinMode(butt,INPUT);
  pinMode(STATUS_pin, OUTPUT);
  pinMode(COL_pin, OUTPUT);

  digitalWrite(s0, LOW);
  digitalWrite(s1, LOW);
  digitalWrite(s2, LOW);
  digitalWrite(s3, LOW);
  
  digitalWrite(w0, LOW);
  digitalWrite(w1, LOW);
  digitalWrite(w2, LOW);
  digitalWrite(w3, LOW);
  
  digitalWrite(OUT_pin, HIGH);
  digitalWrite(STATUS_pin, HIGH);
  digitalWrite(COL_pin, HIGH);
  
  Serial.begin(115200);
  
  Serial.println("Reading sensor values...\n");
}

void loop() {
  // Continuously loop through and read all 225 values (15x15)
  int max=10;
  int maxi=0;
  int maxj=0;
  int button=digitalRead(butt);
  for (int j = 14; j >= 0; j--) 
  { 
    writeMux(j);
    for (int i = 0; i < 15; i++)
     {
      valor = readMux(i);
      if(valor>max)
      {
        max=valor;
       maxi=j;
       maxj=i;
      }
      // Print the raw value to the serial monitor
      // Serial.print(valor);
      // Serial.print("\t");
      
      digitalWrite(COL_pin, !digitalRead(COL_pin));
    }
    // Serial.println();
  }
  Serial.print(maxi);
  Serial.print(",");
  Serial.print(maxj);
  Serial.print(",");
  Serial.print(button);
  Serial.println();
  delay(1000); // Add a small delay to prevent flooding the serial monitor
}

int readMux(byte channel) {
  byte controlPin[] = {s0, s1, s2, s3};

  // Loop through the 4 control pins
  for (int i = 0; i < 4; i++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }

  // Read the value at the SIG pin
  int val = analogRead(SIG_pin);

  // Return the value
  return val;
}

void writeMux(byte channel) {
  byte controlPin[] = {w0, w1, w2, w3};

  // Loop through the 4 control pins
  for (byte i = 0; i < 4; i++) {
    digitalWrite(controlPin[i], muxChannel[channel][i]);
  }
}