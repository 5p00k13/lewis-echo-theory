#!/usr/bin/env python3

import hashlib
import argparse
import json
import os

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def reverse_string(s: str) -> str:
    return s[::-1]

def ascii_transform(s: str) -> str:
    # Convert characters to their ASCII numeric values and represent each as letter(s) if between 1-50
    result = []
    for c in s:
        val = ord(c)
        if 1 <= val <= 26:
            result.append(chr(96 + val))  # a-z
        elif 27 <= val <= 52:
            result.append('a' + chr(96 + (val - 26)))  # aa, ab, etc.
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

def echo_chain(word: str, steps: int = 10, use_reverse=False, use_ascii=False, use_vigenere=False) -> list:
    chain = []
    current = word

    for i in range(steps):
        original = current

        if use_ascii:
            current = ascii_transform(current)

        if use_vigenere:
            key = sha256(original)[:len(original)]
            current = vigenere_cipher(original, key)

        if use_reverse:
            current = reverse_string(current)

        hashed = sha256(current)
        chain.append({
            "step": i + 1,
            "input": original,
            "transformed": current,
            "sha256": hashed
        })

        current = hashed  # Echo logic

    return chain

def load_wordlist(path: str) -> list:
    if not os.path.isfile(path):
        print(f"Wordlist not found: {path}")
        return []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description="Lewis Echo Theory Engine")
    parser.add_argument("--word", help="Single word to echo")
    parser.add_argument("--wordlist", help="File path to wordlist")
    parser.add_argument("--steps", type=int, default=10, help="Echo steps")
    parser.add_argument("--reverse", action="store_true", help="Apply string reversal")
    parser.add_argument("--ascii", action="store_true", help="Apply ASCII symbol transform")
    parser.add_argument("--vigenere", action="store_true", help="Apply Vigenère chaining")

    args = parser.parse_args()

    output = {}

    if args.word:
        output[args.word] = echo_chain(args.word, steps=args.steps, use_reverse=args.reverse,
                                       use_ascii=args.ascii, use_vigenere=args.vigenere)

    if args.wordlist:
        words = load_wordlist(args.wordlist)
        for word in words:
            output[word] = echo_chain(word, steps=args.steps, use_reverse=args.reverse,
                                      use_ascii=args.ascii, use_vigenere=args.vigenere)

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
