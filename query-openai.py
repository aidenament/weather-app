import os
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_weather(location):
    """
    Query OpenAI API to get weather information for a specific location.
    
    Args:
        location (str): The location to get weather information for
        
    Returns:
        str: The weather information response from OpenAI
    """
    if not os.environ.get("OPENAI_API_KEY"):
        return "Error: OPENAI_API_KEY environment variable not set"
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": f"What is the weather in {location} right now?"
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error querying OpenAI API: {str(e)}"

if __name__ == "__main__":
    # Example usage
    location = input("Enter a location: ")
    weather_info = get_weather(location)
    print(f"\nWeather information for {location}:")
    print(weather_info)
