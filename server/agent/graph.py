from langgraph.graph import StateGraph, END
from agent.nodes import (
    query_generator, safety_check,
    execute_node, summary_node
)

class AgentState(dict):
    question: str
    draft_sql: str
    safe: bool
    result: dict
    final_answer: str

graph = StateGraph(AgentState)

graph.add_node("generate", query_generator)
graph.add_node("safety", safety_check)
graph.add_node("execute", execute_node)
graph.add_node("summary", summary_node)

graph.set_entry_point("generate")

graph.add_edge("generate", "safety")

# branching
graph.add_conditional_edges(
    "safety",
    lambda state: "ok" if state["safe"] else "retry",
    {
        "ok": "execute",
        "retry": "generate"
    }
)

graph.add_edge("execute", "summary")
graph.add_edge("summary", END)

app = graph.compile()
