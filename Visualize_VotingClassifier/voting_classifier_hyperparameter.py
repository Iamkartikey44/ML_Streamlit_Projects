import streamlit as st
import matplotlib.pyplot as plt
from HelpingFunctionModel import ModelBuild
import HelpingFunctionData

concentric,linear,outlier,spiral,ushape,xor = HelpingFunctionData.load_dataset()

plt.style.use("seaborn-bright")

st.sidebar.markdown("# Voting Classifier")
dataset = st.sidebar.selectbox("Dataset",
                               ("U-Shaped",'Linearly Separable','Outlier','Two Spirals','Concentric Circles','XOR'))

estimators = st.sidebar.multiselect("Estimators",
                                    ['KNN','Logistic Regression','Gaussian Naive Bayes','SVM','Random Forest'])

voting_type = st.sidebar.radio("Voting Type",("hard","soft"))

st.header(dataset)

fig,ax =plt.subplots()

df = HelpingFunctionData.load_initial_graph(dataset,ax)
orig = st.pyplot(fig)

X = df.iloc[:,:2].values
y = df.iloc[:,-1].values

Model = ModelBuild(X,y)

if st.sidebar.button("Run Algorithm"):
    algos = Model.create_base_estimators(estimators,voting_type)
    
    voting_clf,voting_clf_accuracy = Model.train_voting_classifier(algos,voting_type)
    Model.draw_main_graph(voting_clf,ax)
    orig.pyplot(fig)
    figs = Model.plot_other_graph(algos)

    st.sidebar.header("Classification Metrics")
    st.sidebar.text(f"Voting Classifier Accuracy: {voting_clf_accuracy}")

    accuracy_estimators = Model.calculate_base_model_accuracy(algos)
    

    for i in range(len(accuracy_estimators)):
        st.sidebar.text(f"Accuracy for {algos[i][1]}: {accuracy_estimators[i]}")
    counter=0
    for i in st.columns(len(figs)):
        with i :
            st.pyplot(figs[counter])
            st.text(counter)
        counter+=1         
