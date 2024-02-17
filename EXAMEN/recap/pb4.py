x="xcdbfffghduiiiisdas" 
y="ghxcdbduiiiisddgs"
max=""
for i in range(len(x)):
    for j in range(len(x)):
        if y.find(x[i:j])!=-1:
            if len(x[i:j])>len(max):
                max=x[i:j]
print(len(max))
