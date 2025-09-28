from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from typing import Dict, List, Union
import os


class AgentState(TypedDict):
    messages: List[Union[HumanMessage,AIMessage]]

llm  = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = "AIzaSyCwnj3Ji9LnHGyhi_fQ4ucA6fP-0-69i9I"
)


def process(state: AgentState) -> AgentState:
    response  = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print("====Token usage===")
    info = response.usage_metadata
    print(f"input tokens = {info["input_tokens"]} \noutput token = {info["output_tokens"]} ")
    print("===Response===")
    print(response.content)
    print("===Response===")
    return state


graph = StateGraph(AgentState)

graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()


conversation_history = []
user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    res = agent.invoke({"messages": conversation_history})
    conversation_history = res["messages"]
    print(conversation_history)
    user_input = input("Enter: ")