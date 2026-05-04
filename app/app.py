import streamlit as st
import os, json
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# تنظیم صفحه
st.set_page_config(
    page_title="تحلیل پوستر نمایشگاه تهران",
    page_icon="🎨",
    layout="wide",
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
POSTERS_DIR = os.path.join(BASE_DIR, "posters")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

# فونت بزرگ + راست چین
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;600;800&display=swap');

.rtl-text {
    direction: rtl;
    text-align: right;
    font-family: 'Vazirmatn', sans-serif !important;
}


/* عنوان اصلی */
.main-header {
    font-size:46px !important;
    font-weight:900 !important;
    color:#004D68;
    text-align:right !important;
    padding-right:20px;
}

/* تیترهای بخش */
h2, h3, .element-container h3 {
    text-align:right !important;
}

/* جدول دیتا */
.dataframe td, .dataframe th {
    text-align:right !important;
    direction: rtl !important;
}

/* شماره سطر بیاد راست */
thead tr th:first-child,
tbody tr th {
    text-align:right !important;
}

</style>
""", unsafe_allow_html=True)



st.markdown('<p class="main-header">سامانه تحلیل پوسترهای نمایشگاه بین‌المللی تهران</p>', unsafe_allow_html=True)
st.divider()

# لیست پوسترها
posters = [p for p in os.listdir(POSTERS_DIR) if p.lower().endswith(('.jpg','.png','.jpeg'))]

selected_poster = st.sidebar.selectbox(
"انتخاب پوستر",
posters
)

col1, col2 = st.columns([1.1,1])

with col1:
    st.image(os.path.join(POSTERS_DIR,selected_poster), width="stretch")

poster_name = os.path.splitext(selected_poster)[0]

json_file = os.path.join(RESULTS_DIR,f"{poster_name}.json")
report_img = os.path.join(RESULTS_DIR,f"{poster_name}_report.png")
focal_img = os.path.join(RESULTS_DIR,f"{poster_name}_focal.png")

if os.path.exists(json_file):
    with open(json_file,"r",encoding="utf-8") as f:
        data=json.load(f)
else:
    st.error("فایل تحلیل پیدا نشد")
    st.stop()

# ترجمه فارسی
translation = {

"file_name":"نام فایل",
"dominant_colors":"رنگ‌های غالب",
"color_harmony":"هارمونی رنگ",
"color_temperature":"دمای رنگ",
"color_emotion":"احساس رنگ",
"composition_balance":"تعادل ترکیب‌بندی",
"visual_complexity":"پیچیدگی بصری"

}

values_translate={

"mixed":"ترکیبی",
"warm":"گرم",
"cool":"سرد",
"neutral":"خنثی",
"energetic / exciting":"هیجانی / پرانرژی",
"calm / professional":"آرام / حرفه‌ای",
"balanced":"متعادل",
"slightly unbalanced":"نیمه متعادل",
"unbalanced":"نامتعادل",
"minimalist":"مینیمال",
"moderate":"متوسط",
"complex":"پیچیده"

}

# فارسی سازی داده
persian_data={}

for k,v in data.items():

    key=translation.get(k,k)

    if isinstance(v,str):
        v=values_translate.get(v,v)

    persian_data[key]=v


with col2:

    st.subheader("خلاصه تحلیل")

    rows = ""
    for i, (k, v) in enumerate(persian_data.items(), 1):
        rows += f"""
    <tr>
    <td style="padding:8px;border:1px solid #ddd;text-align:center;font-weight:bold;">{i}</td>
    <td style="padding:8px;border:1px solid #ddd">{k}</td>
    <td style="padding:8px;border:1px solid #ddd">{v}</td>
    </tr>
    """

    table_html = f"""
    <table style="width:100%;border-collapse:collapse;font-size:18px;direction:rtl;text-align:right">
    <thead>
    <tr style="background-color:#004D68;color:white;">
    <th style="padding:8px;border:1px solid #ddd;text-align:center;width:10%;">ردیف</th>
    <th style="padding:8px;border:1px solid #ddd;width:30%;">شاخص</th>
    <th style="padding:8px;border:1px solid #ddd;width:60%;">نتیجه</th>
    </tr>
    </thead>
    <tbody>
    {rows}
    </tbody>
    </table>
    """

    st.markdown(table_html, unsafe_allow_html=True)


    # رنگ‌های غالب
    st.subheader("رنگ‌های غالب")

    colors=data.get("dominant_colors",[])

    if colors:

        fig,ax=plt.subplots(figsize=(6,1))

        for i,c in enumerate(colors):

            # تبدیل 0-255 به 0-1
            c=[x/255 for x in c]

            rect=plt.Rectangle((i,0),1,1,color=c)
            ax.add_patch(rect)

        ax.set_xlim(0,len(colors))
        ax.set_ylim(0,1)
        ax.axis("off")

        st.pyplot(fig)

# گزارش تصویری
st.subheader("گزارش تصویری")

c1, c2 = st.columns(2)

with c1:
    if os.path.exists(report_img):
        st.markdown("<div class='rtl-text'>گزارش تحلیل</div>", unsafe_allow_html=True)
        st.image(report_img, use_container_width=True)

with c2:
    if os.path.exists(focal_img):
        st.markdown("<div class='rtl-text'>کانون توجه</div>", unsafe_allow_html=True)
        st.image(focal_img, use_container_width=True)


# امتیاز طراحی
st.subheader("امتیاز کلی طراحی")

score_color={"balanced":20,"slightly unbalanced":10,"unbalanced":5}
score_complexity={"minimalist":20,"moderate":15,"complex":10}

val=score_color.get(data.get("composition_balance",""),10)
val+=score_complexity.get(data.get("visual_complexity",""),10)

design_score=60+val

st.progress(design_score/100)

st.success(f"امتیاز طراحی: {design_score} از 100")


st.download_button(

"دانلود فایل تحلیل",
data=json.dumps(data,ensure_ascii=False,indent=2),
file_name=f"{poster_name}_analysis.json",
mime="application/json"

)

st.divider()

st.markdown(
"<p style='text-align:center;color:gray'>داشبورد تحلیل پوستر — نسخه پژوهشی</p>",
unsafe_allow_html=True
)
