class Solver{

  rungeKutta(yPrime,zPrime,initalY,initalZ,initalT,finalT,step){
      var t=initalT
      var y=initalY
      var z=initalZ
      var tValues=[t]
      var yValues=[y]
      var zValues=[z]
      for(var t = initalT; t<finalT; t = t + step){
          var k1=yPrime(t,y,z)*step;
          var l1=zPrime(t,y,z)*step;
          var k2=yPrime(t+(step/2),y+(k1/2),z+(l1/2))*step;
          var l2=zPrime(t+(step/2),y+(k1/2),z+(l1/2))*step;
          var k3=yPrime(t+(step/2),y+(k2/2),z+(l2/2))*step;
          var l3=zPrime(t+(step/2),y+(k2/2),z+(l2/2))*step;
          var k4=yPrime(t+step,y+k3,z+l3)*step;
          var l4=zPrime(t+step,y+k3,z+l3)*step;
          y=y+(k1+2*k2+2*k3+k4)/6;
          z=z+(l1+2*l2+2*l3+l4)/6;
          yValues.push(y);
          zValues.push(z);
          tValues.push(t);
      }
      return([tValues,zValues,yValues])
  }
  
  trapezoidReimann(yValues,step){
    var area = 0; 
    for(var i = 0; i<yValues.length -1; i++){
      area = area + ((yValues[i]+yValues[i+1])/2)*step;
    }
    return(area);
  }
  
  zeroInterval(f,startValue, endValue, step){
    var intervals = []
    var intialY = f(startValue);
    var intialSign = this.isPositive(intialY);
    for(var x = startValue+step; x < endValue; x = x + step){
      var nextY = f(x);
      var nextSign = this.isPositive(nextY); 
      if(intialSign != nextSign){
        intervals.push([x-step,x]);
      }
      var intialY = nextY; 
      var intialSign = nextSign;
    }
    return(intervals);
  }
  
  averageInterval(intervalArray){
    var averagedValues = []
    for(var i = 0; i < intervalArray.length; i++){
      averagedValues.push((intervalArray[i][0] + intervalArray[i][1])/2);
    }
    return(averagedValues);
  }
  
  round(number, decimalPlaces){
    const factorOfTen = Math.pow(10, decimalPlaces)
    return Math.round(number * factorOfTen) / factorOfTen
  }
  
  isPositive(value){
    if(value > 0){
      return true;
    }
    else{
      return false;
    }
  }
  
  bisection(f,a,b,tol=1e-5){
    var m = (a+b)/2;
    var fm = f(m);
    var n = 0;
    while(Math.abs(fm)>=1e-5 && n < 10){
      n = n + 1;
        if(fm*f(a)<0){
            b = m;
        }
        else{
            a = m;
        }
        m = (a+b)/2;
        fm = f(m);
    }
    return(m);
}
  
  
}