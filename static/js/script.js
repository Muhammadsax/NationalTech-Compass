// دالة إظهار إشعارات التوست الاحترافية
function showToast(message) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = "bg-academic-blue text-white px-6 py-4 rounded-xl shadow-2xl flex items-center gap-4 animate-fade-in border-r-4 border-tech-blue pointer-events-auto transition-all duration-500 font-['Tajawal']";
    toast.innerHTML = `
        <span class="flex-grow text-sm font-medium">${message}</span>
        <button class="text-white/70 hover:text-white transition-colors">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
    `;
    
    // إغلاق يدوي عند الضغط على الزر
    toast.querySelector('button').onclick = () => {
        toast.classList.add('opacity-0', '-translate-y-4');
        setTimeout(() => toast.remove(), 500);
    };

    container.appendChild(toast);

    // إغلاق تلقائي بعد 5 ثوانٍ
    setTimeout(() => {
        if (toast.parentElement) {
            toast.classList.add('opacity-0', '-translate-y-4');
            setTimeout(() => toast.remove(), 500);
        }
    }, 5000);
}

async function submitAnswers() {
    // 1. جمع الإجابات لـ 20 سؤالاً
    const answers = [];
    for (let i = 1; i <= 20; i++) {
        const val = document.querySelector(`input[name="q${i}"]:checked`)?.value;
        if (val) answers.push(val);
    }

    if (answers.length < 20) { 
        return showToast("يرجى الإجابة على جميع الأسئلة (20 سؤالاً) لضمان دقة النتيجة!"); 
    }

    // 2. إظهار واجهة التحليل (التأثير البصري)
    document.getElementById('navigation-controls').classList.add('hidden');
    const mainContent = document.getElementById('main-content');
    mainContent.innerHTML = `
        <div class="flex flex-col items-center justify-center py-32 bg-white rounded-3xl shadow-xl animate-fade-in">
            <div class="relative w-24 h-24 mb-8">
                <div class="absolute inset-0 rounded-full border-4 border-tech-blue/20"></div>
                <div class="absolute inset-0 rounded-full border-4 border-t-tech-blue animate-spin"></div>
            </div>
            <p class="text-2xl font-bold text-academic-blue font-['Cairo'] mb-2">جاري تحليل بوصلتك التقنية</p>
            <p class="text-gray-500 animate-pulse font-['Tajawal']">خوارزمياتنا تحدد مسارك الأنسب الآن...</p>
        </div>`;

    // 3. إرسال البيانات للسيرفر
    const response = await fetch('/get-result', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ answers: answers })
    });
    
    const data = await response.json();

    // 4. تخزين البيانات مؤقتاً والانتقال لصفحة النتيجة
    setTimeout(() => {
        localStorage.removeItem('quizDraft');
        sessionStorage.setItem('resultData', JSON.stringify(data));
        window.location.href = '/result';
    }, 2500); 
}