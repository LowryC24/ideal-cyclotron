import streamlit as st
import streamlit.components.v1 as components
import itertools
import random
import textwrap
import time
from typing import List, Tuple

st.set_page_config(page_title="SNAP 18", page_icon="🃏", layout="centered")

TARGET = 18

# ============================================================
# CARDS — 30 per level, generated for target 18.
# Numbers are single digits 1-9; each is used exactly once with
# +, -, x, / (no fractions at any step). Solution counts follow
# the canonical-expression counting of the original 24 solver.
# ============================================================
LEVEL1_CARDS = [   # more than 27 solutions each
    [1, 3, 6, 9],   # 64 solutions
    [1, 1, 3, 6],   # 52 solutions
    [1, 1, 2, 9],   # 51 solutions
    [1, 4, 6, 9],   # 46 solutions
    [1, 5, 6, 8],   # 43 solutions
    [2, 5, 6, 9],   # 43 solutions
    [1, 1, 9, 9],   # 42 solutions
    [2, 5, 7, 8],   # 40 solutions
    [3, 6, 7, 8],   # 40 solutions
    [3, 6, 9, 9],   # 40 solutions
    [2, 3, 8, 9],   # 37 solutions
    [1, 3, 7, 9],   # 36 solutions
    [1, 4, 6, 8],   # 36 solutions
    [1, 5, 6, 7],   # 36 solutions
    [2, 4, 7, 9],   # 36 solutions
    [4, 5, 8, 9],   # 36 solutions
    [4, 6, 7, 9],   # 36 solutions
    [5, 6, 8, 9],   # 36 solutions
    [2, 3, 3, 9],   # 36 solutions
    [1, 3, 7, 8],   # 35 solutions
    [1, 4, 5, 9],   # 35 solutions
    [3, 5, 7, 9],   # 35 solutions
    [6, 7, 8, 9],   # 35 solutions
    [2, 2, 3, 6],   # 35 solutions
    [2, 6, 6, 9],   # 35 solutions
    [1, 2, 4, 9],   # 33 solutions
    [1, 2, 8, 9],   # 33 solutions
    [1, 4, 7, 8],   # 33 solutions
    [3, 4, 8, 9],   # 33 solutions
    [2, 4, 4, 9],   # 32 solutions
]

LEVEL2_CARDS = [   # 18 solutions or fewer (as close to 18 as possible)
    [1, 2, 3, 7],   # 18 solutions
    [1, 2, 8, 8],   # 18 solutions
    [2, 3, 3, 6],   # 18 solutions
    [1, 2, 3, 8],   # 17 solutions
    [1, 2, 5, 6],   # 17 solutions
    [3, 5, 6, 9],   # 17 solutions
    [1, 5, 5, 7],   # 17 solutions
    [1, 2, 3, 6],   # 16 solutions
    [1, 3, 4, 5],   # 16 solutions
    [1, 3, 4, 9],   # 16 solutions
    [2, 4, 5, 7],   # 16 solutions
    [2, 6, 7, 8],   # 16 solutions
    [1, 2, 2, 8],   # 16 solutions
    [1, 3, 6, 6],   # 16 solutions
    [3, 3, 6, 9],   # 16 solutions
    [1, 2, 7, 8],   # 15 solutions
    [1, 4, 5, 8],   # 15 solutions
    [2, 4, 7, 8],   # 15 solutions
    [3, 6, 7, 9],   # 15 solutions
    [3, 7, 8, 9],   # 15 solutions
    [1, 4, 6, 6],   # 15 solutions
    [9, 9, 9, 9],   # 15 solutions
    [1, 2, 3, 4],   # 14 solutions
    [1, 2, 4, 6],   # 14 solutions
    [2, 4, 6, 8],   # 14 solutions
    [3, 4, 5, 7],   # 14 solutions
    [4, 5, 6, 8],   # 14 solutions
    [4, 5, 7, 9],   # 14 solutions
    [4, 6, 8, 9],   # 14 solutions
    [2, 2, 4, 8],   # 14 solutions
]

