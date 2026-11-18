# ✅ خطوات نشر الـ FULL BACKEND على Vercel الآن

## 1. ادفع التغييرات (مهم جداً)

```bash
cd /home/user/QuantumPilot-AI
git push origin main
```

## 2. بعد الدفع، اذهب إلى Vercel Dashboard

1. افتح مشروعك: https://vercel.com/ahmedzogly/quantumpilot-ai (أو ابحث عنه)
2. اضغط على **Deployments** tab
3. اضغط **Redeploy** على آخر commit (e7b1e10 أو الأحدث)

## 3. أضف المتغيرات البيئية (ضروري للعمل الحقيقي)

اذهب إلى:
**Settings → Environment Variables**

أضف هذه المتغيرات:

| Name            | Value                              | Environment |
|-----------------|------------------------------------|-------------|
| `IBM_TOKEN`     | مفتاح IBM Cloud API الخاص بك       | Production + Preview |
| `IBM_CRN`       | CRN الخاص بك (crn:v1:...)          | Production + Preview |
| `HF_TOKEN`      | (اختياري) مفتاح HuggingFace        | Production |
| `NEXT_PUBLIC_API_URL` | https://quantumpilot-ai.vercel.app | Production |

## 4. تحقق بعد النشر

افتح هذه الروابط:

- `https://quantumpilot-ai.vercel.app/api/v1/health`
  يجب أن ترى:
  ```json
  {
    "mode": "full",
    "neuralucb": true,
    "real_ibm": true
  }
  ```

- جرب زر **Execute Real** في الواجهة
- جرب Copilot بالعربية

## 5. إذا فشل البناء (شائع جداً)

بسبب حجم `torch` + `qiskit-ibm-runtime`:

**الحلول:**
- استخدم **Vercel Pro** (يسمح بـ 3008MB)
- أو استخدم **Railway** أو **Render** للـ backend الكامل
- أو ارجع للنسخة الخفيفة مؤقتاً

## ملاحظات مهمة

- الـ Full Backend الآن يحاول التحميل من `backend/app/`
- NeuralUCB الحقيقي سيعمل (`reward_net_deep.pt`)
- التنفيذ الحقيقي على IBM سيعمل **فقط** إذا وضعت التوكنات الصحيحة
- قد يأخذ البناء وقت طويل أو يفشل على الخطة المجانية

