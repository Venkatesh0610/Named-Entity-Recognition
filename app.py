import streamlit as st
from spacy import displacy 
import spacy
import wikipedia as w

nlp=spacy.load("en_core_web_sm")
global text

st.title("Wikipedia Scrapper")
text=st.text_area("Enter the text to scrap")
def analyze_text(text):
    return nlp(text)

def main():

    menu=['Scrapper','NER']
    choice= st.sidebar.selectbox('Menu',menu)

    try:
        if choice=="Scrapper":
           
            st.subheader("Please click to scrap the text from wikipedia")
            if st.button('Scrapper'):
                x = st.text_area(w.summary(text))
                
 
    
        if choice=="NER":
            st.title("Named Entity Recognition")
            st.subheader("Please click NER to extract the entities in the text")
                
            if st.button('NER'):
                
                x = w.summary(text)
                docx = analyze_text(x)
                st.subheader("Named Entity Recognition")
                html = displacy.render(docx,style="ent")
                html = html.replace("\n\n","\n")
                st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)
    except:
        st.subheader("Enter the valid name for scrapping..")
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""  
    
if __name__=='__main__':
    main()