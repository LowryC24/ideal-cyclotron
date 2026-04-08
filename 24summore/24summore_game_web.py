import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import itertools
import random
import textwrap
import time
from pathlib import Path
from typing import List, Dict, Tuple

st.set_page_config(page_title="24 SUM+ MORE", page_icon="🃏", layout="centered")


# ============================================================
# TOP SPONSOR BANNER
# ============================================================
def display_sponsor_banner():
    html = textwrap.dedent("""
    <style>
    .sponsor-wrap {
        width: 100%;
        display: flex;
        justify-content: center;
        margin-top: -8px;
        margin-bottom: 14px;
    }

    .sponsor-box {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: linear-gradient(180deg, #ffffff 0%, #f5f7fb 100%);
        border: 1px solid #d4d9e2;
        border-radius: 14px;
        padding: 10px 16px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    }

    .sponsor-text {
        display: flex;
        flex-direction: column;
        line-height: 1.05;
    }

    .sponsored-by {
        font-size: 12px;
        font-weight: 700;
        color: #6b7280;
        letter-spacing: 0.4px;
        text-transform: uppercase;
    }

    .peregrine-name {
        font-size: 18px;
        font-weight: 900;
        color: #123caa;
        letter-spacing: 0.5px;
    }

    .peregrine-sub {
        font-size: 11px;
        font-weight: 700;
        color: #4b5563;
        letter-spacing: 0.35px;
        text-transform: uppercase;
    }

    .eagle {
        width: 34px;
        height: 34px;
        flex: 0 0 auto;
    }
    </style>

    <div class="sponsor-wrap">
        <div class="sponsor-box">
            <svg class="eagle" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-label="Eagle icon">
                <path fill="#123caa" d="M57 12c-7 1-12 5-15 10l-12 1c-8 1-14 6-18 13l-5 9 10-5c3-2 7-3 11-3h3l-8 10c-4 5-9 9-15 11 8 2 17 1 24-3 7-4 12-10 15-17l4-10 8-1-5-4 5-4-7-2 5-5z"/>
                <circle cx="46" cy="18" r="2.2" fill="#ffffff"/>
            </svg>
            <div class="sponsor-text">
                <div class="sponsored-by">Sponsored by</div>
                <div class="peregrine-name">PEREGRINE CAPITAL</div>
                <div class="peregrine-sub">Energising 24SumMore</div>
            </div>
        </div>
    </div>
    """)
    components.html(html, height=72, scrolling=False)


