import React, { useState, useEffect/*, Component */} from 'react';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";

//import ReactDOM from 'react-dom';
//import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'

//import axios from 'axios';
//import Contact from './Dokumen';
//import {
//  BrowserRouter as Router,
//  Switch,
//  Route,
//  Link,
//  Redirect
//} from "react-router-dom";

function Doc1(props) {
    const [currentResult, setCurrentResult] = useState(0);
    useEffect(() => {
        //console.log("masuk sini")
        fetch('/result').then(res => res.json()).then(data => {
            if(data){
                console.log("result received")
                console.log("data",data)
              setCurrentResult(data.content);
              console.log(currentResult);
            }
        });
      }, []);
      console.log(currentResult)
    if (currentResult === 0){
        return(
            <div className="Doc1">
                <p>Retrieving Doc1...</p>
            </div>
        )
    }else{
        return (
            <div>
            <p>{currentResult[0].title}</p>
            <p>{currentResult[0].body}</p>
            </div>
            )
    }
}

export default Doc1;