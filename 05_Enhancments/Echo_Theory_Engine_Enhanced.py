#!/usr/bin/env python3

import hashlib
import argparse
import json
import os
import random

symbol_map = {
    '0': ['0', 'O', ')'],
    '1': ['1', 'l', 'I', '!', '~', 'a'],
    '2': ['2', 'Z', '@'],
    '3': ['3', 'E', '#'],
    '4': ['4', 'A', '$'],
    '5': ['5', 'S', '%'],
    '6': ['6', 'G', '^'],
    '7': ['7', 'T', '&'],
    '8': ['8', 'B', '*'],
    '9': ['9', 'g', '(']
}

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def reverse_string(s: str) -> str:
    return s[::-1]

def ascii_transform(s: str) -> str:
    result = []
    for c in s:
        val = ord(c)
        if 1 <= val <= 26:
            result.append(chr(96 + val))
        elif 27 <= val <= 52:
            result.append('a' + chr(96 + (val - 26)))
        else:
            result.append(str(val))
    return ''.join(result)

def vigenere_cipher(text: str, key: str) -> str:
    result = []
    for i in range(len(text)):
        t = ord(text[i])
        k = ord(key[i % len(key)])
        result.append(chr((t + k) % 256))
    return ''.join(result)

def apply_symbol_variants(s: str) -> str:
    result = []
    for c in s:
        if c in symbol_map:
            result.append(random.choice(symbol_map[c]))
        else:
            result.append(c)
    return ''.join(result)

def echo_chain(word: str, steps: int = 10) -> list:
    chain = []
    current = word

    for i in range(steps):
        original = current
        symbolized = apply_symbol_variants(current)
        ascii_version = ascii_transform(symbolized)
        reversed_version = reverse_string(ascii_version)
        key = sha256(original)[:len(original)]
        vigenere_output = vigenere_cipher(original, key)
        final_input = reverse_string(vigenere_output)
        hashed = sha256(final_input)

        chain.append({
            "step": i + 1,
            "input": original,
            "symbolized": symbolized,
            "ascii": ascii_version,
            "vigenere": vigenere_output,
            "final_input": final_input,
            "sha256": hashed
        })

        current = hashed

    return chain

def main():
    parser = argparse.ArgumentParser(description="Lewis Echo Theory - Enhanced Engine")
    parser.add_argument("--word", help="Single word to process")
    parser.add_argument("--steps", type=int, default=10, help="Number of echo steps")

    args = parser.parse_args()
    output = {}

    if args.word:
        output[args.word] = echo_chain(args.word, steps=args.steps)

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
