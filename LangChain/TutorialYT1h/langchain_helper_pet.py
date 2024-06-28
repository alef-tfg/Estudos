from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType


def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature = 1, model_name="gpt-3.5-turbo-instruct")

    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'pet_color'],
        template = 'I have a {animal_type} pet and i want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet.'
    )

    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key="pet_name")
    
    response = name_chain.invoke({'animal_type': animal_type, 'pet_color': pet_color})
    return response

def langchain_agent():
    llm = OpenAI(temperature=0)
    tools = load_tools(["wikipedia", "llm-math"], llm = llm)

    agent = initialize_agent(
        tools, llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose = True
    )

    result = agent.invoke("What is the average age of a dog? Multiply the age by 3")


if __name__ == "__main__":
    langchain_agent()
    # print(generate_pet_name("snake", "gold"))
