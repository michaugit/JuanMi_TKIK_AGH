grammar JuanMI;

/*
Tokens
*/

TKN_END_LINE            :('.');
TKN_NUMBER              :('LICZBA');
TKN_STRING              :('TEKST');
TKN_BOOL                :('PRAWDA_FALSZ');
TKN_LIST                :('LISTA');
TKN_IF                  :('JEZELI');
TKN_ELSE                :('INACZEJ');
TKN_ELIF                :('JEZELI_INACZEJ');
TKN_FOR                 :('DLA');
TKN_FROM                :('OD');
TKN_TO                  :('DO');
TKN_WHILE               :('DOPOKI');
TKN_NOT                 :('NIE');
TKN_AND                 :('ORAZ');
TKN_OR                  :('LUB');
TKN_FUNCTION            :('FUNKCJA');
TKN_RETURN              :('ZWROC');
TKN_PRINT               :('WYPISZ');
TKN_TRUE                :('PRAWDA');
TKN_FALSE               :('FALSZ');
TKN_END                 :('KONIEC');
TKN_BREAK               :('PRZERWIJ');
TKN_CONTINUE            :('KONTYNUUJ');
TKN_PLUS                :'+';
TKN_MINUS               :'-';
TKN_MUL                 :'*';
TKN_DIV                 :'/';
TKN_POW                 :'^';
TKN_CONCAT              :'++';
TKN_ASSIGN              :':=';
TKN_G                   :'>';
TKN_L                   :'<';
TKN_EQ                  :'=';
TKN_GEQ                 :'>=';
TKN_LEQ                 :'<=';
TKN_NEQ                 :'/=';
TKN_DOTS                :':';
TKN_LBRACKET            :'(';
TKN_RBRACKET            :')';
TKN_LSQUARE             :'[';
TKN_RSQUARE             :']';
TKN_COMMA               :',';
TKN_COMMENT             :([#][a-zA-Z_0-9 \t;]*[\n] | '#{'[a-zA-Z_0-9 \t\n;]*'}#');
TKN_NUMBER_VAL          :[-]?[0-9]+([.][0-9]+)?;
TKN_STRING_VAL          :'"'[a-zA-Z_0-9!? \t\n;]*'"';
TKN_VAR_ID              :[a-zA-Z_][a-zA-Z0-9_]*;
TKN_WHITESPACE          :(' ' | '\t' | '\n') -> skip;


/* left= , right=*/
/*GRAMMAR*/

program:
    code EOF;

code:
    expression TKN_END_LINE |
    expression TKN_END_LINE code |
    TKN_COMMENT code;

var_type:
    TKN_NUMBER | TKN_STRING | TKN_BOOL | TKN_LIST;

varDeclaration:
    var_type TKN_VAR_ID TKN_ASSIGN value;

varAssignment:
    TKN_VAR_ID TKN_ASSIGN value;

functionDeclaration:
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_RETURN value TKN_END_LINE TKN_END |
    TKN_FUNCTION TKN_VAR_ID TKN_LBRACKET fullArgList TKN_RBRACKET TKN_DOTS code TKN_END;

functionCall:
    TKN_VAR_ID TKN_LBRACKET fullValueList TKN_RBRACKET;

expression:
    varDeclaration | varAssignment | printExpression | forLoopExpression | whileLoopExpression |
    conditionalExpression TKN_END | functionCall | functionDeclaration | TKN_RETURN value;

value:
    stringExpression | booleanExpression | arithmeticExpression | listExpression |TKN_VAR_ID | functionCall;

stringExpression:
    stringExpression TKN_CONCAT stringExpression | TKN_STRING_VAL | TKN_VAR_ID | TKN_LBRACKET stringExpression TKN_RBRACKET | functionCall;

booleanExpression:
    booleanExpression (TKN_AND | TKN_OR) booleanExpression | stringExpression (TKN_EQ | TKN_NEQ) stringExpression |
    arithmeticExpression (TKN_G | TKN_L | TKN_LEQ | TKN_GEQ | TKN_EQ | TKN_NEQ) arithmeticExpression | TKN_FALSE | TKN_TRUE |
    TKN_VAR_ID | TKN_NOT booleanExpression | TKN_LBRACKET booleanExpression TKN_RBRACKET | functionCall;

arithmeticExpression:
    TKN_LBRACKET arithmeticExpression TKN_RBRACKET |
    arithmeticExpression (TKN_MUL | TKN_DIV) arithmeticExpression |
    arithmeticExpression (TKN_MINUS | TKN_PLUS) arithmeticExpression |
    TKN_NUMBER_VAL | TKN_VAR_ID | functionCall;

printExpression:
    TKN_PRINT value | TKN_PRINT TKN_LBRACKET value TKN_RBRACKET;

forLoopExpression:
    TKN_FOR TKN_VAR_ID TKN_FROM arithmeticExpression TKN_TO arithmeticExpression TKN_DOTS loopCode TKN_END;

whileLoopExpression:
    TKN_WHILE booleanExpression TKN_DOTS loopCode TKN_END;

conditionalExpression:
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) |  TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression elseExpression |
    TKN_IF booleanExpression TKN_DOTS (code|loopCode) elifExpression | TKN_IF booleanExpression TKN_DOTS (code|loopCode) elseExpression;

elifExpression:
    TKN_ELIF booleanExpression TKN_DOTS (code|loopCode) | elifExpression TKN_ELIF booleanExpression TKN_DOTS (code|loopCode);

elseExpression:
    TKN_ELSE TKN_DOTS (loopCode|code);

listExpression:
    listValue | listExpression TKN_CONCAT listValue;

listValue:
    TKN_LSQUARE valueList TKN_RSQUARE;

valueList:
    value | valueList TKN_COMMA value;

fullValueList:
    TKN_WHITESPACE | valueList;

argList:
    var_type TKN_VAR_ID | argList TKN_COMMA var_type TKN_VAR_ID;

fullArgList:
    TKN_WHITESPACE | argList;

loopCode:
    code | loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode |
    loopCode (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE |
    (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE loopCode | (TKN_BREAK | TKN_CONTINUE) TKN_END_LINE;
















