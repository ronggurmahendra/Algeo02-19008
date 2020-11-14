import React, { useState, useEffect/*, Component */} from 'react';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";

//import ReactDOM from 'react-dom';
//import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'

import axios from 'axios';
//import Contact from './Dokumen';
import {
  BrowserRouter as Router,
  //Switch,
  //Route,
  Link
  //Redirect
} from "react-router-dom";
//import {Router, Link, RouteHandler} from 'react-router';


function App() {
  const [currentResult, setCurrentResult] = useState(0);
  const [HTMLResult, setHTMLResult] = useState();
  const [filestate,setFilestate] = useState();
  const [tabelState,setTabelState] = useState( {__html: '<div>Hello World!</div>'} );
  //const [pageState,setPageState] = useState();
  //setPageState("/");
  
  useEffect(function getResult(){
    console.log("Getting Result")
    fetch('/result').then(res => res.json()).then(data => {
      console.log("result received")
      setCurrentResult(data.content);

    });
  }, []);
  useEffect(function getTabel(){
    console.log("Getting Table")
    fetch('/tabel').then(res => res.json()).then(data => {
      console.log("Table received")
      let temp = document.createElement('div');
      temp.innerHTML = data.content;
      var htmlObject = temp;
      //console.log("state",tabelState)
      setTabelState(data.content);
      
      
      //console.log("state",tabelState)
    });
  }, []);
  /*
  function getResult(){
    console.log("Getting Result")
    fetch('/result').then(res => res.json()).then(data => {
      console.log("result received")
      setCurrentResult(data.content);

    });
  }*/
  function bikinHTML(){
    //getResult();
    let array = [];
    for(let i = 0;i < currentResult.length;i++){
      let j = i + 100;
      let k = i + 200;
      let a = i + 300;
      var iStr = (i+1).toString();
      var link = "/Doc".concat(iStr);
      
      array.push(
        [  <div style = {{border: '1px solid red',marginLeft: "25%",width: "50%",marginBottom:"1px",marginTop:"5px"}}>
          <Router forceRefresh={true}><Link to = {link}  key = {i}>{currentResult[i].title}</Link></Router>
          <p key = {j} style = {{marginBottom:"0px",marginTop:"0px"}}>kalimat pertama : {currentResult[i].body}</p>
          <p key = {k} style = {{marginBottom:"0px",marginTop:"0px"}}>similatity : {currentResult[i].sim} %</p>
          <p key = {a} style = {{marginBottom:"0px",marginTop:"0px"}}>count : {currentResult[i].count}</p>
        </div>]
      );
    }
    //console.log(array)\
    console.log(currentResult)
    setHTMLResult(array)
    //console.log('data.content',data.content)
    //console.log('array',array)
    //console.log('HTMLResult',HTMLResult)
  }

  //bikinHTML();
  var renderList = setInterval(bikinHTML,10000)

  function GetQueryFrontEnd(){
    //a.preventDefault();
    var query = document.getElementById("query").value;
    console.log(query);
    PostQuery(query);
  }

  function PostQuery(data){
    console.log("Sending Query")
    const response = fetch("/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    }).then(
      console.log("masuk sini")
    );
    window.location.reload(false);
  }
  function onChangeHandler(event){
    //console.log(event)
    var files = event.target.files
    //console.log(files[0])
      setFilestate({
       selectedFile: files
    })
  }


  function onClickHandlerUpload () {
    let data = new FormData()
    //var file = document.getElementById("file").value;
    data.append('file', filestate.selectedFile[0],filestate.selectedFile[0].name)
    //console.log(filestate.selectedFile[0].name)
    //data.set('file', filestate.selectedFile)
    console.log(filestate.selectedFile[0])
    //console.log(data)
    axios.post("/upload", data)
  }
  //render() {
    //if(pageState == "/"){
      return (
        <div className="App">
          <div>            
            <form>
              <label>
                Search : <input type="text" id = "query" name = "query" placeholder = "Search" />
                <input type="button" value="Search" onClick = {() => GetQueryFrontEnd()} />
                </label>
            </form>
            <input type="file" name="file" id = "file" onChange={onChangeHandler}/>
            <button type="button" onClick={onClickHandlerUpload}>Upload</button> 
  
          </div>
          <div >
            {HTMLResult}
          </div>
          <div dangerouslySetInnerHTML={{ __html: tabelState }} />
            
          <div>
            <Router forceRefresh={true}><Link to = "/perihal" >perihal</Link></Router>
          </div>
        </div>
        
      )
}
export default App;
  