import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";

function App() {
  const [currentResult, setCurrentResult] = useState(0);
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

  return (
    <div className="App">
      <body>            
        <form>
          <label>
            Search : <input type="text" id = "query" name = "query" placeholder = "Search" />
            <input type="button" value="Search" onClick = {() => GetQueryFrontEnd()} />
            </label>
        </form>
        
      </body>

    </div>
  );
}

export default App;
