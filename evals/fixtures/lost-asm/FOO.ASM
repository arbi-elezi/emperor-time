; FOO.ASM — archaeology probe fixture (DOS-era 8.3 name).
; Dialect CONJECTURE vs runnable truth: see README.md in this directory.
; Intent: smallest program that prints a known string under NASM+ld.
;
; Runnable dialect on this Linux box (VERIFIED in PROBE.md):
;   NASM Intel-syntax, Linux x86-64 ELF, raw syscalls (not libc).
; NOT MASM. NOT DOS .COM / 16-bit INT 21h.

        global  _start

        section .data
msg:    db      "EMPEROR-TIME-ASM-PROBE-OK", 10
len:    equ     $ - msg

        section .text
_start:
        mov     rax, 1              ; sys_write
        mov     rdi, 1              ; stdout
        mov     rsi, msg
        mov     rdx, len
        syscall

        mov     rax, 60             ; sys_exit
        xor     rdi, rdi            ; status 0
        syscall
