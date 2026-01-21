from typing import List


def retrieve_documents(query: str) -> List[str]:
    if not query.strip():
        return []
    return ["service_intro.md"]
