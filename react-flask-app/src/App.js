import React, { useState, useEffect, Component } from 'react';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";
/*
import ReactDOM from 'react-dom';
import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'
*/
import axios from 'axios';
//import Contact from './Dokumen';
function App() {
  const [currentResult, setCurrentResult] = useState(0);
  const [HTMLResult, setHTMLResult] = useState();
  const [filestate,setFilestate] = useState();
  //var url = "http://localhost:3000"
  //const [query,setQuer]
  useEffect(() => {
    //console.log("masuk sini")
    fetch('/result').then(res => res.json()).then(data => {
      console.log("result received")
      setCurrentResult(data.content);

    });
  }, []);

  var renderList = setInterval(function bikinHTML(){
    let array = [];
    for(let i = 0;i < currentResult.length;i++){
      let j = i + 15;
      let k = i + 30;
      array.push(
        [<p key = {i} style = {{background: "white",
          borderTopWidth: 1,
          borderTopmColor: 'red',
          borderTopStyle: 'solid',

          borderLeftWidth: 1,
          borderLeftmColor: 'red',
          borderLeftStyle: 'solid',
          borderRightWidth: 1,
          borderRightmColor: 'red',
          borderRightStyle: 'solid',

          color : 'black',
          borderstyle: "solid",
          marginLeft: "25%",
          width: "50%",
          marginBottom:"0px"}}  
          >title : {currentResult[i].title}</p>,
        <p key = {j} style = {{background: "white",

        color : 'black',
        borderstyle: "solid",
        marginLeft: "25%",
        width: "50%",
      
        borderLeftWidth: 1,
        borderLeftmColor: 'red',
        borderLeftStyle: 'solid',
        borderRightWidth: 1,
        borderRightmColor: 'red',
        borderRightStyle: 'solid',
        marginBottom:"0px",
        marginTop:"0px"
      }}   >kalimat pertama : {currentResult[i].body}</p>,
        <p key = {k} style = {{background: "white",
        borderBottomWidth: 1,
        borderBottomColor: 'red',
        borderBottomStyle: 'solid',
        color : 'black',
        borderstyle: "solid",
        marginLeft: "25%",
        width: "50%",
        borderLeftWidth: 1,
        borderLeftmColor: 'red',
        borderLeftStyle: 'solid',
        borderRightWidth: 1,
        borderRightmColor: 'red',
        borderRightStyle: 'solid',
        marginTop:"0px"
      }}   >similatity : {currentResult[i].sim} %</p>]
      );
    }
    console.log(array)
    setHTMLResult(array)
    //console.log('data.content',data.content)
    //console.log('array',array)
    //console.log('HTMLResult',HTMLResult)
  },2000)

  function GetQueryFrontEnd(){
    //a.preventDefault();
    var query = document.getElementById("query").value;
    console.log(query);
    PostQuery(query);
  }
/*
  var streamresult = setInterval(function () {
    console.log("tetsing")
  },1000);*/

  function PostQuery(data){
    console.log("Sending Query")
    const response = fetch("/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });
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
      </div>

    )
  //}
}
export default App;