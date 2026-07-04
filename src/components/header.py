import streamlit as st
from config.app_config import APP_ICON, APP_NAME, PRIMARY_LIGHT, CARD_BG, CARD_BORDER


def show_header():
    if not st.session_state.get("user"):
        return

    display_name = st.session_state.user.get("name") or st.session_state.user.get(
        "email", ""
    )
    initial = display_name[:1].upper() if display_name else "?"

    st.markdown(
        f"""
        <div style='
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0.25rem;
            margin-bottom: 0.5rem;
        '>
            <div style='display: flex; align-items: center; gap: 0.5rem;'>
                <span style='font-size: 1.4em;'>{APP_ICON}</span>
                <span style='font-weight: 600; font-size: 1.1em;'>{APP_NAME}</span>
            </div>
            <div style='
                display: flex;
                align-items: center;
                gap: 0.6rem;
                background: {CARD_BG};
                border: 1px solid {CARD_BORDER};
                border-radius: 999px;
                padding: 0.35rem 0.9rem 0.35rem 0.35rem;
            '>
                <span style='
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 1.8em;
                    height: 1.8em;
                    border-radius: 50%;
                    background: {PRIMARY_LIGHT};
                    color: #0F172A;
                    font-weight: 700;
                    font-size: 0.9em;
                '>{initial}</span>
                <span style='color: {PRIMARY_LIGHT}; font-size: 0.95em;'>{display_name}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
