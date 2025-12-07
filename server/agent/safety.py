import re

DANGEROUS = [
    "drop",
    "delete",
    "update",
    "insert",
    "alter",
    "truncate",
]

def is_safe(query: str) -> bool:
    q = query.lower().strip()

    # Must be SELECT only
    if not q.startswith("select"):
        return False

    # Block destructive commands
    for cmd in DANGEROUS:
        if re.search(rf"\b{cmd}\b", q):
            return False

    return True
