import streamlit as st
import matplotlib.pyplot as plt

# Define personalized questions and options
questions = [
    {"question": "What is one thing you look forward to every morning?",
     "options": ["A warm cup of coffee", "Going for a walk", "Listening to music", "Nothing in particular"]},
    {"question": "How do you usually unwind after a long day?",
     "options": ["Watching my favorite show", "Reading a book", "Spending time with family",
                 "Scrolling through social media"]},
    {"question": "When faced with a challenge, what is your first instinct?",
     "options": ["Ask for help", "Try to solve it myself", "Avoid thinking about it", "Analyze it thoroughly"]},
    {"question": "How do you feel when you think about your relationships?",
     "options": ["Grateful for my friends and family", "Lonely and disconnected",
                 "Overwhelmed by social obligations", "Content with my circle"]},
    {"question": "What keeps you up at night?",
     "options": ["Exciting thoughts about the future",
                 "Worries about tomorrow",
                 "Regrets from the past",
                 "I sleep soundly"]},
    {"question": "What brings you joy during tough times?",
     "options": ["Talking to a loved one",
                 "Engaging in a hobby",
                 "Taking a break and relaxing",
                 "Finding humor in the situation"]},
    {"question": "How often do you take time for self-care?",
     "options": ["Daily",
                 "A few times a week",
                 "Rarely",
                 "Never"]},
    {"question": "What role does nature play in your life?",
     "options": ["I love being outdoors",
                 "I enjoy nature occasionally",
                 "I prefer staying indoors",
                 "I find nature calming but rarely visit"]},
    {"question": "How do you express your feelings when you're upset?",
     "options": ["Talk it out with someone",
                 "Write in a journal",
                 "Keep it to myself",
                 "Find creative outlets like art or music"]},
    {"question": "If you could change one thing about your daily routine, what would it be?",
     "options": ["Incorporate more exercise",
                 "Spend less time on screens",
                 "Make time for hobbies",
                 "Focus on mindfulness or meditation"]}
]

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'mood_score' not in st.session_state:
    st.session_state.mood_score = 0

# Display title
st.title("Personalized Mood Analyzer")
st.write("Answer each question honestly to get insights into your mood and well-being!")

# Get the current question index
current_index = st.session_state.current_question

# Calculate progress and cap it at 1.0 when finished
progress_value = min((current_index + 1) / len(questions), 1.0)
st.progress(progress_value)


# Define scoring for responses
def score_response(answer):
    positive_answers = [
        # Positive responses
        "A warm cup of coffee",
        "Going for a walk",
        "Listening to music",
        "Spending time with family"
        # Add more nuanced scoring if desired
    ]

    if answer in positive_answers:
        return 2  # Positive answer
    return -1  # Neutral or negative answer


# Display the current question and its options
if current_index < len(questions):
    question = questions[current_index]
    st.write(f"**Q{current_index + 1}: {question['question']}**")

    answer = st.radio("Choose an option:", question["options"], key=current_index)

    # Handle the Next button
    if st.button("Next"):
        # Save the selected answer
        st.session_state.answers.append(answer)
        st.session_state.mood_score += score_response(answer)

        # Move to the next question
        st.session_state.current_question += 1

        # Use st.rerun() to manually rerun the app
        st.rerun()

else:
    # All questions answered
    st.write("### Thank you for completing the questions!")

    # Determine mood based on score ranges
    mood = ""
    if st.session_state.mood_score > 10:
        mood = "Happy"
    elif st.session_state.mood_score > 0:
        mood = "Content"
    elif st.session_state.mood_score < -5:
        mood = "Sad"
    else:
        mood = "Neutral"

    st.write(f"### Your Mood: {mood}")

    # Visualize mood score
    fig, ax = plt.subplots()
    ax.bar(["Mood Score"], [st.session_state.mood_score], color="blue")
    ax.set_ylabel("Score")
    ax.set_title("Your Mood Score")

    # Annotate the bar with the score value
    ax.text(0, st.session_state.mood_score + 0.5, str(st.session_state.mood_score), ha='center')

    st.pyplot(fig)

    # Reset button with confirmation message (simple implementation)
    if st.button("Try Again"):
        # Reset the session state to start over
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.mood_score = 0