LEVEL3_CARDS = [   # hardest: fewer solutions than any Level 2 card
    [1, 2, 3, 5],   # 13 solutions
    [1, 3, 4, 7],   # 13 solutions
    [2, 3, 4, 6],   # 13 solutions
    [2, 7, 8, 9],   # 13 solutions
    [3, 4, 5, 9],   # 13 solutions
    [1, 1, 2, 8],   # 13 solutions
    [2, 4, 4, 8],   # 13 solutions
    [1, 2, 3, 9],   # 12 solutions
    [1, 6, 7, 9],   # 12 solutions
    [2, 4, 5, 8],   # 12 solutions
    [3, 5, 7, 8],   # 12 solutions
    [1, 2, 4, 4],   # 12 solutions
    [2, 2, 5, 9],   # 12 solutions
    [3, 4, 5, 5],   # 12 solutions
    [3, 5, 6, 6],   # 12 solutions
    [1, 2, 5, 7],   # 11 solutions
    [1, 2, 2, 7],   # 11 solutions
    [1, 3, 9, 9],   # 11 solutions
    [1, 6, 6, 9],   # 11 solutions
    [2, 2, 4, 6],   # 11 solutions
    [2, 2, 8, 9],   # 11 solutions
    [2, 3, 6, 6],   # 11 solutions
    [2, 4, 4, 5],   # 11 solutions
    [2, 6, 8, 8],   # 11 solutions
    [3, 3, 5, 7],   # 11 solutions
    [5, 6, 9, 9],   # 11 solutions
    [3, 3, 3, 9],   # 11 solutions
    [1, 2, 4, 7],   # 10 solutions
    [1, 2, 5, 8],   # 10 solutions
    [1, 2, 5, 9],   # 10 solutions
]


