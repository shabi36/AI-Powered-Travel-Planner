# AI-Powered Travel Itinerary Generator

An intelligent web app that creates luxurious, personalized travel itineraries based on user preferences like destination, travel month, budget, dietary needs, and interests — powered by Google's Gemini LLM.

## Problem Statement

Travelers, especially families or those seeking luxury experiences, often struggle to plan customized, experience-rich itineraries. This solution automates the process using AI to save time, enhance personalization, and ensure a seamless travel experience.

---

## Why This Problem?

Planning a high-quality, interest-aligned, and season-aware travel plan can be time-consuming and complex — especially for those with specific needs like dietary preferences, weather concerns, or activity-based interests. This project simplifies it with smart automation.

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
