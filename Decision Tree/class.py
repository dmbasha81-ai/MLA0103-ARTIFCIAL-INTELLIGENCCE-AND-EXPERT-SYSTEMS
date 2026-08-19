import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    'Q1': [True, True, False, False, False, True, True, True, False, False],
    'Q2': ['Hot', 'Hot', 'Hot', 'Cool', 'Cool', 'Cool', 'Hot', 'Hot', 'Cool', 'Cool'],
    'Q3': ['High', 'High', 'High', 'Normal', 'Normal', 'High', 'High', 'Normal', 'Normal', 'High'],
    'Class': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

df['Q1'] = df['Q1'].astype(int)
df['Q2'] = df['Q2'].map({'Hot': 0, 'Cool': 1})
df['Q3'] = df['Q3'].map({'High': 0, 'Normal': 1})
df['Class'] = df['Class'].map({'No': 0, 'Yes': 1})

X = df[['Q1', 'Q2', 'Q3']]
y = df['Class']

model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=2,
    random_state=0
)

model.fit(X, y)

q1 = input("Enter Q1 (True/False): ")
q2 = input("Enter Q2 (Hot/Cool): ")
q3 = input("Enter Q3 (High/Normal): ")

new_data = pd.DataFrame({
    'Q1': [1 if q1 == 'True' else 0],
    'Q2': [0 if q2 == 'Hot' else 1],
    'Q3': [0 if q3 == 'High' else 1]
})

prediction = model.predict(new_data)

if prediction[0] == 1:
    print("Class: Yes")
else:
    print("Class: No")
