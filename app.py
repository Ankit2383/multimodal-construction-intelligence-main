
import streamlit as st
from google import genai
from google.genai import types


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Construction Intelligence Platform",
    page_icon="🏗️",
    layout="wide"
)


# --------------------------------------------------
# GEMINI IMAGE ANALYSIS FUNCTION
# --------------------------------------------------

def analyze_image(api_key, uploaded_image, prompt):
    try:
        client = genai.Client(api_key=api_key)

        image_bytes = uploaded_image.getvalue()

        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=uploaded_image.type
        )

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=[prompt, image_part]
        )

        return response.text or "The AI returned an empty response."

    except Exception as error:
        return f"Analysis failed: {error}"


# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------

st.title("🏗️ Multimodal Construction Intelligence Platform")

st.write(
    "An AI-assisted platform for construction safety, "
    "crack inspection, project planning, and site advice."
)

st.info(
    "Upload construction images for AI-assisted analysis. "
    "Budget estimates are illustrative, not professional quotations."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Project Settings")

st.sidebar.write("Construction Intelligence Platform")

api_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password",
    help="Enter your private Gemini API key."
)

page = st.sidebar.radio(
    "Choose a feature",
    [
        "Dashboard",
        "Site Safety Audit",
        "Crack Diagnostics",
        "Project Planning",
        "Weather Advisory"
    ]
)


# --------------------------------------------------
# 1. DASHBOARD
# --------------------------------------------------

if page == "Dashboard":

    st.header("📊 Project Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Project Status", "Active")
    col2.metric("Core Modules", "4")
    col3.metric("AI Analysis", "Available")

    st.divider()

    st.subheader("Welcome!")

    st.write(
        "This platform demonstrates how AI can assist with "
        "construction-site observations and basic project planning."
    )

    st.subheader("Available Modules")

    st.markdown(
        """
        - 🦺 **Site Safety Audit:** Review visible PPE and potential hazards.
        - 🧱 **Crack Diagnostics:** Describe visible cracks and possible concerns.
        - 📊 **Project Planning:** Calculate an illustrative project budget.
        - 🌦️ **Weather Advisory:** View general advice for selected weather conditions.
        """
    )

    st.warning(
        "AI-generated observations are preliminary. "
        "They do not replace qualified safety inspections or structural assessments."
    )


# --------------------------------------------------
# 2. SITE SAFETY AUDIT
# --------------------------------------------------

elif page == "Site Safety Audit":

    st.header("🦺 Site Safety & PPE Audit")

    st.write(
        "Upload a photograph of a construction site to receive "
        "an AI-assisted review of visible safety conditions."
    )

    image = st.file_uploader(
        "Upload construction-site photo",
        type=["jpg", "jpeg", "png"],
        key="safety_image"
    )

    if image is not None:

        st.image(
            image,
            caption="Uploaded construction-site image",
            use_container_width=True
        )

        if st.button("Analyze Site Safety", key="analyze_safety"):

            if not api_key.strip():

                st.error(
                    "Enter your Gemini API key in the sidebar first."
                )

            else:

                prompt = """
                Analyze this construction-site photograph.

                Create a structured preliminary safety report containing:

                1. General observations about the visible site.
                2. Visible personal protective equipment (PPE), such as
                   helmets, high-visibility vests, boots, gloves, and harnesses.
                3. Potential hazards visible in the photograph.
                4. Suggested precautions and corrective actions.
                5. Limitations of the photograph and uncertain observations.

                For each potential hazard, describe its apparent concern level
                and explain the visible evidence. Do not claim that PPE is
                missing if the relevant person or area cannot be seen clearly.
                Do not invent details that are not visible.

                This is an AI-assisted preliminary review, not a certified
                construction safety inspection.
                """

                with st.spinner("Analyzing site safety..."):

                    result = analyze_image(
                        api_key,
                        image,
                        prompt
                    )

                st.subheader("AI Safety Assessment")
                st.markdown(result)


# --------------------------------------------------
# 3. CRACK DIAGNOSTICS
# --------------------------------------------------