# ============================================================
# CARD DESIGN
# ============================================================
def display_card_html(nums, level_label: str = "1"):
    html = textwrap.dedent(f"""
    <style>
    .new-card {{
        width: 440px;
        height: 440px;
        margin: 20px auto;
        background: radial-gradient(circle at center, #ffe680 0%, #ffae42 45%, #ff5a1f 100%);
        border: 10px solid transparent;
        background-clip: padding-box;
        border-radius: 28px;
        position: relative;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        overflow: hidden;
    }}

    .new-card::before {{
        content: "";
        position: absolute;
        inset: 0;
        padding: 10px;
        border-radius: 28px;
        background: linear-gradient(135deg, #ff2a00, #ffb000, #00a8ff, #0048ff);
        -webkit-mask:
            linear-gradient(#fff 0 0) content-box,
            linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
                mask-composite: exclude;
        pointer-events: none;
    }}

    .burst {{
        position: absolute;
        inset: 0;
        background:
            radial-gradient(circle at center, rgba(255,255,255,0.55), rgba(255,255,255,0) 40%),
            repeating-conic-gradient(
                from 0deg,
                rgba(255,255,255,0.20) 0deg 6deg,
                rgba(255,255,255,0.00) 6deg 12deg
            );
        opacity: 0.55;
        z-index: 0;
    }}

    .number-circle {{
        width: 136px;
        height: 136px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 84px;
        font-weight: 900;
        color: white;
        -webkit-text-stroke: 4px rgba(0,0,0,0.45);
        text-shadow: 0 4px 6px rgba(0,0,0,0.35);
        box-shadow: 0 8px 18px rgba(0,0,0,0.30);
        position: absolute;
        z-index: 2;
        border: 6px solid rgba(255,255,255,0.9);
    }}

    .tl {{ top: 28px; left: 28px; background: #e74c3c; }}
    .tr {{ top: 28px; right: 28px; background: #1f6fff; }}
    .bl {{ bottom: 52px; left: 28px; background: #2dbb41; }}
    .br {{ bottom: 52px; right: 28px; background: #f39c12; }}

    .center-logo {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 30%, #ff7a3d, #d82f00 65%, #9d1f00 100%);
        border: 8px solid #e8e8e8;
        box-shadow: 0 0 20px rgba(0,0,0,0.35);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 3;
        text-align: center;
    }}

    .logo-24 {{
        font-size: 52px;
        font-weight: 900;
        line-height: 1;
        color: #ffd400;
        text-shadow: 0 3px 0 rgba(0,0,0,0.25);
    }}

    .logo-sum {{
        font-size: 20px;
        font-weight: 900;
        line-height: 1;
        color: #ffea66;
        margin-top: 2px;
    }}

    .logo-more {{
        font-size: 20px;
        font-weight: 900;
        line-height: 1;
        color: white;
        margin-top: 2px;
    }}

    .level-badge {{
        position: absolute;
        bottom: 4px;
        left: 50%;
        transform: translateX(-50%);
        width: 112px;
        min-height: 62px;
        background: linear-gradient(180deg, #123caa 0%, #0b2f87 100%);
        color: white;
        border-radius: 12px 12px 8px 8px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.28);
        z-index: 4;
        border: 3px solid rgba(255,255,255,0.9);
        text-align: center;
        padding: 4px 6px 4px 6px;
        line-height: 1.0;
    }}

    .badge-level {{
        display: block;
        font-size: 18px;
        font-weight: 900;
        letter-spacing: 0.4px;
        margin-bottom: 3px;
    }}

    .badge-small {{
        display: block;
        font-size: 12px;
        font-weight: 900;
        letter-spacing: 0.35px;
        line-height: 1.0;
        opacity: 0.98;
    }}
    </style>

    <div class="new-card">
        <div class="burst"></div>

        <div class="number-circle tl">{nums[0]}</div>
        <div class="number-circle tr">{nums[1]}</div>
        <div class="number-circle bl">{nums[2]}</div>
        <div class="number-circle br">{nums[3]}</div>

        <div class="center-logo">
            <div class="logo-24">24</div>
            <div class="logo-sum">SUM+</div>
            <div class="logo-more">MORE</div>
        </div>

        <div class="level-badge">
            <span class="badge-level">LEVEL {level_label}</span>
            <span class="badge-small">PEREGRINE</span>
            <span class="badge-small">CAPITAL</span>
        </div>
    </div>
    """)
    components.html(html, height=500, scrolling=False)


# ============================================================
# SOLVER HELPERS
# ============================================================
def apply_op(x: int, op: str, y: int) -> int:
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            raise ZeroDivisionError
        if x % y != 0:
            raise ValueError("Fraction not allowed")
        return x // y
    else:
        raise ValueError("Invalid operator")


def canonical_binary(a_expr: str, op: str, b_expr: str) -> str:
    if op in ['+', '*']:
        left, right = sorted([a_expr, b_expr])
        return f"({left} {op} {right})"
    return f"({a_expr} {op} {b_expr})"


def combine(x_val: int, x_expr: str, op: str, y_val: int, y_expr: str) -> Tuple[int, str]:
    val = apply_op(x_val, op, y_val)
    expr = canonical_binary(x_expr, op, y_expr)
    return val, expr


