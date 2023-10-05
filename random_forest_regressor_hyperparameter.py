import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.datasets import load_boston

st.set_page_config(page_title="RandomForest Hyperparamter Tuning App",layout='wide')


def build_model(df):
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=(100-split_size)/100,random_state=42)

    st.markdown("**1.2. Data Splits**")
    st.write("Training Set")
    st.info(X_train.shape)
    st.write("Test Set")
    st.info(X_test.shape)

    st.markdown("**1.3. Variable Details**:")
    st.write("X_variable")
    st.info(list(X.columns))
    st.write("Y_variable")
    st.info(y.name)
    
    rf = RandomForestRegressor(n_estimators=parameter_n_estimators,
                               random_state=parameter_random_state,
                               max_features=parameter_max_features,
                               criterion=parameter_criterion,
                               min_samples_split=parameter_min_samples_split,
                               min_samples_leaf=parameter_min_samples_leaf,
                               bootstrap=parameter_bootstrap,
                               oob_score=parameter_oob_score,
                               n_jobs=parameter_n_jobs)
    rf.fit(X_train,y_train)

    st.subheader("2. Model Performance")

    st.markdown("**2.1. Training Set**")
    y_pred_train = rf.predict(X_train) 
    st.write("Coefficient of determination ($R^2$):")
    st.info(r2_score(y_train,y_pred_train))

    st.write("Error (MSE or MAE):")
    st.info(mean_squared_error(y_train,y_pred_train))

    st.markdown("**2.2. Test Set**")
    y_pred = rf.predict(X_test)
    st.write("Coefficient of determination ($R^2$):")
    st.info(r2_score(y_test,y_pred))

    st.write("Error (MSE or MAE):")
    st.info(mean_squared_error(y_test,y_pred))

    st.subheader("**3. Model Parameters**")
    st.write(rf.get_params())

st.write("""
# Hyperparameter Tuning
In this implementation, we are doing random forest hyperparameter tunning , we  try different combination and
get best parameters for any dataset.           
""")   
st.warning("Make a dataset like target variable should be last column")
with st.sidebar.header("1. Upload your CSV data"):
    upload_file = st.sidebar.file_uploader("Upload your dataset",type=['csv'])
    st.sidebar.markdown("""
    [Example of CSV dataset]()
""")            

with st.sidebar.header('2. Set Paramters'):
    split_size= st.sidebar.slider("Data Split ratio (% for Training Set)",10,90,80,5)

with st.sidebar.subheader('2.1 Learning Parameters'):
    parameter_n_estimators = int(st.sidebar.number_input("Number of estimators",0,1000,100,10))
    parameter_max_features = st.sidebar.selectbox("Max Features",('auto','sqrt','log2'))
    parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
    parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

with st.sidebar.subheader('2.2 General Parameters'):
    parameter_random_state = int(st.sidebar.number_input('Seed Number(random state)',0,1000,42,1))
    parameter_criterion = st.sidebar.selectbox("Performance measure(criterion)",options=['mse','mae'])
    parameter_bootstrap = st.sidebar.radio("Bootstrap samples when building trees (bootstrap)",('True','False'))
    parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)',('True','False'))
    parameter_n_jobs = st.sidebar.selectbox('Number of jobs to run in parallel (n_jobs)', options=[1, -1])

st.subheader('1. Dataset')

if upload_file is not None:
    dataset = pd.read_csv(upload_file)
    st.markdown("**1.1. Glimpse of Dataset**")
    st.write(dataset)
    build_model(dataset)
else:
    st.info("Awaiting for CSV file to be uploaded.")
    if st.button("Press to use Example Datatset"):
        boston = load_boston()
        X = pd.DataFrame(boston.data, columns=boston.feature_names)
        Y = pd.Series(boston.target, name='response')
        dataset = pd.concat( [X,Y], axis=1 )

        st.markdown("The Boston housing dataset is used as the example.")
        st.write(dataset.head(5))

        build_model(dataset)



