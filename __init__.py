from .check_modul import *
from .nodes.nodes import *
from .nodes.openAi_api import *

NODE_CLASS_MAPPINGS = {
    "Concatenate Hello World": ConcatenateHelloWorld,
    "openai_api_response": openai_api_response,
    "print_text": print_textt,
    }
    
print("\033[34mComfyUI Tutorial Nodes: \033[92mLoaded\033[0m")    