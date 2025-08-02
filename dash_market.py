import streamlit as st
import pandas as pd
from marketDA import outlier,add_col_date,top_low,columns_counts,Product_line_columns,data_sales_median
from visuals import histplot,box_plot_sales,bar_plot_counts,bar_plot_product_line,data_sales_median_plot_bar,sales_median_plot_line

@st.cache_data
def load_data():
    return pd.read_csv("D:\\dataAnalysisPython\\test\\pro-test6\\supermarket-sales-analysis\\SuperMarket Analysis.csv")

data_sales = load_data()

st.title("لوحه تحليل مبيعات المحل")

sections = st.sidebar.radio(
    'انتقل الى :',
    (
        "مقدمة وبيانات الجدول",
        "لمعرفه عدد الصفوف",
        "المقارنه متغيرين",
        "حسب الوسيط لاعمده"
    )
)

if sections == "مقدمة وبيانات الجدول":
    st.write('جلب البيانات من ملف csv :')
    st.dataframe(data_sales.head(10))

    st.write("ملخص احصائى :")
    with st.expander("ملخص احصائى"):
        st.write(data_sales.describe())

    st.write("القيم المفقوده :")
    with st.expander("القيم المفقوده :"):
        st.write(data_sales.isnull().sum())
    
    histplot(data_sales , 'Sales')

    sum_outliers,q1,q3,iqr,lb,ub = outlier('Sales')
    st.write(f'الربع الاول = {q1}')
    st.write(f'الربع الثالث = {q3}')
    st.write(f'المدى الربيعى = {iqr}')
    st.write(f'الحد الادنى = {lb}')
    st.write(f'الحد الاقصى = {ub}')
    st.write(f'عدد القيم الشاذه = {sum_outliers}')

    box_plot_sales(data_sales , 'Sales')

    st.subheader("اضافه عمود اليوم و اسماء ايام الاسبوع و الشهر و الساعه")
    df = add_col_date('Date','Time')
    st.dataframe(df)

    max_sales , top_10 , min_sales , low_10 = top_low()

    st.write("اعلى 10 مبيعات :")
    st.dataframe(top_10)

    st.write("اعلى عمله بيع :")
    st.dataframe(max_sales)

    st.write("اقل 10 مبيعات :")
    st.dataframe(low_10)

    st.write("اقل عمله بيع :")
    st.dataframe(min_sales)

if sections == "لمعرفه عدد الصفوف":
    st.subheader("عدد المبيعات لكل نوع من العملاء :")
    df = columns_counts('Customer type')
    st.dataframe(df)
    bar_plot_counts('Customer type',df.index,df.values)
    st.write('العملاء الاعضاء اكثر من العملاء العاديين')

    st.subheader("عدد المبيعات لذكور و الاناث :")
    df2 = columns_counts('Gender')
    st.dataframe(df2)
    bar_plot_counts('Gender',df2.index,df2.values)
    st.write('العملاء الاناث اكثر من العملاء الذكور')

    st.subheader("عدد المبيعات لكل قسم :")
    df3 = columns_counts('Product line')
    st.dataframe(df3)
    bar_plot_counts('Product line',df3.index,df3.values)
    st.write("قسم اكسوارات الموضه اكثر قسم يدخل فيه عملاء و قسم الصحه و الجمال هو اقل قسم يدخل فيه عملاء")

if sections == "المقارنه متغيرين":
    st.header("مقارنه بين متغيرين")
    st.subheader("المقارنه بين نوع العميل  و كل قسم")
    df = Product_line_columns("Customer type")
    st.dataframe(df)
    bar_plot_product_line(df,'Customer type')
    st.write('اكثر قسم يقوم فيه عمليات شراء من العملاء الاعضاء هو قسم الطعام و المشرويات و اقل قسم يقوم فيه مبيعات من قبل الاعملاء الاعضاء هو قسم الصحه و الجمال')
    st.write('اكثر قسم يقوم فيه العملاء العاديين بعمليات شراء هو اكسسوارات الموضه و اقل قسم يقوم فيه العملاء العاديين بعمليات شراء هو قسم المنزل و اسلوب الحياه')

    st.subheader("المقارنه بين نوع الجنس  و كل قسم")
    df2 = Product_line_columns("Gender")
    st.dataframe(df2)
    bar_plot_product_line(df2,'Gender')
    st.write('اكثر قسم يقوم فيه عمليات شراء من قبل الاناث هو قسم اكسسوارات الموضه واقل قسم يقوم فيه عمليات شراء من قبل الاناث هو الصحه و الجمال')
    st.write('اكثر قسم يقوم فيه عمليات شراء من قبل الذكور هو اكسسورارت الكترونيه و اقل قسم يقوم فيه عمليات شراء من قبل الذكور هو المنزل و اسلوب الحياه')

    st.subheader("المقارنه بين نسبه هامش الربح و كل قسم")
    df3 = Product_line_columns("gross margin percentage")
    st.dataframe(df3)
    bar_plot_product_line(df3,'gross margin percentage')
    st.write('اعلى نسبه هامش الربح من قسم اكسسوارات الموضه و اقل نسبه هامش ربح من قسم الصحه و الجمال')

