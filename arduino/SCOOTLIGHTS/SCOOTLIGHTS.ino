// NeoPixel Ring simple sketch (c) 2013 Shae Erisson
// released under the GPLv3 license to match the rest of the AdaFruit NeoPixel library

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

// THIS IS USED FOR CORRECTING GAMMA AND MAKING COLORS LOOK MORE GOODER
const uint8_t PROGMEM gamma8[] = {
  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
  2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
  5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
  10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
  17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
  25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
  37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
  51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
  69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
  90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112, 114,
  115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137, 138, 140, 142,
  144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 167, 169, 171, 173, 175,
  177, 180, 182, 184, 186, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213,
  215, 218, 220, 223, 225, 228, 231, 233, 236, 239, 241, 244, 247, 249, 252, 255
};

// Which pin on the Arduino is connected to the NeoPixels?
// On a Trinket or Gemma we suggest changing this to 1
#define RINGPIN            9
#define STRIPPIN           11
#define P1BUTTONPIN        22
#define P1GRIDPIN          20
#define P2BUTTONPIN        18
#define P2GRIDPIN          15

// How many NeoPixels are attached to the Arduino?
#define NUMRINGPIXELS      48
#define NUMSTRIPPIXELS     128
#define NUMGRIDPIXELS      64

// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values.
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMSTRIPPIXELS, STRIPPIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel rings = Adafruit_NeoPixel(NUMRINGPIXELS, RINGPIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel p1grid = Adafruit_NeoPixel(NUMGRIDPIXELS, P1GRIDPIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel p1butt = Adafruit_NeoPixel(1, P1BUTTONPIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel p2grid = Adafruit_NeoPixel(NUMGRIDPIXELS, P2GRIDPIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel p2butt = Adafruit_NeoPixel(1, P2BUTTONPIN, NEO_GRB + NEO_KHZ800);

int delayval = 100;

int black[3] = {0, 0, 0};
int red[3] = {255, 0, 0};
int green[3] = {0, 255, 0};
int blue[3] = {0, 0, 255};
int aqua[3] = {0, 255, 255};
int magenta[3] = {250, 0, 200};
int orange[3] = {255, 128, 0};
int yellow[3] = {255, 255, 0};
int white[3] = {150, 150, 150};


int l_color[3] = {200, 200, 200};
int r_color[3] = {200, 200, 200};

void setup() {


  strip.begin(); // This initializes the NeoPixel library.
  rings.begin(); // This initializes the NeoPixel library.
  p1grid.begin();
  p2grid.begin();
  p1butt.begin();
  p2butt.begin();
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {

  // For a set of NeoPixels the first NeoPixel is 0, second is 1, all the way up to the count of pixels minus one.


  // simpleWave(0.03, 1, 1000);


  RunningLights(delayval);


  //  for (int i = 0; i < NUMPIXELS; i++) {
  //    pixels.setPixelColor(i, new_color); // Moderately bright green color.
  //
  //    pixels.show(); // This sends the updated pixel color to the hardware.
  //
  //    delay(delayval); // Delay for a period of time (in milliseconds).
  //
  //  }
  //  for (int i = 0; i < NUMPIXELS; i++) {
  //
  //    // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
  //    pixels.setPixelColor(i, pixels.Color(0, 0, 0)); // Moderately bright green color.
  //
  //    pixels.show(); // This sends the updated pixel color to the hardware.
  //
  //    delay(delayval); // Delay for a period of time (in milliseconds).
  //
  //  }
}

void readColor() {
  if (Serial.available() ) {
    char val0 = Serial.read();
    char val1 = Serial.read();

    if (val0 == '-')
      memcpy(l_color, black, sizeof(int) * 3);
    if (val0 == 'r')
      memcpy(l_color, red, sizeof(int) * 3);
    if (val0 == 'g')
      memcpy(l_color, green, sizeof(int) * 3);
    if (val0 == 'b')
      memcpy(l_color, blue, sizeof(int) * 3);
    if (val0 == 'w')
      memcpy(l_color, white, sizeof(int) * 3);
    if (val0 == 'a')
      memcpy(l_color, aqua, sizeof(int) * 3);
    if (val0 == 'm')
      memcpy(l_color, magenta, sizeof(int) * 3);
    if (val0 == 'o')
      memcpy(l_color, orange, sizeof(int) * 3);
    if (val0 == 'y')
      memcpy(l_color, yellow, sizeof(int) * 3);

    if (val1 == '-')
      memcpy(r_color, black, sizeof(int) * 3);
    if (val1 == 'r')
      memcpy(r_color, red, sizeof(int) * 3);
    if (val1 == 'g')
      memcpy(r_color, green, sizeof(int) * 3);
    if (val1 == 'b')
      memcpy(r_color, blue, sizeof(int) * 3);
    if (val1 == 'w')
      memcpy(r_color, white, sizeof(int) * 3);
    if (val1 == 'a')
      memcpy(r_color, aqua, sizeof(int) * 3);
    if (val1 == 'm')
      memcpy(r_color, magenta, sizeof(int) * 3);
    if (val1 == 'o')
      memcpy(r_color, orange, sizeof(int) * 3);
    if (val1 == 'y')
      memcpy(r_color, yellow, sizeof(int) * 3);

  }
}

//void simpleWave(float rate, int cycles, int wait) {
//  float pos = 0.0;
//  // cycle through x times
//  for (int x = 0; x < (strip.numPixels()*cycles); x++)
//  {
//    pos = pos + rate;
//    for (int i = 0; i < strip.numPixels(); i++) {
//      // sine wave, 3 offset waves make a rainbow!
//      float level1 = sin(i + pos) * new_color[0] + 128;
//      float level2 = sin(i + pos) * new_color[1] + 128;
//      float level3 = sin(i + pos) * new_color[2] + 128;
//      // set color level
//      strip.setPixelColor(i, (int)level1, (int)level2, (int)level3);
//    }
//    strip.show();
//    delay(wait);
//  }
//}

void RunningLights(int WaveDelay) {
  int Position = 0;
  int loop_max = rings.numPixels() * strip.numPixels();
  
  for (int i = 0; i < loop_max; i++)
  {
    /////////////////// buttons
    p1butt.setPixelColor(0, pgm_read_byte(&gamma8[l_color[0]]), pgm_read_byte(&gamma8[l_color[1]]), pgm_read_byte(&gamma8[l_color[2]]));
    p2butt.setPixelColor(0, pgm_read_byte(&gamma8[r_color[0]]), pgm_read_byte(&gamma8[r_color[1]]), pgm_read_byte(&gamma8[r_color[2]]));
    p1butt.show();
    p2butt.show();
    Position++; // = 0; //Position + Rate;

    //////////////////////////// RINGS
    for (int i = 0; i < rings.numPixels() / 4; i++) {
      rings.setPixelColor(i, ((sin(( Position) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[0]]),
                          ((sin(( Position) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[1]]),
                          ((sin(( Position) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[2]]));
    }
    for (int i = rings.numPixels()/4; i < rings.numPixels() / 4 * 2; i++) {
      rings.setPixelColor(i, ((sin(( Position+loop_max/4) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[0]]),
                          ((sin(( Position+loop_max/4) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[1]]),
                          ((sin(( Position+loop_max/4) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[2]]));
    }
    for (int i = rings.numPixels()/4*2; i < rings.numPixels() / 4 * 3; i++) {
      rings.setPixelColor(i, ((sin(( Position+loop_max/4*2) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[0]]),
                          ((sin(( Position+loop_max/4*2) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[1]]),
                          ((sin(( Position+loop_max/4*2) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[2]]));
    }
    for (int i = rings.numPixels()/4*3; i < rings.numPixels(); i++) {
      rings.setPixelColor(i, ((sin(( Position+loop_max/4*3) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[0]]),
                          ((sin(( Position+loop_max/4*3) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[1]]),
                          ((sin(( Position+loop_max/4*3) / 2) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[2]]));
    }
    rings.show();


    //////////////////////////// STRIP

    for (int i = 0; i < strip.numPixels() / 2; i++) {
      strip.setPixelColor(i, ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[0]]),
                          ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[1]]),
                          ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[l_color[2]]));
    }
    for (int i = strip.numPixels() / 2; i < strip.numPixels(); i++) {
      strip.setPixelColor(i, ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[0]]),
                          ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[1]]),
                          ((sin((i + Position) / 4) * 127 + 128) / 255)*pgm_read_byte(&gamma8[r_color[2]]));
    }
    strip.show();

    ///////////////////////  GRIDS
    for (int i = 0; i < p1grid.numPixels(); i++) {
      p1grid.setPixelColor(i, ((sin(( Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[l_color[0]]),
                           ((sin(( Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[l_color[1]]),
                           ((sin(( Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[l_color[2]]));
    }
    for (int i = 0; i < p2grid.numPixels(); i++) {
      p2grid.setPixelColor(i, ((sin((Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[r_color[0]]),
                           ((sin((Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[r_color[1]]),
                           ((sin(( Position/4)) * 97 + 160) / 255)*pgm_read_byte(&gamma8[r_color[2]]));
    }
    p1grid.show();
    p2grid.show();

    readColor();

    delay(WaveDelay);
  }

}
