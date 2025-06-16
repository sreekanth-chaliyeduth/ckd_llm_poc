# CKD LLM PoC

A small proof-of-concept exploring how to quickly prototype and test LLM-based healthcare applications. Built to experiment with Playwright for testing and Cursor for rapid development. Uses the [Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/aryannandanwar/ckdchronic-kidney-disease-dataset-with-stages) from Kaggle.

---

## 🎯 What I Was Exploring
- How to quickly prototype healthcare AI applications
- Using Playwright for UI/API testing
- Cursor's capabilities for rapid development
- Basic LLM integration patterns
- Simple testing frameworks for AI systems

---

## ✅ What This PoC Includes
- FastAPI backend for patient data & prediction
- Basic HTML UI for data input
- Mock LLM responses (no real API yet)
- Simple testing setup:
  - Playwright for UI/API testing
  - Basic LLM evaluation metrics
  - Test matrix for CKD scenarios
  - Automated report generation
- `run_tests.sh` script to run everything

---

## 🧪 Testing & Evaluation Focus
- **UI Testing with Playwright**
  - Basic form validation
  - Simple error handling
  - Response time monitoring

- **API Testing**
  - Endpoint validation
  - Data model testing
  - Error scenarios

- **LLM Evaluation**
  - Basic prediction accuracy
  - Response time tracking
  - Simple explanation quality
  - Risk factor identification

- **Test Matrix**
  - Basic patient scenarios
  - Missing data handling
  - Simple medical conditions

---

## 🧱 Project Structure
```
backend/     # FastAPI + mock LLM + dataset
frontend/    # HTML input form for patient prediction
metrics/     # LLM evaluation scripts and reports
tests/       # Playwright tests using Page Object Model
reports/     # Generated test and evaluation reports
run_tests.sh # Runs the entire flow (API, eval, tests)
README.md    # You're here
```

---

## 🚀 Quickstart

### 1. Setup
```bash
pip install uv
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
playwright install
```

### 2. Run Everything
```bash
chmod +x run_tests.sh
./run_tests.sh
```

It will:
- Start FastAPI backend
- Run mock model evaluation
- Run UI and API tests
- Show reports

---

## 📊 Output Summary
- ✅ LLM Evaluation CSV: `reports/llm_evaluation.csv`
- ✅ Evaluation Summary: `reports/llm_evaluation_summary.json`
- ✅ Classification Report: `reports/llm_classification_report.json`
- ✅ Test Report (UI/API): `reports/playwright-report.html`
- ✅ Coverage Report: `reports/htmlcov/index.html`
- ✅ Eval Dashboard: `reports/llm_evaluation_report.html`

---

## 🔮 Future Plans
- Add more test scenarios
- Try real LLM API integration
- Add more medical conditions
- Improve evaluation metrics
- Add basic clinical validation
- Try EHR system integration

---

## ⚠️ Final Note
This is **just a prototype** built to explore:
1. How to quickly build and test healthcare AI applications
2. Playwright's capabilities for UI/API testing
3. Cursor's potential for rapid prototyping
4. Basic LLM integration patterns

Built this over a weekend (about 3 hours total) to see how quickly we could get something working. It's far from production-ready, but I'm happy with how it turned out as a starting point. The combination of Playwright for testing and Cursor for development made it surprisingly quick to get something functional.

Not intended for any real medical use. Just a learning exercise in rapid prototyping and testing of AI systems.

---

## 🎓 Learning Resources
- [Playwright Testing](https://playwright.dev/python/docs/intro)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [LLM Evaluation Best Practices](https://arxiv.org/abs/2310.19736)
- [Healthcare AI Testing Guidelines](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-software-medical-device)
