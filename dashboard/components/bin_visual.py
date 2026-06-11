# pyrefly: ignore [missing-import]
import streamlit as st


def show_bin(fill_percentage):

    filled_rows = int(fill_percentage / 10)

    rows = []

    for i in range(10):

        if i < filled_rows:
            rows.append("│█████████│")
        else:
            rows.append("│         │")

    rows.reverse()

    bin_visual = "\n".join(rows)

    st.code(
        f"""
┌─────────┐
{bin_visual}
└─────────┘

{fill_percentage:.1f}% Full
"""
    )
