%{
#include <stdio.h>
void yyerror(const char *s) { (void)s; }
int yylex(void) { return 0; }
%}
%%
input: /* empty */ ;
%%
int main(void) {
    puts("EMPEROR-TIME-YACC-PROBE-OK");
    return 0;
}
