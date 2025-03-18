AI Travel Planning Assistant
Overview
The AI Travel Planning Assistant is a Streamlit-based web application that helps users generate personalized travel plans based on their preferences. Users can input their travel type, interests, preferred season, trip duration, and budget, and the app will generate a detailed travel plan, including recommended cities, destination insights, a detailed itinerary, and a budget breakdown.

The app also allows users to download their travel plan as a PDF for easy sharing and reference.

Features
User-Friendly Interface: Built with Streamlit for an intuitive and interactive experience.

Customizable Inputs: Users can specify their travel preferences, including:

Travel type (e.g., Leisure, Adventure, Cultural, Business)

Interests (e.g., Food, Nature, Art, Nightlife)

Preferred season (e.g., Summer, Winter, Spring, Autumn)

Trip duration (1–14 days)

Budget range (e.g., 
500
–
500–1000, 
1000
–
1000–2000)
AI-Powered Travel Plans: Uses the TripCrew class to generate personalized travel plans.

Structured Output: Displays the travel plan in collapsible sections, including:

Recommended cities

Destination insights

Detailed itinerary

Budget breakdown

PDF Export: Users can download their travel plan as a PDF.

Getting Started
Prerequisites
Before running the app, ensure you have the following installed:

Python 3.8 or higher

Streamlit

FPDF (for PDF generation)

python-dotenv (for environment variables)

Installation
Clone the Repository:

git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner

Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

If you don't have a requirements.txt file, install the required packages manually:
pip install streamlit fpdf python-dotenv


Running the App

Run the Streamlit App:
streamlit run app.py

Access the App:

Open your browser and navigate to http://localhost:8501.

Use the sidebar to input your travel preferences and click Generate Travel Plan.

How It Works
User Inputs:

The user selects their preferences in the sidebar.

The app validates the inputs to ensure all fields are filled out.

Travel Plan Generation:

The TripCrew class generates a travel plan based on the inputs.

Display Results:

The app displays the travel plan in collapsible sections.

An image of the recommended city is shown in the "Recommended Cities" section.

Save and Share:

The app generates a PDF of the travel plan and provides a download link.

Example Output
Inputs:
Travel Type: Leisure

Interests: Food, Art

Season: Summer

Duration: 7 days

Budget: 
1000
–
1000–2000

Output:
Recommended Cities: Paris, France (with an image of Paris)

Destination Insights: Paris is known for its art, culture, and cuisine. It's perfect for your interests!

Detailed Itinerary:

Day 1: Visit the Eiffel Tower.

Day 2: Explore the Louvre Museum.

Day 3: Enjoy local cuisine.

Budget Breakdown:

Accommodation: $300

Food: $200

Activities: $150

Total: $650

Download Link: A link to download the travel plan as a PDF.

Customization
Integrating AI Models
The app can be customized to use different AI models or APIs for generating travel plans. Here’s how:

Using Hugging Face Transformers:

Replace the hardcoded logic in the TripCrew class with calls to a Hugging Face model (e.g., GPT-2, Mistral-7B).

Using OpenAI GPT:

Replace the logic with calls to the OpenAI API.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Streamlit for the easy-to-use web app framework.

FPDF for generating PDFs.

TripCrew for the travel plan generation logic.

Contact
For questions or feedback, please contact:

Your Name- Moitri De

Email: maitreede330@gmail.com

GitHub:https://github.com/MAITREED03
