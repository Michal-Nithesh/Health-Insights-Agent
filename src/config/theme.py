import streamlit as st
from config.app_config import (
    PRIMARY_COLOR,
    PRIMARY_LIGHT,
    SECONDARY_COLOR,
    ACCENT_COLOR,
    TEXT_MUTED,
    CARD_BG,
    CARD_BORDER,
    FONT_FAMILY,
)


def inject_global_css():
    """Injects the shared design system (fonts, cards, buttons, chat bubbles)."""
    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

            html, body, [class*="css"] {{
                font-family: {FONT_FAMILY};
            }}

            /* Hide the default Streamlit form submission helper text */
            div[data-testid="InputInstructions"] > span:nth-child(1) {{
                visibility: hidden;
            }}

            /* Buttons */
            .stButton > button {{
                border-radius: 10px;
                font-weight: 500;
                transition: all 0.15s ease;
                border: 1px solid {CARD_BORDER};
            }}
            .stButton > button:hover {{
                border-color: {PRIMARY_COLOR};
                color: {PRIMARY_LIGHT};
                transform: translateY(-1px);
            }}
            .stButton > button[kind="primary"] {{
                background: linear-gradient(90deg, {PRIMARY_COLOR}, {ACCENT_COLOR});
                border: none;
            }}

            /* Inputs */
            .stTextInput input, .stNumberInput input, .stTextArea textarea {{
                border-radius: 10px !important;
            }}

            /* Generic card container */
            .hia-card {{
                background: {CARD_BG};
                border: 1px solid {CARD_BORDER};
                border-radius: 14px;
                padding: 1.25rem 1.5rem;
                margin-bottom: 1rem;
            }}

            /* Hero / welcome banner */
            .hia-hero {{
                text-align: center;
                padding: 3rem 1.5rem;
                border-radius: 20px;
                background: linear-gradient(135deg, rgba(37,99,235,0.12), rgba(124,58,237,0.10));
                border: 1px solid {CARD_BORDER};
                margin-bottom: 1.5rem;
            }}
            .hia-hero h1 {{
                font-size: 2.4em;
                margin-bottom: 0.2em;
                background: linear-gradient(90deg, {PRIMARY_LIGHT}, {ACCENT_COLOR});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            .hia-hero p.tagline {{
                color: {TEXT_MUTED};
                font-size: 1.1em;
            }}

            /* Chat bubbles */
            .hia-chat-row {{
                display: flex;
                margin: 0.4rem 0;
            }}
            .hia-chat-row.user {{ justify-content: flex-end; }}
            .hia-chat-row.assistant {{ justify-content: flex-start; }}
            .hia-bubble {{
                max-width: 78%;
                padding: 0.75rem 1rem;
                border-radius: 16px;
                line-height: 1.45;
                white-space: pre-wrap;
            }}
            .hia-bubble.user {{
                background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
                color: white;
                border-bottom-right-radius: 4px;
            }}
            .hia-bubble.assistant {{
                background: {CARD_BG};
                border: 1px solid {CARD_BORDER};
                border-bottom-left-radius: 4px;
            }}

            /* Sidebar polish */
            section[data-testid="stSidebar"] .stButton > button {{
                text-align: left;
                justify-content: flex-start;
            }}

            /* Badge / pill */
            .hia-badge {{
                display: inline-block;
                padding: 0.15rem 0.6rem;
                border-radius: 999px;
                background: {CARD_BG};
                border: 1px solid {CARD_BORDER};
                font-size: 0.8em;
                color: {PRIMARY_LIGHT};
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
