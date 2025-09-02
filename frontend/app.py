import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "interview_type" not in st.session_state:
    st.session_state.interview_type = ""
if "messages" not in st.session_state:
    st.session_state.messages = []

# Main title
st.title("🎯 AI Interview Coach")

# Check if interview has started
if not st.session_state.interview_started:
    # Show initial interface
    st.markdown("### Get ready for your next interview with AI-powered coaching")
    
    # Dropdown menu for interview types
    interview_type = st.selectbox(
        "Select Interview Type:",
        options=["Data Science", "HR Interview", "Software Engineering"],
        index=0,
        help="Choose the type of interview you want to practice"
    )
    
    # Display selected option
    st.write(f"You selected: **{interview_type}**")
    
    # Submit button
    if st.button("Start Interview Coaching", type="primary"):
        st.session_state.interview_started = True
        st.session_state.interview_type = interview_type
        st.session_state.messages = [
            {"role": "assistant", "content": f"Welcome to your {interview_type} interview session! I'm your AI interview coach. Let's start with some questions. Tell me about yourself."}
        ]
        st.rerun()

else:
    # Show chat interface
    st.markdown(f"### {st.session_state.interview_type} Interview Session")
    
    # Add a back button
    if st.button("← Back to Selection", type="secondary"):
        st.session_state.interview_started = False
        st.session_state.messages = []
        st.rerun()
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your response here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response (placeholder for now)
        ai_response = f"Thank you for sharing that. Let me ask you another {st.session_state.interview_type.lower()} related question..."
        
        # Add AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        
        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(ai_response)
    


