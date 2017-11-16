const int pinBtnLeft = 6;
const int pinBtnRight = 10;
 
 
//Variables for the states of the SNES buttons
boolean boolBtnLeft;
boolean boolBtnRight;
 
 
void setup()
{
  pinMode( 13, OUTPUT );
  pinMode( pinBtnLeft, INPUT_PULLUP );
  pinMode( pinBtnRight, INPUT_PULLUP );
 
  
  boolBtnLeft = false;
  boolBtnRight = false;
 
}
 
 
void loop()
{
  digitalWrite ( 13 , digitalRead(pinBtnLeft));
  fcnProcessButtons();  
}
 

void fcnProcessButtons()
{
  boolean boolBtnLeft = !digitalRead(pinBtnLeft);
  if ( boolBtnLeft )
  {
    //Set key1 to the U key
    Keyboard.set_key1( KEY_F );
  } else {
    Keyboard.set_key1( 0 );
  }
  boolean boolBtnRight = !digitalRead(pinBtnRight);
  if ( boolBtnRight )
  {
    //Set key1 to the U key
    Keyboard.set_key2( KEY_J );
  } else {
    Keyboard.set_key2( 0 );
  }
    
  //Send all of the set keys.
  Keyboard.send_now();
 
 
}
