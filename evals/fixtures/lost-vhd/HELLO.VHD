-- HELLO.VHD — archaeology probe fixture (DOS-era 8.3 name).
-- Dialect CONJECTURE: see README.md in this directory.
-- Intent: smallest entity+architecture that prints a known string via report.
entity hello is
end entity hello;

architecture behav of hello is
begin
  process is
  begin
    report "EMPEROR-TIME-VHD-PROBE-OK";
    wait;
  end process;
end architecture behav;
