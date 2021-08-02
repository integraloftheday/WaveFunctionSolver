class Plotter {
  
  constructor(div="plot",title="",xaxis = "",yaxis=""){
    this.plotDiv = document.getElementById(div);
    this.traces = []
    this.title = title;
    this.xaxis = xaxis; 
    this.yaxis = yaxis;
    this.layout = {
      title: title,
      xaxis: {
        title: xaxis,
        },
      yaxis: {
        title:yaxis
      }
    };
    Plotly.newPlot(this.plotDiv,this.traces,this.layout);
  }
  
  init(){
    Plotly.newPlot(this.plotDiv,this.traces,this.layout);
  }
  
  setAxisMaxY(maxY){
    this.layout = {
      title: this.title,
      xaxis: {
        title: this.xaxis,
        },
      yaxis: {
        title:this.yaxis,
        range: [0,maxY]
      }
    };
    
    Plotly.newPlot(this.plotDiv,this.traces,this.layout);
  }
  
  plotFromEquations(equations,minX,maxX,step,name=null){
    var x = [];
    var y = [];
    for(var i = minX; i < maxX;i = i + step){
      x.push(i);
      y.push(equations.eval(i));
    }
    if(name == null){
      this.traces.push({
        x: x,
        y: y,
        fill: 'tozeroy'
      });
    }
    else{
      this.traces.push({
        x:x,
        y:y,
        name:name,
        fill: 'tozeroy'
      });
    }
    
    Plotly.newPlot(this.plotDiv,this.traces,this.layout);
  }
  
  plotFromPoints(x,y,name=null){
    this.graphPlot(x,y,name);
  }
  
  graphPlot(x,y,name=null){
   if(name == null){
      this.traces.push({
        x: x,
        y: y
      });
    }
    else{
      this.traces.push({
        x:x,
        y:y,
        name:name
      });
    }
    
    Plotly.newPlot(this.plotDiv, this.traces,this.layout);
  }
  
  plotSeries(series){
    this.traces = [];
    var x = []
    for(var i = 0; i<series.length; i++){
      x.push(i);
    }
    this.plotFromPoints(x,series);
    
  }
  
  graphClear(){
    this.traces = [];
    Plotly.newPlot(this.plotDiv, this.traces,this.layout);
  }
  
}