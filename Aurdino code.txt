const int LED=D3; const int fan=D4; const int TV=D5; const int AC=D6; void setup()
{
pinMode(LED, OUTPUT); pinMode(fan, OUTPUT); pinMode(TV, OUTPUT); pinMode(AC, OUTPUT); Serial.begin(9600);
}
void loop()
{
if(Serial.available()>0)
 
{
char sleep =Serial.read(); if(sleep=='S')
{


digitalWrite(LED, HIGH); digitalWrite(fan, LOW); digitalWrite(TV, HIGH); digitalWrite(AC, HIGH);
}
if(sleep=='R')
{


digitalWrite(LED, LOW); digitalWrite(fan, LOW); digitalWrite(TV, HIGH); digitalWrite(AC, HIGH);
}
if(sleep=='T')
{
digitalWrite(TV, LOW); digitalWrite(AC, HIGH); digitalWrite(LED, LOW); digitalWrite(fan, LOW);
}
if(sleep=='C')
{
digitalWrite(LED,LOW); digitalWrite(fan, HIGH); digitalWrite(TV, LOW); digitalWrite(AC, LOW);
}
}
}
