import json
import requests
import streamlit as st



# Title
st.title("Loan Default Prediction App")

st.image("img/image.jpg")

# breaf introduction to app
st.write("""
## About

Small Business Administration(SBA) is an agency of the Federal Government that exists to serve, support, 
and protect the interests of small businesses. One way SBA assist these small business enterprises is through a loan guarantee program which is designed to encourage the bank to grant loans to small business.
But, since SBA loans only guarantee a portion of the entire loan balance, banks will incur some losses if a small business defaults on its SBA-guaranteed loan. Therefore, banks are still faced with a difficult choice as to whether they should grant such a loan because of the high risk of default. 
One way to uniform their decision-making is through analyzing relevant historical data.

**This Streamlit App utilizes a Machine Learning model as Api to predict if a loan will be paid in full or not, 
based on the following criteria: type of industry, number of business employees, the amount disbursed by the bank, Gross Amount of Loan Approved by Bank, SBA's Guaranteed Amount of Approved Loan and Loan term in months.**

The Notebook, model and documentation are available on [Github](https://github.com/Luissalazarsalinas/Loan-Default-Prediction)

Made by Luis Fernando Salazar S.

"""
)



## Transform binary variables
def create_binary(content):
    if content =="Yes":
        content = 1
    elif content == "Not":
        content = 0
    elif content == "New":
        content = 1
    elif content == "Established":
        content = 0
    elif content == "Active":
        content = 1
    elif content == "Not active":
        content = 0

    return content
    
#
st.sidebar.header("Input Features for Loan")

# ----Create inputs----
# Class for New and Real state variables
bool_var = ("Yes", "Not")
real_var = ("New", "Established") 
rece_var = ("Active", "Not active")

# Categorical vairables
new = st.sidebar.selectbox("Is business new or already established?", real_var )
realestate = st.sidebar.selectbox("A loan backed by real estate?", bool_var)
recession = st.sidebar.selectbox("Loan State during recession(2007-2009)", rece_var)

# Numerical vairables 
naics_code = st.sidebar.number_input("Industry(NAICS code)", min_value=11, max_value=92)
st.sidebar.markdown("[NAICS CODE LIST](https://www.census.gov/naics/?58967?yearbck=2022)")
no_emp = st.sidebar.number_input("Number of Business Employees", min_value=0, max_value=9945)
disb_gross = st.sidebar.number_input("Amount Disbursed in $")
grappv_gross = st.sidebar.number_input("Gross Amount of Loan Approved by Bank in $")
sba_appv = st.sidebar.number_input("SBA's Guaranteed Amount of Approved Loan in $")
term = st.sidebar.slider("Loan term in months", min_value=0, max_value=527)



# Prediction button
prediction = st.button("Detect Result")

if prediction:
    
    data = {
            'NAICS_2DIG': naics_code,
            'Term': term,
            'NoEmp':no_emp,
            'New': create_binary(new),
            'DisbursementGross':disb_gross,
            'GrAppv':grappv_gross,
            'SBA_Appv':sba_appv,
            'Recession':create_binary(recession), 
            'RealEstate':create_binary(realestate),
            'portion': (sba_appv/grappv_gross)
            }

    st.write(f"""### Loan details:\n
    
    1. Industry(NAICS code): {naics_code}\n
    2. Loan term in months: {term}\n
    3. Number of Business Employees: {no_emp}\n
    4. New or old Business: {new}\n
    5. Amount Disbursed [$]: {disb_gross}$\n
    6. Gross Amount of Loan Approved by Bank [$]: {grappv_gross}$\n
    7. SBA's Guaranteed Amount of Approved Loan [$]: {sba_appv}$\n
    8. Loan State during recession(2007-2009): {recession}\n
    9. Loan backed by real estate: {realestate}\n
    10. Portion: {(sba_appv/grappv_gross)}\n
                """)

    # request 
    post_rest = requests.post("https://loan-default-detector.herokuapp.com/inferece", json = data)
    rest_str = json.dumps(post_rest.json())
    result = json.loads(rest_str)

    st.header("Loan result")

    st.write(f"""### Status: {result["status"]}
                  """)
    st.write(f"""### Score: {result["score"]}
                  """)



    

