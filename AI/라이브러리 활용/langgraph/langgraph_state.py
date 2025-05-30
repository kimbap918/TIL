import os
import operator
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

from typing import TypedDict

# State
from pydantic import BaseModel

# State schema
class StateSchema(BaseModel):
    counter: int
    alphabet: list[str]

# Initialize state
initial_state = StateSchema(counter=0, alphabet=[])

# Node
def node_a(state: dict) -> dict:
    state['counter'] += 1
    state['alphabet'] = state['alphabet'] + ["hello!"]
    return state

# Graph
graph_builder = StateGraph(StateSchema, initial_state)
graph_builder.add_node("node_a", node_a)

# Edge
graph_builder.add_edge(START, "node_a")
graph_builder.add_edge("node_a", END)


graph = graph_builder.compile()

from IPython.display import display
from PIL import Image
from io import BytesIO

try:
    # 이미지 데이터를 bytes로 받음
    img_bytes = graph.get_graph().draw_mermaid_png()
    img = Image.open(BytesIO(img_bytes))
    img.save("graph.png")
except:
    pass
