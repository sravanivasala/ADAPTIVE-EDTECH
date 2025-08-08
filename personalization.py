
from backend.utils.prompt_templates import content_prompt

def recommend_content(user_id):
    # Mock user profile (this would normally come from a database or model)
    profile = {
        "level": "beginner",
        "interests": ["AI", "Python"]
    }
    
    # Format the prompt using the profile
    prompt = content_prompt.format(profile=profile)

    # Return mocked recommended content
    return {
        "user_id": user_id,
        "recommended": ["Intro to AI", "Python Basics"],
        "generated_prompt": prompt
    }
