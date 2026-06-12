from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# منطق الحساب
MAJORS_DATA = {
    "software": {
        "name": "هندسة البرمجيات (Software Engineering)",
        "reason": "لديك قدرة عالية على التحليل وبناء الأنظمة من الصفر، وتهتم بدورة حياة البرمجيات بالكامل.",
        "skills": "تحليل المتطلبات، البرمجة الشيئية (OOP)، إدارة المشاريع، ضمان الجودة (QA).",
        "jobs": "مهندس برمجيات، محلل نظم، مطور ويب، مدير مشاريع برمجية.",
        "challenge": "لغز: نظام يحتاج لتخزين بيانات الموظفين مع منع التكرار وسرعة البحث، ما هي أفضل بنية بيانات (Data Structure) تستخدمها؟"
    },
    "mobile": {
        "name": "تطوير تطبيقات المتنقلة (Mobile Developer)",
        "reason": "تنجذب نحو ابتكار حلول محمولة تركز على تجربة المستخدم والتفاعل السريع مع التكنولوجيا السحابية.",
        "skills": "تصميم UI/UX، تقنيات Flutter/Kotlin، التكامل مع الحوسبة السحابية.",
        "jobs": "مطور تطبيقات ذكية، مطور أنظمة تجارة إلكترونية، أخصائي دعم سحابي.",
        "challenge": "تحدٍ: كيف تضمن أن تطبيقك يستهلك أقل قدر من بطارية الهاتف أثناء تحديث البيانات؟"
    },
    "internet": {
        "name": "مهندس تقنيات الإنترنت (Internet Technologies)",
        "reason": "تملك شغفاً ببناء المواقع والأنظمة التي تربط العالم عبر شبكة الويب العالمية.",
        "skills": "تطوير Full Stack، بروتوكولات الويب (HTTP/HTTPS)، أمن المعلومات.",
        "jobs": "مطور ويب متكامل، مهندس واجهات خلفية (Back-End)، إداري شبكات.",
        "challenge": "لغز: ما هو البروتوكول المسؤول عن تحويل اسم الموقع (مثل google.com) إلى عنوان IP؟"
    },
    "network": {
        "name": "مهندس شبكات الحاسوب (Network Engineer)",
        "reason": "تفضل العمل على البنية التحتية، ربط الأجهزة، وضمان استمرارية الاتصال والتدفق السلس للبيانات.",
        "skills": "تصميم الشبكات، إدارة السيرفرات، شهادات CCNA، أمن الشبكات.",
        "jobs": "مهندس شبكات، مدير أنظمة، أخصائي دعم فني، مبرمج شبكات.",
        "challenge": "تحدٍ: إذا فقدت مجموعة أجهزة الاتصال فجأة، ما هي أول أداة (Command) تستخدمها لفحص الاتصال بالخادم؟"
    },
    "cyber": {
        "name": "أمن المعلومات والأمن السيبراني (Cyber Security)",
        "reason": "لديك حس أمني عالٍ ورغبة في حماية الأنظمة من التهديدات الرقمية واكتشاف الثغرات.",
        "skills": "التشفير (Cryptography)، اختبار الاختراق، التحقيق الجنائي الرقمي.",
        "jobs": "محلل أمن سيبراني، مختبر اختراق، محقق جنائي رقمي.",
        "challenge": "لغز: وجدت فلاش ميموري (USB) ملقاة في ممر الشركة، ما هو التصرف الصحيح والآمن برأيك؟"
    },
    "ai": {
        "name": "علم البيانات والذكاء الاصطناعي (AI & Data Science)",
        "reason": "تستمتع بالتعامل مع البيانات الضخمة وبناء نماذج ذكية تحاكي القدرات البشرية وتتنبأ بالنتائج.",
        "skills": "التعلم الآلي (Machine Learning)، الإحصاء، تنقيب البيانات، لغة Python.",
        "jobs": "عالم بيانات، مهندس تعلم آلي، محلل بيانات ضخمة.",
        "challenge": "لغز: لديك نمط (2, 4, 8, 16)، ما هو الرقم القادم؟ وكيف يمكن للخوارزمية استنتاج هذه العلاقة؟"
    }
}

def calculate_major(answers):
    scores = {"software": 0, "mobile": 0, "internet": 0, "network": 0, "cyber": 0, "ai": 0}
    
    for ans in answers:
        if ans in scores:
            scores[ans] += 1
        
    top_major_key = max(scores, key=scores.get)
    return MAJORS_DATA[top_major_key]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/get-result', methods=['POST'])
def get_result():
    data = request.json
    answers = data.get('answers')
    
    # حساب النتيجة
    result_data = calculate_major(answers)
    
    return jsonify(result_data)

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')