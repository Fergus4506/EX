class ConcatenateHelloWorld:     

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {       
                    "text1": ("STRING", {"multiline": False, "default": "Hello"}),
                    "text2": ("STRING", {"multiline": False, "default": "World"}),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "Tutorial Nodes"

    def concatenate_text(self, text1, text2):

        text_out = text1 + " " + text2
        
        return (text_out,)
class print_textt:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }
    RETURN_TYPES = ()
    FUNCTION = "print_text"
    CATEGORY = "Tutorial Nodes"
    def print_text(self, text,extra_pnginfo):
        workflow = extra_pnginfo[0]["workflow"]
        node = next(
            (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
            None,
        )
        if node:
            node["widgets_values"] = [text]
        return {}