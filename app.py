import streamlit as st

st.title("Kelas Awan Pintar")

st.header("Mari Belajar fungsi Streamlit Dasar")

st.subheader("Ayo Guys kita belajar streamlit dari dasar")

st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

st.markdown("# Test 1")
st.markdown("## Test 1")
st.markdown("### Test 1")

st.markdown("""
#test 1
            
##test2

###test3
""",True)

code = '''def hello():
    print("Hello, Streamlit!)'''
st.code(code, language='python')

import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()
st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule