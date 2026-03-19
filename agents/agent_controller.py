from llama_index.core.agent import ReActAgent


def create_agent(context, tools, llm, verbose=True, max_iterations=10):
    tools = tools
    context = context
    llm = llm
    agent = ReActAgent(llm=llm, tools=tools, context=context, verbose=verbose, max_iterations=max_iterations, memory=None)
    return agent
