# -*- coding: utf-8 -*-
"""runtime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/agent87/IhuguraChatBot/blob/main/haystack/runtime.ipynb

# Setup the Haystack engine & related
"""

#!pip install --upgrade pip
#!pip install git+https://github.com/deepset-ai/haystack.git#egg=farm-haystack[colab]#

from haystack.utils import convert_files_to_dicts, print_answers
from haystack.nodes import FARMReader, TransformersReader

# In-Memory Document Store
from haystack.document_stores import InMemoryDocumentStore

document_store = InMemoryDocumentStore()





dicts = [{ "content" : b, "meta" : {'name': 'Criminal Procedure'}}]

document_store.write_documents(dicts)

# An in-memory TfidfRetriever based on Pandas dataframes

from haystack.nodes import TfidfRetriever

retriever = TfidfRetriever(document_store=document_store)

# Load a  local model or any of the QA models on
# Hugging Face's model hub (https://huggingface.co/models)

reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

from haystack.pipelines import ExtractiveQAPipeline

pipe = ExtractiveQAPipeline(reader, retriever)

prediction = pipe.run(
    query="what is an unlawful detention?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
)

print_answers(prediction, details="minimum")