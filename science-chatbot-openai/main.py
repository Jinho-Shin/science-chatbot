import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
import openai
openai.api_key="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"

############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        query= text
        response = openai.Completion.create(
        engine= "text-davinci-002",
            prompt=query,
            temperature=0.1,
            max_tokens=256,
            top_p=1,
            best_of=1,
            frequency_penalty=0.47,
            presence_penalty=0.31)
        answer = response['choices'][0]['text']
        output.append(answer)
    
    return SimpleText(dict(text=output))
