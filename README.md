# npchat-eval

This project is a Python library with a command line to measure the quality of the npchat retriever.

npchat is a RAG system built over blog articles.
In npchat we don't have a way to know if the retriever is returning the correct references.

Also we have several RAG features and we want to test if turning any off will change the quality of the retrieval.

## Running tests

Run the test suite with:

```
uv run pytest -v
```

Licensed under the Apache License, Version 2.0.
See [LICENSE](LICENSE) for details.