if sections == "حسب الوسيط لاعمده" :
    st.header('حسب الوسيط')
    st.subheader("حساب الوسيط على حسب الفرع")
    df = data_sales_median('Branch')
    st.dataframe(df)
    data_sales_median_plot_bar(df.index , df.values , 'Branch')
    st.write('اعلى نسبه مبيعات من فرع الجيزا و اقل نسبه مبيعات من فرع الاسكندريه')

    st.subheader("حساب الوسيط على حسب المدينه")
    df2 = data_sales_median('City')
    st.dataframe(df2)
    data_sales_median_plot_bar(df2.index , df2.values , 'City')
    st.write('اعلى نسبه مبيعات من مدينه تايبيداو و اقل نسبه مبيعات من مدينه يانغو')

    st.subheader("حساب الوسيط على حسب نوع العميل")
    df3 = data_sales_median('Customer type')
    st.dataframe(df3)
    data_sales_median_plot_bar(df3.index , df3.values , 'Customer type')
    st.write('اعلى نسبه مبيعات من العملاء الاعضاء واقل نسبه مبيعات من العملاء العاديين')

    st.subheader("حساب الوسيط على حسب طريقه نوع الجنس")
    dfa = data_sales_median('Payment')
    st.dataframe(dfa)
    data_sales_median_plot_bar(dfa.index , dfa.values , 'Payment')
    st.write('اكثر طريقه دفع مستخدمه من قبل العملاء هى الطريقه النقديه و اقل طريقه مستخدمه من قبل العملاء هى طريقه بطاقه الائتمان')

    st.subheader("حساب الوسيط على حسب طريقه نوع الجنس")
    df5 = data_sales_median('Gender')
    st.dataframe(df5)
    data_sales_median_plot_bar(df5.index , df5.values , 'Gender')
    st.write('اعلى نسبه مبيعات من قبل العملاء الاناث و اقل نسبه مبيعات من قبل العملاء الذكور')

    st.subheader("حساب الوسيط على حسب طريقه القسم")
    df6 = data_sales_median('Product line')
    st.dataframe(df6)
    data_sales_median_plot_bar(df6.index , df6.values , 'Product line')
    st.write('اعلى قسم فى نسبه المبيعات هو قسم الصحه و الجمال واقل قسم فى المبيعات هو قسم اكسسوارات الموضه')

    st.subheader("حساب الوسيط على حسب طريقه اليوم")
    df7 = data_sales_median('day')
    st.dataframe(df7)
    sales_median_plot_line(df7.index , df7.values , 'day')
    st.write('اعلى يوم يكون فيه نسبه مبيعات اكثر هو 20 و اقل يوم يكون فيه نسبه مبيعات اقل هو 13')

    st.subheader("حساب الوسيط على حسب طريقه ايام الاسبوع")
    df8 = data_sales_median('week')
    st.dataframe(df8)
    sales_median_plot_line(df8.index , df8.values , 'week')
    st.write('اعلى يوم من ايام الاسبوع يكون فيه نسبه مبيعات اعلى هو يوم السبت و اقل يوم من ايام الاسبوع يكون فيه نسبه مبيعات اقل هو يوم الاربعاء')

    st.subheader("حساب الوسيط على حسب طريقه ايام الشهر")
    df9 = data_sales_median('month')
    st.dataframe(df9)
    sales_median_plot_line(df9.index , df9.values , 'month')
    st.write('اعلى شهر كان فيه نسبه مبيعات اكثر هو شهر 1 و اقل شهر كان فيه نسبه المبيعات اقل هو شهر 3')

    st.subheader("حساب الوسيط على حسب طريقه ايام الساعه")
    df10 = data_sales_median('hour')
    st.dataframe(df10)
    sales_median_plot_line(df10.index , df10.values , 'hour')
    st.write('اعلى ساعه يكون فيه نسبه مبيعات عاليه هى الشاعه 7 مساء و اقل ساعه يكون فيه نسبه المبيعات اقل هى الساعه 6 مساء')


    

