import pandas as pd
import streamlit as st

df = pd.read_csv('sales.csv')
df_new = df.iloc[:, :55]
x_label = df_new.columns[1:-2]

# function needed


def get_data_by_productCode(code):
    data = {'week': [], 'sales': []}
    get_data = df_new.loc[df_new['Product_Code'] == code]
    for i in range(len(x_label)):

        data['week'].append(i+1)
        data['sales'].append(*get_data[x_label[i]])
    df_prod = pd.DataFrame(data)
    return df_prod


# streamlit app
st.title('Dashboard analisis penjualan produk')

selectbox = st.sidebar.selectbox(
    'Pilih Produk apa yang ingin kamu lihat!',
    ('P'+str(i+1) for i in range(len(x_label)-1))
)

if(selectbox):
    # st.pyplot(get_data_by_productCode(selectbox))
    # fig, ax = plt.subplots()
    # ax.hist(get_data_by_productCode(selectbox), bins=20)

    # st.pyplot(fig)

    # p = figure(
    #     title='visualisasi analisis penjualan produk',
    #     x_axis_label='Minggu',
    #     y_axis_label='Banyak penjualan')

    data = get_data_by_productCode(selectbox)
    st.line_chart(data)

#     p.line([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
#            legend_label='Analisis Penjualan', line_width=2)

#     st.bokeh_chart(p, use_container_width=True)

# print(get_data_by_productCode(selectbox)['week'].tolist())
