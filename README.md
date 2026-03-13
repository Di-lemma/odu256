# odu256

```
|  ||
|  |
||  |
|  |
```

**odu256** is a small experimental project that models the combinatorial structure of the Ifá divination system and uses Retrieval-Augmented Generation (RAG) to generate interpretations grounded in Odu corpus literature.

The Ifá system, from the Yoruba religious tradition, encodes signs using two columns of four marks. Each mark appears in one of two forms, producing 256 possible configurations. These correspond to the **256 Odu**, which form the foundation of the Ifá literary corpus.

This project explores that symbolic structure computationally:

1. Randomly generate a valid Odu pattern.
2. Encode the pattern deterministically as binary.
3. Map the two 4-bit columns to the 16 principal Odu.
4. Use the resulting Odu pair as a retrieval key.
5. Retrieve relevant literature and verses from a corpus.
6. Use an LLM to generate an interpretation grounded in retrieved sources.

The goal is not to reproduce religious practice, but to show how symbolic systems can be modeled computationally and combined with modern RAG pipelines.

## Why do this

This repository is a small experiment in combining:

* symbolic modeling of cultural knowledge systems
* deterministic encoding and indexing
* retrieval-augmented generation (RAG)
* language-model interpretation grounded in source texts

It serves mainly as a technical exploration and portfolio example of building a structured RAG pipeline around a non-trivial symbolic domain.

Example pipeline

```
random grid, e.g.

|  ||
|  |
||  |
|  |

    ↓
binary encoding
    ↓
column-major 8-bit representation
    ↓
integer ID (0–255)
    ↓
map to major Odu pair
    ↓
retrieve literature
    ↓
LLM generates an interpretation
```

## Disclaimer

Ifá divination is part of a living religious tradition practiced by trained priests and communities worldwide.
This project is not a substitute for that practice and should be understood purely as a computational and educational experiment.
