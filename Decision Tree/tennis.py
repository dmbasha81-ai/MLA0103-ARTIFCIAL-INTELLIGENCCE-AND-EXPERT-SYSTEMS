import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temp': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild',
             'Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal',
                 'High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'Play_Tennis': ['No','No','Yes','Yes','Yes','No','Yes','No',
                    'Yes','Yes','Yes','Yes','Yes','No']
}

df = pd.DataFrame(data)

df['Outlook'] = df['Outlook'].map({'Sunny': 0, 'Overcast': 1, 'Rain': 2})
df['Temp'] = df['Temp'].map({'Hot': 0, 'Mild': 1, 'Cool': 2})
df['Humidity'] = df['Humidity'].map({'High': 0, 'Normal': 1})
df['Wind'] = df['Wind'].map({'Weak': 0, 'Strong': 1})
df['Play_Tennis'] = df['Play_Tennis'].map({'No': 0, 'Yes': 1})

X = df[['Outlook', 'Temp', 'Humidity', 'Wind']]
y = df['Play_Tennis']

model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=0
)

model.fit(X, y)

outlook = input("Enter Outlook (Sunny/Overcast/Rain): ")
temp = input("Enter Temperature (Hot/Mild/Cool): ")
humidity = input("Enter Humidity (High/Normal): ")
wind = input("Enter Wind (Weak/Strong): ")

new_data = pd.DataFrame({
    'Outlook': [outlook],
    'Temp': [temp],
    'Humidity': [humidity],
    'Wind': [wind]
})

new_data['Outlook'] = new_data['Outlook'].map({
    'Sunny': 0, 'Overcast': 1, 'Rain': 2
})

new_data['Temp'] = new_data['Temp'].map({
    'Hot': 0, 'Mild': 1, 'Cool': 2
})

new_data['Humidity'] = new_data['Humidity'].map({
    'High': 0, 'Normal': 1
})

new_data['Wind'] = new_data['Wind'].map({
    'Weak': 0, 'Strong': 1
})

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Play Tennis: Yes")
else:
    print("Play Tennis: No")
