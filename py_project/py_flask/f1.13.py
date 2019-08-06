#~/add/<x>/<y> -> 리다이렉트 -> ~/mul?res=xxx -> 리다이렉트 -> ~/show/<value>
# add 페이지는 x+y
# mul 페이지는 res*10 해서 던져준다
# show 에서는 최종값을 보여준다


from flask import Flask,url_for,redirect,request
        
@app.route('/add/<int:x>/<int:y>')  
def add(x,y) :
    sum=x+y
    return redirect(url_for('%s?res=%s' %(url_for('mulFuc'),sum))


@app.route('/mul')

def mulFuc( ):
    sum1 = int(request.args.get('res'))*10
    return redirect(url_for('show',value=sum1))

@app.route('/show/<value>')  
def show(value) :
    return '최종값='+value


if __name__=="__main__" :
    app.run(debug=True)
