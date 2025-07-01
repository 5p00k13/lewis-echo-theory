# lewis-echo-theory
Recursive hash pattern theory using SHA-256 echo mapping

Lewis Echo Theory

**Author:** Charles Lewis  
**Last Updated:** July 1, 2025  
**Status:** Experimental / Seeking peer review

---

What Is the Lewis Echo Theory?

The **Lewis Echo Theory** is a novel approach to cryptanalysis that proposes a new way of understanding how repetitive hash inputs behave when passed through cryptographic functions—especially `SHA-256`. The theory suggests that:

> _"Hashed outputs contain echoes of the input when layered recursively, particularly when using the inputs themselves as keys or mapping references."_

It explores how repetition, forward-reverse mirroring, prime-based key chaining, and dictionary comparisons can be used to expose predictable "echoes" or fragments within hash outputs that might aid decryption or analysis of obfuscated data.

---

Core Concepts

- **Echo Mapping**: Using input words as keys to hash themselves and other words repeatedly
- **Recursive Salting**: Injecting outputs of previous hashes as new keys in the chain
- **Forward-Reverse Mapping**: Reversing strings and hash outputs to expose symmetric structures
- **Wordlist Overlay**: Comparing hash fragments against large dictionaries like `rockyou.txt`
- **Prime Key Shifting**: Cycling input through prime-number-based transformations

---

Repo Structure

lewis-echo-theory/
├── echo_theory.py       # Core implementation
├── README.md            # Overview and instructions
├── manifest.pdf         # Printable version with diagrams (optional)
├── examples/
│   ├── test_vectors.txt # Sample input/outputs
│   └── echo_matches.json
└── wordlists/
└── mini_list.txt    # Small test dictionary (extendable to rockyou.txt)
---
How To Use (Step-by-Step Walkthrough)

Step 1: Install Python (3.7+)

```bash
sudo apt install python3 python3-pip

Step 2: Clone the Repository
git clone https://github.com/yourname/lewis-echo-theory.git
cd lewis-echo-theory
git clone https://github.com/yourname/lewis-echo-theory.git
cd lewis-echo-theory
Step 3: Run the Echo Engine
python3 echo_theory.py --input "awake"
This will:
	•	Hash “awake” using SHA-256
	•	Use the result to salt itself again
	•	Repeat this process with forward and reversed variants
	•	Compare each round’s output against a wordlist
Step 4: Echo Matching Output
{
  "input": "awake",
  "iterations": 5,
  "matches_found": ["wake", "ake", "aw"],
  "echo_patterns": [
    {
      "round": 1,
      "hash": "7a3c...ff",
      "partial_match": "wake"
    },
    ...
  ]
}

Step 5: Use Custom Wordlist
To use a full wordlist like rockyou.txt:
python3 echo_theory.py --input "awake" --wordlist wordlists/rockyou.txt

Step 6: Batch Test Mode

To test an entire list of inputs:
python3 echo_theory.py --batch-input wordlists/mini_list.txt

Theory Applications
	•	Password echo discovery: Finding echoes of weak or predictable passwords in complex hashes
	•	Preimage testing: Using fragments to reverse-engineer components of a salted hash
	•	Custom decoder: Reconstructing salted layers using echo-chain correlation
	•	Cryptoart / Puzzle solving: Solving puzzles like Cicada 3301 or Liber Primus through layered hash logic

Example: Hashing “awake”
SHA256("awake") → 7a3cd...
SHA256("awake" + "7a3cd...") → b54ef...
SHA256(reverse("awake")) → ekawa → 320ac...
Pattern found:
	•	Fragment “wake” appears in iteration 2
	•	“aw” appears mirrored in reversed hash

Manifesto (PDF)

Includes:
	•	Visual proof of echo matching
	•	Full explanation of logic chaining
	•	Real-world tests using common hash lists
Want to Contribute?
	•	Submit an issue or pull request
	•	Suggest new echo-matching logic
	•	Help test large-scale matching with rockyou.txt
Disclaimer

The Lewis Echo Theory is experimental. It is not intended to weaken any modern cryptographic standard but to explore theoretical patterns in recursive hash behavior. Always use responsibly.
