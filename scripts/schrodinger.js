class Schrodinger{
  
  constructor(){
    this.infiteWall = 0; 
    this.delta = 0;
    this.xMin = -1;
    this.xMax = 1;
    this.step = 0.1; 
    this.c = -1;
    this.Emin = 0;
    this.Emax = 5;
    this.V;
    this.solver = new Solver();
    this.intialY = 0;
    this.intialYPrime = 0.01;
    this.getHTMLParameters();
    this.solutionE = [];
    this.Eindex = 0
  }
  
  vBoundary(t){
    var v = 0;
    if(t> this.xMax){
      v = this.infiteWall; 
    }
    else if(t<this.xMin){
      v = this.infiteWall;
    }
    else{
      v = this.V(t)
    }
    return(v)
  }
  
  zPrime (E,t,y,z){
    
    return((y*(E-this.vBoundary(t)))/this.c);
  }
  
  yPrime(E,t,y,z){
    return z;
  }
  
  fbyE(E){
    var results = this.solver.rungeKutta((t,y,z)=>{return(this.yPrime(E,t,y,z))},(t,y,z)=>{return(this.zPrime(E,t,y,z))}, this.intialY,this.intialYPrime,this.xMin-this.delta,this.xMax+this.delta,this.step);
    return(results[2][results[2].length - 1]);
  }
  
  solve(){
    var maxY = 0;
    this.getHTMLParameters();
    var intervals = this.solver.zeroInterval((x) =>{return(this.fbyE(x))},this.Emin,this.Emax,this.step);
    
    console.log(intervals);
    for(var i = 0; i< intervals.length; i ++){
      this.solutionE.push(this.solver.bisection((x) =>{return(this.fbyE(x))},intervals[i][0],intervals[i][1]));
    }
    
    for(var j = 0; j<this.solutionE.length; j++){
      var results = this.solver.rungeKutta((t,y,z)=>{return(this.yPrime(this.solutionE[j],t,y,z))},(t,y,z)=>{return(this.zPrime(this.solutionE[j],t,y,z))}, this.intialY,this.intialYPrime,this.xMin-this.delta,this.xMax+this.delta,this.step);
      results[2] = results[2].map((x)=>{ // convert wave to probaility function
        return(x**2);
      });
      var scaler = 1/this.solver.trapezoidReimann(results[2],this.step); //normalize
      results[2] = results[2].map((x)=>{
        return(scaler*x);
      });
      
      var _maxY = Math.max(results[2]);
      if(_maxY > maxY){
        maxY = _maxY;
      }
      
      plotter.plotFromPoints(results[0],results[2],`E=${this.solver.round(this.solutionE[j],3)}`);  
    }
    plotterE.plotSeries(this.solutionE);
    plotter.setAxisMaxY(maxY);
    plotter.plotFromEquations(potentialEditor.equations,this.xMin,this.xMax,this.step,"Potential");
    //plotter.plotFromEquations(potentialEditor.equations,this.xMin,this.xMax,this.step);
  }
  
  getHTMLParameters(){
    this.xMin = parseFloat(document.getElementById("xMin").value);
    this.xMax = parseFloat(document.getElementById("xMax").value);
    this.step = parseFloat(document.getElementById("xStep").value);
    this.Emin = parseFloat(document.getElementById("Emin").value);
    this.Emax = parseFloat(document.getElementById("Emax").value);
  }
  
}