import streamlit
import pandas

streamlit.title("My Parents New Healthy Diner!")
streamlit.header("Today's Breakfast Menu is here!")
streamlit.text("🥣Omega 3 & Blueberry Oatmeal")
streamlit.text(" 🥗 Kale, Spinach & Rocket smothie")
streamlit.text(" 🐔 Hard-boiled free Range EGG!")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_first_fruit = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_first_fruit)


my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_first_fruit)

