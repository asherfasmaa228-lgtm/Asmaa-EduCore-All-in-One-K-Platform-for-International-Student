import streamlit as st
import random
import time

# ==========================================
# 1. الإعدادات الجمالية والهوية البصرية (CSS)
# ==========================================
st.set_page_config(page_title="Asmaa-EduCore", page_icon="🚀", layout="centered")

st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: 800; text-align: center; color: #1E1E2F; }
    .subtitle { font-size: 15px; text-align: center; color: #6E6E80; margin-bottom: 25px; }
    .vocab-card { background-color: #F8F9FA; border-radius: 10px; padding: 12px; margin-bottom: 10px; border-left: 5px solid #4A90E2; }
    .halal-box { background-color: #E8F5E9; border: 2px solid #4CAF50; border-radius: 12px; padding: 15px; text-align: center; }
    .haram-box { background-color: #FFEBEE; border: 2px solid #F44336; border-radius: 12px; padding: 15px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌟 Asmaa-EduCore 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>The All-in-One Digital Ecosystem for International Students in South Korea</div>", unsafe_allow_html=True)

# ==========================================
# 2. قواعد البيانات المختصرة والذكية
# ==========================================
HARAM_INGREDIENTS = ['pork', 'pig', '돼지고기', '삼겹살', 'alcohol', 'gelatin', 'ham']

FOOD_DB = {
    "bibimbap": {"name": "بيبيومباب (أرز ومقبلات)", "halal": True, "note": "آمن تماماً - تأكد من عدم إضافة لحم غير حلال."},
    "samgyeopsal": {"name": "سامغيوبسال (لحم خنزير)", "halal": False, "note": "محرم قطعيًا - يعتمد كليًا على لحم الخنزير."},
    "ramen": {"name": "راميون (نودلز كورية)", "halal": False, "note": "احذر - يحتوي غالباً على مستخلصات دهن الخنزير في المرق."},
    "tteokbokki": {"name": "توكبوكي (كعك الأرز الحار)", "halal": True, "note": "آمن بشكل عام - طالما أن المرق نباتي أو سمك."}
}

KOREAN_VOCAB = [
    {"kor": "안녕하세요", "pron": "Annyeonghaseyo", "ar": "مرحباً", "cat": "👋 التحيات"},
    {"kor": "감사합니다", "pron": "Gamsahabnida", "ar": "شكراً جزيلاً", "cat": "👋 التحيات"},
    {"kor": "밥", "pron": "Bap", "ar": "طعام / أرز", "cat": "🍎 الأطعمة"},
    {"kor": "물", "pron": "Mul", "ar": "ماء", "cat": "🍎 الأطعمة"},
    {"kor": "학교", "pron": "Hakgyo", "ar": "مدرسة / جامعة", "cat": "🏫 الحياة اليومية"},
    {"kor": "친구", "pron": "Chingu", "ar": "صديق", "cat": "🏫 الحياة اليومية"}
]

# ==========================================
# 3. محرك التنقل الجانبي المستقر (Sidebar)
# ==========================================
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    selected_app = st.selectbox(
        "اختر التطبيق لتشغيله:",
        ["💡 أكاديمية اللغة الكورية", "🍳 فاحص الأطعمة الحلال", "⏱️ مؤقت بريك الذكي"]
    )
    st.divider()
    st.info("🎯 المطور: الطالبة أسماء\n\nتحدى الإمكانيات بالبرمجة من الهاتف.")

# ==========================================
# [التطبيق الأول]: الأكاديمية التعليمية والأغاني
# ==========================================
if selected_app == "💡 أكاديمية اللغة الكورية":
    st.header("📚 الأكاديمية الكورية التفاعلية")
    
    cat_filter = st.selectbox("تصفية حسب الفئة:", ["الكل", "👋 التحيات", "🍎 الأطعمة", "🏫 الحياة اليومية"])
    for item in KOREAN_VOCAB:
        if cat_filter == "الكل" or item["cat"] == cat_filter:
            st.markdown(f"<div class='vocab-card'><b>{item['kor']}</b> ({item['pron']})<br>الترجمة: {item['ar']}</div>", unsafe_allow_html=True)
            
    st.divider()
    st.subheader("🎵 تعلم عبر نصوص الأغاني (K-Pop)")
    st.code("보고 싶다 (Missing you / أشتاق إليك)\n이렇게 말하니까 더 보고 싶다\n너희 사진을 보고 있어도 보고 싶다", language="text")

# ==========================================
# [التطبيق الثاني]: فاحص الأطعمة الحلال والكاميرا
# ==========================================
elif selected_app == "🍳 فاحص الأطعمة الحلال":
    st.header("🔍 نظام فحص سلامة الأغذية")
    mode = st.radio("طريقة الفحص:", ["📋 اختر منتج من الداتا", "📸 فحص ذكي بالتقاط صورة"])
    
    if mode == "📋 اختر منتج من الداتا":
        food_key = st.selectbox("اختر المنتج الكوري:", list(FOOD_DB.keys()), format_func=lambda x: FOOD_DB[x]["name"])
        f = FOOD_DB[food_key]
        if f["halal"]:
            st.markdown(f"<div class='halal-box'><h3>✅ منتج حلال</h3><p><b>{f['name']}</b></p><p>{f['note']}</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='haram-box'><h3>❌ غير حلال</h3><p><b>{f['name']}</b></p><p>{f['note']}</p></div>", unsafe_allow_html=True)
            
    elif mode == "📸 فحص ذكي بالتقاط صورة":
        img = st.camera_input("التقط صورة لملصق المكونات")
        if img:
            with st.spinner("جاري فحص ومطابقة النصوص برمجياً..."):
                time.sleep(1.2)
                ocr_text = ["물", "설탕", "돼지고기", "밀가루"]  # محاكاة الكلمات الخارجة من الصورة
                matches = [i for i in ocr_text if i in HARAM_INGREDIENTS]
                st.success("تم المسح بنجاح!")
                if matches:
                    st.markdown(f"<div class='haram-box'><h3>⚠️ تحذير: منتج غير حلال!</h3><p>تم العثور على مكونات محرمة: <b>{', '.join(matches)}</b></p></div>", unsafe_allow_html=True)
                else:
                    st.markdown("<div class='halal-box'><h3>✅ المنتج آمن وحلال</h3><p>لم يتم رصد أي مكونات محرمة.</p></div>", unsafe_allow_html=True)

# ==========================================
# [التطبيق الثالث]: مؤقت بريك الذكي
# ==========================================
elif selected_app == "⏱️ مؤقت بريك الذكي":
    st.header("⏱️ مؤقت التركيز وتنظيم الوقت")
    c1, c2 = st.columns(2)
    with c1: study = st.number_input("المذاكرة (دقائق):", min_value=1, value=25)
    with c2: break_t = st.number_input("الراحة (دقائق):", min_value=1, value=5)
    
    if st.button("🚀 ابدأ المؤقت"):
        st.toast("تم تشغيل العداد!")
        bar = st.progress(0)
        for p in range(100):
            time.sleep(0.03)
            bar.progress(p + 1)
        st.balloons()
        st.success(f"🎉 أحسنتِ! انتهت جلسة التركيز. خذي بريك {break_t} دقائق.")
