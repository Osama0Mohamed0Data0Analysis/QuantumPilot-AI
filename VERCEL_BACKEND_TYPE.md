# Vercel Backend Type - QuantumPilot AI

## السؤال: هل Vercel يشغّل الباك اند الكامل أم الخفيف؟

### الإجابة النهائية:
**Vercel يشغّل النسخة الخفيفة فقط (Lightweight Mock Backend)**

### التفاصيل الدقيقة:

| العنصر                    | ما يُنشر على Vercel                  | الباك اند الكامل (Full)          |
|---------------------------|-------------------------------------|----------------------------------|
| **ملف الـ API**           | `api/index.py`                      | `backend/app/main.py`            |
| **الإعداد في vercel.json**| `@vercel/python` على `api/index.py` | غير مستخدم على Vercel            |
| **الحجم / المتطلبات**     | خفيف جداً (FastAPI + requests فقط) | ثقيل (torch + qiskit-ibm-runtime + mitiq) |
| **تنفيذ IBM حقيقي**       | **محاكاة فقط** (is_simulated: True) | حقيقي عبر QiskitRuntimeService  |
| **NeuralUCB الحقيقي**     | محاكاة + خطط ثابتة                 | نموذج حقيقي (reward_net_deep.pt) |
| **Space Weather**         | يعمل (NOAA live أو fallback)        | يعمل كاملاً                      |
| **Copilot**               | يعمل (قواعد + regex)                | يعمل + يمكن ربطه بالنموذج        |
| **Job Monitor**           | محاكاة تقدم بناءً على hash         | يتصل بـ IBM حقيقي                |
| **Execute / Real**        | يرجع QUEUED وهمي                    | يرسل مهمة حقيقية لـ IBM         |

### لماذا يستخدم Vercel النسخة الخفيفة؟

1. **قيود Vercel Python Runtime**:
   - Serverless + وقت تنفيذ محدود
   - لا يدعم تثبيت torch + qiskit-ibm-runtime بسهولة
   - يتطلب حجم صغير جداً للـ function

2. **التصميم الأصلي للمشروع**:
   - `api/index.py` مصمم خصيصاً لـ Vercel (خفيف + يعمل بدون توكنات ثقيلة)
   - الباك اند الكامل موجود في `backend/` للـ Docker والتطوير المحلي

3. **النتيجة على Vercel**:
   - الواجهة الأمامية كاملة (Frontend)
   - الـ API يعمل بشكل ممتاز للعرض التوضيحي (Demo)
   - كل الميزات الرئيسية تعمل (Copilot, Charts, Cost, Job Monitor)
   - **لكن** التنفيذ الحقيقي على IBM هو "محاكاة"

### كيف تعرف أنك على الخفيف أم الكامل؟

عندما تشغّل المنصة:

- **على Vercel**:
  - `is_simulated: true` في معظم الردود
  - Job ID يبدأ بـ `job-` أو mock
  - لا يحتاج IBM Token حقيقي

- **على Docker / Codespaces / Local Full**:
  - يحاول الاتصال بـ `QiskitRuntimeService`
  - يستخدم النموذج الحقيقي `reward_net_deep.pt`
  - `is_simulated: false` عند نجاح الاتصال

### الوضع الحالي بعد الإصلاحات (2026-07-26)

- ✅ تم إصلاح الـ routing في `vercel.json`
- ✅ النسخة الخفيفة تعمل بشكل ممتاز محلياً
- ✅ عند إعادة النشر على Vercel → سيعمل **الخفيف فقط**

### كيف تشغّل الباك اند الكامل؟

```bash
# الطريقة الموصى بها
docker-compose up --build

# أو محلياً
cd backend
uvicorn app.main:app --port 8000
```

### ملخص سريع للمستخدم

**Vercel = النسخة الخفيفة (ممتازة للعرض والتجربة)**  
**Docker / Codespaces = النسخة الكاملة (للتنفيذ الحقيقي على IBM)**

هذا التصميم مقصود وصحيح لأسباب تقنية.