# ============================================================
# SOLVER
# ============================================================
def find_solutions(nums: List[int]) -> List[str]:
    ops = ['+', '-', '*', '/']
    solutions = set()

    for perm in itertools.permutations(nums):
        a, b, c, d = perm
        a_expr, b_expr, c_expr, d_expr = map(str, perm)

        for op1 in ops:
            for op2 in ops:
                for op3 in ops:
                    try:
                        r1_val, r1_expr = combine(a, a_expr, op1, b, b_expr)
                        r2_val, r2_expr = combine(r1_val, r1_expr, op2, c, c_expr)
                        r3_val, r3_expr = combine(r2_val, r2_expr, op3, d, d_expr)
                        if r3_val == 24:
                            solutions.add(f"{r3_expr} = 24")
                    except Exception:
                        pass

                    try:
                        r1_val, r1_expr = combine(b, b_expr, op2, c, c_expr)
                        r2_val, r2_expr = combine(a, a_expr, op1, r1_val, r1_expr)
                        r3_val, r3_expr = combine(r2_val, r2_expr, op3, d, d_expr)
                        if r3_val == 24:
                            solutions.add(f"{r3_expr} = 24")
                    except Exception:
                        pass

                    try:
                        r1_val, r1_expr = combine(b, b_expr, op2, c, c_expr)
                        r2_val, r2_expr = combine(r1_val, r1_expr, op3, d, d_expr)
                        r3_val, r3_expr = combine(a, a_expr, op1, r2_val, r2_expr)
                        if r3_val == 24:
                            solutions.add(f"{r3_expr} = 24")
                    except Exception:
                        pass

                    try:
                        r1_val, r1_expr = combine(c, c_expr, op3, d, d_expr)
                        r2_val, r2_expr = combine(b, b_expr, op2, r1_val, r1_expr)
                        r3_val, r3_expr = combine(a, a_expr, op1, r2_val, r2_expr)
                        if r3_val == 24:
                            solutions.add(f"{r3_expr} = 24")
                    except Exception:
                        pass

                    try:
                        left_val, left_expr = combine(a, a_expr, op1, b, b_expr)
                        right_val, right_expr = combine(c, c_expr, op3, d, d_expr)
                        final_val, final_expr = combine(left_val, left_expr, op2, right_val, right_expr)
                        if final_val == 24:
                            solutions.add(f"{final_expr} = 24")
                    except Exception:
                        pass

    return sorted(solutions)


# ============================================================
# EXCEL LOADING
# ============================================================
def row_has_four_numbers(row: pd.Series) -> bool:
    non_empty = [x for x in row.iloc[0:4] if pd.notna(x) and str(x).strip() != ""]
    return len(non_empty) == 4


def extract_cards(df: pd.DataFrame, start_row: int, end_row: int) -> List[List[int]]:
    """
    Excel rows are 1-based in your description.
    Only rows with 4 filled numeric values in the first 4 columns are counted as cards.
    Empty future rows are ignored.
    """
    cards = []
    raw = df.iloc[start_row - 1:end_row, 0:4]

    for _, row in raw.iterrows():
        if not row_has_four_numbers(row):
            continue
        try:
            nums = [int(float(x)) for x in row.iloc[0:4]]
            cards.append(nums)
        except Exception:
            continue

    return cards


def load_all_levels(excel_file: Path) -> Dict[int, List[List[int]]]:
    df = pd.read_excel(str(excel_file), header=None, engine="openpyxl")

    level1 = extract_cards(df, 3, 78)
    level2 = extract_cards(df, 80, 156)
    level3 = extract_cards(df, 158, 221)

    levels = {
        1: level1[:],
        2: level2[:],
        3: level3[:],
        4: level1[:] + level2[:],
        5: level2[:] + level3[:],
        6: level1[:] + level2[:] + level3[:],
    }

    for level in levels:
        random.shuffle(levels[level])

    return levels


LEVEL_NAMES = {
    1: "1",
    2: "2",
    3: "3",
    4: "1+2",
    5: "2+3",
    6: "1+2+3",
}


# ============================================================
# STATE HELPERS
# ============================================================
def reset_current_level():
    st.session_state.current = 0
    st.session_state.show_solution = False
    st.session_state.score = 0
    st.session_state.start_time = time.time()


def restart_all():
    for key in ["all_cards", "selected_level", "current", "show_solution", "game_exited", "score", "start_time"]:
        if key in st.session_state:
            del st.session_state[key]


def format_elapsed(seconds: float) -> str:
    total = int(seconds)
    mins = total // 60
    secs = total % 60
    return f"{mins:02d}:{secs:02d}"


# ============================================================
# MAIN APP
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
excel_file = BASE_DIR / "24summore.xlsx"

st.title("🃏 24 SUM+ MORE")
display_sponsor_banner()

st.markdown("**Use all 4 numbers exactly once to make 24 using +, -, ×, ÷ and brackets**")
st.markdown("**Fractions are not allowed in any calculation step.**")

if "game_exited" not in st.session_state:
    st.session_state.game_exited = False

