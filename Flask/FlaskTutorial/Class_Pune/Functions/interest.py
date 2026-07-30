from flask import Flask,request

app=Flask(__name__)

@app.route('/',methods=['POST'])
def simpleInterest():
    # total=0
    # interest=0
    
    if request.method=='POST':
        principal=float(request.form.get('principal',))
        rate=float(request.form.get('rate',0))
        time=float(request.form.get('time',0))

        interest=(principal * rate * time) / 100
        
        total=principal + interest
        
    return f'simple Interest: {interest} ,total amount :{total} '
        
        
if __name__=='__main__':
    app.run(debug=True)