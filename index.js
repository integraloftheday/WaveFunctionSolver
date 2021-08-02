//global variables 
var threeD = false;
var Graph2D;
var Graph3D;
var canvas2D;
var canvas3D;
var ContG =false;
var potentialEditor; 
var plotter;
var plotterE;
var sSolve; 

//function Onload
function onLoad(){
  potentialEditor = new EquationEditor("V","Vequations");
  plotter = new Plotter("plot","Wavefunction Squared","x","|ψ| * |ψ|");
  plotterE = new Plotter("plotE","Energy Levels","n","E");
  sSolve = new Schrodinger(); 
  off();
  intialValues();
  solve();
}

function intialValues(){
  var name = "V";
  var numEq = 1
  document.getElementById(`Eq-${name}-${numEq}`).value = 500;
  document.getElementById(`Min-${name}-${numEq}`).value = -0.1;
  document.getElementById(`Max-${name}-${numEq}`).value = 0.1;
  
    document.getElementById("xMin").value = -4;
    document.getElementById("xMax").value = 4;
    document.getElementById("xStep").value = 0.1;
    document.getElementById("Emin").value = 10;
    document.getElementById("Emax").value =20;
  
}

//Overlay code
function on() {
  document.getElementById("overlay").style.display = "block";
  document.getElementById("under").style.display = "none";
}

function off() {
  document.getElementById("overlay").style.display = "none";
  document.getElementById("under").style.display = "block";
  plotter.init();
  plotterE.init();
  $('[data-toggle="popover"]').popover("hide")
}

//Popover Intilization
function popoverLoad(){
  $(function () {
    $('[data-toggle="popover"]').popover()
  })
}

//graph button function
function graphB(){
  potentialEditor.equations.clear();
  potentialEditor.parseEquations();
  plotter.plotFromEquations(potentialEditor.equations,-1,1,0.1);
}

function solve(){
  console.log("SOLVE");
  off();
  potentialEditor.equations.clear();
  potentialEditor.parseEquations();
  sSolve.V = (x) => {return(potentialEditor.equations.eval(x))}; 
  console.log("Solution" + sSolve.solve());
}

function clearG(){
  console.log("Clearing")
  sSolve.solutionE = [];
  plotter.graphClear();
}

