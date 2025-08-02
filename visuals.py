import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# مخطط التوزيع التكرارى ل المبيعات
def histplot(df , col):
    st.subheader(" التوزيع التكراري لمبيعات :")
    fig1, ax1 = plt.subplots()
    sns.histplot(data=df, x=col, kde=True, ax=ax1)
    ax1.axvline(df[col].mean(), color='red', label='mean')
    ax1.axvline(df[col].median(), color='black', label='median')
    ax1.legend()
    st.pyplot(fig1)
# الرسم الصندوقى لمبيعات
def box_plot_sales(df,col):
    st.subheader("الرسم الصندوقى لمبيعات :")
    fig , ax = plt.subplots()
    sns.boxplot(data = df , x = col , ax = ax)
    st.pyplot(fig)

def bar_plot_counts(col,labels,count):
    st.subheader(f"{col}مخطط الاعمده ل ")
    fig ,ax = plt.subplots()
    sns.barplot(x = labels , y = count , ax = ax)
    ax.set_xlabel(col)
    ax.set_ylabel("count")
    ax.set_title(f"counts {col}")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

def bar_plot_product_line(df,col):
    st.subheader("مخطط الاعمده بين متغيرين")
    fig , ax = plt.subplots()
    df.plot(kind = 'bar' , figsize = (16,6) ,  colormap='Set3' , ax = ax)
    ax.set_xlabel('Product line')
    ax.set_ylabel(f'count {col}')
    ax.set_title(f"bar plot count Product line {col}")
    ax.legend(title= col)
    st.pyplot(fig)

def data_sales_median_plot_bar(labels,count,col):
    st.subheader("مخطط الاعمده ل الوسيط")
    fig ,ax = plt.subplots()
    sns.barplot(x = labels , y = count, ax = ax)
    ax.set_ylabel(col)
    ax.set_xlabel("med sales")
    ax.set_title(f"median sales for {col}")
    st.pyplot(fig)

def sales_median_plot_line(labels,count,col):
    st.subheader("الرسم الخطى لتاريخ")
    fig , ax = plt.subplots()
    sns.lineplot(x = labels , y = count , color = "red" , marker = 's' ,ax =ax)
    ax.set_xlabel("med sales")
    ax.set_ylabel(col)
    ax.set_title(f"median sales for {col}")
    st.pyplot(fig)
