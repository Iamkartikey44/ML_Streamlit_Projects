import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_moons
from sklearn.tree import DecisionTreeClassifier,plot_tree,export_graphviz
from sklearn.metrics import accuracy_score,confusion_matrix
from graphviz import Source
from os import system

st.set_page_config(page_title='HyperparameterTunning',layout='wide')

hide_style ="""
<style>
      #MainMenu {visibility:hidden}
      footer {visibility:hidden}
      header {visibility:hidden}


"""
st.markdown(hide_style,unsafe_allow_html=True)

st.warning("Make a dataset like target variable should be First column")
with st.sidebar.header("1. Upload your CSV data"):
    upload_file = st.sidebar.file_uploader("Upload your dataset",type=['csv'])
    st.sidebar.markdown("""
    [Example of CSV dataset]()
""")  


st.sidebar.markdown("# Hyperparameter_of_DecisionTree",unsafe_allow_html=True)

criterion = st.sidebar.selectbox("Criterion",('gini','entropy'))
splitter = st.sidebar.selectbox("Splitter",('best','random'))
max_depth = int(st.sidebar.number_input("Max Depth",min_value=1,step=10))
min_samples_split = st.sidebar.slider("Min Samples Split",1,100,2,key=1234)
min_samples_leaf = st.sidebar.slider("Min Samples Leaf",1,100,1,key=5678)
max_features = st.sidebar.slider("Max Features",1,2,2,key=1456,step=2)
max_leaf_nodes = int(st.sidebar.number_input("Max Leaf Nodes",min_value=4,step=1))
min_impurity_decrease  = st.sidebar.number_input("Min Impurity Decrease")


def build_model(df):
    X = df.iloc[:,1:]
    Y = df.iloc[:,0]
    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    st.markdown("**1.2. Data Splits**")
    st.write("Training Set")
    st.info(X_train.shape)
    st.write("Test Set")
    st.info(X_test.shape)

    st.markdown("**1.3. Variable Details**:")
    st.write("X_variable")
    st.info(list(X.columns))
    st.write("Y_variable")
    st.info(Y.name)

    clf = DecisionTreeClassifier(criterion=criterion,splitter=splitter,max_depth=max_depth,random_state=42,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,max_features=max_features,max_leaf_nodes=max_leaf_nodes,min_impurity_decrease=min_impurity_decrease)
    clf.fit(X_train, y_train)
 

    st.subheader("2. Model Performance")

    st.markdown("**2.1. Training Set**")
    y_pred_train = clf.predict(X_train) 
    
    st.write("Coefficient of determination (Accuracy_Score):")
    st.info(accuracy_score(y_train,y_pred_train))

    st.write("Confusion Matrix:")
    st.info(confusion_matrix(y_train,y_pred_train))

    st.markdown("**2.2. Test Set**")
    y_pred = clf.predict(X_test)
    st.write("Coefficient of determination (Accuracy Score):")
    st.info(accuracy_score(y_test,y_pred))

    st.write("Confusion Matrix:")
    st.info(confusion_matrix(y_test,y_pred))

    st.subheader("**3. Model Parameters**")
    st.write(clf.get_params())

    st.info("Tree for Model")
    tree  = export_graphviz(clf)
    
    st.graphviz_chart(tree) 

 

if upload_file is not None:
    dataset = pd.read_csv(upload_file)
    st.markdown("**1.1. Glimpse of Dataset**")
    st.dataframe(dataset)
    build_model(dataset)
else:
    st.info("Awaiting for CSV file to be uploaded.")
    if st.button("Press to Use Example Dataset: "):
        X,y = make_moons(n_samples=500,noise=0.30,random_state=42)
    
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        st.dataframe(pd.DataFrame(np.column_stack([X,y])))
        clf = DecisionTreeClassifier(criterion=criterion,splitter=splitter,max_depth=max_depth,random_state=42,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,max_features=max_features,max_leaf_nodes=max_leaf_nodes,min_impurity_decrease=min_impurity_decrease)
        clf.fit(X_train, y_train)
        y_pred= clf.predict(X_test)
        
        
        st.subheader(f"Accuracy for Decision Tree :{round(accuracy_score(y_test,y_pred),2)}")

        tree  = export_graphviz(clf,feature_names=["Col1","Col2"])
    
        st.graphviz_chart(tree) 
        

 