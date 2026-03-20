# DAY 3 RESTORED: THE TECH INTERVIEW BOT
print("--- 🤖 GOOGLE/DELOITTE INTERVIEW SIMULATOR ---")

# 1. Storing data in Lists
questions = [
    "What is the extension of a Python file?",
    "Which keyword is used for a loop?",
    "What symbol is used for comments?"
]
answers = [".py", "for", "#"]

score = 0

# 2. The Interview Loop
for i in range(len(questions)):
    print(f"\nQuestion {i+1}: {questions[i]}")
    user_input = input("Your Answer: ").lower().strip()
    
    if user_input == answers[i]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answers[i]}")

# 3. Final Result
print(f"\n--- FINAL SCORE: {score}/3 ---")
if score == 3:
    print("🌟 RESULT: SELECTED! Welcome to Google Hyderabad!")
else:
    print("📚 RESULT: Keep practicing your basics!")