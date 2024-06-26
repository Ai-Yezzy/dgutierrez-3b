import streamlit as st

def show_about_me():
    st.markdown("# ABOUT ME")
    st.markdown("""
    Hey there! 👋 I'm a third-year BSIS student with a passion for technology and a love for exploring new ideas. When I'm not buried in code or studying, you'll often find me on the basketball court, strumming my guitar, or lost in the world of music. These hobbies are not just pastimes for me; they are avenues for relaxation and creative expression.
    """)

    st.markdown("---")

    st.image("pages/about_me_pp.jpg")
    st.markdown("""
    Photo by [Your Name](https://example.com) on [Unsplash](https://unsplash.com)
    """)

    st.markdown("---")

    with st.expander("More about me"):
        st.markdown("""
        My journey in BSIS has been filled with exciting challenges and rewarding experiences. I'm particularly interested in exploring machine learning applications and developing solutions that make a difference. Learning about AI and its real-world applications has been a fascinating part of my academic journey so far.

        ### Personal Interests

        - **Basketball: I love basketball and enjoy playing both in friendly games with friends and in competitive matches.
        - **Music: I have a wide-ranging taste in music, from classic rock to modern pop. Music is always with me, whether I'm studying or relaxing.

        ### Future Goals

       I am excited to keep expanding my knowledge and skills in information systems. I aim to utilize my expertise to make significant contributions to the tech industry and beyond.
        """)

    st.markdown("---")

    st.info("Connect with me on [Facebook](https://www.facebook.com/dex.pog)")
    st.info("Visit my personal website [here](https://www.facebook.com/dex.pog)")

# Main function to run the app
def main():
    show_about_me()

if __name__ == "__main__":
    main()
