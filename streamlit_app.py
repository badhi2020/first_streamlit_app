import streamlit

streamlit.title("This is the Title")

streamlit.header("This is the Header")

streamlit.subheader("This is the Subheader")

streamlit.caption("This is the Caption")

streamlit.text("This is the Text")

streamlit.code("a=123, b=234, c=a+b")



import panda
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
