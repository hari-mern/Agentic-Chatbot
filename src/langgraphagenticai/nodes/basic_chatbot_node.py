from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot logic implementaion
    """

    def __init__(self,model):
        self.llm=model

    def process(self,state:State)-> dict:
        """
        processes the input state and generates a chatbot respose.
        """

        return {"messages": self.llm.invoke(state['messages'])}