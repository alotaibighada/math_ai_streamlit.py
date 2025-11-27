import streamlit as st

# عنوان البرنامج
st.title("برنامج Math AI")

# قسم لإدخال البيانات
st.header("إدخال البيانات")

num1 = st.number_input("أدخل الرقم الأول:", value=0)
num2 = st.number_input("أدخل الرقم الثاني:", value=0)

# اختيار العملية
operation = st.selectbox("اختر العملية:", ["جمع", "طرح", "ضرب", "قسمة"])

# زر الحساب
if st.button("احسب"):
    if operation == "جمع":
        result = num1 + num2
    elif operation == "طرح":
        result = num1 - num2
    elif operation == "ضرب":
        result = num1 * num2
    elif operation == "قسمة":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "لا يمكن القسمة على صفر"
    st.success(f"النتيجة: {result}")

# إضافة نص توضيحي أو تعليمات
st.info("هذا البرنامج يقوم بالعمليات الحسابية الأساسية على الرقمين المدخلين.")
