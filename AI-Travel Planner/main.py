from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import markdown

app = Flask(__name__)

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

template = """
You are a smart and professional AI travel assistant.

Generate a luxurious, well-organized, and personalized travel itinerary* based on the following user preferences:

- Destination: {destination}  
- Duration (in days): {duration}  
- Budget (in Rs): {budget}  
- Month of Travel: {month}  
- Traveler style: {travel-style}  
- Interests: {interests}  
- Dietary Preferences: {dietary}

Instructions:
- Consider weather, events, and travel feasibility based on the month.
- Structure the plan clearly, day by day (Day 1, Day 2, etc.), using bullet points and bolded headings.
- Include:
  - Travel Options: For arrival and local transportation
  - Accommodation: Tailored to traveler type and comfort
  - Experiences & Activities: Relevant to interests
  - Local Food & Beverages: Include items suitable for dietary preferences
  - Luxury Tips & Suggestions: To elevate the experience


Ensure the tone is elegant and professional. Format the content cleanly with spacing and bold section titles. Use markdown formatting for structure and clarity.
"""

prompt_template = PromptTemplate.from_template(template)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_inputs = {
        "destination": request.form['destination'],
        "duration": request.form['duration'],
        "budget": request.form['budget'],
        "interests": request.form['interests'],
        "month": request.form['month'],
        "dietary": request.form['dietary'],
        "travel-style": request.form['travel-style']
    }

    chain = prompt_template | llm
    response = chain.invoke(user_inputs)

    travel_plan_md = response.content
    travel_plan_html = markdown.markdown(travel_plan_md)

    return render_template('result.html', travel_plan=travel_plan_html)

if __name__ == "__main__":
    app.run(debug=True)