elif page == "Crack Diagnostics":

    st.header("🧱 Crack Diagnostics")

    st.write(
        "Upload a photograph of a wall or concrete surface "
        "for an AI-assisted visual assessment."
    )

    image = st.file_uploader(
        "Upload wall or concrete photo",
        type=["jpg", "jpeg", "png"],
        key="crack_image"
    )

    if image is not None:

        st.image(
            image,
            caption="Uploaded wall or concrete surface",
            use_container_width=True
        )

        if st.button("Analyze Cracks", key="analyze_cracks"):

            if not api_key.strip():

                st.error(
                    "Enter your Gemini API key in the sidebar first."
                )

            else:

                prompt = """
                Examine this photograph of a wall or concrete surface.

                Provide a structured preliminary visual report containing:

                1. Visible cracks or surface defects, if any.
                2. Their apparent location, pattern, and direction.
                3. Possible causes, clearly labelled as possibilities.
                4. Recommended next steps and monitoring suggestions.
                5. Signs that warrant prompt inspection by a qualified professional.
                6. Limitations of drawing conclusions from a photograph.

                Do not invent cracks or defects that are not visible.
                Do not claim an exact crack width, structural integrity,
                or a definitive engineering diagnosis from the image alone.

                Recommend assessment by a qualified structural engineer
                when defects appear potentially serious.
                """

                with st.spinner("Analyzing wall or concrete surface..."):

                    result = analyze_image(
                        api_key,
                        image,
                        prompt
                    )

                st.subheader("AI Crack Assessment")
                st.markdown(result)


# --------------------------------------------------
# 4. PROJECT PLANNING AND COST ESTIMATION
# --------------------------------------------------

elif page == "Project Planning":

    st.header("📊 Project Planning & Cost Estimation")

    st.write(
        "Estimate a basic construction budget using the built-up area "
        "and an assumed cost per square foot."
    )

    area = st.number_input(
        "Built-up area (square feet)",
        min_value=100,
        value=1000,
        step=100
    )

    rate = st.number_input(
        "Estimated cost per square foot (₹)",
        min_value=500,
        value=1800,
        step=100
    )

    progress = st.slider(
        "Project completion (%)",
        min_value=0,
        max_value=100,
        value=0
    )

    budget = area * rate
    estimated_spent = budget * progress / 100
    remaining = budget - estimated_spent

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Estimated Total Budget",
        f"₹{budget:,.0f}"
    )

    col2.metric(
        "Estimated Cost Incurred",
        f"₹{estimated_spent:,.0f}"
    )

    col3.metric(
        "Estimated Remaining Budget",
        f"₹{remaining:,.0f}"
    )

    st.progress(progress / 100)

    st.caption(
        "These calculations assume that spending follows the completion "
        "percentage. Actual project expenditure may differ significantly."
    )


# --------------------------------------------------
# 5. WEATHER ADVISORY
# --------------------------------------------------

elif page == "Weather Advisory":

    st.header("🌦️ Construction Site Weather Advisory")

    st.write(
        "Select a weather condition to view general construction-site precautions."
    )

    weather = st.selectbox(
        "Select weather condition",
        [
            "Normal",
            "High Wind",
            "Heavy Rain",
            "Extreme Heat"
        ]
    )

    advice = {
        "Normal": """
        - Follow standard site safety procedures.
        - Inspect tools and equipment before use.
        - Keep walkways and work areas clear.
        """,

        "High Wind": """
        - Check official wind measurements and site safety limits.
        - Secure loose materials and temporary structures.
        - Suspend crane or work-at-height activities when required
          by the site safety plan.
        """,

        "Heavy Rain": """
        - Check drainage and water accumulation.
        - Watch for slippery surfaces and electrical hazards.
        - Inspect excavations and access routes.
        - Stop outdoor work if conditions become unsafe.
        """,

        "Extreme Heat": """
        - Provide drinking water, shade, and rest breaks.
        - Monitor workers for signs of heat stress.
        - Adjust strenuous work according to site procedures.
        """
    }

    st.subheader(f"Precautions for {weather}")

    st.warning(advice[weather])

    st.caption(
        "This module provides general guidance, not a live weather forecast. "
        "Follow official weather alerts and qualified site personnel."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Multimodal Construction Intelligence Platform | "
    "Educational project prototype"
)
