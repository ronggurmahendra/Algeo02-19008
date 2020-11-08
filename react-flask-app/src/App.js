import React, { useState, useEffect, Component } from 'react';
import logo from './logo.svg';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";
import axios from 'axios';
function App() {
  const [currentResult, setCurrentResult] = useState(0);
  const [filestate,setFilestate] = useState();
  //var url = "http://localhost:3000"
  //const [query,setQuer]
  useEffect(() => {
    //console.log("masuk sini")
    fetch('/result').then(res => res.json()).then(data => {
      console.log("result received")
      setCurrentResult(data.content);
      console.log(data);
    });
  }, []);

  function GetQueryFrontEnd(){
    //a.preventDefault();
    var query = document.getElementById("query").value;
    console.log(query);
    PostQuery(query);
  }

 // var streamresult = setInterval()

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

  return (
    <div className="App">
      <body>            
        <form>
          <label>
            Search : <input type="text" id = "query" name = "query" placeholder = "Search" />
            <input type="button" value="Search" onClick = {() => GetQueryFrontEnd()} />
            </label>
        </form>
        

        <input type="file" name="file" id = "file" onChange={onChangeHandler}/>
        <button type="button" onClick={onClickHandlerUpload}>Upload</button> 
      </body>

    </div>
  );
}

export default App;
