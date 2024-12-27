import streamlit as st

# Define questions and options
questions = [
    {"question": "How do you feel when you wake up?",
     "options": ["Excited", "Tired", "Worried", "Neutral"]},
    {"question": "How do you usually spend your free time?",
     "options": ["Hanging out with friends", "Sleeping", "Overthinking", "Reading or relaxing"]},
    {"question": "How do you handle stress?",
     "options": ["Stay optimistic", "Feel overwhelmed", "Panic", "Stay calm"]},
    {"question": "What describes your current mood?",
     "options": ["Happy", "Sad", "Anxious", "Calm"]},
    {"question": "How do you feel about your future?",
     "options": ["Hopeful", "Lost", "Scared", "Content"]},
    {"question": "What do you do when faced with a problem?",
     "options": ["Find a solution", "Avoid it", "Worry about it", "Analyze it calmly"]},
    {"question": "How would you describe your social life?",
     "options": ["Very active", "Lonely", "Stressful", "Balanced"]},
    {"question": "How often do you feel energetic during the day?",
     "options": ["Very often", "Rarely", "Sometimes", "Moderately"]},
    {"question": "What helps you relax the most?",
     "options": ["Spending time with loved ones", "Sleeping alone", "Distracting yourself", "Meditating"]},
    {"question": "What do you think about before going to bed?",
     "options": ["Good memories", "Regrets", "What could go wrong", "Nothing much"]},
]

# Define moods and their corresponding scores
mood_scores = {
    "Happy": 0,
    "Sad": 0,
    "Anxious": 0,
    "Calm": 0,
}

# Suggestions for each mood
mood_suggestions = {
    "Happy": "Keep spreading positivity! Try a creative activity today.",
    "Sad": "It's okay to feel down sometimes. Talk to someone you trust or journal your thoughts.",
    "Anxious": "Take a deep breath. Try meditation, light exercise, or listening to calming music.",
    "Calm": "Enjoy the peace. Consider activities like yoga or reading to maintain your calmness.",
}

# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# Display title
st.title("Psychological Mood Analyzer")
st.write("Answer each question honestly to get a personalized mood analysis!")

# Get the current question index
current_index = st.session_state.current_question

# Display the current question and its options
if current_index < len(questions):
    question = questions[current_index]
    st.write(f"**Q{current_index + 1}: {question['question']}**")
    answer = st.radio("Choose an option:", question["options"], key=current_index)

    # Next button
    if st.button("Next"):
        # Save the selected answer
        st.session_state.answers.append(answer)
        # Move to the next question
        st.session_state.current_question += 1
        st.rerun()
else:
    # All questions answered
    st.write("### Thank you for completing the questions!")

    # Calculate mood scores
    for answer in st.session_state.answers:
        if answer in ["Excited", "Hanging out with friends", "Stay optimistic", "Hopeful", "Find a solution",
                      "Very active", "Very often", "Spending time with loved ones", "Good memories"]:
            mood_scores["Happy"] += 1
        elif answer in ["Tired", "Sleeping", "Feel overwhelmed", "Sad", "Lost", "Avoid it", "Lonely", "Rarely",
                        "Sleeping alone", "Regrets"]:
            mood_scores["Sad"] += 1
        elif answer in ["Worried", "Overthinking", "Panic", "Anxious", "Scared", "Worry about it", "Stressful",
                        "Sometimes", "Distracting yourself", "What could go wrong"]:
            mood_scores["Anxious"] += 1
        elif answer in ["Neutral", "Reading or relaxing", "Stay calm", "Calm", "Content", "Analyze it calmly",
                        "Balanced", "Moderately", "Meditating", "Nothing much"]:
            mood_scores["Calm"] += 1

    # Determine the dominant mood
    mood = max(mood_scores, key=mood_scores.get)

    # Display the result
    st.subheader(f"Your mood is: {mood}")
    st.write(mood_suggestions[mood])

    # Reset button
    if st.button("Restart"):
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.experimental_rerun()
