"""
================================================================================
HORIZON QUICK-AUDIT - Sales Enablement Tool
================================================================================

iOS "Add to Home Screen" Instructions:
--------------------------------------
1. Open this app in Safari on your iPhone
2. Tap the Share button (square with arrow pointing up)
3. Scroll down and tap "Add to Home Screen"
4. Name it "Horizon Audit" and tap "Add"
5. The app will now launch full-screen without the browser address bar!

Built by: Manav Davis
Purpose: Demonstrating sales-focused technical solutions for Horizon Payments
================================================================================
"""

import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# =============================================================================
# PAGE CONFIGURATION
# =============================================================================

st.set_page_config(
    page_title="Horizon Quick-Audit",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =============================================================================
# BRAND COLORS - FinTech Minimalist
# =============================================================================

DEEP_NAVY = "#003366"
TRUST_BLUE = "#2E86C1"
SUCCESS_GREEN = "#27AE60"
WASTE_RED = "#E74C3C"
BASE_GREY = "#7F8C8D"
CLEAN_WHITE = "#FFFFFF"
LIGHT_BG = "#F8FAFC"

# =============================================================================
# CUSTOM CSS - Native iPhone App Experience
# =============================================================================

st.markdown(f"""
<style>
    /* Hide ALL Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}
    [data-testid="stToolbar"] {{display: none;}}
    [data-testid="stDecoration"] {{display: none;}}
    [data-testid="stStatusWidget"] {{display: none;}}

    /* Remove default padding for app-like feel */
    .main .block-container {{
        padding: 1rem 1rem 2rem 1rem;
        max-width: 480px;
        margin: 0 auto;
    }}

    /* Smooth animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.02); }}
    }}

    /* App header - premium feel */
    .app-header {{
        background: linear-gradient(135deg, {DEEP_NAVY} 0%, #004080 100%);
        color: {CLEAN_WHITE};
        padding: 1.5rem 1rem;
        border-radius: 0 0 20px 20px;
        text-align: center;
        margin: -1rem -1rem 1.5rem -1rem;
        box-shadow: 0 4px 20px rgba(0,51,102,0.25);
    }}

    .app-header h1 {{
        margin: 0;
        font-size: 1.4rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }}

    .app-header .tagline {{
        margin: 0.3rem 0 0 0;
        font-size: 0.8rem;
        opacity: 0.85;
        font-weight: 400;
    }}

    /* Tab styling - iOS segmented control look */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0;
        background: #E8EEF4;
        border-radius: 12px;
        padding: 4px;
        margin-bottom: 1.5rem;
    }}

    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        padding: 0.6rem 1rem;
        font-weight: 600;
        font-size: 0.9rem;
        color: {DEEP_NAVY};
        background: transparent;
        border: none;
        flex: 1;
        justify-content: center;
    }}

    .stTabs [aria-selected="true"] {{
        background: {CLEAN_WHITE} !important;
        color: {DEEP_NAVY} !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}

    .stTabs [data-baseweb="tab-highlight"] {{
        display: none;
    }}

    .stTabs [data-baseweb="tab-border"] {{
        display: none;
    }}

    /* Waste metric card - the big number */
    .waste-card {{
        background: linear-gradient(135deg, {WASTE_RED} 0%, #C0392B 100%);
        color: {CLEAN_WHITE};
        padding: 1.8rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(231,76,60,0.35);
        animation: fadeIn 0.4s ease-out;
    }}

    .waste-card .label {{
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        opacity: 0.95;
    }}

    .waste-card .amount {{
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0.4rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }}

    .waste-card .subtext {{
        font-size: 0.8rem;
        opacity: 0.9;
    }}

    /* Narrative box - the explanation */
    .narrative-box {{
        background: {LIGHT_BG};
        border-left: 4px solid {TRUST_BLUE};
        padding: 1.2rem;
        border-radius: 0 12px 12px 0;
        margin: 1.5rem 0;
        animation: fadeIn 0.5s ease-out;
    }}

    .narrative-box p {{
        margin: 0;
        color: #444;
        font-size: 0.9rem;
        line-height: 1.6;
    }}

    .narrative-box strong {{
        color: {DEEP_NAVY};
    }}

    .narrative-box .highlight {{
        color: {WASTE_RED};
        font-weight: 600;
    }}

    .narrative-box .savings {{
        color: {SUCCESS_GREEN};
        font-weight: 600;
    }}

    /* Form styling - clean and premium */
    .priority-badge {{
        background: linear-gradient(135deg, {SUCCESS_GREEN} 0%, #1E8449 100%);
        color: {CLEAN_WHITE};
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 1rem;
    }}

    /* Input fields - iOS style */
    .stTextInput > div > div > input {{
        border-radius: 12px;
        border: 2px solid #E0E5EC;
        padding: 0.9rem 1rem;
        font-size: 1rem;
        background: {CLEAN_WHITE};
        transition: all 0.2s ease;
    }}

    .stTextInput > div > div > input:focus {{
        border-color: {TRUST_BLUE};
        box-shadow: 0 0 0 3px rgba(46,134,193,0.15);
    }}

    .stTextInput > label {{
        font-weight: 600;
        color: {DEEP_NAVY};
        font-size: 0.9rem;
    }}

    /* File uploader - clean */
    .stFileUploader > div {{
        border-radius: 12px;
        border: 2px dashed #D0D5DC;
        background: {LIGHT_BG};
    }}

    .stFileUploader > label {{
        font-weight: 600;
        color: {DEEP_NAVY};
        font-size: 0.9rem;
    }}

    /* Slider styling */
    .stSlider > div > div > div > div {{
        background: {TRUST_BLUE} !important;
    }}

    .stSlider > label {{
        font-weight: 600;
        color: {DEEP_NAVY};
        font-size: 0.9rem;
    }}

    /* All buttons - full width, premium feel */
    .stButton > button {{
        width: 100%;
        padding: 1rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 700;
        border-radius: 14px;
        border: none;
        background: linear-gradient(135deg, {DEEP_NAVY} 0%, #004080 100%);
        color: {CLEAN_WHITE};
        box-shadow: 0 4px 15px rgba(0,51,102,0.3);
        transition: all 0.2s ease;
        min-height: 56px;
        letter-spacing: 0.3px;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,51,102,0.4);
    }}

    .stButton > button:active {{
        transform: translateY(0);
    }}

    /* Success state */
    .success-card {{
        background: linear-gradient(135deg, {SUCCESS_GREEN} 0%, #1E8449 100%);
        color: {CLEAN_WHITE};
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 8px 25px rgba(39,174,96,0.35);
        animation: fadeIn 0.4s ease-out;
    }}

    .success-card h3 {{
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
    }}

    .success-card p {{
        margin: 0;
        opacity: 0.95;
        font-size: 0.9rem;
    }}

    /* Section labels */
    .section-label {{
        color: {DEEP_NAVY};
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }}

    /* Divider */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #D0D5DC, transparent);
        margin: 1.5rem 0;
    }}

    /* Chart container */
    .chart-container {{
        background: {CLEAN_WHITE};
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        margin: 1rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SESSION STATE
# =============================================================================

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# =============================================================================
# APP HEADER
# =============================================================================

st.markdown("""
<div class="app-header">
    <h1>Horizon Quick-Audit</h1>
    <p class="tagline">See What You're Really Paying</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# TWO-TAB NAVIGATION
# =============================================================================

tab1, tab2 = st.tabs(["Visual Audit", "Priority Handoff"])

# =============================================================================
# TAB 1: VISUAL AUDIT (THE PITCH)
# =============================================================================

with tab1:
    # Sliders in columns to prevent weird stretching
    col1, col2 = st.columns([1, 1])

    with col1:
        monthly_volume = st.slider(
            "Monthly Volume",
            min_value=10000,
            max_value=250000,
            value=50000,
            step=5000,
            format="$%d"
        )

    with col2:
        current_rate = st.slider(
            "Current Rate",
            min_value=2.0,
            max_value=5.0,
            value=3.5,
            step=0.1,
            format="%.1f%%"
        )

    st.markdown("<hr>", unsafe_allow_html=True)

    # ==========================================================================
    # THE "WHY" LOGIC
    # ==========================================================================

    # True cost (Interchange) is approximately 1.8%
    INTERCHANGE_RATE = 1.8

    # Calculate segments
    interchange_cost = monthly_volume * (INTERCHANGE_RATE / 100)
    total_fees = monthly_volume * (current_rate / 100)
    processor_markup = total_fees - interchange_cost  # The "Waste"

    # Horizon cuts the markup in half (40% of the waste eliminated)
    horizon_savings = processor_markup * 0.5
    remaining_markup = processor_markup - horizon_savings

    # Annual calculations
    annual_waste = processor_markup * 12
    annual_savings = horizon_savings * 12

    # ==========================================================================
    # SIMPLE BREAKDOWN - Where Your Money Goes
    # ==========================================================================

    # What Horizon would charge (interchange + small markup)
    horizon_total = interchange_cost + (remaining_markup * 0.5)

    st.markdown(f"""
    <div style="background: {LIGHT_BG}; border-radius: 16px; padding: 1.2rem; margin-bottom: 1rem;">
        <p style="margin: 0 0 1rem 0; font-weight: 700; color: {DEEP_NAVY}; font-size: 0.9rem;">
            Where Your ${total_fees:,.0f}/month Goes:
        </p>

        <div style="margin-bottom: 0.8rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: #666;">Visa & Mastercard (unavoidable)</span>
                <span style="font-weight: 600; color: {DEEP_NAVY};">${interchange_cost:,.0f}</span>
            </div>
            <div style="background: #E0E0E0; border-radius: 8px; height: 12px; overflow: hidden;">
                <div style="background: {BASE_GREY}; height: 100%; width: 100%;"></div>
            </div>
        </div>

        <div>
            <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                <span style="color: {WASTE_RED}; font-weight: 600;">Processor's Markup (the waste)</span>
                <span style="font-weight: 700; color: {WASTE_RED};">${processor_markup:,.0f}</span>
            </div>
            <div style="background: #E0E0E0; border-radius: 8px; height: 12px; overflow: hidden;">
                <div style="background: {WASTE_RED}; height: 100%; width: 100%;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================================
    # BEFORE vs AFTER - Simple Comparison
    # ==========================================================================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="background: #FFF5F5; border: 2px solid {WASTE_RED}; border-radius: 14px; padding: 1.2rem; text-align: center; height: 140px;">
            <div style="font-size: 0.75rem; color: {WASTE_RED}; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">Now</div>
            <div style="font-size: 2rem; font-weight: 800; color: {WASTE_RED}; margin: 0.3rem 0;">${total_fees:,.0f}</div>
            <div style="font-size: 0.8rem; color: #666;">per month</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: #F0FFF4; border: 2px solid {SUCCESS_GREEN}; border-radius: 14px; padding: 1.2rem; text-align: center; height: 140px;">
            <div style="font-size: 0.75rem; color: {SUCCESS_GREEN}; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">With Horizon</div>
            <div style="font-size: 2rem; font-weight: 800; color: {SUCCESS_GREEN}; margin: 0.3rem 0;">${total_fees - horizon_savings:,.0f}</div>
            <div style="font-size: 0.8rem; color: #666;">per month</div>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================================================
    # BIG SAVINGS CARD
    # ==========================================================================

    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {SUCCESS_GREEN} 0%, #1E8449 100%); color: white; padding: 1.5rem; border-radius: 16px; text-align: center; margin: 1rem 0; box-shadow: 0 8px 25px rgba(39,174,96,0.35);">
        <div style="font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.95;">You Save</div>
        <div style="font-size: 2.5rem; font-weight: 800; margin: 0.3rem 0;">${horizon_savings:,.0f}/mo</div>
        <div style="font-size: 1.1rem; font-weight: 600; opacity: 0.95;">${annual_savings:,.0f} per year</div>
    </div>
    """, unsafe_allow_html=True)

    # ==========================================================================
    # SIMPLE EXPLANATION
    # ==========================================================================

    st.markdown(f"""
    <div style="background: {LIGHT_BG}; border-left: 4px solid {TRUST_BLUE}; padding: 1rem; border-radius: 0 12px 12px 0; margin-top: 1rem;">
        <p style="margin: 0; color: #444; font-size: 0.9rem; line-height: 1.6;">
            <strong style="color: {DEEP_NAVY};">The Problem:</strong> Your processor charges a "flat rate" of {current_rate}%.
            But Visa/Mastercard only takes about 1.8%. The rest—<strong style="color: {WASTE_RED};">${processor_markup:,.0f}/month</strong>—is pure profit for your processor.
            <br><br>
            <strong style="color: {DEEP_NAVY};">The Fix:</strong> Horizon uses "Interchange Plus" pricing.
            We pass through the Visa/MC cost and add a small, transparent markup.
            <strong style="color: {SUCCESS_GREEN};">You keep ${horizon_savings:,.0f} more every month.</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# TAB 2: PRIORITY HANDOFF (THE CLOSE)
# =============================================================================

with tab2:

    if st.session_state.form_submitted:
        # Show success state
        st.markdown("""
        <div class="success-card">
            <h3>Priority Request Sent!</h3>
            <p>Your National Sales Manager has been notified and will prepare a formal quote within 24 hours.</p>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()

        # Reset button
        if st.button("Submit Another Lead"):
            st.session_state.form_submitted = False
            st.rerun()

    else:
        st.markdown('<span class="priority-badge">Lock In These Rates</span>', unsafe_allow_html=True)

        st.markdown("""
        <p style="color: #666; font-size: 0.9rem; margin-bottom: 1.5rem;">
        Complete the form below to secure priority underwriting review.
        </p>
        """, unsafe_allow_html=True)

        # Form fields - using columns for proper mobile layout
        col1, col2 = st.columns([1, 1])

        with col1:
            business_name = st.text_input(
                "Business Name",
                placeholder="Joe's Pizza"
            )

        with col2:
            owner_name = st.text_input(
                "Owner Name",
                placeholder="Joe Martinez"
            )

        # Phone field - full width
        phone = st.text_input(
            "Phone Number",
            placeholder="(555) 123-4567"
        )

        st.markdown("<hr>", unsafe_allow_html=True)

        # Statement upload
        st.markdown('<p class="section-label">Statement Upload</p>', unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Scan Merchant Statement",
            type=['png', 'jpg', 'jpeg', 'pdf'],
            help="Take a photo of their processing statement for accurate analysis",
            label_visibility="collapsed"
        )

        if uploaded_file:
            st.success(f"Statement uploaded: {uploaded_file.name}")

        st.markdown("<br>", unsafe_allow_html=True)

        # Submit button
        if st.button("Send to Underwriting", type="primary"):
            if business_name and owner_name and phone:
                st.session_state.form_submitted = True
                st.toast("Priority Request Sent to National Sales Manager!", icon="🎉")
                st.rerun()
            else:
                st.error("Please complete all required fields.")

# =============================================================================
# FOOTER - Subtle branding
# =============================================================================

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 0.5rem; color: #999; font-size: 0.7rem;">
    Horizon Quick-Audit | Built for Horizon Payments
</div>
""", unsafe_allow_html=True)