if "all_cards" not in st.session_state:
    try:
        st.session_state.all_cards = load_all_levels(excel_file)
        st.session_state.selected_level = 1
        st.session_state.current = 0
        st.session_state.show_solution = False
        st.session_state.score = 0
        st.session_state.start_time = time.time()
    except FileNotFoundError:
        st.error(f"❌ Excel file '{excel_file}' not found!")
        st.stop()
    except PermissionError:
        st.error(
            f"❌ Cannot open '{excel_file}'.\n\n"
            "Please close the Excel file first, and make sure OneDrive is not locking it."
        )
        st.stop()
    except Exception as e:
        st.error(f"❌ Unexpected error while loading Excel file: {e}")
        st.stop()

selected_level = st.selectbox(
    "Choose difficulty level",
    options=[1, 2, 3, 4, 5, 6],
    format_func=lambda x: {
        1: "Level 1",
        2: "Level 2",
        3: "Level 3",
        4: "Level 4 (Level 1 + Level 2)",
        5: "Level 5 (Level 2 + Level 3)",
        6: "Level 6 (Level 1 + Level 2 + Level 3)",
    }[x],
    index=st.session_state.selected_level - 1
)

if selected_level != st.session_state.selected_level:
    st.session_state.selected_level = selected_level
    reset_current_level()
    st.session_state.game_exited = False

# Global action buttons
top_col1, top_col2, top_col3 = st.columns(3)
with top_col1:
    if st.button("🔄 Start from Beginning", use_container_width=True):
        reset_current_level()
        st.session_state.game_exited = False
        random.shuffle(st.session_state.all_cards[selected_level])
        st.rerun()

with top_col2:
    if st.button("🔀 Shuffle Cards", use_container_width=True):
        random.shuffle(st.session_state.all_cards[selected_level])
        reset_current_level()
        st.session_state.game_exited = False
        st.rerun()

with top_col3:
    if st.button("❌ Exit Game", use_container_width=True):
        st.session_state.game_exited = True
        st.rerun()

if st.session_state.game_exited:
    st.info("Game exited. You can choose a level and click **Start from Beginning** whenever you want to play again.")
    st.stop()

cards = st.session_state.all_cards[selected_level]

if not cards:
    st.warning(f"No cards found for Level {selected_level}.")
    st.stop()

# Score + Timer
elapsed = time.time() - st.session_state.start_time
m1, m2 = st.columns(2)
with m1:
    st.metric("Score", st.session_state.score)
with m2:
    st.metric("Time", format_elapsed(elapsed))

if st.session_state.current < len(cards):
    card = cards[st.session_state.current]

    st.subheader(
        f"Level {LEVEL_NAMES[selected_level]} — Card {st.session_state.current + 1} of {len(cards)}"
    )

    display_card_html(card, level_label=LEVEL_NAMES[selected_level])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🆘 I need help – Show solutions", type="primary", use_container_width=True):
            st.session_state.show_solution = True
            st.session_state.score -= 1

    with col2:
        if st.button("✅ I have the solution – Next card", use_container_width=True):
            st.session_state.score += 1
            st.session_state.current += 1
            st.session_state.show_solution = False
            st.rerun()

    if st.session_state.show_solution:
        solutions = find_solutions(card)
        if solutions:
            st.success(f"🎉 Found {len(solutions)} solution(s):")
            for sol in solutions:
                st.code(sol, language=None)
        else:
            st.warning("No valid integer-only solutions found.")

        st.caption("You can now move to the next card when ready.")

else:
    st.balloons()
    st.success(f"🎉 Congratulations! You completed all cards in Level {LEVEL_NAMES[selected_level]}!")

    final_time = format_elapsed(time.time() - st.session_state.start_time)
    st.info(f"Final score: **{st.session_state.score}** | Total time: **{final_time}**")

    end_col1, end_col2 = st.columns(2)
    with end_col1:
        if st.button("Restart This Level", use_container_width=True):
            reset_current_level()
            st.session_state.game_exited = False
            random.shuffle(st.session_state.all_cards[selected_level])
            st.rerun()

    with end_col2:
        if st.button("Restart Everything", use_container_width=True):
            restart_all()
            st.rerun()

st.caption("Cards are loaded from the Excel workbook by level.")