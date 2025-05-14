# AI-Powered Travel Planner

An intelligent web app that creates personalized travel itineraries based on user preferences like destination, travel month, budget, dietary needs, and interests — powered by Google's Gemini LLM.

## Problem Statement

Design an AI assistant that generates end-to-end travel itineraries based on user input such as destination, duration, budget, and interests.The solution should suggest travel options, accommodations, key attractions, and local cuisines or beverages to try.



---

## Why This Problem?

Lack of Personalization in traditional travel booking platforms.Time-consuming to manually plan itineraries that cater to specific interests, budgets, and dietary needs.Rapid growth in luxury and experience-based travel, yet limited automated tools to curate it effectively.Opportunity to leverage LLMs to deliver intelligent, context-aware travel planning assistance.



---

## Proposed Solution
- Flask Web App: Built a Flask-based web application with a user-friendly interface.
- User Input: Collects data from users via an HTML form (destination, budget, interests, etc.).
- Backend Processing: Flask app collects user input, processes it with LangChain, and feeds it into the Gemini LLM to generate the itinerary.
- Prompt Engineering: A custom prompt formats the LLM's output with specific instructions (headings, bullet points, bold text).
- LLM Response: Gemini 1.5 Pro generates the travel itinerary based on user preferences.
- Result Rendering: Flask renders the output on a web page with proper formatting using CSS and regex to handle text styles.



---

## Tech Stack

- *Frontend:* HTML, CSS 
- *Backend:* Python (Flask Framework)
- *LLM Integration:* Google Gemini via LangChain
- *Prompt Engineering:* LangChain PromptTemplate
- *Environment Management:* python-dotenv

---

## Features

- 7 user input fields: Destination, Month, Budget, Duration, Travel Style, Interests, Dietary Preferences
- Rich and well-structured AI-generated itinerary
- Responsive HTML interface with structured formatting
- LLM response processing with Markdown to HTML conversion for clean display
- Support for luxury travel tips, food suggestions, and cultural experiences

---


## Challenges Faced

- Formatting AI response for HTML readability (Markdown → HTML)
- Handling user inputs with special characters (e.g., asterisks, colons)
- Structuring prompts to generate professional, elegant outputs
- Ensuring layout looks clean across devices

## References

- LangChain Documentation
https://docs.langchain.com/

- Google Gemini API via LangChain
https://python.langchain.com/docs/integrations/chat/google_gemini/

- Flask Official Documentation
https://flask.palletsprojects.com/

- Markdown Guide
https://www.markdownguide.org/

- Python dotenv Library
https://pypi.org/project/python-dotenv/

- Regex in Python
https://docs.python.org/3/library/re.html

- Requests Module
https://docs.python-requests.org/en/latest/
