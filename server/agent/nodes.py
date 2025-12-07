from langchain_google_genai import ChatGoogleGenerativeAI
from agent.tools import get_schema
from agent.safety import is_safe
from agent.tools import run_query

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# 1. Query Generator Node
def query_generator(state):
    question = state["question"]
    schema = get_schema()

    prompt = f"""
    You are an SQL generator. Use ONLY this schema:

    {schema}

    Convert the user request into a SELECT-only SQL query.
    """

    sql = llm.invoke(prompt + question).content
    return {"draft_sql": sql}


# 2. Safety Check Node
def safety_check(state):
    sql = state["draft_sql"]

    if is_safe(sql):
        return {"safe": True}
    else:
        return {"safe": False}


# 3. Execution Node
def execute_node(state):
    result = run_query(state["draft_sql"])
    return {"result": result}


# 4. Summary Node
def summary_node(state):
    result = state["result"]
    
    answer = llm.invoke(
        f"Summarize this result in simple text: {result}"
    ).content

    return {"final_answer": answer}
