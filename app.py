import streamlit as st
import pyttsx3

def main():
    st.title("🎙️ Voice Synthesizer")
    st.subheader("Transform Text into Speech Instantly")

    st.markdown(
        """
        Welcome to the **Voice Synthesizer App**, where you can:
        - Convert text into natural-sounding speech.
        - Customize the voice, speed, and volume.
        - Save the speech as an audio file.  
        Let's get started!
        """
    )

    # Text Input
    text = st.text_area("📝 Enter Text Below", placeholder="Type something you'd like to hear...")

    # Initialize pyttsx3 engine locally
    engine = pyttsx3.init()

    # Voice Selection
    voices = engine.getProperty('voices')
    voice_options = [voice.name for voice in voices]
    selected_voice = st.radio("🎙️ Choose a Voice", voice_options, index=0)

    # Set the selected voice
    selected_voice_id = [voice.id for voice in voices if voice.name == selected_voice][0]
    engine.setProperty('voice', selected_voice_id)

    # Speech Rate
    st.markdown("#### 🕒 Speech Speed")
    new_rate = st.slider("Adjust the words per minute", min_value=50, max_value=300, value=150)
    engine.setProperty('rate', new_rate)

    # Volume Control
    st.markdown("#### 🔊 Volume")
    new_volume = st.slider("Set the volume level", min_value=0.0, max_value=1.0, value=1.0)
    engine.setProperty('volume', new_volume)

    # Speak Button
    st.markdown("---")
    if st.button("🔊 Play Speech"):
        if text.strip():
            engine.say(text)
            engine.runAndWait()
            st.success("✅ Speech played successfully!")
        else:
            st.warning("⚠️ Please enter some text first.")

    # Save Audio Button
    st.markdown("---")
    if st.button("💾 Save Speech to File"):
        if text.strip():
            filename = st.text_input("Enter a Filename (e.g., output.mp3):", "output.mp3")
            if filename:
                engine.save_to_file(text, filename)
                engine.runAndWait()
                engine.endLoop()
                st.success(f"✅ Audio saved as `{filename}`!")
            else:
                st.warning("⚠️ Please enter a valid filename.")
        else:
            st.warning("⚠️ Please enter some text to save.")

    st.markdown("---")
    st.markdown("Built with using **Streamlit** and **pyttsx3**.")

if __name__ == "__main__":
    main()
