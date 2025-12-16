import streamlit as st
import random
from application import get_temperature,get_news,news_summarizer,smart_plan

def get_random_quote():
    quotes = [
        "The sun is a daily reminder that we too can rise again from the darkness, that we too can shine our own light.",
        "Write it on your heart that every day is the best day in the year.",
        "I get up every morning and it’s going to be a great day. You never know when it’s going to be over, so I refuse to have a bad day.",
        "Today’s goals: Coffee and kindness. Maybe two coffees, and then kindness.",
        "An early-morning walk is a blessing for the whole day.",
        "Morning is an important time of day because how you spend your morning can often tell you what kind of day you are going to have.",
        "Lose an hour in the morning, and you will spend all day looking for it.",
        "When you arise in the morning, think of what a precious privilege it is to be alive – to breathe, to think, to enjoy, to love."
    ]
    return random.choice(quotes)

def get_random_image():
    image_urls = [
        "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8",
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
        "https://images.unsplash.com/photo-1494548162494-384bba4ab999",
        "https://images.unsplash.com/photo-1520038410233-7141be7e6f97",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
    ]
    return random.choice(image_urls)



def home_page():
    st.title("Your Morning Buddy 🌞")
    st.markdown("---")
    st.subheader("A thought of the day")
    st.info(f"{get_random_quote()}")
    st.image(get_random_image(),caption="A beautiful morning to start your day",use_container_width=True)
    st.markdown("---")
    st.write("Use sidebar to get new updates")

def wether_news_city():
    st.header("Get weather information of your city")
    city=st.text_input("Enter your city name :")
    if st.button("Fetch Weather"):
        if city:
            with st.spinner("The AI is writing .... Wait for a while"):
                try:
                    details=get_temperature(city)
                    if "Error" in details or "fail" in details or "API key" in details:
                        st.error(f"An error occure {details}")
                    else:
                        st.subheader(f"Your {city} weather detail:")
                        st.success(f"{details}")
                except Exception as e:
                    st.error(f"An error occurred {e}")
        else:
            st.error("Please write city name.")


def news_interest():
    st.header("Get news based on your interest")
    interest=st.text_input("Enter your area of interest (e.g. Technology, Science, Trading, Teaching, AI, Computer)")
    if st.button("Fetch News"):
        if interest:
            with st.spinner("The AI is writing .... Wait for a while"):
                try:
                    article = get_news(interest)
                    if "Error" in article or "fail" in article or "API key" in article:
                        st.error(f"An error occure {article}")
                    elif not article:
                        st.warning("No news found.")
                    else:
                        st.subheader(f"Articles based on your interest : {interest}")
                        titles=[]
                        url=[]
                        image_url=[]
                        for i in article:
                            titles.append(i['title'])
                            url.append(i['url'])
                            image_url.append(i['urlToImage'])
                        col1,col2,col3,col4,col5=st.columns(5)
                        with col1:
                            st.subheader(titles[0])
                            st.markdown("---")
                            st.image(image_url[0])
                            st.markdown("---")
                            st.write("Read full article here ",url[0])
                            st.markdown("---")
                            st.write(news_summarizer(url[0]))
                        with col2:
                            st.subheader(titles[1])
                            st.markdown("---")
                            st.image(image_url[1])
                            st.markdown("---")
                            st.write("Read full article here ", url[1])
                            st.markdown("---")
                            st.write(news_summarizer(url[1]))
                        with col3:
                            st.subheader(titles[2])
                            st.markdown("---")
                            st.image(image_url[2])
                            st.markdown("---")
                            st.write("Read full article here ", url[2])
                            st.markdown("---")
                            st.write(news_summarizer(url[2]))
                        with col4:
                            st.subheader(titles[3])
                            st.markdown("---")
                            st.image(image_url[3])
                            st.markdown("---")
                            st.write("Read full article here ", url[3])
                            st.markdown("---")
                            st.write(news_summarizer(url[3]))
                        with col5:
                            st.subheader(titles[4])
                            st.markdown("---")
                            st.image(image_url[4])
                            st.markdown("---")
                            st.write("Read full article here ", url[4])
                            st.markdown("---")
                            st.write(news_summarizer(url[4]))

                except Exception as e:
                    st.error(f"An error occurred {e}")
        else:
            st.error("Please write interest.")
def smart_planner():
    st.header("Your Smart Planner Day")
    city=st.text_input("Enter your city name :")

    if st.button("Let's Plan"):
        if city:
            with st.spinner("The AI is writing .... Wait for a while"):

                plan=smart_plan(city)
                st.subheader(plan)
                st.success("Have a nice day!!")
        else:
            st.error("Please write city name.")



st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page_option=st.sidebar.radio("Choose Page : ",("Home","Get Weather of your city","News by Interest","Smart Planner"))
st.sidebar.markdown("---")



#page routing
if page_option=="Home":
    home_page()
elif page_option=="Get Weather of your city":
    wether_news_city()
elif page_option=="News by Interest":
    news_interest()
elif page_option=="Smart Planner":
    smart_planner()

























