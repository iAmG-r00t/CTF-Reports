#!/usr/bin/env python3
"""
Solve task interpreter puzzle challenge
"""

import struct
from hashlib import sha256
from binascii import hexlify, unhexlify

STACK_MAX_SIZE = 128
PROGRAM_MAX_SIZE = 2048

STACK = []

def op_push(code):
    off = 0
    if len(code) < 1:
        raise Exception("Opcode processing error")

    # finds length of unpacked code...
    l = struct.unpack('B', code[off:off+1])[0]

    off += 1
    
    if len(code[off:]) < l:
        raise Exception("Opcode processing error")

    STACK.append(code[off:off+l])
    off += l

    return off

def op_dup(code):
    if len(STACK) < 1:
        raise Exception("Opcode processing error")

    STACK.append(STACK[-1])
    return 0

def op_equal(code):
    if len(STACK) < 2:
        raise Exception("Opcode processing error")

    STACK.append(bytes([STACK.pop() == STACK.pop()]))
    return 0

def op_hash(code):
    if len(STACK) < 1:
        raise Exception("Opcode processing error")

    STACK.append(sha256(STACK.pop()).digest())
    return 0

def op_verify(code):
    if len(STACK) < 1:
        raise Exception("Opcode processing error")

    if STACK.pop() == b'\x00':
        raise Exception("Verify failed")
    return 0

OPS = {
    1: op_push,
    6: op_dup,
    7: op_equal,
    8: op_hash,
    9: op_verify,
}

def process(code):
    pc = 0
    while pc < len(code):
        f = OPS.get(code[pc], None)
        
        if not f:
            raise Exception(f'Wrong opcode {code[pc]}')

        pc += f(code[pc+1:]) + 1

        if len(STACK) > STACK_MAX_SIZE:
            raise Exception("Stack size exceeds")

msg = b'\x01\x04\x74\x65\x73\x74'
sig = b'\x01\x01\x00'

unlock = b''
unlock += msg
unlock += b'\x06'
unlock += b'\x07'
unlock += sig
unlock += msg
unlock += b'\x06'

print(hexlify(unlock))

process(unlock)

print(STACK)