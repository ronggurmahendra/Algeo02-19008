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
        fetch('/Get_Doc1').then(res => res.json()).then(data => {
            if(data){
                console.log("Doc1 received")
                console.log("data",data)
                setCurrentResult(data);
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
            <p>{currentResult.title}</p>
            <p>{currentResult.content}</p>
            </div>
            )
    }
}

export default Doc1;