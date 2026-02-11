"""
================================================================================
HORIZON POCKET ANALYST - Sales Enablement Tool
================================================================================

iOS "Add to Home Screen" Instructions:
--------------------------------------
1. Open this app in Safari on your iPhone
2. Tap the Share button (square with arrow pointing up)
3. Scroll down and tap "Add to Home Screen"
4. Name it "Horizon Analyst" and tap "Add"
5. The app will now launch full-screen without the browser address bar!

Built by: Manav Davis
Purpose: Demonstrating sales-focused technical solutions for Horizon Payments
================================================================================
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime
import base64

# =============================================================================
# PAGE CONFIGURATION & CUSTOM CSS
# =============================================================================

st.set_page_config(
    page_title="Horizon Pocket Analyst",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Horizon Brand Colors
NAVY_BLUE = "#003366"
EMERALD_GREEN = "#2E86C1"
LIGHT_GREEN = "#28B463"
CLEAN_WHITE = "#FFFFFF"
LIGHT_GRAY = "#F8F9FA"

# Custom CSS for mobile-first, app-like experience
st.markdown(f"""
<style>
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    /* Mobile-first responsive design */
    .main .block-container {{
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
    }}

    /* Custom header styling */
    .horizon-header {{
        background: linear-gradient(135deg, {NAVY_BLUE} 0%, #004080 100%);
        color: {CLEAN_WHITE};
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(0,51,102,0.3);
    }}

    .horizon-header h1 {{
        margin: 0;
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }}

    .horizon-header p {{
        margin: 0.3rem 0 0 0;
        font-size: 0.85rem;
        opacity: 0.9;
    }}

    /* Big savings display */
    .savings-display {{
        background: linear-gradient(135deg, {EMERALD_GREEN} 0%, {LIGHT_GREEN} 100%);
        color: {CLEAN_WHITE};
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 6px 20px rgba(46,134,193,0.4);
    }}

    .savings-display .label {{
        font-size: 1rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.95;
    }}

    .savings-display .amount {{
        font-size: 3rem;
        font-weight: 800;
        margin: 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }}

    .savings-display .subtext {{
        font-size: 0.9rem;
        opacity: 0.9;
    }}

    /* Commission easter egg */
    .commission-box {{
        background: linear-gradient(135deg, #F39C12 0%, #E67E22 100%);
        color: {CLEAN_WHITE};
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(243,156,18,0.4);
    }}

    /* Metric cards */
    .metric-card {{
        background: {CLEAN_WHITE};
        border: 2px solid {LIGHT_GRAY};
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin: 0.5rem 0;
    }}

    .metric-card .metric-label {{
        font-size: 0.8rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}

    .metric-card .metric-value {{
        font-size: 1.5rem;
        font-weight: 700;
        color: {NAVY_BLUE};
        margin: 0.3rem 0;
    }}

    /* Touch-friendly buttons */
    .stButton > button {{
        width: 100%;
        padding: 0.8rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        background: linear-gradient(135deg, {NAVY_BLUE} 0%, #004080 100%);
        color: {CLEAN_WHITE};
        box-shadow: 0 4px 12px rgba(0,51,102,0.3);
        transition: all 0.3s ease;
        min-height: 50px;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,51,102,0.4);
    }}

    .stButton > button:active {{
        transform: translateY(0);
    }}

    /* Success button variant */
    .success-btn > button {{
        background: linear-gradient(135deg, {LIGHT_GREEN} 0%, #1E8449 100%) !important;
    }}

    /* Accordion styling */
    .streamlit-expanderHeader {{
        background: {LIGHT_GRAY};
        border-radius: 10px;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.8rem !important;
    }}

    .streamlit-expanderContent {{
        background: {CLEAN_WHITE};
        border-radius: 0 0 10px 10px;
        padding: 1rem;
    }}

    /* Form styling */
    .stTextInput > div > div > input {{
        border-radius: 10px;
        border: 2px solid #E0E0E0;
        padding: 0.8rem;
        font-size: 1rem;
    }}

    .stTextInput > div > div > input:focus {{
        border-color: {EMERALD_GREEN};
        box-shadow: 0 0 0 2px rgba(46,134,193,0.2);
    }}

    /* Navigation menu */
    .nav-link {{
        font-size: 0.85rem !important;
        padding: 0.6rem 0.8rem !important;
    }}

    /* Section headers */
    .section-header {{
        color: {NAVY_BLUE};
        font-size: 1.2rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid {EMERALD_GREEN};
    }}

    /* About page styling */
    .about-card {{
        background: {CLEAN_WHITE};
        border-left: 4px solid {EMERALD_GREEN};
        padding: 1.2rem;
        border-radius: 0 12px 12px 0;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}

    /* Objection badge */
    .objection-badge {{
        background: {NAVY_BLUE};
        color: {CLEAN_WHITE};
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.5rem;
    }}

    /* Script text styling */
    .script-text {{
        background: #F0F7FF;
        border-radius: 8px;
        padding: 1rem;
        font-style: italic;
        color: #333;
        line-height: 1.6;
    }}

    /* Toggle switch label */
    .toggle-label {{
        color: {NAVY_BLUE};
        font-weight: 600;
        font-size: 0.9rem;
    }}

    /* Divider */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, {EMERALD_GREEN}, transparent);
        margin: 1.5rem 0;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

if 'leads' not in st.session_state:
    st.session_state.leads = pd.DataFrame(columns=[
        'timestamp', 'business_name', 'owner_name', 'monthly_volume',
        'current_rate', 'estimated_savings', 'statement_uploaded'
    ])

if 'show_commission' not in st.session_state:
    st.session_state.show_commission = False

# =============================================================================
# HEADER
# =============================================================================

st.markdown("""
<div class="horizon-header">
    <h1>💳 Horizon Pocket Analyst</h1>
    <p>Your Mobile Sales Command Center</p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# NAVIGATION
# =============================================================================

selected = option_menu(
    menu_title=None,
    options=["Calculator", "Objections", "Capture", "About"],
    icons=["calculator-fill", "shield-check", "person-plus-fill", "info-circle-fill"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {
            "padding": "0!important",
            "background-color": LIGHT_GRAY,
            "border-radius": "12px",
            "margin-bottom": "1rem"
        },
        "icon": {"color": EMERALD_GREEN, "font-size": "1rem"},
        "nav-link": {
            "font-size": "0.8rem",
            "text-align": "center",
            "margin": "0px",
            "padding": "0.7rem 0.5rem",
            "--hover-color": "#E8F4FD",
            "border-radius": "10px",
            "font-weight": "600"
        },
        "nav-link-selected": {
            "background": f"linear-gradient(135deg, {NAVY_BLUE} 0%, #004080 100%)",
            "color": CLEAN_WHITE,
            "font-weight": "700"
        },
    }
)

# =============================================================================
# TAB 1: THE HOOK (SAVINGS CALCULATOR)
# =============================================================================

if selected == "Calculator":
    st.markdown('<p class="section-header">💰 Savings Calculator</p>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    Show merchants exactly how much they could save by switching to Horizon Payments.
    </p>
    """, unsafe_allow_html=True)

    # Monthly Volume Input
    monthly_volume = st.number_input(
        "Monthly Credit Card Volume ($)",
        min_value=1000,
        max_value=10000000,
        value=50000,
        step=5000,
        format="%d",
        help="Enter the merchant's average monthly credit card processing volume"
    )

    # Current Rate Input
    current_rate = st.slider(
        "Current Processing Rate (%)",
        min_value=1.5,
        max_value=5.0,
        value=3.0,
        step=0.1,
        help="Their current effective rate (total fees ÷ volume)"
    )

    st.markdown("<hr>", unsafe_allow_html=True)

    # CALCULATIONS
    current_monthly_fees = monthly_volume * (current_rate / 100)
    current_annual_fees = current_monthly_fees * 12

    # Conservative 30% reduction
    savings_percentage = 0.30
    monthly_savings = current_monthly_fees * savings_percentage
    annual_savings = monthly_savings * 12

    horizon_monthly_fees = current_monthly_fees - monthly_savings
    horizon_annual_fees = horizon_monthly_fees * 12
    horizon_rate = current_rate * (1 - savings_percentage)

    # Metric Cards Row
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Current Monthly Fees</div>
            <div class="metric-value" style="color: #C0392B;">${current_monthly_fees:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Horizon Monthly Fees</div>
            <div class="metric-value" style="color: {LIGHT_GREEN};">${horizon_monthly_fees:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    # BIG SAVINGS DISPLAY
    st.markdown(f"""
    <div class="savings-display">
        <div class="label">Estimated Annual Savings</div>
        <div class="amount">${annual_savings:,.0f}</div>
        <div class="subtext">That's ${monthly_savings:,.0f}/month back in your pocket!</div>
    </div>
    """, unsafe_allow_html=True)

    # PLOTLY CHART
    fig = go.Figure()

    fig.add_trace(go.Bar(
        name='Current Provider',
        x=['Annual Fees'],
        y=[current_annual_fees],
        marker_color='#C0392B',
        text=[f'${current_annual_fees:,.0f}'],
        textposition='outside',
        textfont=dict(size=14, color='#C0392B', family='Arial Black')
    ))

    fig.add_trace(go.Bar(
        name='Horizon Payments',
        x=['Annual Fees'],
        y=[horizon_annual_fees],
        marker_color=LIGHT_GREEN,
        text=[f'${horizon_annual_fees:,.0f}'],
        textposition='outside',
        textfont=dict(size=14, color=LIGHT_GREEN, family='Arial Black')
    ))

    fig.update_layout(
        barmode='group',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Arial", size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=11)
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        height=280,
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            tickformat='$,.0f'
        ),
        xaxis=dict(showticklabels=False)
    )

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # EASTER EGG - Rep View Toggle
    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        rep_view = st.toggle("🔐 Rep View", key="rep_toggle", help="See your commission estimate")

    if rep_view:
        # Commission calculation: 25% of the savings
        estimated_commission = annual_savings * 0.25
        monthly_commission = estimated_commission / 12

        st.markdown(f"""
        <div class="commission-box">
            <div style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;">
                💼 Your Estimated Commission
            </div>
            <div style="font-size: 2rem; font-weight: 800; margin: 0.3rem 0;">
                ${estimated_commission:,.0f}/year
            </div>
            <div style="font-size: 0.85rem; opacity: 0.9;">
                (~${monthly_commission:,.0f}/month residual)
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="text-align: center; font-size: 0.75rem; color: #888; margin-top: 0.5rem;">
        *Based on 25% of merchant savings. Actual commission may vary.
        </p>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 2: THE SHIELD (OBJECTION HANDLING)
# =============================================================================

elif selected == "Objections":
    st.markdown('<p class="section-header">🛡️ Objection Handler</p>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    Turn "no" into "let's talk more." Tap any objection for an empathy-first response script.
    </p>
    """, unsafe_allow_html=True)

    # Objection 1: Too Busy
    with st.expander("⏰ \"I'm too busy right now...\""):
        st.markdown("""
        <span class="objection-badge">TIME OBJECTION</span>

        <div class="script-text">
        "I completely understand—running a business is non-stop. That's exactly why I'm here.
        <br><br>
        What if I told you I could <strong>save you 2-3 hours of headaches every month</strong> on top of putting money back in your pocket?
        <br><br>
        Let me take a quick photo of your statement. I'll do all the analysis on my end, and if there's nothing to save, you'll never hear from me again. <strong>30 seconds now could mean thousands back this year.</strong> Fair?"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Pull out your phone immediately. The photo offer makes it tangible and low-commitment.")

    # Objection 2: Contract Fears
    with st.expander("📝 \"I'm locked in a contract...\""):
        st.markdown("""
        <span class="objection-badge">CONTRACT OBJECTION</span>

        <div class="script-text">
        "Ah, I hear that a lot. Here's the good news—<strong>most contracts aren't as locked as they seem.</strong>
        <br><br>
        Nine times out of ten, when I look at the fine print with merchants, we find either a reasonable exit clause or the savings are so significant that any cancellation fee pays for itself in 2-3 months.
        <br><br>
        Let me take a look at your statement and contract. <strong>The worst case? You get a free analysis. The best case? You start saving immediately.</strong> What do you have to lose?"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Offer to personally review their contract. Shows expertise and builds trust.")

    # Objection 3: Happy with Current Provider
    with st.expander("😊 \"I'm happy with my current processor...\""):
        st.markdown("""
        <span class="objection-badge">LOYALTY OBJECTION</span>

        <div class="script-text">
        "That's great to hear—loyalty is a valuable trait in business. I respect that.
        <br><br>
        But let me ask you this: <strong>when was the last time your processor proactively reached out to lower your rates?</strong>
        <br><br>
        The industry changes constantly, and most processors count on business owners being 'happy enough' not to look around. I'm not here to bash anyone—<strong>I'm here to make sure you're getting what you deserve.</strong>
        <br><br>
        A quick comparison costs nothing and takes 5 minutes. If your current deal is truly the best, I'll be the first to shake your hand and say 'stay put.'"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** The 'when did they lower your rates' question plants a powerful seed of doubt.")

    # Objection 4: Need to Think About It
    with st.expander("🤔 \"Let me think about it...\""):
        st.markdown("""
        <span class="objection-badge">STALL OBJECTION</span>

        <div class="script-text">
        "Absolutely, this is a business decision and I want you to feel 100% confident.
        <br><br>
        Just so I can help you think it through—<strong>what's the main thing you'd want to consider?</strong> Is it the timing, the transition process, or something else?
        <br><br>
        <em>[Listen carefully, then address their specific concern]</em>
        <br><br>
        Here's my commitment: I'll leave you with my direct line. But while we're together, let me at least capture your current statement so I can send you a detailed comparison. <strong>That way you'll have real numbers to think about, not guesses.</strong>"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** 'Think about it' usually means there's a hidden objection. Dig deeper with curiosity, not pressure.")

    # Objection 5: Bad Past Experience
    with st.expander("😤 \"I've been burned before...\""):
        st.markdown("""
        <span class="objection-badge">TRUST OBJECTION</span>

        <div class="script-text">
        "I'm really sorry to hear that. Unfortunately, our industry has some bad actors, and it makes my job harder—but more important.
        <br><br>
        Can I ask what happened? <em>[Listen with genuine empathy]</em>
        <br><br>
        Here's how Horizon is different: <strong>We don't do hidden fees. We don't do bait-and-switch.</strong> Everything I show you today is what you get. Period.
        <br><br>
        I know trust is earned, not given. So let's start small—<strong>let me do a free analysis with zero obligation.</strong> If anything feels off at any point, you tell me to walk, and I will. Fair?"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Validate their pain first. Don't defend the industry—differentiate yourself from it.")

    # Objection 6: Price/Rate Focused
    with st.expander("💵 \"Just give me your rate...\""):
        st.markdown("""
        <span class="objection-badge">PRICE OBJECTION</span>

        <div class="script-text">
        "I wish I could give you one number, but here's the truth—<strong>anyone who quotes a single rate without seeing your statement is either lying or guessing.</strong>
        <br><br>
        Your effective rate depends on your card mix, ticket size, and how transactions are processed. That's why I need to see the actual data.
        <br><br>
        What I <em>can</em> promise is this: <strong>We typically save businesses 20-30% on their total processing costs.</strong> Let me prove it with your real numbers instead of throwing out a rate that doesn't mean anything."
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Redirect from 'rate' to 'total cost.' This is where you demonstrate expertise.")

# =============================================================================
# TAB 3: THE CLOSE (LEAD CAPTURE)
# =============================================================================

elif selected == "Capture":
    st.markdown('<p class="section-header">📋 Lead Capture</p>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    Capture the deal details before you leave. Every lead logged is a step closer to closing.
    </p>
    """, unsafe_allow_html=True)

    with st.form("lead_capture_form", clear_on_submit=True):
        # Business Info
        business_name = st.text_input(
            "Business Name *",
            placeholder="e.g., Joe's Pizza Palace"
        )

        owner_name = st.text_input(
            "Owner/Contact Name *",
            placeholder="e.g., Joe Martinez"
        )

        # Volume & Rate (pre-populated if they used calculator)
        col1, col2 = st.columns(2)
        with col1:
            lead_volume = st.number_input(
                "Monthly Volume ($)",
                min_value=0,
                max_value=10000000,
                value=50000,
                step=5000
            )
        with col2:
            lead_rate = st.number_input(
                "Current Rate (%)",
                min_value=0.0,
                max_value=10.0,
                value=3.0,
                step=0.1
            )

        # Statement Photo Upload
        st.markdown("**📸 Statement Photo**")
        uploaded_file = st.file_uploader(
            "Upload merchant statement photo",
            type=['png', 'jpg', 'jpeg', 'pdf'],
            help="Take a photo of their processing statement for analysis"
        )

        # Notes
        notes = st.text_area(
            "Quick Notes",
            placeholder="Any important details about the conversation...",
            height=80
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Submit Button
        submitted = st.form_submit_button(
            "📤 Submit Lead",
            use_container_width=True
        )

        if submitted:
            if not business_name or not owner_name:
                st.error("Please fill in Business Name and Owner Name.")
            else:
                # Calculate estimated savings for the lead
                estimated_savings = (lead_volume * (lead_rate/100) * 0.30) * 12

                # Create new lead entry
                new_lead = pd.DataFrame([{
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'business_name': business_name,
                    'owner_name': owner_name,
                    'monthly_volume': lead_volume,
                    'current_rate': lead_rate,
                    'estimated_savings': estimated_savings,
                    'statement_uploaded': 'Yes' if uploaded_file else 'No'
                }])

                # Add to session state
                st.session_state.leads = pd.concat(
                    [st.session_state.leads, new_lead],
                    ignore_index=True
                )

                # Success notification
                st.toast("✅ Lead captured successfully!", icon="🎉")
                st.success("**Success!** Lead sent to National Sales Manager.")
                st.balloons()

    # Show captured leads summary
    if len(st.session_state.leads) > 0:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<p class="section-header">📊 Today\'s Captured Leads</p>', unsafe_allow_html=True)

        total_pipeline = st.session_state.leads['estimated_savings'].sum()

        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Pipeline Value</div>
            <div class="metric-value" style="color: {LIGHT_GREEN};">${total_pipeline:,.0f}</div>
            <div style="font-size: 0.8rem; color: #666;">{len(st.session_state.leads)} leads captured</div>
        </div>
        """, unsafe_allow_html=True)

        # Display leads as cards (mobile-friendly)
        for idx, lead in st.session_state.leads.iterrows():
            st.markdown(f"""
            <div class="about-card">
                <strong style="color: {NAVY_BLUE};">{lead['business_name']}</strong><br>
                <span style="color: #666; font-size: 0.85rem;">
                👤 {lead['owner_name']} | 💰 ${lead['monthly_volume']:,}/mo |
                📈 ${lead['estimated_savings']:,.0f} potential savings
                </span>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# TAB 4: ABOUT (THE "WHY HIRE ME" PAGE)
# =============================================================================

elif selected == "About":
    st.markdown('<p class="section-header">👋 About This Tool</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-card">
        <h4 style="color: {NAVY_BLUE}; margin-top: 0;">Built for Horizon Payments</h4>
        <p style="color: #555; line-height: 1.6; margin-bottom: 0;">
        This <strong>Horizon Pocket Analyst</strong> was designed and developed by
        <strong>Manav Davis</strong> specifically for the Business Solutions Consultant role
        at Horizon Payments.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-card">
        <h4 style="color: {NAVY_BLUE}; margin-top: 0;">💡 Why I Built This</h4>
        <p style="color: #555; line-height: 1.6;">
        I believe in <strong>showing, not telling.</strong> Instead of just talking about
        my skills in an interview, I wanted to demonstrate exactly how I approach problems:
        </p>
        <ul style="color: #555; line-height: 1.8;">
            <li><strong>Identify the need:</strong> Field reps need mobile-friendly tools</li>
            <li><strong>Design the solution:</strong> Clean, fast, touch-optimized interface</li>
            <li><strong>Deliver value:</strong> Real calculations, real objection handlers, real lead capture</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-card">
        <h4 style="color: {NAVY_BLUE}; margin-top: 0;">🛠️ Technical Skills Demonstrated</h4>
        <ul style="color: #555; line-height: 1.8; margin-bottom: 0;">
            <li><strong>Python & Streamlit:</strong> Full-stack web application development</li>
            <li><strong>Data Visualization:</strong> Interactive Plotly charts</li>
            <li><strong>UX/UI Design:</strong> Mobile-first, brand-aligned interface</li>
            <li><strong>Sales Acumen:</strong> Objection handling scripts & value propositions</li>
            <li><strong>Cloud Deployment:</strong> Production-ready for Streamlit Cloud</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-card">
        <h4 style="color: {NAVY_BLUE}; margin-top: 0;">🎯 My Approach to Sales</h4>
        <p style="color: #555; line-height: 1.6; margin-bottom: 0;">
        I believe modern sales is about <strong>education over persuasion</strong> and
        <strong>value over volume.</strong> This tool embodies that philosophy—it helps
        merchants see their own savings, not just hear a pitch.
        <br><br>
        <em>"The best salespeople don't convince. They clarify."</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Contact / CTA
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem;">
        <p style="color: {NAVY_BLUE}; font-weight: 600; font-size: 1.1rem;">
        Ready to discuss how I can bring this energy to Horizon?
        </p>
        <p style="color: #666; font-size: 0.9rem;">
        Let's connect and make great things happen.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 0.5rem; color: #999; font-size: 0.75rem;">
    Horizon Pocket Analyst v1.0 | Built with 💙 for Horizon Payments
</div>
""", unsafe_allow_html=True)
