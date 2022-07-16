import streamlit

# streamlit.title("This is the Title")

# streamlit.header("This is the Header")

# streamlit.subheader("This is the Subheader")

# streamlit.caption("This is the Caption")

# streamlit.text("This is the Text")

# streamlit.code("a=123, b=234, c=a+b")



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


# streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple','Avocado'])
# streamlit.dataframe(my_fruit_list)


frutis_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Apple','Avocado'])
fruits_to_show = streamlit.loc(frutis_selected)
streamlit.dataframe(fruits_to_show)
