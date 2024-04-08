# 510_lab2
# How to Run
Open the terminal and run the following commands:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

# What's include
app.py - main running application.
.gitignore - tells Git which files or directories to ignore in a project.
BostonHousing.csv - csv dataset for application.
requirements.txt - list all the dependencies that the project needs to run correctly.
README.md - includes the text info of the basic introduction of this GitHub Repository, how to run, what's included, lessons learned, questions / uncertainties

# Lesson Learned
practical experience in data analysis, visualization, and web app development. 
how to effectively present data insights through interactive elements.

💾 Embracing Static Content
Streamlit shines when it comes to displaying static content like text and media. The library's text and media elements, along with its layout options, enable the creation of well-structured and informative pages with minimal effort.

📊 Data Representation
st.dataframe is the go-to widget for displaying data due to its built-in functionalities like filtering and sorting. However, it falls short on interactivity.
st.table, while offering more flexibility in layout and the ability to embed interactive components, lacks the convenience of built-in data manipulation features.
Third-party Components
Extensions like streamlit-ag-grid can be leveraged to enhance data interactivity, providing a bridge where Streamlit's default components may not suffice.

✨ The Power of Interactivity
Understanding how Streamlit refreshes the page and manages state is crucial. It reruns the entire script upon interaction or code changes, which can be optimized with callbacks and session state management to create efficient applications.

# questions
How can I effectively select and utilize data visualization tools to enhance the interpretability of my dataset in the web app project?
