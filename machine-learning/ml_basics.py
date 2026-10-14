# Hours studied
X = [[1], [2], [3], [4], [5], [6]]

# Exam scores
y = [35, 40, 50, 55, 65, 75]



from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

predicted_score = model.predict([[7]])

print("Predicted exam score:", predicted_score[0])