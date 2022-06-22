import struct
from hashlib import sha256
from binascii import hexlify, unhexlify
from Crypto.PublicKey import RSA


STACK_MAX_SIZE = 128
PROGRAM_MAX_SIZE = 2048

STACK = []

def op_nop(code):
	return 0

def op_push(code):
	off = 0
	if len(code) < 1:
		raise Exception("Opcode processing error")

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

def op_check_sig(code):
	if len(STACK) < 3:
		raise Exception("Opcode processing error")
	
	pub_key = STACK.pop()
	msg = sha256(STACK.pop()).digest()
	sig = STACK.pop()

	msg = int.from_bytes(msg, 'big')
	if len(pub_key) < 129:
		raise Exception("Opcode processing error")
	n = int.from_bytes(pub_key[:128], 'big')
	e = int.from_bytes(pub_key[128:], 'big')
	sig = int.from_bytes(sig, 'big')

	pub_key = RSA.RsaKey(n=n, e=e)
	STACK.append(bytes([pow(sig, pub_key.e, pub_key.n) == msg]))
	return 0

OPS = {
	0: op_nop,
	1: op_push,
	#2: op_add,
	#3: op_sub,
	#4: op_not,
	6: op_dup,
	7: op_equal,
	8: op_hash,
	9: op_verify,
	0x0c: op_check_sig,
	# 0x0d: op_halt
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

def solve(lock, unlock):
	if len(lock) > PROGRAM_MAX_SIZE or len(unlock) > PROGRAM_MAX_SIZE:
		return False

	process(unlock)
	process(lock)

	if STACK[0] == b'\x01':
		return True

	return False

lock = b''
lock += b'\x08'
lock += b'\x01\x20\x9f\x86\xd0\x81\x88\x4c\x7d\x65\x9a\x2f\xea\xa0\xc5\x5a\xd0\x15\xa3\xbf\x4f\x1b\x2b\x0b\x82\x2c\xd1\x5d\x6c\x15\xb0\xf0\x0a\x08'
lock += b'\x07'
lock += b'\x09'
lock += b'\x01\x83\xb8\x1d\x31\x39\x5e\xd5\xf6\xb7\x14\xac\x1e\x12\xaa\x4a\x72\xca\x24\x7f\xce\x87\x8a\xe6\xf9\x04\x25\xb1\x82\x35\xff\x99\xb1\xf0\x9f\x98\xd3\xfb\xdb\x6d\xeb\x0b\x35\x6f\x63\x51\x67\x44\x8c\x66\x66\xb9\x5c\x44\xb5\x3a\x81\x5b\xce\xbf\xeb\xb2\x2a\x34\x71\xd1\x94\x85\xad\xca\x7f\x30\x37\x7d\xb5\x56\x46\x78\x4c\xe8\xa7\x6f\x43\xcf\x0a\x2d\x32\x13\x76\x5d\x10\xe1\x9f\xe3\xc5\x19\x74\xe9\x69\xe1\xfa\x5b\x71\x4c\x9d\x9c\x0c\x35\xcf\xe8\x53\x2d\x12\xa6\x23\x1e\xd4\x9c\x59\xd3\xab\x81\xa2\x36\x50\x18\x55\xdf\x35\xd1\x01\x00\x01'
lock += b'\x0c'

unlock = unhexlify(input('Enter the script to solve the puzzle: '))
if solve(lock, unlock):
	print('Great job!')
else:
	print('Try again :(')
