import streamlit
#title
streamlit.title('My Parents New Healthy Diner') 
#creating header and the menu items
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
#creating a second header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#importing pandas library, creating a DATAFRAME called my_fruit_list and loading the S3 file
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list) #display the dataframe on sreamlit
