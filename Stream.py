import streamlit as st
import numpy as np
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

df = pd.read_csv(r"C:\Users\91822\OneDrive\Documents\Capstone-05\Copper_Set.xlsx - Result 1 (1).csv", low_memory=False)
item_type_mapping = {'W':1,'WI':2,'S':3,'Others':4,'PL':5,'IPL':6,'SLAWR':7}
status_mapping = {'Lost':0, 'Won':1, 'Draft':2, 'To be approved':3, 'Not lost for AM':4,
                                 'Wonderful':5, 'Revised':6, 'Offered':7, 'Offerable':8}
st.set_page_config(page_title="Industrial Copper Modeling",page_icon="🏨",layout="wide")

def setting_bg():
    st.markdown(f""" <style>.stApp {{
                        background:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjBK6t0e03ylnUGepRRtQVKr3e1f2egri-bQ&usqp=CAU");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)
setting_bg()
st.markdown("<h1 style='text-align: center; color: #00FF00;'>Industrial Copper Modeling</h1>", unsafe_allow_html=True)

# Use columns to organize elements horizontally
options=option_menu("Predictions based On ML",["Selling Price","Staus of the Product"],
                    icons=["cash-coin", "award-fill"])

if options == "Selling Price":
    col1,col2,col3=st.columns(3)
    with col1:
       st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxIQEhUSEBIQEhUXFxIVFRAQEA8QEhAXFRgXFhgSFRUYHSggGBslGxcWITEhKCkrLi4uFx8zODUtNygtLisBCgoKDg0OGxAQGy0lHyUrLS0tLS0rLS0tLS8tLSstLS0tLS0tNS8tLy0tLS0tLS0tLSstLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABgcBBAUCAwj/xABKEAABAwEEBQcHBwsCBwAAAAABAAIDEQQFEiEGMUFRcQcTImFykbIjMjNzgaGxFCRCUpLBwiU0Q1NigoOis9HwY3QVFjWjw+Hx/8QAGgEBAAIDAQAAAAAAAAAAAAAAAAEDAgQFBv/EADoRAAIBAgQCCAMFBwUAAAAAAAABAgMRBBIhMQVBE1FhcYGRofAiMrFCUsHR4QYUNYKywvEVM0OSov/aAAwDAQACEQMRAD8Aq9ERXGIREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBERAEREAREQBFtXZYH2iRsUQBcd5oGga3E7AF6vi7X2WV0T6EihDhUB4IycPeOIKi6vYw6WGfo7/ABWvbnba/maaIikzCIiAIiIAiLIHu19XFAYREQBERAEREAREQBERAEREAREQBERAEREARF6Y6hBFMiDmARlnmNqAsrQW5eYh514pJKAc9bGZUHE6yvhyhXXzkInaOlF0XU2xEk/yuoeDnL5aCW+W0PcZXucG7KuoatcfuW5pjfZsuBmBsgkZKHNdqINGkdzitX4s/aeKti48VUtHO92k9LWTa15ZWVmiBFtHtgi9RMLiGtBcSQA0CpcTkABtKlEOh+BoNpmbGT9COjiOLiKd2XWVjKajua9fFUqCTqO19t234L/HaRVF176uB9nGNrhLGcsYGbSdQeNnH4ZLkKU01dGdGtCtDPTd178fM27osJtEzIgaYjm76rQKud7ACppe98R3fzcEMdDhxuAp0GklrQfrONCTXYRvXJ5Ooa2l7/qQkjiXM+4OWLXc094260iztaebkcwue4Ma0Rnmmiu8837lVL4pWeyOfXowxeK6OorxhG9u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",width=400)
    with col2:
        status = st.selectbox('Status', df['status'].unique())
        item_type = st.selectbox('Item Type', df['item type'].unique())
        application = st.selectbox('Application', df['application'].unique())
        country = st.selectbox('Country Number', df['country'].unique())
        st.write("Minimum value=0.00001,Maximum value=6.807")
        quantity=st.text_input("Enter the Quantity in Logs")
    with col3:
        st.write("Minimum Value=0.16, Maximum Value=2.66")
        thickness_log=st.text_input("Enter the Thickness ")
        st.write("Minimum Value=1, Maximum Value=2990")
        width=st.text_input("Enter the Width ")
        st.write("Minimum Value=12458, Maximum Value=30408185")
        customer=st.text_input("Enter the Customer ID ")
        st.write("Minimum Value=611728, Maximum Value=1722207579")
        product_ref=st.text_input("Enter the Product Refernce: ")


    with open(r"C:\Users\91822\OneDrive\Documents\Project 5\Regression_model.pkl", 'rb') as file_1:
      regression_model = pickle.load(file_1)
    with col2:
        predict_button_1 = st.button("Predict Selling Price")
    if predict_button_1:
      status = status_mapping.get(status)
      item_type = item_type_mapping.get(item_type)
      country = float(country) 
      application = float(application)  
      product_ref = float(product_ref)  
      quantity = float(quantity)
      thickness_log = float(thickness_log)
      width = float(width)
      customer = float(customer)

      new_sample_1 = np.array([[quantity, status, item_type, application,
                         thickness_log, width, country, customer, product_ref,0]])
      new_pred_1 = regression_model.predict(new_sample_1)[0]
      predicted_selling_price = np.exp(new_pred_1)
      rounded_predicted_selling_price = round(predicted_selling_price, 3)

      st.write('# :green[Predicted Selling price:]', f"${rounded_predicted_selling_price}")

if options == "Staus of the Product":
    col1,col2,col3=st.columns(3)
    with col1:
       st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFctTenqYAcXUgn1dBy2PeRmR75IBIEH76RQ&usqp=CAU",width=450)
    with col2:
        item_type = st.selectbox('Item Type', df['item type'].unique())
        application = st.selectbox('Application', df['application'].unique())
        country = st.selectbox('Country Number', df['country'].unique())
        st.write("Minimum value=0.00001,Maximum value=6.807")
        quantity=st.text_input("Enter the Quantity in Logs")
        st.write("Minimum Value=0.16, Maximum Value=2.66")
        thickness_log=st.text_input("Enter the Thickness ")
    with col3:
        st.write("Minimum Value=5.983 ,Maximum Value=7.391")
        selling_price_log=st.text_input("Enter the Selling Price ")
        st.write("Minimum Value=1, Maximum Value=2990")
        width=st.text_input("Enter the Width ")
        st.write("Minimum Value=12458, Maximum Value=30408185")
        customer=st.text_input("Enter the Customer ID ")
        st.write("Minimum Value=611728, Maximum Value=1722207579")
        product_ref=st.text_input("Enter the Product Refernce: ")

    with open(r"C:\Users\91822\OneDrive\Documents\Project 5\Classification_Model.pkl", 'rb') as file_1:
      classification_model = pickle.load(file_1)
    with col2:
       predict_button_2 = st.button("Predict Status")

    if predict_button_2:
      item_type = item_type_mapping.get(item_type)
      country = float(country) 
      application = float(application)  
      product_ref = float(product_ref)  
      quantity = float(quantity)
      thickness_log = float(thickness_log)
      width = float(width)
      customer = float(customer)
      selling_price_log=float(selling_price_log)

        # -----Sending the user enter values for prediction to our model-----
      new_sample_2 = np.array(
               [[np.log(quantity), np.log(selling_price_log), item_type, application, np.log(thickness_log), width, country, customer, product_ref]])
      new_pred_2 = classification_model.predict(new_sample_2)
         
      if new_pred_2 ==1:
        st.write('# :green[The Status is: Won]')
      else:
        st.write('# :red[The Status is: Lost]')







