-- HELLO.ADB — archaeology probe fixture (DOS-era 8.3 name).
-- Dialect CONJECTURE: see README.md in this directory.
-- Intent: smallest procedure that prints a known string via Ada.Text_IO.
with Ada.Text_IO;
procedure Hello is
begin
   Ada.Text_IO.Put_Line ("EMPEROR-TIME-ADA-PROBE-OK");
end Hello;
