grammar v1;

/*
Parser rules
*/

stmt  : (line (EOF | '\n'))+;

/*line  : (WORD | NUMB);*/

/*line  : (INT|NUMBER) VARIABLE EQUAL NUMB;*/

/*line  : d_type VARIABLE EQUAL NUMB;*/

/*line  : (decl | assign | both);*/

line  : (v_init | conditional | output | END);

v_init  : (decl | assign | both);

decl  : d_type VARIABLE;

assign  : VARIABLE EQUAL NUMB;

both  : d_type VARIABLE EQUAL NUMB;

d_type  : (INTEGER|NUMBER);

conditional   : (r_if | ELSE);

r_if  :  IF (VARIABLE | NUMB) relation (VARIABLE | NUMB);

relation  : (GREATER | LESS | EQUAL);

output  : OUTPUT (VARIABLE)+;

/*
Lexer rules
*/

fragment A  : 'a';

fragment B  : 'b';

fragment C  : 'c';

fragment D  : 'd';

fragment E  : 'e';

fragment F  : 'f';

fragment G  : 'g';

fragment H  : 'h';

fragment I  : 'i';

fragment J  : 'j';

fragment K  : 'k';

fragment L  : 'l';

fragment M  : 'm';

fragment N  : 'n';

fragment O  : 'o';

fragment P  : 'p';

fragment Q  : 'q';

fragment R  : 'r';

fragment S  : 's';

fragment T  : 't';

fragment U  : 'u';

fragment V  : 'v';

fragment W  : 'w';

fragment X  : 'x';

fragment Y  : 'y';

fragment Z  : 'z';

fragment LOWER  : [a-z];

fragment UPPER  : [A-Z];

fragment NUM  : [0-9];

INTEGER   : I N T E G E R;

NUMBER  : N U M B E R;

OUTPUT  : O U T P U T;

IF  : I F;

ELSE  : E L S E;

END   : E N D;

VARIABLE  : (LOWER | UPPER)+;

EQUAL   : '=';

GREATER   : '>';

LESS   : '<';

NUMB   : (NUM)+;

TEXT  : {self._input.LA(-1) == ord('[') or self._input.LA(-1) == ord('(')}? ~[\])]+ ;

WHITESPACE  : (' ' | '\t')+ -> skip;

NEWLINE  : ('\r'? '\n' | '\r')+ ;
