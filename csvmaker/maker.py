import pandas as pd
vector = []
while True:
    user_id = input("Enter User ID (or type 'exit' to finish): ")
    if user_id.lower() == 'exit':
        break
    vector.append([user_id, input("Enter Password: ")])
    

df = pd.DataFrame(vector, columns=['User_ID', 'Password'])
df.to_csv("user_credentials.csv", index=False)
