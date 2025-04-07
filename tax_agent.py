from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
import os
from dotenv import load_dotenv
from phi.model.ollama import Ollama

# Load environment variables
load_dotenv()

# Create Tax Agent
tax_agent = Agent(
    model=Ollama(id="deepseek-r1:1.5b"),
    tools=[DuckDuckGo(), Newspaper4k()],
    description="You are a professional tax consultant with expertise in multiple countries' tax systems.",
    instructions=[
        "For any tax-related query:",
        "1. FIRST search for the latest tax rules and rates from official government websites",
        "2. Provide the ACTUAL current tax rates and brackets",
        "3. Show the EXACT calculation if numbers are provided",
        "4. Include specific examples with numbers",
        "5. Cite the official sources you found",
        "6. If the query is about a specific country, focus on that country's tax laws",
        "7. For calculations, show the step-by-step process with actual numbers",
        "8. Be direct and specific - avoid generic disclaimers",
        "9. If you find multiple sources, use the most recent official source",
        "10. If you can't find specific information, say so directly",
    ],
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
)


def get_tax_answer(query: str, country: str = "India") -> str:
    """
    Get tax-related answer using the tax agent
    """
    prompt = f"""
    Country: {country}
    Query: {query}
    
    Please provide:
    1. Current tax rates and brackets
    2. Specific calculation if numbers are provided
    3. Official source of information
    4. Example calculation if applicable
    """

    response = tax_agent.run(prompt)
    return response.content


# Example usage
if __name__ == "__main__":
    # Test the agent
    test_query = "What is the income tax rate for salary between 5-10 lakhs in India?"
    answer = get_tax_answer(test_query)
    print(answer)
