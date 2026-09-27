MODULE Hello;
(* HELLO.MOD — archaeology probe fixture (DOS-era 8.3 name). *)
(* Dialect CONJECTURE: see README.md in this directory. *)
(* Intent: smallest Modula-2 program that prints a known string via WriteString. *)
FROM StrIO IMPORT WriteString, WriteLn;
BEGIN
  WriteString("EMPEROR-TIME-MOD-PROBE-OK");
  WriteLn
END Hello.
