
# Multimodal Construction Intelligence Platform

An AI-powered web application that uses image analysis and interactive tools to support construction-site safety reviews, crack inspection, project cost estimation, and general weather-related safety guidance.

## Features

### 1. AI Site Safety Audit
- Upload a construction-site photograph.
- Identify visible personal protective equipment (PPE).
- Highlight potential hazards.
- Generate preliminary safety recommendations.

### 2. AI Crack Diagnostics
- Upload a wall or concrete photograph.
- Describe visible cracks and surface defects.
- Explore possible causes and recommended next steps.

### 3. Project Planning
- Enter the built-up area and estimated cost per square foot.
- Calculate the estimated project budget.
- Estimate incurred and remaining costs using a completion percentage.

### 4. Weather Advisory
- Select a weather condition.
- View general construction-site precautions.

## Technology Stack

- Python
- Streamlit
- Google Gemini API
- Pillow
- Pandas

## Project Structure

```text
multimodal-construction-intelligence/
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Prerequisites
- Python installed on your computer
- A Google Gemini API key for AI image analysis

### Setup

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Start the application:

```bash
python -m streamlit run app.py
```

5. Open the local URL shown in the terminal.

6. Enter your Gemini API key in the application sidebar to use the AI analysis features.

## API Key Security

Keep your Gemini API key private. Do not hardcode it in source files or commit it to GitHub. For public deployment, configure the key using Streamlit Community Cloud secrets.

## Limitations

- Image assessments depend on image quality, lighting, and visibility.
- AI-generated observations may be incomplete or incorrect.
- Cost estimates are illustrative and do not represent professional quotations.
- Weather advice is general guidance and is not a live weather forecast.
- The application does not replace qualified construction safety inspections or structural engineering assessments.

## Future Improvements

- Export AI reports as PDF.
- Add historical analysis and report tracking.
- Add a live weather API integration.
- Add project progress visualizations.
- Improve error handling and input validation.

## Disclaimer

This application is an educational prototype. Its AI-generated output must not be treated as a certified safety inspection or structural diagnosis.