# ============================================================
# CARD DESIGN (SNAP 18 — same look as the printed cards)
# ============================================================
def display_card_html(nums, level_label: str = "1"):
    html = textwrap.dedent(f"""
    <style>
    .new-card {{
        width: 440px;
        height: 440px;
        margin: 20px auto;
        background: radial-gradient(circle at center, #ffe680 0%, #ffae42 45%, #ff5a1f 100%);
        border: 8px solid #c23a00;
        border-radius: 24px;
        position: relative;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        overflow: hidden;
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
        width: 122px;
        height: 122px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'DejaVu Sans', Verdana, sans-serif;
        font-size: 56px;
        font-weight: 900;
        color: white;
        -webkit-text-stroke: 3px rgba(0,0,0,0.5);
        text-shadow: 0 3px 2px rgba(0,0,0,0.35);
        box-shadow: 0 8px 18px rgba(0,0,0,0.30);
        position: absolute;
        z-index: 2;
        border: 9px solid rgba(255,255,255,0.95);
    }}

    .tl {{ top: 13px; left: 13px; background: #e74c3c; }}
    .tr {{ top: 13px; right: 13px; background: #1f6fff; }}
    .bl {{ bottom: 32px; left: 13px; background: #2dbb41; }}
    .br {{ bottom: 32px; right: 13px; background: #f39c12; }}

    .center-logo {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -52%);
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

    .logo-snap {{
        font-family: 'DejaVu Sans', Verdana, sans-serif;
        font-size: 27px;
        font-weight: 900;
        line-height: 1;
        color: #ffd400;
        letter-spacing: 1px;
        text-shadow: 0 2px 0 rgba(0,0,0,0.25);
    }}

    .logo-18 {{
        font-family: 'DejaVu Sans', Verdana, sans-serif;
        font-size: 56px;
        font-weight: 900;
        line-height: 1.05;
        color: #ffd400;
        text-shadow: 0 3px 0 rgba(0,0,0,0.25);
    }}

    .level-badge {{
        position: absolute;
        bottom: 16px;
        left: 50%;
        transform: translateX(-50%);
        min-width: 110px;
        background: linear-gradient(180deg, #123caa 0%, #0b2f87 100%);
        color: white;
        border-radius: 9px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.28);
        z-index: 4;
        border: 3px solid rgba(255,255,255,0.9);
        text-align: center;
        padding: 6px 14px;
        line-height: 1.0;
        white-space: nowrap;
        font-family: 'DejaVu Sans', Verdana, sans-serif;
        font-size: 17px;
        font-weight: 900;
        letter-spacing: 0.5px;
    }}
    </style>

    <div class="new-card">
        <div class="burst"></div>

        <div class="number-circle tl">{nums[0]}</div>
        <div class="number-circle tr">{nums[1]}</div>
        <div class="number-circle bl">{nums[2]}</div>
        <div class="number-circle br">{nums[3]}</div>

        <div class="center-logo">
            <div class="logo-snap">SNAP</div>
            <div class="logo-18">18</div>
        </div>

        <div class="level-badge">LEVEL {level_label}</div>
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
                    # 1. (((a op b) op c) op d)
                    try:
                        r1_val, r1_expr = combine(a, a_expr, op1, b, b_expr)
                        r2_val, r2_expr = combine(r1_val, r1_expr, op2, c, c_expr)
                        r3_val, r3_expr = combine(r2_val, r2_expr, op3, d, d_expr)
                        if r3_val == TARGET:
                            solutions.add(f"{r3_expr} = {TARGET}")
                    except Exception:
                        pass

                    # 2. ((a op (b op c)) op d)
                    try:
                        r1_val, r1_expr = combine(b, b_expr, op2, c, c_expr)
                        r2_val, r2_expr = combine(a, a_expr, op1, r1_val, r1_expr)
                        r3_val, r3_expr = combine(r2_val, r2_expr, op3, d, d_expr)
                        if r3_val == TARGET:
                            solutions.add(f"{r3_expr} = {TARGET}")
                    except Exception:
                        pass

                    # 3. (a op ((b op c) op d))
                    try:
                        r1_val, r1_expr = combine(b, b_expr, op2, c, c_expr)
                        r2_val, r2_expr = combine(r1_val, r1_expr, op3, d, d_expr)
                        r3_val, r3_expr = combine(a, a_expr, op1, r2_val, r2_expr)
                        if r3_val == TARGET:
                            solutions.add(f"{r3_expr} = {TARGET}")
                    except Exception:
                        pass

                    # 4. (a op (b op (c op d)))
                    try:
                        r1_val, r1_expr = combine(c, c_expr, op3, d, d_expr)
                        r2_val, r2_expr = combine(b, b_expr, op2, r1_val, r1_expr)
                        r3_val, r3_expr = combine(a, a_expr, op1, r2_val, r2_expr)
                        if r3_val == TARGET:
                            solutions.add(f"{r3_expr} = {TARGET}")
                    except Exception:
                        pass

                    # 5. ((a op b) op (c op d))
                    try:
                        left_val, left_expr = combine(a, a_expr, op1, b, b_expr)
                        right_val, right_expr = combine(c, c_expr, op3, d, d_expr)
                        final_val, final_expr = combine(left_val, left_expr, op2, right_val, right_expr)
                        if final_val == TARGET:
                            solutions.add(f"{final_expr} = {TARGET}")
                    except Exception:
                        pass

    return sorted(solutions)


# ============================================================
# LEVELS (cards are built into this file — no Excel needed)
# ============================================================
def build_levels():
    level1 = [list(c) for c in LEVEL1_CARDS]
    level2 = [list(c) for c in LEVEL2_CARDS]
    level3 = [list(c) for c in LEVEL3_CARDS]

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
st.title("🃏 SNAP 18")

st.markdown(f"**Use all 4 numbers exactly once to make {TARGET} using +, -, ×, ÷ and brackets**")
st.markdown("**Fractions are not allowed in any calculation step.**")

if "game_exited" not in st.session_state:
    st.session_state.game_exited = False

if "all_cards" not in st.session_state:
    st.session_state.all_cards = build_levels()
    st.session_state.selected_level = 1
    st.session_state.current = 0
    st.session_state.show_solution = False
    st.session_state.score = 0
    st.session_state.start_time = time.time()

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

st.caption("SNAP 18 — 30 cards per level (90 in total), built into this file.")
