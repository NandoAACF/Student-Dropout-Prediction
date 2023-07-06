import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache_data
def load_data():
    # Menampilkan data
    df = pd.read_csv('data.csv', sep=';')
    df.drop(df[df['Target'] == 'Enrolled'].index, inplace = True)

    return df

df = load_data()

def show_insight_page():
    st.title('Student Dropout Insight')
    
    st.markdown("### **1. Bagaimana distribusi mahasiswa yang graduate dan dropout?**")

    target_counts = df['Target'].value_counts()

    plt.figure(figsize = (5,5))

    plt.pie(target_counts, labels=target_counts.index, autopct='%1.1f%%')

    plt.title('Target Distribution')

    st.pyplot(plt)

    st.write('Tampak bahwa distribusinya masih cukup balance sehingga tidak perlu dilakukan penanganan khusus untuk mengatasi masalah imbalance data.')




    st.markdown("### **2. Bagaimana pengaruh status perkawinan terhadap tingkat kelulusan mahasiswa?**")
    plt.figure(figsize = (7,4))
    ax = sns.countplot(data = df, x = 'Marital status', hue = 'Target')

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan siswa berdasarkan status perkawinan')
    st.pyplot(plt)

    st.write('Keterangan:')
    st.write('1 = Single')
    st.write('2 = Married')
    st.write('3 = Widower')
    st.write('4 = Divorced')
    st.write('5 = Facto Union')
    st.write('6 = Legally Separated')

    st.write('Tampak bahwa ada perbedaan signifikan antara tingkat kelulusan mahasiswa yang belum menikah dibanding yang sudah menikah.')
    st.write('Jumlah mahasiswa single yang lulus sebesar hampir 2 kali lipat lebih banyak dibandingkan mahasiswa single yang dropout.')
    st.write('Sebaliknya jumlah mahasiswa sudah menikah justru lebih banyak yang dropout dibandingkan yang berhasil lulus')




    st.markdown('### **3. Apakah mahasiswa yang menggunakan beasiswa memiliki tingkat kelulusan yang lebih tinggi?**')
    plt.figure(figsize = (5,4))
    ax = sns.countplot(data = df, x = 'Scholarship holder', hue = 'Target')

    # Untuk menampilkan nilai detail di atas bar
    for i in ax.containers:
        ax.bar_label(i,)

    plt.title('Kelulusan siswa berdasarkan status beasiswa')
    st.pyplot(plt)

    st.write('Keterangan:' )
    st.write('0 = Tidak menggunakan beasiswa')
    st.write('1 = Menggunakan beasiswa')
    st.write('Tampak jelas bahwa lebih dari 85% mahasiswa yang menggunakan beasiswa berhasil lulus')
    st.write('Sebaliknya, mahasiswa yang tidak menggunakan beasiswa memiliki jumlah yang hampir sama antara yang lulus dan tidak lulus.')




    st.markdown("### **4. Apakah umur berpengaruh terhadap tingkat kelulusan mahasiswa?**")
    # Lakukan binning untuk age
    bins = [10, 20, 30, 40, 50, 60, 70]
    labels = ['11-20', '21-30', '31-40', '41-50', '51-60', '61-70']
    df['Age'] = pd.cut(df['Age at enrollment'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(9, 5))
    ax = sns.countplot(data=df, x='Age', hue='Target')

    # Memberi anotasi
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan umur')
    st.pyplot(plt)

    st.write('Ya, tampak bahwa umur berpengaruh terhadap tingkat kelulusan mahasiswa.')
    st.write('Terlihat bahwa semakin tua umur mahasiswa, maka semakin sedikit pula persentase mahasiswa yang lulus.')




    st.markdown('### **5. Apakah GDP berpengaruh terhadap tingkat kelulusan mahasiswa?**')
    plt.figure(figsize=(9, 5))
    ax = sns.countplot(data=df, x='GDP', hue='Target')

    # Menambah anotasi
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan GDP')
    st.pyplot(plt)

    st.write('Tampak bahwa GDP tidak terlalu berpengaruh terhadap tingkat kelulusan mahasiswa.')
    st.write('Hal tersebut karena jumlah mahasiswa yang lulus dan tidak lulus pada setiap GDP hampir sama.')
    st.write('Namun, bila dicermati secara lebih detail, tampak bahwa GDP 1.79, 2.02, 3.51 memiliki persentase mahasiswa yang lulus lebih tinggi dibandingkan GDP yang lain')


    st.markdown('### **6. Apakah ada relasi antara jumlah SKS dengan nilai yang didapatkan di semester 1?**')
    plt.figure(figsize=(10, 5))
    ax = sns.lineplot(data=df, x='Curricular units 1st sem (approved)', y='Curricular units 1st sem (grade)')

    plt.title('Approved vs Grade Curricular Units 1st Semester')
    st.pyplot(plt)
    st.write('Tampak ada perbedaan yang signifikan mengenai nilai yang didapatkan mahasiswa yang mengambil di bawah 5 sks dan di atas 5 sks.')
    st.write('Mahasiswa yang mengambil di bawah 5 sks mendapatkan nilai yang jauh lebih jelek dibandingkan mahasiswa yang mengambil di atas 5 sks.')
    st.write('Namun, tidak ada perbedaan signifikan mengenai nilai yang didapatkan mahasiswa yang mengambil antara 5-20 sks.')
    st.write('Mahasiswa yang mengambil di atas 21 sks mendapatkan nilai yang lebih baik dibandingkan mahasiswa yang mengambil di bawah 20 sks.')

    st.markdown('### **7. Apakah ada relasi antara jumlah SKS dengan nilai yang didapatkan di semester 2?**')
    plt.figure(figsize=(10, 5))
    ax = sns.lineplot(data=df, x='Curricular units 2nd sem (approved)', y='Curricular units 2nd sem (grade)')

    plt.title('Approved vs Grade Curricular Units 2nd Semester')
    st.pyplot(plt)
    st.write('Tampak bahwa polanya masih sama seperti pada analisis semester 1 di atas.')


    st.markdown('### **8. Bagaimana pengaruh jumlah SKS di semester 1 terhadap tingkat kelulusan mahasiswa?**')
    # Melakukan binning untuk jumlah SKS
    bins = [0, 4, 8, 12, 16, 20, 24]
    labels = ['1-4', '5-8', '9-12', '13-16', '17-20', '21-24']
    df['Jumlah SKS 1st Sem'] = pd.cut(df['Curricular units 1st sem (approved)'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(9, 5))
    ax = sns.countplot(data=df, x='Jumlah SKS 1st Sem', hue='Target')

    # Anotasi
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan jumlah SKS semester 1')
    st.pyplot(plt)

    st.write('Tampak bahwa mahasiswa yang mengambil 1-4 SKS memiliki persentase kelulusan yang sangat kecil.')
    st.write('Sebaliknya, mahasiswa yang mengambil di atas 5 sks memiliki persentase kelulusan yang lebih besar.')




    st.markdown('### **9. Bagaimana pengaruh jumlah SKS di semester 2 terhadap tingkat kelulusan mahasiswa?**')
    # Melakukan binning untuk jumlah SKS
    bins = [0, 4, 8, 12, 16, 20]
    labels = ['1-4', '5-8', '9-12', '13-16', '17-20']
    df['Jumlah SKS 2nd Sem'] = pd.cut(df['Curricular units 2nd sem (approved)'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(9, 5))
    ax = sns.countplot(data=df, x='Jumlah SKS 2nd Sem', hue='Target')

    # Anotasi
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan jumlah SKS semester 2')
    st.pyplot(plt)

    st.write('Pola yang tampak masih sama seperti semester 1 di atas')
    st.write('Tampak bahwa mahasiswa yang mengambil 1-4 SKS memiliki persentase kelulusan yang sangat kecil.')
    st.write('Sebaliknya, mahasiswa yang mengambil di atas 5 sks memiliki persentase kelulusan yang lebih besar.')




    st.markdown('### **10. Bagaimana persebaran IP mahasiswa di semester 1?**')

    plt.figure(figsize=(9, 5))

    sns.histplot(data=df, x='Curricular units 1st sem (grade)')

    plt.title('Distribusi IP Mahasiswa di Semester 1')
    plt.xlabel('IP Mahasiswa')
    plt.ylabel('Count')

    st.pyplot(plt)

    st.write('Tampak bahwa persebaran IP mahasiswa di semester 1 ada di antara 10 - 16')
    st.write('Ada sekitar 600 mahasiswa yang mendapatkan IP 0')
    st.write('Hal tersebut mungkin terjadi jika mahasiswa tidak pernah mengikuti kelas pada mata kuliah yang sudah ia daftarkan.')



    st.markdown('### **11. Bagaimana pengaruh IP mahasiswa di semester 1 terhadap tingkat kelulusan mahasiswa?**')
    # Melakukan binning untuk nilai semester 1
    bins = [9.5, 10.25, 11, 11.75, 12.5, 13.25, 14, 14.75, 15.5, 16.25]
    labels = ['9.60-10.25', '10.26-11.00', '11.01-11.75', '11.76-12.50', '12.51-13.25', '13.26-14.00', '14.01-14.75', '14.76-15.50', '15.51-16.25']
    df['1st Sem Grade Group'] = pd.cut(df['Curricular units 1st sem (grade)'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(12, 5))
    ax = sns.countplot(data=df, x='1st Sem Grade Group', hue='Target')

    # Anotasi
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan IP semester 1')
    st.pyplot(plt)

    st.write('Tampak jelas bahwa semakin tinggi IP, maka semakin besar pula persentase mahasiswa yang lulus.')
    st.write('Mahasiswa yang mendapatkan IP 9.6-10.25 memiliki persentase kelulusan yang sangat kecil.')
    st.write('Hal ini menunjukkan bahwa IP memang berpengaruh terhadap kelulusan mahasiswa.')

    


    st.markdown('### **12. Bagaimana persebaran IP mahasiswa di semester 2?**')

    plt.figure(figsize=(9, 5))

    sns.histplot(data=df, x='Curricular units 2nd sem (grade)')

    plt.title('Distribusi IP Mahasiswa di Semester 2')
    plt.xlabel('IP Mahasiswa')
    plt.ylabel('Count')

    st.pyplot(plt)

    st.write('Tampak bahwa persebaran IP mahasiswa di semester 2 ada di antara 10 - 17')
    st.write('Ada sekitar 800 mahasiswa yang mendapatkan IP 0')
    st.write('Distribusi ini masih mirip dengan distribusi IP pada semester 1.')

    
    
    st.markdown('### **13. Bagaimana pengaruh IP mahasiswa di semester 2 terhadap tingkat kelulusan mahasiswa?**')
    # Melakukan binning untuk nilai semester 2
    bins = [9.5, 10.25, 11, 11.75, 12.5, 13.25, 14, 14.75, 15.5, 16.25]
    labels = ['9.60 - 10.25', '10.26 - 11.00', '11.01 - 11.75', '11.76 - 12.50', '12.51 - 13.25', '13.26 - 14.00', '14.01 - 14.75', '14.76 - 15.50', '15.51 - 16.25']
    df['2nd Sem Grade Group'] = pd.cut(df['Curricular units 2nd sem (grade)'], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(13, 5))
    ax = sns.countplot(data=df, x='2nd Sem Grade Group', hue='Target')

    # Anotasi
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2, p.get_height()),
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.title('Kelulusan siswa berdasarkan IP semester 2')
    st.pyplot(plt)

    st.write('Sama seperti semester 1, tampak jelas bahwa semakin tinggi IP, maka semakin besar pula persentase mahasiswa yang lulus.')


    st.markdown('## **Kesimpulan**')
    st.markdown('**Karakteristik Mahasiswa yang Lulus:**')
    st.write('1. Mahasiswa yang masih single')
    st.write('2. Penerima beasiswa')
    st.write('3. Memiliki umur di bawah 30 tahun')
    st.write('4. Mengambil lebih dari 5 sks')
    st.write('5. Memiliki IP di atas 12.50')
