#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np


# In[52]:


df=pd.read_csv("D:\\programs\\python\\class\\twitter-sentiment-analysis2\\train.csv", encoding="latin-1")


# In[53]:


df=df.sample(1000)


# In[54]:


df


# In[55]:


from textblob import TextBlob


# In[56]:


testimonial = TextBlob(" is so sad for my APL friend.............")
testimonial.sentiment


# In[57]:


df['SentimentText'].values


# In[58]:


subjectivity= []
polarity = []
for val in df['SentimentText']:
    testimonial = TextBlob(val)
    testimonial.sentiment
    subjectivity.append(testimonial.sentiment.subjectivity)
    polarity.append(testimonial.sentiment.polarity)


# In[59]:


df['polarity']=polarity


# In[60]:


df


# In[61]:


rating=[]
for i in df['polarity']:
    if i>0:
        rating.append(1)
    else:
        rating.append(0)


# In[62]:


df['rating']=rating


# In[63]:


df


# In[64]:


y=df['rating']
x=df['SentimentText']


# In[65]:


from sklearn.model_selection import train_test_split
# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(x,y,random_state=0,test_size=.20)


# In[66]:


print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# In[67]:


X_train.head()


# In[68]:


from sklearn.feature_extraction.text import CountVectorizer

# Fit the CountVectorizer to the training data
vect = CountVectorizer().fit(X_train)


# In[69]:


# transform the documents in the training data to a document-term matrix
X_train_vectorized = vect.transform(X_train)

X_train_vectorized


# In[ ]:


vect.get


# In[70]:


X_train_vectorized.toarray()


# In[71]:


from sklearn.linear_model import LogisticRegression

# Train the model
model = LogisticRegression()
model.fit(X_train_vectorized, y_train)


# In[72]:


from sklearn.metrics import roc_auc_score

# Predict the transformed test documents
predictions = model.predict(vect.transform(X_test))

print('AUC: ', roc_auc_score(y_test, predictions))


# In[73]:


a=model.predict(vect.transform(X_test))


# In[74]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,model.predict(vect.transform(X_test)))


# In[75]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,model.predict(vect.transform(X_test)))


# In[76]:


a=np.array(a)


# In[77]:


a


# In[78]:


print(len(a),len(X_test),X_test.shape)


# In[79]:


df1=pd.DataFrame(X_test)


# In[80]:


df1.reset_index(drop=True)


# In[81]:


df1['new']=a


# In[82]:


df1


# In[83]:


f=[]
for i in df1['new']:
    if i == 0:
        f.append('~Bad')
    else:
        f.append('~Good')


# In[84]:


df1['sentiment']=f


# In[85]:


df2=df1.drop(columns='new')


# In[86]:


final_df=df2.reset_index(drop=True)


# In[87]:


final_df


# In[89]:


import win32com.client 
import speech_recognition as sr


# In[91]:


i="yes"
a=[]
while (i=="yes"): 
    speaker = win32com.client.Dispatch("SAPI.SpVoice") 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hey, Tell me about your phone ? ")
        speaker.Speak("hey, Tell me about your phone ?  ")
        print("Listining now ..... ")
        #print("Speak now :")
        #speaker.Speak("Speak now :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            a.append(text)
        except:
            print("Sorry could not recognize what you said")
    #i=1
    r1 = sr.Recognizer()
    #i=="no"
    with sr.Microphone() as source:
        print("should we continue ?")
        speaker.Speak("should we continue ? ")
        print("Listining now ..... ")
        audio1 = r1.listen(source)
        try:
            i = r1.recognize_google(audio1)
            print("You said : {}".format(i))
            #a.append(text)
        except:
            print("Sorry could not recognize what you said")
            

print(a)
y=model.predict(vect.transform(a))
print(y)
r=0
for t in y:
    r+=1
    if t==0:
        speaker.Speak("your Feedback for phone {} is recognized as Bad Review!".format(r))
    else:
        speaker.Speak("your Feedback for phone {} is recognized as Good Review!".format(r))
# if y[0]==0:
#     speaker.Speak("your Feedback is recognized as Bad Review!")
# else:
#     speaker.Speak("your Feedback is recognized as Good Review!")


# In[ ]:




