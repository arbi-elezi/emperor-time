%{
#include <stdio.h>
%}
%%
.|\n    /* ignore */
%%
int main(void) {
    puts("EMPEROR-TIME-LEX-PROBE-OK");
    return 0;
}
int yywrap(void) { return 1; }
