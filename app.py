"""
================================================================================
HORIZON POCKET ANALYST v2.0 - Sales Enablement Tool
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
import plotly.express as px
from streamlit_option_menu import option_menu
from datetime import datetime
import numpy as np

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
GOLD = "#D4AF37"
ORANGE = "#E67E22"

# Custom CSS for mobile-first, app-like experience
st.markdown(f"""
<style>
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}

    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.02); }}
    }}

    @keyframes shimmer {{
        0% {{ background-position: -200% 0; }}
        100% {{ background-position: 200% 0; }}
    }}

    .animate-fade-in {{
        animation: fadeInUp 0.5s ease-out forwards;
    }}

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
        animation: fadeInUp 0.4s ease-out;
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

    /* Award badge */
    .award-badge {{
        background: linear-gradient(135deg, {GOLD} 0%, #B8860B 100%);
        color: #1a1a1a;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
        margin: 0.5rem 0;
        box-shadow: 0 2px 10px rgba(212,175,55,0.4);
        text-transform: uppercase;
        letter-spacing: 0.5px;
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
        animation: fadeInUp 0.5s ease-out;
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

    /* Earnings display - special gold accent */
    .earnings-display {{
        background: linear-gradient(135deg, {GOLD} 0%, #B8860B 100%);
        color: #1a1a1a;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 6px 20px rgba(212,175,55,0.4);
        animation: fadeInUp 0.5s ease-out;
    }}

    .earnings-display .label {{
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .earnings-display .amount {{
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }}

    .earnings-display .subtext {{
        font-size: 0.85rem;
        opacity: 0.85;
    }}

    /* Commission easter egg */
    .commission-box {{
        background: linear-gradient(135deg, {ORANGE} 0%, #D35400 100%);
        color: {CLEAN_WHITE};
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(230,126,34,0.4);
        animation: fadeInUp 0.4s ease-out;
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
        animation: fadeInUp 0.4s ease-out;
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

    /* Insight card */
    .insight-card {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: {CLEAN_WHITE};
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
    }}

    /* Active listening card */
    .listening-card {{
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: {CLEAN_WHITE};
        padding: 1rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 4px 15px rgba(17,153,142,0.3);
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

    /* Progress bar styling */
    .bonus-progress {{
        background: #E0E0E0;
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }}

    .bonus-progress-fill {{
        background: linear-gradient(90deg, {LIGHT_GREEN} 0%, {EMERALD_GREEN} 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
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
        animation: fadeInUp 0.4s ease-out;
    }}

    .about-card-gold {{
        background: {CLEAN_WHITE};
        border-left: 4px solid {GOLD};
        padding: 1.2rem;
        border-radius: 0 12px 12px 0;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        animation: fadeInUp 0.4s ease-out;
    }}

    /* Horizon spotlight */
    .horizon-spotlight {{
        background: linear-gradient(135deg, {NAVY_BLUE} 0%, #004080 100%);
        color: {CLEAN_WHITE};
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,51,102,0.3);
    }}

    /* Skills alignment table */
    .skills-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        margin: 1rem 0;
    }}

    .skills-table th {{
        background: {NAVY_BLUE};
        color: {CLEAN_WHITE};
        padding: 0.8rem;
        text-align: left;
        font-size: 0.85rem;
    }}

    .skills-table th:first-child {{
        border-radius: 10px 0 0 0;
    }}

    .skills-table th:last-child {{
        border-radius: 0 10px 0 0;
    }}

    .skills-table td {{
        padding: 0.8rem;
        border-bottom: 1px solid #E0E0E0;
        font-size: 0.85rem;
    }}

    .skills-table tr:last-child td:first-child {{
        border-radius: 0 0 0 10px;
    }}

    .skills-table tr:last-child td:last-child {{
        border-radius: 0 0 10px 0;
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

    /* Divider */
    hr {{
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, {EMERALD_GREEN}, transparent);
        margin: 1.5rem 0;
    }}

    /* Quote badge */
    .quote-badge {{
        background: {LIGHT_GREEN};
        color: {CLEAN_WHITE};
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }}

    /* Value statement box */
    .value-statement {{
        background: linear-gradient(135deg, {EMERALD_GREEN} 0%, {LIGHT_GREEN} 100%);
        color: {CLEAN_WHITE};
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        margin: 1rem 0;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 6px 20px rgba(46,134,193,0.3);
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

if 'leads' not in st.session_state:
    st.session_state.leads = pd.DataFrame(columns=[
        'timestamp', 'business_name', 'owner_name', 'phone', 'email',
        'monthly_volume', 'current_rate', 'estimated_savings',
        'lead_source', 'quote_requested', 'statement_uploaded'
    ])

if 'quote_count' not in st.session_state:
    st.session_state.quote_count = 0

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
# NAVIGATION - 5 TABS
# =============================================================================

selected = option_menu(
    menu_title=None,
    options=["Calculator", "Earnings", "Objections", "Capture", "About"],
    icons=["calculator-fill", "graph-up-arrow", "shield-check", "person-plus-fill", "award-fill"],
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
        "icon": {"color": EMERALD_GREEN, "font-size": "0.9rem"},
        "nav-link": {
            "font-size": "0.7rem",
            "text-align": "center",
            "margin": "0px",
            "padding": "0.6rem 0.3rem",
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
# TAB 1: CALCULATOR (ENHANCED)
# =============================================================================

if selected == "Calculator":
    st.markdown('<p class="section-header">💰 Savings Calculator</p>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    <em>"Transparent pricing. Real savings."</em> — Show merchants exactly what they could save.
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

    # SAVINGS MODE SELECTOR
    st.markdown("**Savings Estimate Mode**")
    savings_mode = st.radio(
        "Select savings estimate",
        options=["Conservative (30%)", "Typical (40%)", "Optimized (50%)"],
        horizontal=True,
        index=1,
        help="Based on Horizon's track record of 30-50% savings",
        label_visibility="collapsed"
    )

    # Parse savings percentage
    if "30%" in savings_mode:
        savings_percentage = 0.30
    elif "40%" in savings_mode:
        savings_percentage = 0.40
    else:
        savings_percentage = 0.50

    st.markdown("<hr>", unsafe_allow_html=True)

    # CALCULATIONS
    current_monthly_fees = monthly_volume * (current_rate / 100)
    current_annual_fees = current_monthly_fees * 12

    monthly_savings = current_monthly_fees * savings_percentage
    annual_savings = monthly_savings * 12

    horizon_monthly_fees = current_monthly_fees - monthly_savings
    horizon_annual_fees = horizon_monthly_fees * 12

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

    # NSM QUOTE BUTTON
    if st.button("📋 Request NSM Quote", use_container_width=True):
        st.session_state.quote_count += 1
        st.toast("Quote request sent to National Sales Manager!", icon="✅")
        st.success("**Quote Requested!** Your NSM will prepare a detailed proposal.")

    # REP VIEW TOGGLE
    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        rep_view = st.toggle("🔐 Rep View", key="rep_toggle", help="See your commission estimate")

    if rep_view:
        # Commission calculation: 25% of the savings
        upfront_commission = annual_savings * 0.25
        monthly_residual = horizon_monthly_fees * 0.25

        st.markdown(f"""
        <div class="commission-box">
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.9;">
                💼 Upfront Commission (25%)
            </div>
            <div style="font-size: 1.8rem; font-weight: 800; margin: 0.2rem 0;">
                ${upfront_commission:,.0f}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="border: 2px solid {GOLD};">
            <div class="metric-label">Monthly Residual (25%)</div>
            <div class="metric-value" style="color: {GOLD};">${monthly_residual:,.0f}/mo</div>
            <div style="font-size: 0.75rem; color: #888;">Recurring passive income!</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p style="text-align: center; font-size: 0.75rem; color: #888; margin-top: 0.5rem;">
        💡 See the <strong>Earnings</strong> tab for long-term income projections
        </p>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 2: EARNINGS (NEW - RESIDUAL INCOME PROJECTOR)
# =============================================================================

elif selected == "Earnings":
    st.markdown('<p class="section-header">📈 Residual Income Projector</p>', unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    See the power of recurring revenue. Close deals today, earn income for years.
    </p>
    """, unsafe_allow_html=True)

    # Note about draw
    st.markdown(f"""
    <div class="insight-card">
        <strong>💡 Getting Started?</strong><br>
        <span style="font-size: 0.85rem;">$375/week draw available while you build your book of business</span>
    </div>
    """, unsafe_allow_html=True)

    # INPUTS
    deals_per_month = st.slider(
        "Deals Closed Per Month",
        min_value=1,
        max_value=15,
        value=5,
        help="Average number of new merchant accounts per month"
    )

    avg_volume = st.slider(
        "Average Merchant Monthly Volume ($)",
        min_value=10000,
        max_value=150000,
        value=50000,
        step=5000,
        help="Typical monthly processing volume per merchant"
    )

    # Assumptions
    avg_rate = 2.5  # Average rate charged
    avg_savings_pct = 0.35  # 35% average savings
    residual_pct = 0.25  # 25% residual

    # Calculate per-deal residual
    monthly_fees_per_merchant = avg_volume * (avg_rate / 100) * (1 - avg_savings_pct)
    residual_per_merchant = monthly_fees_per_merchant * residual_pct

    st.markdown("<hr>", unsafe_allow_html=True)

    # Projections
    months = np.arange(1, 37)  # 3 years
    cumulative_accounts = months * deals_per_month
    monthly_residual_income = cumulative_accounts * residual_per_merchant

    # Key milestones
    month_6_income = 6 * deals_per_month * residual_per_merchant
    month_12_income = 12 * deals_per_month * residual_per_merchant
    month_24_income = 24 * deals_per_month * residual_per_merchant
    month_36_income = 36 * deals_per_month * residual_per_merchant

    # BIG EARNINGS DISPLAY
    st.markdown(f"""
    <div class="earnings-display">
        <div class="label">Projected Monthly Income (Year 2)</div>
        <div class="amount">${month_24_income:,.0f}/mo</div>
        <div class="subtext">With {deals_per_month * 24} active accounts</div>
    </div>
    """, unsafe_allow_html=True)

    # Milestone cards
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Month 6</div>
            <div class="metric-value" style="color: {EMERALD_GREEN};">${month_6_income:,.0f}/mo</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Year 1</div>
            <div class="metric-value" style="color: {LIGHT_GREEN};">${month_12_income:,.0f}/mo</div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Year 2</div>
            <div class="metric-value" style="color: {GOLD};">${month_24_income:,.0f}/mo</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Year 3</div>
            <div class="metric-value" style="color: {ORANGE};">${month_36_income:,.0f}/mo</div>
        </div>
        """, unsafe_allow_html=True)

    # GROWTH CHART
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=monthly_residual_income,
        mode='lines',
        fill='tozeroy',
        line=dict(color=EMERALD_GREEN, width=3),
        fillcolor='rgba(46,134,193,0.3)',
        name='Monthly Residual'
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Arial", size=12),
        margin=dict(l=20, r=20, t=40, b=40),
        height=280,
        xaxis=dict(
            title="Months",
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            tickvals=[6, 12, 18, 24, 30, 36],
            ticktext=['6mo', '1yr', '18mo', '2yr', '30mo', '3yr']
        ),
        yaxis=dict(
            title="Monthly Income",
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            tickformat='$,.0f'
        ),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # Key insight
    st.markdown(f"""
    <div class="insight-card">
        <strong>🎯 The Insight</strong><br>
        <span style="font-size: 0.9rem;">
        Close just {deals_per_month} deals/month and you'll earn <strong>${month_24_income:,.0f}/month in passive income</strong> by Year 2.
        That's on top of your upfront commissions!
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: center; font-size: 0.75rem; color: #888; margin-top: 1rem;">
    *Projections based on average merchant volume and 25% residual rate. Actual results may vary.
    </p>
    """, unsafe_allow_html=True)

# =============================================================================
# TAB 3: OBJECTIONS (POLISHED)
# =============================================================================

elif selected == "Objections":
    st.markdown('<p class="section-header">🛡️ Objection Handler</p>', unsafe_allow_html=True)

    # ACTIVE LISTENING CARD
    st.markdown(f"""
    <div class="listening-card">
        <strong>👂 Active Listening First</strong>
        <div style="font-size: 0.85rem; margin-top: 0.5rem; line-height: 1.5;">
        ✓ Pause before responding<br>
        ✓ Repeat back what you heard<br>
        ✓ Ask clarifying questions
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    Turn "no" into "let's talk more." Tap any objection for an empathy-first response.
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
        Horizon is built on transparency. A quick comparison costs nothing and takes 5 minutes. If your current deal is truly the best, I'll be the first to shake your hand and say 'stay put.'"
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
        Here's how Horizon is different: <strong>We're built on transparency—no hidden fees, no bait-and-switch.</strong> Everything I show you today is what you get. Period.
        <br><br>
        We've been recognized 4 years in a row as one of Portland's Top 100 Fastest-Growing companies—that doesn't happen by burning customers. Let's start small—<strong>a free analysis with zero obligation.</strong> If anything feels off, you tell me to walk, and I will. Fair?"
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
        What I <em>can</em> promise is this: <strong>Horizon typically saves businesses 30-50% on their total processing costs.</strong> Let me prove it with your real numbers instead of throwing out a rate that doesn't mean anything."
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Redirect from 'rate' to 'total cost.' This is where you demonstrate expertise.")

    # Objection 7: Need to Talk to Partner (NEW)
    with st.expander("👥 \"I need to talk to my partner/spouse...\""):
        st.markdown("""
        <span class="objection-badge">DECISION-MAKER OBJECTION</span>

        <div class="script-text">
        "That makes total sense—important business decisions should include all the stakeholders.
        <br><br>
        Here's what I can do: let me put together <strong>a clear, one-page comparison</strong> that you can show them tonight. Numbers speak louder than words, right?
        <br><br>
        Quick question—<strong>if the savings look as good as I think they will, what would your partner need to see to feel confident?</strong>
        <br><br>
        <em>[Listen, then tailor your follow-up accordingly]</em>
        <br><br>
        I'll send you the comparison, and let's set up a quick 10-minute call for tomorrow. That way I can answer any questions you both might have. Sound good?"
        </div>
        """, unsafe_allow_html=True)

        st.info("💡 **Pro Tip:** Provide ammunition for their conversation. Make it easy for them to sell it internally.")

# =============================================================================
# TAB 4: LEAD CAPTURE (ENHANCED)
# =============================================================================

elif selected == "Capture":
    st.markdown('<p class="section-header">📋 Lead Capture</p>', unsafe_allow_html=True)

    # FIRST 30 DAYS BONUS TRACKER
    if st.session_state.quote_count > 0:
        bonus_earned = st.session_state.quote_count * 100
        progress_pct = min(st.session_state.quote_count / 20 * 100, 100)  # Cap at 20 quotes

        st.markdown(f"""
        <div class="metric-card" style="border: 2px solid {GOLD};">
            <div class="metric-label">🎯 First 30 Days Bonus</div>
            <div class="metric-value" style="color: {GOLD};">${bonus_earned}</div>
            <div style="font-size: 0.8rem; color: #666;">{st.session_state.quote_count} quotes × $100 each</div>
            <div class="bonus-progress" style="margin-top: 0.5rem;">
                <div class="bonus-progress-fill" style="width: {progress_pct}%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
    Capture deal details before you leave. Every lead logged is a step closer to closing.
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

        # Contact Info
        col1, col2 = st.columns(2)
        with col1:
            phone = st.text_input(
                "Phone",
                placeholder="(555) 123-4567"
            )
        with col2:
            email = st.text_input(
                "Email",
                placeholder="joe@pizzapalace.com"
            )

        # Volume & Rate
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

        # Lead Source
        lead_source = st.selectbox(
            "Lead Source",
            options=["Scheduled Appointment", "Walk-in/Door Knock", "Referral", "Follow-up", "Other"]
        )

        # Quote Requested Toggle
        quote_requested = st.checkbox("📋 Quote Requested", help="Check if merchant wants a formal quote")

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
            "📤 Submit to NSM",
            use_container_width=True
        )

        if submitted:
            if not business_name or not owner_name:
                st.error("Please fill in Business Name and Owner Name.")
            else:
                # Calculate estimated savings for the lead
                estimated_savings = (lead_volume * (lead_rate/100) * 0.35) * 12

                # Update quote count if quote requested
                if quote_requested:
                    st.session_state.quote_count += 1

                # Create new lead entry
                new_lead = pd.DataFrame([{
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'business_name': business_name,
                    'owner_name': owner_name,
                    'phone': phone,
                    'email': email,
                    'monthly_volume': lead_volume,
                    'current_rate': lead_rate,
                    'estimated_savings': estimated_savings,
                    'lead_source': lead_source,
                    'quote_requested': 'Yes' if quote_requested else 'No',
                    'statement_uploaded': 'Yes' if uploaded_file else 'No'
                }])

                # Add to session state
                st.session_state.leads = pd.concat(
                    [st.session_state.leads, new_lead],
                    ignore_index=True
                )

                # Success notification
                st.toast("Lead captured successfully!", icon="✅")
                st.success("**Success!** Lead sent to your National Sales Manager for quote preparation.")
                st.balloons()

    # Show captured leads summary
    if len(st.session_state.leads) > 0:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<p class="section-header">📊 Today\'s Pipeline</p>', unsafe_allow_html=True)

        total_pipeline = st.session_state.leads['estimated_savings'].sum()
        quotes_count = len(st.session_state.leads[st.session_state.leads['quote_requested'] == 'Yes'])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Pipeline Value</div>
                <div class="metric-value" style="color: {LIGHT_GREEN};">${total_pipeline:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Leads / Quotes</div>
                <div class="metric-value" style="color: {NAVY_BLUE};">{len(st.session_state.leads)} / {quotes_count}</div>
            </div>
            """, unsafe_allow_html=True)

        # Display leads as cards
        for idx, lead in st.session_state.leads.iterrows():
            quote_badge = f'<span class="quote-badge">QUOTE</span>' if lead['quote_requested'] == 'Yes' else ''
            st.markdown(f"""
            <div class="about-card">
                <strong style="color: {NAVY_BLUE};">{lead['business_name']}</strong> {quote_badge}<br>
                <span style="color: #666; font-size: 0.85rem;">
                👤 {lead['owner_name']} | 💰 ${lead['monthly_volume']:,}/mo |
                📈 ${lead['estimated_savings']:,.0f} potential savings
                </span>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# TAB 5: ABOUT (COMPLETE OVERHAUL)
# =============================================================================

elif selected == "About":
    # HORIZON SPOTLIGHT
    st.markdown(f"""
    <div class="horizon-spotlight">
        <div class="award-badge">🏆 4× Portland Business Journal Top 100</div>
        <h3 style="margin: 1rem 0 0.5rem 0; font-size: 1.3rem;">Horizon Payments</h3>
        <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">
        "Advocating for business owners across the nation"
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Core Values
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem;">
            <div style="font-size: 1.5rem;">🤝</div>
            <div style="font-size: 0.75rem; color: {NAVY_BLUE}; font-weight: 600;">Transparency</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem;">
            <div style="font-size: 1.5rem;">🎯</div>
            <div style="font-size: 0.75rem; color: {NAVY_BLUE}; font-weight: 600;">Partnership</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem;">
            <div style="font-size: 1.5rem;">📈</div>
            <div style="font-size: 0.75rem; color: {NAVY_BLUE}; font-weight: 600;">Growth</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # WHY I BUILT THIS
    st.markdown('<p class="section-header">💡 Why I Built This</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="about-card">
        <p style="color: #555; line-height: 1.6; margin: 0;">
        I believe in <strong>showing, not telling.</strong>
        <br><br>
        Instead of just talking about my skills in an interview, I built a production-ready tool that solves a real problem: <strong>field reps need mobile-first technology</strong> to close deals faster.
        <br><br>
        This app demonstrates how I approach challenges—understand the need, design the solution, deliver value.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # SKILLS → ROLE ALIGNMENT
    st.markdown('<p class="section-header">🎯 Skills → Role Alignment</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <table class="skills-table">
        <tr>
            <th>You're Looking For</th>
            <th>This Tool Proves It</th>
        </tr>
        <tr>
            <td><strong>Communication</strong></td>
            <td>Clear, intuitive UX design</td>
        </tr>
        <tr>
            <td><strong>Active Listening</strong></td>
            <td>Empathy-first objection scripts</td>
        </tr>
        <tr>
            <td><strong>Confidence</strong></td>
            <td>Built this before the interview</td>
        </tr>
        <tr>
            <td><strong>Independence</strong></td>
            <td>Self-directed, production-ready</td>
        </tr>
        <tr>
            <td><strong>Adaptability</strong></td>
            <td>Mobile-first for field flexibility</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # VALUE STATEMENT
    st.markdown(f"""
    <div class="value-statement">
        "I don't just apply for jobs—I solve problems."
    </div>
    """, unsafe_allow_html=True)

    # TECHNICAL SKILLS
    st.markdown(f"""
    <div class="about-card-gold">
        <h4 style="color: {NAVY_BLUE}; margin-top: 0;">🛠️ Technical Edge</h4>
        <p style="color: #555; line-height: 1.6; margin: 0;">
        • <strong>Python & Streamlit:</strong> Full-stack app development<br>
        • <strong>Data Visualization:</strong> Interactive Plotly charts<br>
        • <strong>UX/UI Design:</strong> Mobile-first, brand-aligned interface<br>
        • <strong>Cloud Deployment:</strong> Production-ready on Streamlit Cloud
        </p>
    </div>
    """, unsafe_allow_html=True)

    # CLOSING STATEMENT
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align: center; padding: 1rem;">
        <p style="color: {NAVY_BLUE}; font-weight: 600; font-size: 1.1rem; margin-bottom: 0.5rem;">
        Ready to advocate for business owners—together.
        </p>
        <p style="color: #888; font-size: 0.85rem; margin: 0;">
        Built by <strong>Manav Davis</strong> for Horizon Payments
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 0.5rem; color: #999; font-size: 0.75rem;">
    Horizon Pocket Analyst v2.0 | Built with 💙 for Horizon Payments
</div>
""", unsafe_allow_html=True)
