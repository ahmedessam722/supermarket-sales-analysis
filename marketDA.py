import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# جلب البيانات من ملف csv
data_sales = pd.read_csv("D:\\dataAnalysisPython\\test\\pro-test6\\supermarket-sales-analysis\\SuperMarket Analysis.csv")
# عرض 10 صفوف
print(data_sales.head(10))

# القيم الفريده
cols = ['Customer type','Product line','Branch','City','Payment']
for col in cols:
    print(data_sales[col].unique())

# معلومات عن الجدول
print(data_sales.info())

# ملخص احصائى
print(data_sales.describe())

# معرفه القيم المفقوده
print(data_sales.isnull().sum())
# لا يوجد قيم شاذه

# التوزيع التكرارى ل المبيعات
sns.histplot(data= data_sales , x= 'Sales')
plt.axvline(data_sales['Sales'].mean(),color = "red")
plt.axvline(data_sales['Sales'].median(),color = "black")
plt.show()

# معرفه القيم الشاذه
def outlier(col):
    q1 = data_sales[col].quantile(0.25)
    q3 = data_sales[col].quantile(0.75)
    iqr = q3 - q1
    lb = q1 - 1.5 * iqr
    ub = q3 + 1.5 * iqr
    outliers = data_sales[(data_sales[col] < lb) | (data_sales[col] > ub)]
    sum_outliers = len(outliers)
    return q1,q3,iqr,lb,ub ,sum_outliers
outlier('Sales')
# سيتم الاحتفاظ ب البيانات الشاذه لانها مهمه

# مخطط الرسم الصندوقى ل المبيعات
sns.boxplot(data = data_sales , x = 'Sales')
plt.show()


def add_col_date(col,col2):
    data_sales[col] = pd.to_datetime(data_sales[col])
    # اضافه عمود اليوم و اسماء ايام الاسبوع و الشهر
    data_sales['day'] = data_sales[col].dt.day
    data_sales['week'] = data_sales[col].dt.day_name()
    data_sales['month'] = data_sales[col].dt.month

    data_sales[col2] = pd.to_datetime(data_sales[col2])
    # اضافه عمود الساعه
    data_sales['hour'] = data_sales[col2].dt.hour
    return data_sales
add_col_date('Date','Time')

# داله لمعرفه اعلى 10 مبيعات و اقل 10 مبيعات 
def top_low():
    max_sales = data_sales.loc[data_sales['Sales'].idxmax()]
    top_10 = data_sales.nlargest(10,'Sales')
    min_sales = data_sales.loc[data_sales['Sales'].idxmin()]
    low_10 = data_sales.nsmallest(10,'Sales')
    return max_sales , top_10 , min_sales , low_10
top_low()

# التحليل الاستكشافى

columns_count = ['Customer type' , 'Gender','Product line']
# داله لمعرفه عدد الصفوفه
def columns_counts(col):
    df = data_sales[col].value_counts().sort_values()
    print(f"count {col}:\n {df}")
    return df
# رسم مخطط الاعمده
def columns_counts_bar_plot(labels,count,col):
    plt.figure(figsize = (16,6))
    sns.barplot(x = labels , y = count)
    plt.xlabel(col)
    plt.ylabel("count")
    plt.title(f"counts {col}")
    plt.show()
for col in columns_count:
    df = columns_counts(col)
    columns_counts_bar_plot(df.index,df.values,col)


columns = ['Customer type','Gender','gross margin percentage']
#  داله لمقارنه متغيران
def Product_line_columns(col):
    Customer_type = pd.crosstab(data_sales[col], data_sales['Product line'])
    print(f"{col} : \n {Customer_type}")
    return Customer_type
# رسم مخطط الاعمده
def product_line_columns_plot(df,col):
    df.plot(kind = 'bar' , figsize = (16,6) ,  colormap='Set3')
    plt.xlabel('Product line')
    plt.ylabel(f'count {col}')
    plt.title(f"bar plot count Product line {col}")
    plt.legend(title= col)
    plt.tight_layout()
    plt.show()
for col in columns:
    df = Product_line_columns(col)
    product_line_columns_plot(df,col)

data_cols = ['Branch','City','Customer type','Payment','Gender','Product line']
data_cols2 = ['day','week' ,'month' ,'hour']
# داله لحسب الوسيط لاعمده
def data_sales_median(col):
    data = data_sales.groupby(col)['Sales'].median().sort_values()
    print(f"med {col} : \n {data}")
    return data
# مخطط الاعمده
def data_sales_median_plot(labels,count,col):
    plt.figure(figsize=(16,6))
    sns.barplot(x = labels , y = count)
    plt.ylabel(col)
    plt.xlabel("med sales")
    plt.title(f"median sales for {col}")
    plt.show()
for col in data_cols:
    df = data_sales_median(col)
    data_sales_median_plot(df.index,df.values,col)
# الرسم الخطى
def data_sales_median_plot_line(labels,count,col):
    plt.figure(figsize=(16,6))
    sns.lineplot(x = labels , y = count , color = "red" , marker = 's')
    plt.xlabel("med sales")
    plt.ylabel(col)
    plt.title(f"median sales for {col}")
    plt.show()
for col in data_cols2:
    df = data_sales_median(col)
    data_sales_median_plot_line(df.index,df.values,col)

