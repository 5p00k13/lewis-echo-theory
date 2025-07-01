#!/usr/bin/env python3

import hashlib
import argparse
import json
import os

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def reverse_string(s: str) -> str:
    return s[::-1]

def load_wordlist(path: str) -> list:
    if not os.path.isfile(path):
        print(f"Wordlist not found: {path}")
        return []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def echo_chain(word: str, iterations: int = 5, wordlist: list = None):
    results = []
    current = word
    found = []

    for i in range(1, iterations + 1):
        h = sha256(current)
        rh = sha256(reverse_string(current))

        match1 = [w for w in wordlist if w in h] if wordlist else []
        match2 = [w for w in wordlist if w in rh] if wordlist else []

        round_result = {
            "round": i,
            "input": current,
            "hash": h,
            "reverse_hash": rh,
            "matches_forward": match1,
            "matches_reverse": match2
        }

        found.extend(match1 + match2)
        results.append(round_result)

        # Layer the next input (recursive salt)
        current = current + h[:8]  # Simulate recursive salting

    return {
        "input": word,
        "iterations": iterations,
        "matches_found": list(set(found)),
        "echo_chain": results
    }

def main():
    parser = argparse.ArgumentParser(description="Lewis Echo Theory Analyzer")
    parser.add_argument("--input", help="Word to analyze")
    parser.add_argument("--wordlist", help="Path to wordlist", default="wordlists/mini_list.txt")
    parser.add_argument("--batch-input", help="Test a wordlist in batch mode")
    parser.add_argument("--output", help="Save results as JSON")

    args = parser.parse_args()

    wordlist = load_wordlist(args.wordlist) if args.wordlist else []

    results = []

    if args.batch_input:
        targets = load_wordlist(args.batch_input)
        for word in targets:
            results.append(echo_chain(word, wordlist=wordlist))
    elif args.input:
        results = echo_chain(args.input, wordlist=wordlist)
    else:
        print("Please provide --input or --batch-input")
        return

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"[+] Results saved to {args.output}")
    else:
        print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
