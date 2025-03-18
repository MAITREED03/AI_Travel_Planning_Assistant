import streamlit as st
from trip_agents import TripCrew  # Import the TripCrew class
from fpdf import FPDF  # For generating PDFs
import base64  # For encoding PDF for download
from dotenv import load_dotenv  # For loading environment variables
import os

# Load environment variables
load_dotenv()

# Function to generate a PDF
def generate_pdf(plan):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content to the PDF
    pdf.cell(200, 10, txt="Your AI-Generated Travel Plan", ln=True, align="C")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Recommended Cities:\n{plan['city_selection']}")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Destination Insights:\n{plan['city_research']}")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Detailed Itinerary:\n{plan['itinerary']}")
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Budget Breakdown:\n{plan['budget']}")

    # Save the PDF to a file
    pdf_output = "travel_plan.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Streamlit app
def main():
    st.set_page_config(page_title="AI Travel Planning Assistant", layout="wide")
    st.title("🤖 AI Travel Planning Assistant")

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Trip Preferences")
        travel_type = st.selectbox("Travel Type", ["Leisure", "Business", "Adventure", "Cultural"])
        interests = st.multiselect("Interests", ["History", "Food", "Nature", "Art", "Shopping", "Nightlife"])
        season = st.selectbox("Season", ["Summer", "Winter", "Spring", "Fall"])
        duration = st.slider("Trip Duration (days)", 1, 14, 7)
        budget = st.selectbox("Budget Range", ["$500-$1000", "$1000-$2000", "$2000-$5000", "Luxury"])

    # Button to generate the travel plan
    if st.button("Generate Travel Plan"):
        if not interests:
            st.error("Please select at least one interest.")
        elif not travel_type or not season or not duration or not budget:
            st.error("Please fill out all fields.")
        else:
            inputs = {
                "travel_type": travel_type,
                "interests": interests,
                "season": season,
                "duration": duration,
                "budget": budget
            }

            with st.spinner("🤖 AI Agents are working on your perfect trip..."):
                try:
                    # Run the TripCrew and capture the result (a dictionary)
                    crew_output = TripCrew(inputs).run()

                    # Debugging: inspect the raw crew_output structure
                    st.subheader("Debugging: Crew Output Data")
                    st.write("Type of output:", type(crew_output))
                    try:
                        st.json(crew_output)
                    except Exception as ex:
                        st.write(crew_output)

                    # Extract outputs using the keys from the returned dictionary
                    city_selection = crew_output.get('city_selection', "❌ No city selection found.")
                    city_research = crew_output.get('city_research', "❌ No city research found.")
                    itinerary = crew_output.get('itinerary', "❌ No itinerary generated.")
                    budget_breakdown = crew_output.get('budget', "❌ No budget breakdown available.")

                    # Display results in expanders
                    st.subheader("Your AI-Generated Travel Plan")
                    with st.expander("Recommended Cities"):
                        st.markdown(city_selection)
                        st.image("https://via.placeholder.com/600x400.png?text=Paris+Image", caption="Paris, France")
                    with st.expander("Destination Insights"):
                        st.markdown(city_research)
                    with st.expander("Detailed Itinerary"):
                        st.markdown(itinerary)
                    with st.expander("Budget Breakdown"):
                        st.markdown(budget_breakdown)

                    # Generate and display a download link for the PDF
                    pdf_file = generate_pdf(crew_output)
                    with open(pdf_file, "rb") as f:
                        pdf_data = f.read()
                    b64 = base64.b64encode(pdf_data).decode()
                    href = f'<a href="data:application/octet-stream;base64,{b64}" download="travel_plan.pdf">Download Your Travel Plan as PDF</a>'
                    st.markdown(href, unsafe_allow_html=True)

                    st.success("✅ Trip planning completed! Enjoy your journey!")
                except Exception as e:
                    st.error(f"An error occurred while processing the results: {e}")

if __name__ == "__main__":
    main()