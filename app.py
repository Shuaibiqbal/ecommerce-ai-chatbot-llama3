from flask import Flask, render_template, request, jsonify
# from langchain.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from context_data import get_context

app = Flask(__name__)

# llm = Ollama(model="llama3")
llm = ChatOllama(model="llama3")


# General question model
general_prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant.\n\nQuestion: {question}\nAnswer:"
)
general_chain = LLMChain(llm=llm, prompt=general_prompt)

# Context-based model
context_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an e-commerce assistant.

Only answer if the context below contains the information. If not, say:
"Sorry, I don't have enough information."

Context:
{context}

Question: {question}
Answer:
"""
)
context_chain = LLMChain(llm=llm, prompt=context_prompt)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("message", "")

    # Simulate "cloud context" (you can connect to a real DB or API)
    context = get_context(question)

    if context:
        # Use context-based model
        response = context_chain.invoke({"context": context, "question": question})
    else:
        # Fallback to general model
        response = general_chain.invoke({"question": question})

    return jsonify({"response": response["text"].strip()})


if __name__ == "__main__":
    app.run(debug=True)
