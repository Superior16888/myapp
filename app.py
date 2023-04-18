import os
import streamlit as st

html_files = [f for f in os.listdir('static') if f.endswith('.html')]

def main():
    st.title("List of HTML files in static folder")
    st.write(html_files)

if __name__ == '__main__':
    main()
    
