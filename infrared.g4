grammar infrared;

/*Parser rules*/
ired_related : ( IRED_PIN | IRED_READ);


/*Lexer rules rules*/
IRED : II RR EE DD;

IRED_PIN : P I N '(' (NUM)+ ')';

IRED_READ : RR EE AA DD '(' ')';
